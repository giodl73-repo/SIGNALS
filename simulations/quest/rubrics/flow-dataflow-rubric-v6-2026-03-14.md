# flow-dataflow Rubric — v6

## Change Log

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10..C-12 from R1 excellence signals: pre-trace vocabulary gate, interleaved boundary gates, domain entity exposure per boundary |
| v3 | 2026-03-14 | Added C-13..C-15 from R2 excellence signals: pre-declared staleness contract, additive elapsed time calculation, incumbent baseline section |
| v4 | 2026-03-14 | Added C-16..C-18 from R3 excellence signals: cross-role reference chain, immutability declaration, incremental boundary elapsed computation |
| v5 | 2026-03-14 | Added C-19..C-21 from R4 excellence signals: machine-verifiable citation convention, stage-write progression gate, binary freshness verdict per boundary |
| v6 | 2026-03-14 | Added C-22..C-24 from R5 excellence signals: formal pre-declared registry table, phase gate self-verification checklists, upfront constraint section with inline callback syntax |

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

## Aspirational Criteria (weight: 10 pts total) — **17 criteria in v6**

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
| C-22 | **Formal pre-declared registry table** | format | A registry table — mapping every artifact to a machine-parseable token (e.g., `[A-xx]`) with at minimum an owner and description column — is produced before any role output begins. The table must enumerate all artifacts that will be cited downstream: a prefix declaration (C-19) or a flat label list satisfies token convention but does not satisfy this criterion. Every citation target named in any subsequent role must appear as a row in this table. A citation to a target not in the table does not pass. The table form makes citation targets first-class, enumerable, and column-verifiable independent of prose context. |
| C-23 | **Phase gate self-verification checklists** | behavior | At least one phase boundary contains a checklist the model must produce and explicitly tick (or mark as passed/failed) before the next phase may begin. Each checklist item must reference a specific named criterion or field required to be present (e.g., "Every boundary check has `Freshness verdict: FRESH or STALE`"). Non-compliance appears in the output as an unticked or failed item — readable by any evaluator without rubric access. An evaluator-facing summary or post-hoc audit does not satisfy this criterion; the checklist must be part of the model's required output at the phase boundary. |
| C-24 | **Upfront constraint section with inline callback syntax** | behavior | A named constraint section (e.g., STRUCTURAL CONSTRAINTS, PROTOCOL RULES) declares all structural requirements once, prominently, before any role output begins. Each constraint is given a short identifier (e.g., SC-1, R-09). Every role instruction that applies a constraint references it by that identifier at the point of application (e.g., "Apply SC-2:", "Per SC-2, Stage N+1 may not be written until…", "[SC-3: compare Elapsed…]"). C-19 requires a declared citation convention; C-20 requires a write-order prohibition; C-24 requires that these and other structural requirements be consolidated in one upfront section and back-referenced by name at every enforcement point, creating two-level enforcement: declaration and inline callback. A variation that declares constraints upfront without inline callbacks, or applies constraints inline without an upfront declaration section, does not pass. |

---

## Scoring Worksheet

```
Essential passed:     ___ / 4    =>  (___ / 4)  * 60 = ___
Recommended passed:   ___ / 3    =>  (___ / 3)  * 30 = ___
Aspirational passed:  ___ / 17   =>  (___ / 17) * 10 = ___
                                     Composite       = ___

Golden: all 4 essential pass AND composite >= 80
```

---

## Criterion rationale — v6 additions

**C-22 (formal pre-declared registry table)** is a strictly stronger form of C-19. C-19 requires that citation targets follow a declared, consistent convention. C-22 requires that all citation targets be pre-registered as rows in a structured table before any role output — making the target set enumerable and column-verifiable rather than discoverable only by scanning the output. A variation can satisfy C-19 with a prefix declaration or flat label list without producing a table. V-02 and V-05's `[A-xx]` REGISTRY TABLES with owner and description columns satisfy C-22; prefix-only approaches (V-01, V-04) and flat label registries (V-03) do not.

**C-23 (phase gate self-verification checklists)** is a new enforcement pattern. Prior criteria establish structural requirements (C-11, C-14, C-18, C-21) and require the model to satisfy them — but compliance is evaluated externally by the scorer. C-23 requires that the model produce a checklist at a phase boundary and tick each item, making compliance self-documenting in the output artifact. An unticked item is visible to any reader without rubric access. V-04's PHASE 2 GATE — which checks C-11/C-12/C-14/C-21 per boundary before Phase 3 — is the canonical exemplar.

**C-24 (upfront constraint section with inline callback syntax)** is a new two-level enforcement pattern that extends C-20 and C-19 into a general architectural principle. C-20 requires a write-order prohibition; C-19 requires a citation convention. C-24 requires that all structural requirements — including those from C-19 and C-20 — be consolidated in a named upfront section with short identifiers, and that every enforcement point in role instructions reference the constraint by identifier. Prior rounds enforced constraints inline or declared them upfront; V-03 (Protocol Rules) and V-05 (STRUCTURAL CONSTRAINTS) do both, creating a named declaration that can be audited at the top and a callback trail that can be traced through the roles.
