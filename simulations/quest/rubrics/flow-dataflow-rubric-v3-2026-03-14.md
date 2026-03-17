Done. Here is the complete v3 rubric:

---

# flow-dataflow Rubric — v3

## Change Log

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10..C-12 from R1 excellence signals: pre-trace vocabulary gate, interleaved boundary gates, domain entity exposure per boundary |
| v3 | 2026-03-14 | Added C-13..C-15 from R2 excellence signals: pre-declared staleness contract, additive elapsed time calculation, incumbent baseline section |

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

## Aspirational Criteria (weight: 10 pts total) — **8 criteria in v3**

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

---

## Scoring Worksheet

```
Essential passed:     ___ / 4   =>  (___ / 4) * 60 = ___
Recommended passed:   ___ / 3   =>  (___ / 3) * 30 = ___
Aspirational passed:  ___ / 8   =>  (___ / 8) * 10 = ___
                                    Composite      = ___

Golden: all 4 essential pass AND composite >= 80
```

---

## Three new criteria, two causal chains

**C-13 → C-14** close the gap between C-05 and C-06. In v2 per-stage latency and stale windows were structurally disconnected: a variation could pass C-05 and C-06 independently with no numeric link between them. C-13 pre-declares the staleness threshold as a contract; C-14 accumulates stage latencies into a total that can be evaluated against that contract. Together they make the stale analysis derivable rather than asserted.

**C-15** closes the V-01 weakness noted in the R2 scorecard: vocabulary seeded from template blanks is weaker than vocabulary seeded from a business narrative. An INCUMBENT section fires two independent vocabulary surfaces (business narrative + DOMAIN CONTEXT gate) before Stage 1, and grounds C-08 and C-09 in known incumbent failure modes rather than abstract suggestions.

  time vs. threshold) rather than an assertion. A post-hoc stale window can be
  fabricated to fit the pipeline; a pre-declared threshold cannot be adjusted
  after the timing facts are known.

- **C-14 (additive elapsed time calculation)** -- V-03's Time-in-transition:
  fields accumulated into an explicit LIVE->PERSISTED total that made C-13
  evaluation computable rather than claimed. Without a cumulative total, a stale
  threshold is a number with no pipeline-derived quantity to compare it against.
  C-14 is the mechanism that gives C-13 its teeth.

- **C-15 (incumbent/manual-process baseline)** -- V-02's INCUMBENT section was
  the richest C-07, C-08, C-09, and C-10 surface in Round 2. Organic vocabulary
  seeding from a business narrative is more durable than vocabulary seeding from
  template blanks (the V-01 weakness noted in the scorecard). Connecting the
  baseline to recovery prescriptions or trade-off analysis prevents the baseline
  from being a decorative preamble.

The causal chains added in v3:

- C-13 declares the staleness contract -> C-14 accumulates the elapsed time that
  makes the contract verifiable -> together they close the gap between C-05
  (per-stage latency) and C-06 (stale window), which were structurally
  disconnected in v2.

- C-15 seeds vocabulary organically from business context -> that vocabulary feeds
  C-10 (domain context gate) and C-07 (domain framing in lineage), creating two
  independent surfaces for domain terms before any stage block is written. It also
  gives C-08 (recovery prescriptions) and C-09 (trade-off analysis) a concrete
  comparison anchor, replacing abstract "add retry logic" suggestions with
  gap-closure framing tied to known incumbent failure modes.

---

## Discriminator Notes

| Round | Gap | What lower-scoring variations missed | What higher-scoring variations did |
|-------|-----|--------------------------------------|-------------------------------------|
| R1 | C-07 partial | Entity name in one field only; schema and error fields used generic terms | Full DOMAIN CONTEXT gate; entity names in table cells, gates, and stale analysis |
| R1 | C-02 partial | BOUNDARY SUMMARY written post-hoc after all STAGE blocks | BOUNDARY CHECK gate interleaved between every stage pair |
| R2 | C-11 partial (V-02) | Declarative interleaving instruction with no STOP command or anti-batch prohibition | Behavioral + negative framing: STOP before each boundary + explicit "two consecutive stage blocks without a BOUNDARY CHECK is not permitted" |
| R2 | C-06 derivable vs. asserted (V-03) | Stale windows asserted or synthesized after pipeline stages described | Stale threshold declared as contract in DOMAIN CONTEXT; stale analysis evaluates elapsed-time calculation against that threshold |
| R2 | C-10 organic vs. template-forced (V-01 vs. V-02) | Vocabulary seeded by filling template blanks; no business narrative behind the terms | INCUMBENT narrative seeds vocabulary before DOMAIN CONTEXT gate fires; two independent vocabulary surfaces before Stage 1 |
