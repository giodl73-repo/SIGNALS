Reading the scorecard carefully before writing.

**New patterns from R16:**

**C-50** emerges from V-04 C-48 PASS+: "SC-8, SC-9, SC-11, SC-13 entries explicitly name [A-01] in **both** governed-token declaration **and** enforcement mechanism." C-48 requires governed tokens named; C-50 requires the same authority token to appear in both slots of the same entry — dual-slot anchoring.

**C-51** emerges from V-04 C-49 PASS+: "its absence is a protocol violation **detectable from the header line alone**." C-49 requires the mechanism named; C-51 requires the mechanism description to include a detectability-location claim — where in the structure a violation surfaces.

---

```markdown
# flow-dataflow Rubric — v17

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

## Aspirational Criteria (weight: 10 pts total) — **44 criteria in v17**

Weight per criterion: 10 / 44 ≈ **0.227 pts**. PARTIAL = 50% of criterion weight (≈ 0.114 pts).

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
| C-19 | **Machine-verifiable citation convention** | format | Every citation to a named artifact or section uses a token format (e.g., [A-NN], SC-N) that can be verified by string match against the registry without reading surrounding prose. Citations using only prose titles or back-references ("as above") do not pass. |
| C-20 | **Stage-write progression gate** | behavior | An explicit named constraint forbids any role from writing a lineage stage until all prior roles have finalized their stages. The gate is declared in STRUCTURAL CONSTRAINTS with its enforcement mechanism named. An implied ordering without a named, enforced gate does not pass. |
| C-21 | **Binary freshness verdict per boundary** | behavior | Every boundary check block concludes with an explicit FRESH / STALE verdict (or binary equivalent) derived from C-14's cumulative elapsed total vs. C-13's declared threshold. A boundary that discusses staleness without a binary verdict does not pass. |
| C-22 | **Formal pre-declared registry table** | format | The [A-01]–[A-NN] artifact registry is declared as a formal table before any role writes. The table lists artifact ID, artifact name, and owning role for every artifact the trace will reference. A registry appended after the trace or missing the owning-role column does not pass. |
| C-23 | **Phase gate self-verification checklists** | behavior | Each named phase gate contains an explicit itemized checklist that the model verifies before proceeding. Each checklist item must reference at least one artifact token from C-22's registry. A phase gate with prose instructions but no itemized checklist does not pass. |
| C-24 | **Upfront constraint section with inline callback syntax** | format | A STRUCTURAL CONSTRAINTS section appears before Stage 1 and lists each constraint with its inline callback syntax (e.g., "cite as [A-NN]"). Constraints introduced mid-trace, or constraints without associated callback syntax, do not pass. |
| C-25 | **Phase gate artifacts as first-class registry rows** | format | Phase gate completion artifacts are registered as named [A-NN] rows in C-22's registry table with their own artifact IDs. A phase gate output that is referenced in prose but not registered as a named row does not pass. |
| C-26 | **Non-natural role ordering as citation stress test** | behavior | Roles are ordered in a non-natural sequence (any order other than Finance → Operations → Commerce), and this ordering is explicitly stated as a citation stress test designed to exercise skip-level and cross-role citation requirements. Natural Finance → Operations → Commerce ordering does not satisfy this criterion. |
| C-27 | **Named recovery formula anchoring incumbent baseline** | depth | The INCUMBENT BASELINE section includes a named formula that quantifies the incumbent's failure rate, latency, or cost using at least one registry token citation. The formula must surface a value that reappears in C-08 (recovery prescriptions) or C-09 (trade-off analysis) by token callback. A qualitative baseline without a named, token-anchored formula does not pass. |
| C-28 | **Named-column boundary block schema** | format | A BOUNDARY BLOCK SCHEMA section names every column that will appear in each boundary check table before any boundary block is written. Column names in the schema must match boundary block column headers verbatim. A boundary block with unschematized columns, or a schema declared after any boundary block, does not pass. |
| C-29 | **Trade-off analysis as prompt-required section with baseline token citation** | behavior | STRUCTURAL CONSTRAINTS names the TRADE-OFF ANALYSIS section as prompt-required and mandates at least one citation to the incumbent baseline by registry token (e.g., [A-NN]). A trade-off section that references the baseline by prose name without a token citation does not pass. |
| C-30 | **Output register declaration with format-specific field-compliance markers** | format | The REGISTER DECLARATION includes compliance markers for every structural field in the output (e.g., ✓ / × or equivalent field-level tags). Markers must be format-specific: tabular fields carry column-presence markers; non-tabular fields carry label-sequence markers. A register without per-field compliance markers does not pass. |
| C-31 | **Pre-declared boundary block schema section** | format | The BOUNDARY BLOCK SCHEMA from C-28 is a standalone named section, not a subsection of STRUCTURAL CONSTRAINTS. It appears before Stage 1 and enumerates every required field for every boundary block type. A schema embedded as a subsection rather than a standalone named section does not pass. |
| C-32 | **Register compliance marker mapping per structural field** | format | Each compliance marker in C-30's REGISTER DECLARATION is mapped to the specific criterion it satisfies (e.g., "[A-04] boundary check → C-11 ✓"). A register with markers but no criterion cross-reference mapping does not pass. |
| C-33 | **Register-invariant declaration for non-tabular output registers** | depth | The REGISTER DECLARATION includes a REGISTER INVARIANT block naming at least one structural property that is preserved across tabular and non-tabular format modes. A register that handles format variation without declaring its invariant properties does not pass. |
| C-34 | **Per-boundary incumbent equivalent column with token-cited baseline derivation** | depth | Every boundary check table includes an INCUMBENT EQUIVALENT column. Each cell in that column cites the incumbent baseline source by registry token (e.g., "from [A-NN]"). A boundary that omits the INCUMBENT EQUIVALENT column, or fills it without a token citation, does not pass. |
| C-35 | **INCUMBENT TOTAL as pre-trade-off closing artifact with additive breakdown** | depth | The trace produces an INCUMBENT TOTAL artifact registered as [A-NN] that sums INCUMBENT EQUIVALENT values across all boundaries with an itemized additive breakdown. This artifact appears immediately before TRADE-OFF ANALYSIS and is cited by token in that section. An incumbent total synthesized within the trade-off section rather than pre-registered does not pass. |
| C-36 | **Baseline-first artifact ordering in citation-complete boundary cells** | format | In each boundary check table, the INCUMBENT EQUIVALENT cell appears before the proposed pipeline value cell (above or to the left). This ordering ensures the baseline is declared before comparison. A table where the incumbent equivalent follows the proposed value does not pass. |
| C-37 | **REGISTER DECLARATION Parts A/B as single-location C-34/C-35 authority** | format | The REGISTER DECLARATION is structured as Part A (per-boundary INCUMBENT EQUIVALENT column declarations, satisfying C-34) and Part B (INCUMBENT TOTAL artifact declaration, satisfying C-35), both within a single contiguous named section. Splitting Parts A and B into separate sections does not pass. |
| C-38 | **Skip-level citation requirement in non-natural role ordering** | behavior | In any non-natural role sequence satisfying C-26, a role that cites an artifact owned by a non-adjacent role must use an explicit skip-level citation (e.g., "skip-level cite: [A-NN] from Role 1 to Role 3"). A cross-role citation across a skip without skip-level notation does not pass. |
| C-39 | **Skip-level SC names governed role in its body** | behavior | The structural constraint governing skip-level citation (satisfying C-38) names the governed role explicitly in its body text (e.g., "This constraint governs Role 3's citation of Role 1 artifacts"). An SC body that describes the skip-level rule without naming the governed role does not pass. |
| C-40 | **Skip-level SC declares position distance in its body** | behavior | The skip-level governing SC satisfying C-39 explicitly states the positional distance of the skip in its body (e.g., "position distance = 2: Role 3 cites Role 1, skipping Role 2"). An SC that names the governed role but omits the numerical position distance does not pass. |
| C-41 | **Phase Gate 2 skip-level verification item cites governing SC identifier** | behavior | Phase Gate 2's verification checklist includes at least one item that cites the skip-level governing SC by its identifier (e.g., "Skip-level citation present per [SC-12]?"). A checklist item that checks the skip-level citation without naming the governing SC does not pass. |
| C-42 | **C-37+C-41 closed verification chain as co-occurrence requirement** | behavior | C-37 (REGISTER DECLARATION Parts A/B) and C-41 (Phase Gate 2 SC citation) must co-occur: the REGISTER DECLARATION's closed-chain paragraph cross-references the skip-level SC, and Phase Gate 2 verifies compliance against that same SC. Either element in isolation does not pass. |
| C-43 | **All three skip-level SC attributes co-present in a single SC block** | behavior | The skip-level SC satisfying C-39, C-40, and C-41 presents all three attributes — governed role name, position distance, and Phase Gate 2 citation trigger — within a single contiguous SC block without distributing them across multiple SCs or sections. Spreading these attributes across multiple locations does not pass. |
| C-44 | **Baseline-closure SC as named upfront constraint enforcing C-15's C-08/C-09 connection** | behavior | STRUCTURAL CONSTRAINTS includes a named SC (e.g., SC-13 BASELINE CLOSURE) that mandates the incumbent baseline's connection to both recovery prescriptions (C-08) and trade-off analysis (C-09) via inline token callbacks placed at those sections' headers. An SC that names the baseline without specifying inline callbacks at both sites does not pass. |
| C-45 | **Format-mode declaration with criterion substitution map for non-tabular register variants** | format | STRUCTURAL CONSTRAINTS includes a named SC (e.g., SC-14 FORMAT MODE DECLARATION) that activates for non-tabular output registers and supplies a substitution map replacing column-form criteria (C-28, C-30, C-32, C-34, C-37) with prose-equivalent label-sequence criteria. An SC that declares non-tabular mode without a complete substitution map does not pass. |
| C-46 | **SC-13 BASELINE CLOSURE as named navigation entry in REGISTER DECLARATION closed-chain paragraph** | format | The REGISTER DECLARATION's closed-chain paragraph contains an explicit named entry for SC-13 (BASELINE CLOSURE) identifying it as governing authority for the baseline-to-analysis connection. SC-13 existing in STRUCTURAL CONSTRAINTS but absent from the closed-chain paragraph does not pass. |
| C-47 | **SC-14 FORMAT MODE DECLARATION as named navigation entry in REGISTER DECLARATION closed-chain paragraph (non-tabular only)** | format | In non-tabular output designs, the REGISTER DECLARATION's closed-chain paragraph contains an explicit named entry for SC-14 (FORMAT MODE DECLARATION). This criterion is inapplicable for tabular designs. A non-tabular design that omits SC-14 from the closed-chain paragraph does not pass. |
| C-48 | **Governed artifact tokens named per SC closed-chain entry** | format | Every SC entry in the REGISTER DECLARATION closed-chain paragraph names the specific [A-NN] artifact tokens the SC governs (e.g., "SC-9 governs [A-04], [A-07], [A-10]"). An SC entry that identifies the SC without listing its governed artifact tokens does not pass. |
| C-49 | **Enforcement mechanism named per SC closed-chain entry** | format | Every SC entry in the REGISTER DECLARATION closed-chain paragraph names the enforcement mechanism (e.g., "enforced by inline callbacks at both section headers verifying [A-01] citation by token match without output-prose inspection"). An SC entry that names governed tokens but omits the enforcement mechanism does not pass. |
| C-50 | **Baseline authority token dual-slot presence per SC closed-chain entry** | format | At least one SC closed-chain entry names the baseline authority token (e.g., [A-01]) in both the governed-token declaration and the enforcement-mechanism description within the same entry (e.g., "SC-13 governs [A-12], [A-14] ... enforced by inline callbacks verifying [A-01] citation"). An entry where the authority token appears in only one slot — governed-token list or enforcement mechanism — but not both, does not pass. |
| C-51 | **Violation-detectability location in enforcement mechanism** | depth | At least one SC closed-chain entry's enforcement-mechanism description includes a detectability statement that names the structural location where a violation would surface (e.g., "detectable from the header line alone", "absent label sequence in any boundary paragraph fails by the substitution map's prescribed form"). Naming the enforcement mechanism without specifying where the violation is detectable does not pass. |
```
