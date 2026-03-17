Reading the v17 rubric and R17 scorecard carefully before deriving the new criteria.

**R17 excellence signals:**

**C-52** emerges from V-04 C-51 PASS+: "Full per-SC table matches R17 variation summary." C-51 requires each SC entry to carry a detectability-location qualifier; C-52 requires those qualifiers to be consolidated into a standalone DETECTABILITY INDEX covering every SC in the prompt — not only the closed-chain entries — forming a single machine-scannable reference.

**C-53** emerges from V-04 C-50 PASS+: C-50 names four specific SCs (SC-8, SC-9, SC-11, SC-13) as the dual-slot set; the PASS+ signal is that every SC referencing **any** `[A-xx]` registry token must exhibit the same dual-slot anchoring — not limited to [A-01]-bearing SCs. An SC referencing [A-05], [A-08], or [A-13] that names the token in the governed-artifact slot but omits it from the enforcement clause is a single-slot violation.

---

```markdown
# flow-dataflow Rubric — v18

## Change Log

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10..C-12 from R1 excellence signals: pre-trace vocabulary gate, interleaved boundary gates, domain entity exposure per boundary |
| v3 | 2026-03-14 | Added C-13..C-15 from R2 excellence signals: pre-declared staleness contract, additive elapsed time calculation, incumbent baseline section |
| v4 | 2026-03-14 | Added C-16..C-18 from R3 excellence signals: cross-role reference chain, immutability declaration, incremental boundary elapsed computation |
| v5 | 2026-03-14 | Added C-19..C-21 from R4 excellence signals: machine-verifiable citation convention, stage-write progression gate, binary freshness verdict per boundary |
| v6 | 2026-03-14 | Added C-22..C-24 from R5 excellence signals: formal pre-declared registry table, phase gate self-verification checklists, upfront constraint section with inline callback syntax |
| v7 | 2026-03-14 | Added C-25..C-27 from R6 excellence signals: phase gate artifacts as first-class registry rows, non-natural role ordering as citation stress test, named recovery formula anchoring incumbent baseline |
| v8 | 2026-03-14 | Added C-28..C-30 from R7 excellence signals: named-column boundary block schema for column-level completeness verification, trade-off analysis as prompt-required section with baseline token citation, output register declaration with format-specific field-compliance markers |
| v9 | 2026-03-15 | Added C-31..C-33 from R8 excellence signals: pre-declared boundary block schema section, register-specific compliance marker mapping per structural field, register-invariant declaration for non-tabular output registers |
| v10 | 2026-03-14 | Added C-34..C-35 from R9 excellence signals: per-boundary incumbent equivalent column with token-cited baseline derivation, INCUMBENT TOTAL as required pre-trade-off closing artifact with additive breakdown and token citation in trade-off section |
| v11 | 2026-03-15 | Added C-36..C-38 from R10 excellence signals: baseline-first artifact ordering for citation-complete boundary cells, REGISTER DECLARATION Parts A/B as single-location C-34/C-35 authority, skip-level citation requirement in non-natural role ordering |
| v12 | 2026-03-15 | Added C-39..C-41 from R11 excellence signals: skip-level SC must name governed role in its body, skip-level SC must declare position distance in its body, Phase Gate 2 skip-level verification item must cite governing SC identifier by number |
| v13 | 2026-03-15 | Added C-42..C-43 from R12 excellence signals: C-37+C-41 closed verification chain as co-occurrence requirement, all three skip-level SC attributes co-present in a single SC block without distribution |
| v14 | 2026-03-15 | Added C-44..C-45 from R13 excellence signals: baseline-closure SC as named upfront constraint enforcing C-15's C-08/C-09 connection by token callback, format-mode declaration with criterion substitution map for non-tabular register variants |
| v15 | 2026-03-15 | Added C-46..C-47 from R14 excellence signals: SC-13 BASELINE CLOSURE as named navigation entry in REGISTER DECLARATION closed-chain paragraph, SC-14 FORMAT MODE DECLARATION as named navigation entry in REGISTER DECLARATION closed-chain paragraph for non-tabular variants |
| v16 | 2026-03-15 | Added C-48..C-49 from R15 excellence signals: governed artifact tokens named in each SC closed-chain entry, enforcement mechanism named in each SC closed-chain entry |
| v17 | 2026-03-15 | Added C-50..C-51 from R16 excellence signals: baseline authority token dual-slot presence per SC closed-chain entry, violation-detectability location in enforcement mechanism |
| v18 | 2026-03-15 | Added C-52..C-53 from R17 excellence signals: per-SC detectability index as standalone reference consolidating all SC detectability locations, dual-slot anchoring extended to all token-referencing SCs beyond [A-01] |

## Purpose

Score a `flow-dataflow` skill output: a data lineage trace covering source, transformation stages,
and destination for a Finance, Operations, or Commerce pipeline scenario.

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

## Aspirational Criteria (weight: 10 pts total) — **46 criteria in v18**

Weight per criterion: 10 / 46 ≈ **0.217 pts**. PARTIAL = 50% of criterion weight (≈ 0.109 pts).

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
| C-18 | **Incremental boundary elapsed computation** | depth | Each boundary check names its own latency contribution as an explicit increment on the running elapsed total from C-14. A boundary that states its latency without tying it to the cumulative total does not pass. |
| C-19 | **Machine-verifiable citation convention** | format | All artifact references use `[A-xx]` token form throughout the prompt. A missing `[A-xx]` where one is required constitutes a violation detectable without reading surrounding context. Free-form artifact names without bracket-token form do not pass. |
| C-20 | **Stage-write progression gate** | behavior | SC-2 functions as an explicit inline gate: the model may not write the content of Stage N until the preceding boundary check between Stage N-1 and Stage N is completed inline. A trailing boundary summary that is not an inline gate does not satisfy. |
| C-21 | **Binary freshness verdict per boundary** | format | SC-4 mandates exactly the token `FRESH` or exactly the token `STALE` as the verdict cell at every boundary. Free-form latency commentary without a binary verdict does not pass. |
| C-22 | **Formal pre-declared registry table** | format | An ARTIFACT REGISTRY table appears before any role output, listing every `[A-xx]` token with its artifact name and the role responsible for producing it. Artifacts introduced without a registry entry do not pass. |
| C-23 | **Phase gate self-verification checklists** | behavior | [A-05] (Phase Gate 1) and [A-08] (Phase Gate 2) are required named artifacts, each containing a checklist. Every checklist item names the SC it verifies. Phase gate artifacts that lack checklist items or omit SC citations do not pass. |
| C-24 | **Upfront constraint section with inline callback syntax** | format | A STRUCTURAL CONSTRAINTS section appears before any role output. Each constraint uses `[Apply SC-N at <location>]` callback syntax at every inline occurrence point. A STRUCTURAL CONSTRAINTS section without inline callbacks does not pass. |
| C-25 | **Phase gate artifacts as first-class registry rows** | format | [A-05], [A-08], and any additional phase gate artifacts (e.g., [A-00]) each appear as named rows in ARTIFACT REGISTRY with their producing-role assignment. A phase gate artifact absent from ARTIFACT REGISTRY does not pass. |
| C-26 | **Non-natural role ordering as citation stress test** | behavior | The role execution order is non-natural — the first role is not Finance — forcing citation chains to follow actual artifact dependency order rather than domain-canonical (Finance-first) order. Finance-first ordering does not satisfy this criterion. |
| C-27 | **Named recovery formula anchoring incumbent baseline** | depth | Recovery prescriptions in [A-12] use the formula `Fall back to [A-01] if [specific named failure condition]`, naming both the baseline artifact token ([A-01]) and a concrete, named failure trigger. A generic fallback instruction without [A-01] citation or without a named trigger condition does not pass. |
| C-28 | **Named-column boundary block schema** | format | A standalone BOUNDARY BLOCK SCHEMA section declares the exact column order for all boundary tables. The schema appears before role output, enabling column-level completeness verification without reading the tables. A boundary schema embedded inline within a role does not satisfy. |
| C-29 | **Trade-off analysis as prompt-required section** | behavior | SC-8 mandates [A-14] as a required named section. The section cites at least one `[A-xx]` baseline token and provides ≥2 explicitly stated trade-off dimensions. An optional, unconditional, or citation-free trade-off section does not pass. |
| C-30 | **Output register declaration with format-specific field-compliance markers** | format | A REGISTER DECLARATION section with Part A (field-compliance mapping) and Part B (INCUMBENT TOTAL structure) appears before role output. Part A maps each required boundary field to its column header, required cell form, and a disqualifying cell form. |
| C-31 | **Pre-declared boundary block schema section** | format | The BOUNDARY BLOCK SCHEMA section appears before all role output — not mid-prompt or after the first role. Its pre-role position makes it the sole citable schema authority for boundary completeness verification. |
| C-32 | **Register-specific compliance marker mapping** | format | REGISTER DECLARATION Part A provides a four-column mapping for every required boundary field: (1) field name, (2) exact column header, (3) required cell form, (4) disqualifying cell form. Partial mapping — covering some fields but not all — does not pass. |
| C-33 | **Register-invariant declaration for non-tabular registers** | format | For non-tabular output variants, REGISTER DECLARATION Part A is reformulated as a labeled-sentence compliance map that preserves field-completeness verification without requiring tabular structure. A prompt that includes a non-tabular variant but only declares tabular compliance does not pass. |
| C-34 | **Per-boundary incumbent equivalent column** | depth | Every boundary table row includes an `Incumbent Equiv.` column citing `[A-01]: [named manual step + duration]`. A boundary row that omits the incumbent-equivalent cell does not pass. |
| C-35 | **INCUMBENT TOTAL as required pre-trade-off artifact** | depth | REGISTER DECLARATION Part B defines [A-13] as an additive role-by-role elapsed total with a Grand Total row. [A-13] must appear before [A-14] in the output sequence and must be cited by token in [A-14]. A trade-off section that does not reference [A-13] does not pass. |
| C-36 | **Baseline-first artifact ordering** | behavior | SC-11 enforces a positional lock: [A-01] must be written before any stage trace or boundary block in the output. A prompt that permits [A-01] to be deferred until after Stage 1 is written does not satisfy. |
| C-37 | **REGISTER DECLARATION Parts A/B as single-location authority** | format | REGISTER DECLARATION includes the verbatim statement: "This section is the sole authoritative reference for C-34 and C-35." No other prompt section may define the Part A field-compliance map or the Part B INCUMBENT TOTAL structure. |
| C-38 | **Skip-level citation requirement** | behavior | SC-12 requires the third-executing role (in non-natural ordering) to cite boundary artifacts produced by the first-executing role, skipping the immediately preceding role. A prompt that only requires sequential role citations does not satisfy. |
| C-39 | **Skip-level SC names governed role** | behavior | SC-12 body text names the governing (first-executing, skipped-to) role by its role label — not by role number alone or by a generic reference. A body text that says "the first role" without naming the role label does not pass. |
| C-40 | **Skip-level SC declares position distance** | behavior | SC-12 body text explicitly states the position distance (e.g., "Position distance is two"). An SC-12 that implies skip-level behavior without naming the ordinal distance does not pass. |
| C-41 | **Phase Gate 2 skip-level item cites SC identifier** | behavior | [A-08] Phase Gate 2 checklist includes an item that verifies SC-12 compliance and cites "`[SC-12]`" by its numbered identifier. A checklist item that verifies skip-level behavior without citing the SC number does not pass. |
| C-42 | **C-37+C-41 closed verification chain co-occurrence** | behavior | Both REGISTER DECLARATION Parts A/B (satisfying C-37) and a Phase Gate 2 `[SC-12]`-citing item (satisfying C-41) are present in the same prompt. A prompt with only one of these elements does not satisfy the closed-chain co-occurrence requirement. |
| C-43 | **All three skip-level SC attributes co-present in single block** | format | SC-12 contains all three required attributes — (1) governed artifact token, (2) governed role name, (3) position distance — in a single contiguous block. Distributing any attribute across multiple SCs or sections does not pass. |
| C-44 | **Baseline-closure SC as named upfront constraint** | behavior | SC-13 BASELINE CLOSURE appears in the STRUCTURAL CONSTRAINTS section and enforces that [A-01] is cited in both [A-12] (recovery prescriptions, satisfying C-08) and [A-14] (trade-off analysis, satisfying C-09), closing the C-15 comparison loop. An SC-13 that requires [A-01] citation in only one of these artifacts does not pass. |
| C-45 | **Format-mode declaration with criterion substitution map** | format | SC-14 FORMAT MODE DECLARATION names the active output format and provides an explicit substitution map: for each tabular criterion (e.g., C-28, C-32, C-34), it names the non-tabular equivalent form that satisfies the criterion in the active mode. A mode declaration without a criterion-by-criterion substitution map does not pass. |
| C-46 | **SC-13 BASELINE CLOSURE as named entry in closed-chain paragraph** | format | The REGISTER DECLARATION closed-chain paragraph contains a named entry labeled "SC-13 BASELINE CLOSURE" that specifies the governed artifacts ([A-12], [A-14]) and describes its enforcement mechanism. An unlabeled or implicit SC-13 reference does not pass. |
| C-47 | **SC-14 FORMAT MODE DECLARATION as named closed-chain entry** | format | For non-tabular variants, the REGISTER DECLARATION closed-chain paragraph contains a named entry labeled "SC-14 FORMAT MODE DECLARATION" specifying the governed format-substitution scope and enforcement mechanism. Its absence when non-tabular mode is active is a protocol violation detectable from the closed-chain paragraph alone. |
| C-48 | **Governed artifact tokens named in each SC closed-chain entry** | format | Every entry in the REGISTER DECLARATION closed-chain paragraph names the `[A-xx]` token(s) it governs. An entry that describes enforcement without naming a governed artifact token does not pass. |
| C-49 | **Enforcement mechanism named in each SC closed-chain entry** | format | Every entry in the REGISTER DECLARATION closed-chain paragraph describes its enforcement pathway by name (e.g., "positional lock", "header-callback", "cell-form requirement"). A closed-chain entry that names governed tokens but does not describe how the constraint is enforced does not pass. |
| C-50 | **Baseline authority token dual-slot presence** | format | In every SC closed-chain entry that governs [A-01]-referencing behavior, the token `[A-01]` appears in BOTH the governed-token declaration slot AND the enforcement mechanism slot of the same entry. An entry where `[A-01]` appears in the governed-token slot but is absent from the enforcement clause does not pass. |
| C-51 | **Violation-detectability location in enforcement mechanism** | format | Every SC entry in the REGISTER DECLARATION closed-chain paragraph includes a detectability-location qualifier in its enforcement mechanism description — a phrase naming where in the prompt structure a violation surfaces (e.g., "detectable from the header line alone", "detectable at the role-opener line"). An enforcement description without a detectability-location qualifier does not pass. |
| C-52 | **Per-SC detectability index as standalone reference** | format | A named DETECTABILITY INDEX section — or an equivalent named table within STRUCTURAL CONSTRAINTS — consolidates every SC identifier with its violation-detection location phrase in a single machine-scannable reference. The index covers all SCs in the prompt, not only the closed-chain entries; coverage is verifiable by matching row count to SC count. Detectability information embedded solely in individual SC prose bodies without a dedicated summary index does not pass. |
| C-53 | **Dual-slot anchoring extends to all token-referencing SCs** | format | Dual-slot anchoring (C-50) applies to every SC in the prompt that references any `[A-xx]` registry token — not limited to [A-01]-referencing SCs. An SC that names [A-05], [A-08], [A-13], or any other registry token in its governed-artifact slot must also name that same token in its enforcement clause. A prompt where dual-slot is present for [A-01]-bearing SCs but absent for other token-bearing SCs does not pass. |
```
