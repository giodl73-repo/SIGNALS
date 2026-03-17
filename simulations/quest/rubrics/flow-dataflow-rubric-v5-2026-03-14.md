Three new criteria added. Here is the updated rubric:

---

# flow-dataflow Rubric — v5

## Change Log

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10..C-12 from R1 excellence signals: pre-trace vocabulary gate, interleaved boundary gates, domain entity exposure per boundary |
| v3 | 2026-03-14 | Added C-13..C-15 from R2 excellence signals: pre-declared staleness contract, additive elapsed time calculation, incumbent baseline section |
| v4 | 2026-03-14 | Added C-16..C-18 from R3 excellence signals: cross-role reference chain, immutability declaration, incremental boundary elapsed computation |
| v5 | 2026-03-14 | Added C-19..C-21 from R4 excellence signals: machine-verifiable citation convention, stage-write progression gate, binary freshness verdict per boundary |

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

## Aspirational Criteria (weight: 10 pts total) — **14 criteria in v5**

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
| C-19 | **Machine-verifiable citation target convention** | format | A formal citation convention — a consistent prefix, schema, or required field (e.g., `ARTIFACT:` prefix, `R-xx` IDs, `Citing:` row) — is declared and applied uniformly to every named handoff target in the variation. Every citation made by any subsequent role or section uses this convention, making references verifiable by token match rather than prose judgment. A variation that names handoff targets using inconsistent or ad hoc labels does not pass. C-16 checks whether citations are named; C-19 checks whether citation targets are created via a machine-parseable convention applied without exception. |
| C-20 | **Stage-write progression gate** | behavior | The prompt contains an explicit write-order prohibition: Stage N+1 may not be written until the boundary block between Stage N and Stage N+1 is fully complete with all required fields present. The prohibition must be stated as a sequencing constraint that names the gate condition (e.g., "Do not write Stage N+1 until this block is complete"). C-11 requires interleaved boundary block placement; C-20 requires an explicit deferral prohibition that makes the boundary block a structural prerequisite for stage advancement. A prompt that instructs boundary block placement without a write-order prohibition does not pass. |
| C-21 | **Binary freshness verdict per boundary** | depth | Each BOUNDARY CHECK block contains a required declarative verdict field (FRESH / STALE or equivalent binary) derived by comparing the cumulative elapsed total against the pre-declared threshold from C-13. C-14 requires the elapsed total to exist; C-18 requires it to be computed incrementally; C-21 requires that each boundary produce an explicit pass/fail verdict, converting the elapsed computation into a decision gate. A boundary block that records elapsed time without a verdict field does not pass. A verdict that appears only in the final stale analysis does not satisfy this criterion. |

---

## Scoring Worksheet

```
Essential passed:     ___ / 4    =>  (___ / 4)  * 60 = ___
Recommended passed:   ___ / 3    =>  (___ / 3)  * 30 = ___
Aspirational passed:  ___ / 14   =>  (___ / 14) * 10 = ___
                                     Composite       = ___

Golden: all 4 essential pass AND composite >= 80
```

---

## Criterion rationale — v5 additions

**C-19 (machine-verifiable citation target convention)** is a strictly stronger form of C-16. C-16 requires that each citation name its source. C-19 requires that named sources follow a *declared, consistent convention* that makes citation targets unambiguous without prose interpretation. A variation can satisfy C-16 with ad hoc labels ("the Domain Context section above", "the baseline we defined earlier") without establishing a reusable convention. V-01's `ARTIFACT:` prefix and V-05's required `Citing:` row both satisfy C-19; arbitrary named references do not.

**C-20 (stage-write progression gate)** is a strictly stronger form of C-11 combined with C-18. C-11 requires that boundary blocks appear inline between stage pairs; C-18 requires the elapsed field to be computed incrementally within those blocks. C-20 requires that the prompt explicitly prohibit writing Stage N+1 until the current boundary block is complete. Without this, a model can mentally skip ahead to stage content and fill boundary fields retroactively, provided the final output positions them correctly. C-20's deferral prohibition makes retroactive completion structurally prohibited. V-01's "Do not write Stage N+1 until this block is complete" is the canonical form.

**C-21 (binary freshness verdict per boundary)** closes a gap left by C-14 and C-18. Both address *computation* of cumulative elapsed time; neither requires the total to produce a decision at each boundary. C-21 requires an explicit FRESH/STALE verdict field at every boundary, committing to a conclusion at the crossing point rather than deferring to the final stale analysis. V-03's inertia framing demonstrated the pattern (F-02 verdict field per boundary) while failing C-14 and C-18 in full, confirming that the verdict dimension is orthogonal to the computation dimension.
verifiable citation target convention)** is a strictly stronger form of C-16. C-16 requires that each citation name its source rather than use generic back-references. C-19 requires that named sources follow a *declared, consistent convention* — a prefix, ID system, or required field — that makes citation targets unambiguous without prose interpretation. The distinction: a variation can satisfy C-16 by naming sources with ad hoc labels ("the Domain Context section above", "the baseline we defined earlier") without ever establishing a reusable convention. C-19 fails in that case because the citation targets are not machine-parseable across roles. V-01's `ARTIFACT:` prefix and V-05's required `Citing:` row both satisfy C-19; arbitrary named references do not.

**C-20 (stage-write progression gate)** is a strictly stronger form of C-11 in combination with C-18. C-11 requires that boundary blocks appear inline between consecutive stage pairs; C-18 requires that the cumulative elapsed field be computed incrementally within those blocks. C-20 requires that the prompt explicitly prohibit writing the next stage until the current boundary block is complete — a write-order constraint that makes the boundary block a prerequisite, not merely a required element. The behavioral distinction: a variation can comply with C-11 and C-18 while still allowing the model to mentally skip ahead to stage content and fill in boundary fields retroactively, provided the final output positions them correctly. C-20's deferral prohibition makes retroactive completion structurally prohibited, not merely discouraged. V-01's "Do not write Stage N+1 until this block is complete" is the canonical form.

**C-21 (binary freshness verdict per boundary)** closes a gap left by C-14 and C-18. Both criteria address the *computation* of cumulative elapsed time. Neither requires the computed total to produce a decision at each boundary. C-21 requires that each boundary block contain an explicit FRESH/STALE verdict — a binary field that commits to a conclusion at the boundary rather than deferring judgment to the final stale analysis. The behavioral consequence: a model that computes elapsed time correctly but withholds the verdict until post-trace can still avoid committing to a staleness determination at the moment the data crosses a boundary. C-21 eliminates that deferral. V-03's inertia framing demonstrated the pattern (F-02 verdict field per boundary) while failing to satisfy C-14 and C-18 in full, confirming that the verdict dimension is orthogonal to the computation dimension.
