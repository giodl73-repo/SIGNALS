Written. Here is the complete updated rubric:

---

# flow-dataflow Rubric — v2

## Change Log

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10..C-12 from V-05 excellence signals: pre-trace vocabulary gate, interleaved boundary gates, domain entity exposure per boundary |

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

## Aspirational Criteria (weight: 10 pts total) — **5 criteria in v2**

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Recovery prescriptions** | depth | Every "no handling" annotation from C-02 and every loss point from C-03 has a paired, specific recovery suggestion. |
| C-09 | **Pattern trade-off analysis** | behavior | Named alternative pattern with at least two quantified or qualified trade-off dimensions. |
| C-10 | **Pre-trace domain context gate** | format | A DOMAIN CONTEXT section appears before the first stage block, locking entity names, downstream consumer, and business cadence. At least two of those terms reappear verbatim in subsequent lineage or stale-window content. |
| C-11 | **Interleaved boundary gates** | behavior | A boundary check block appears between every consecutive stage pair — inline, not post-hoc. A trailing BOUNDARY SUMMARY alone does not satisfy this criterion. |
| C-12 | **Domain entity exposure per boundary** | format | Every boundary check that satisfies C-11 names a domain entity from the scenario vocabulary. "data" or "records" alone does not pass. |

---

## Scoring Worksheet

```
Essential passed:     ___ / 4   =>  (___ / 4) * 60 = ___
Recommended passed:   ___ / 3   =>  (___ / 3) * 30 = ___
Aspirational passed:  ___ / 5   =>  (___ / 5) * 10 = ___
                                    Composite      = ___

Golden: all 4 essential pass AND composite >= 80
```

---

## What changed from v1

**Three new aspirational criteria (C-10, C-11, C-12)** encode the structural patterns that separated 100-point from 95-point variations in Round 1:

- **C-10 (pre-trace vocabulary gate)** — V-01 and V-03 scored C-07 PARTIAL because domain terms appeared in the lineage chain but drifted to generic in schema fields and error descriptions. C-10 forces the vocabulary to be declared and committed before any tracing begins.
- **C-11 (interleaved boundary gates)** — V-02 failed golden because its BOUNDARY SUMMARY was post-hoc; the model completed all stage blocks first and then produced a summary that could abbreviate or omit. C-11 makes skipping a boundary structurally impossible.
- **C-12 (domain entity per boundary)** — V-05's third independent C-07 surface at transition edges. Boundaries are the highest-omission-risk locations; requiring a domain entity name there closes the loop between C-10 vocabulary seeding and C-11 structural enforcement.

The causal chain: C-10 seeds vocabulary → C-11 forces each boundary to be examined before the next stage is written → C-12 requires the boundary check to use C-10 vocabulary, so domain terms cannot drift to generic at precisely the transitions where errors are most commonly missed.
 names, consumer, and cadence are all present. At least two of those terms reappear verbatim in subsequent lineage or stale-window content. |
| C-11 | **Interleaved boundary gates** — Error handling and loss-exposure checks appear inline between each pair of adjacent stage blocks -- not collected into a separate post-hoc summary section -- making it structurally impossible to complete a stage transition without annotating the boundary. | behavior | A boundary check block (or equivalent inline annotation) appears between every consecutive stage pair. No stage-to-stage transition is present without an interleaved error-handling and loss-exposure annotation. A post-hoc BOUNDARY SUMMARY that follows all stages does not satisfy this criterion alone. |
| C-12 | **Domain entity exposure per boundary** — Each inline boundary check names the specific domain entity (from C-10 or C-07 vocabulary) exposed at that transition edge -- not a generic "data" or "record" -- creating an independent domain-vocabulary surface at the highest-omission-risk location. | format | Every boundary check that satisfies C-11 also contains a domain entity name drawn from the scenario vocabulary. Boundaries annotated only as "data" or "records" do not pass. |

---

## Scoring Worksheet

```
Essential passed:     ___ / 4   =>  (___ / 4) * 60 = ___
Recommended passed:   ___ / 3   =>  (___ / 3) * 30 = ___
Aspirational passed:  ___ / 5   =>  (___ / 5) * 10 = ___
                                    Composite      = ___

Golden: all 4 essential pass AND composite >= 80
```

### Partial credit rule

C-07 (Domain framing): if domain entity names appear in the lineage chain but
not in boundary checks or stale window analysis, award 0.5 / 1.0 (reduces
recommended score by 5 pts).

C-02 (Boundary error handling): a post-hoc boundary summary that covers all
boundaries but was written after all stage blocks awards 0.5 / 1.0 -- essential
threshold not met, golden blocked.

---

## Discriminator Notes (from Round 1)

These distinctions separated 100-point from 95-point variations:

| Gap | What 95-pt variations missed | What 100-pt variations did |
|-----|------------------------------|---------------------------|
| C-07 partial | Entity name in one field only; schema and error fields used generic terms | Full DOMAIN CONTEXT gate; entity names appear in table cells, gates, and stale analysis |
| C-02 partial | BOUNDARY SUMMARY written post-hoc after all STAGE blocks | BOUNDARY CHECK gate interleaved between every stage pair |

C-10, C-11, C-12 are the rubric encoding of those discriminators. A variation
that satisfies all five aspirational criteria is structurally resistant to the
two most common partial-pass failure modes: silent boundary omission and
vocabulary drift in error/latency fields.

The causal chain: C-10 seeds the vocabulary -> C-11 forces each boundary to be
examined before the next stage is written -> C-12 requires that the boundary
check uses C-10 vocabulary, closing the loop so domain terms cannot drift to
generic at precisely the transitions where errors are most commonly missed.
