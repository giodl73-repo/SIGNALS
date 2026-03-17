Reading the scorecard evidence carefully to extract the R15 excellence signals before writing.

Two new patterns emerge from the R15 scorecard:

**C-48**: V-01 C-46 evidence — "Governing authority named; **[A-12] and [A-14] both named**." The closed-chain entry doesn't merely name the SC; it names the governed artifact tokens, making the entry a navigable index from register → SC → governed section without reading the SC body.

**C-49**: V-01 C-46 evidence — "its inline callbacks at both section headers enforce the [A-01] citation obligation **by token match without output-prose inspection**." The enforcement mechanism is named in the entry itself, making the closed-chain paragraph a self-describing authority map.

Both apply universally to every SC listed in the closed-chain paragraph.

---

```markdown
# flow-dataflow Rubric — v16

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

## Aspirational Criteria (weight: 10 pts total) — **42 criteria in v16**

Weight per criterion: 10 / 42 ≈ **0.238 pts**. PARTIAL = 50% of criterion weight (≈ 0.119 pts).

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
| C-20 | **Stage-write progression gate** | behavior | A hard gate constraint — "Stage N+1 may not be written until the preceding BOUNDARY CHECK block is fully populated" — appears as an SC-numbered inline callback at every stage advance in STRUCTURAL CONSTRAINTS. A gate stated once without per-transition callbacks does not pass. |
| C-21 | **Binary freshness verdict per boundary** | behavior | Each boundary block carries a binary verdict — exactly `FRESH` or `STALE`, no other form — derived by comparing cumulative elapsed against the C-13 threshold. A verdict that uses qualitative language or omits the verdict entirely does not pass. |
| C-22 | **Formal pre-declared registry table** | format | An ARTIFACT REGISTRY table is declared before any role output begins, enumerating every artifact by ID, name, owner, and description. A registry assembled during role output or lacking pre-declaration does not pass. |
| C-23 | **Phase gate self-verification checklists** | behavior | At least two phase gates (e.g., post-first-role and post-second-role) appear as named artifacts in the registry and carry a self-verification checklist with each item individually ticked (✓ or ✗). The next role is explicitly gated on checklist completion. |
| C-24 | **Upfront constraint section with inline callbacks** | format | A STRUCTURAL CONSTRAINTS section precedes all role output and each SC carries an inline callback directive (`[Apply SC-N at every ...]`) that will be triggered at every applicable structural position. A constraint listed without a callback directive does not pass. |
| C-25 | **Phase gate artifacts as registry rows** | format | Both phase gate artifacts (post-first-role and post-second-role) appear as named rows in the ARTIFACT REGISTRY with ID, owner, and description. Phase gates that exist only in role prose without registry registration do not pass. |
| C-26 | **Non-natural role ordering as citation stress test** | behavior | The variation uses a non-default role sequence that forces at least one role to skip over an intervening role when citing, creating a verifiable skip-level citation requirement. A natural or default role ordering does not satisfy this criterion. |
| C-27 | **Named recovery formula anchoring incumbent baseline** | depth | The recovery prescriptions section requires a named formula (e.g., `Fall back to [A-01] if [specific failure condition]`) that anchors every prescription to the incumbent baseline artifact by token. A recovery section without a named formula anchored to the baseline token does not pass. |
| C-28 | **Named-column boundary block schema** | format | A BOUNDARY BLOCK SCHEMA section declares the required column names and their ordering for every boundary block. Column names in the schema must match the Part A compliance marker table exactly. A schema implied by example or stated informally does not pass. |
| C-29 | **Trade-off as prompt-required section with baseline token citation** | behavior | The trade-off section is declared as a required artifact in STRUCTURAL CONSTRAINTS (not optional) and its prompt instruction requires citation of at least three named tokens including the incumbent baseline. A trade-off that is optional or lacks mandatory baseline token citation does not pass. |
| C-30 | **Output register declaration with field-compliance markers** | format | A REGISTER DECLARATION section (Parts A and B) appears in STRUCTURAL CONSTRAINTS, enumerating every required field with its required cell form and at least one disqualifying form. A register with no compliance marker table does not pass. |
| C-31 | **Pre-declared boundary block schema section** | format | The BOUNDARY BLOCK SCHEMA is a standalone named section declared before any role output begins — not embedded in a role's instructions or in the register declaration. A schema that appears only inside a role block or as an inline note does not pass. |
| C-32 | **Register-specific compliance marker mapping per structural field** | format | REGISTER DECLARATION Part A maps each required field to three items: Column Header (exact string), Required Cell Form (machine-parseable pattern), and Disqualifying Form. A Part A that lists required fields without mapping all three items does not pass. |
| C-33 | **Register-invariant declaration for non-tabular output registers** | format | For non-tabular register variants, a REGISTER-INVARIANT section explicitly lists the structural fields that must appear in prose output regardless of format. A non-tabular register with no invariant declaration does not pass. (Conditional: applies only when C-45 format-mode declaration is active.) |
| C-34 | **Incumbent Equiv. column with token-cited baseline derivation** | depth | REGISTER DECLARATION Part A is the sole authoritative reference for the `Incumbent Equiv.` cell form. Every boundary block's incumbent equivalent cell derives its value from the baseline artifact by token (e.g., `[A-01]: [named manual step + duration]`). A cell that states an equivalent without citing the baseline token does not pass. |
| C-35 | **INCUMBENT TOTAL before trade-off** | behavior | REGISTER DECLARATION Part B is the sole authoritative reference for the INCUMBENT TOTAL section format. This section appears immediately before the trade-off section, with a per-role breakdown table and a Grand Total row cited by artifact token in the trade-off section. An INCUMBENT TOTAL appearing elsewhere or without role breakdown does not pass. |
| C-36 | **Baseline-first artifact ordering** | behavior | A named SC explicitly prohibits any boundary block or stage trace from appearing before the incumbent baseline artifact is fully produced. The constraint must name the baseline artifact by token. An ordering constraint implied or stated without token reference does not pass. |
| C-37 | **REGISTER DECLARATION Parts A/B as single-location authority** | format | REGISTER DECLARATION explicitly states that it is the sole authoritative reference for the `Incumbent Equiv.` cell form (C-34) and the INCUMBENT TOTAL section format (C-35). A register that defines compliance markers in multiple locations does not pass. |
| C-38 | **Skip-level citation requirement in non-natural ordering** | behavior | For non-natural role sequences, a named SC requires the last role to cite an artifact from the first role (skipping the middle role), creating a verified skip-level citation. The SC must name the specific artifact token and citation field. |
| C-39 | **Skip-level SC names governed role** | format | The skip-level SC names the role it governs (e.g., "Commerce's `Citing:` line must include...") in its own body text. A skip-level SC that states the citation requirement without naming the governed role does not pass. |
| C-40 | **Skip-level SC declares position distance** | format | The skip-level SC explicitly states the position distance between the skipping role and the cited role (e.g., "The position distance is two: Commerce occupies position 3, Finance occupies position 1"). A skip-level SC without a stated position distance does not pass. |
| C-41 | **Phase Gate 2 item cites governing SC by identifier** | format | The Phase Gate 2 checklist contains at least one item that cites the skip-level SC by its SC identifier number (e.g., `[SC-12]`). An item that references the requirement without citing the SC number does not pass. |
| C-42 | **C-37 + C-41 closed verification chain co-occurrence** | behavior | Both C-37 (REGISTER DECLARATION as single-location authority) and C-41 (Phase Gate 2 item citing the skip-level SC by number) must be present in the same output. Either alone is insufficient; their co-occurrence closes the register-to-verification chain. |
| C-43 | **All three skip-level SC attributes in a single SC block** | format | The skip-level SC block contains all three required attributes — governed role named, position distance declared, Phase Gate 2 citation instruction — in a single block without distributing them across multiple SCs or notes. |
| C-44 | **Baseline-closure SC enforcing C-15's C-08/C-09 connection** | behavior | SC-13 BASELINE CLOSURE appears as a named constraint in STRUCTURAL CONSTRAINTS and requires the incumbent baseline artifact token to appear in both the recovery section (C-08) and the trade-off section (C-09), with inline callbacks at both section headers. An SC that requires C-15 without enforcing its C-08/C-09 connection by token callback does not pass. |
| C-45 | **Format-mode declaration with criterion substitution map (non-tabular)** | format | For non-tabular output registers, SC-14 FORMAT MODE DECLARATION appears in STRUCTURAL CONSTRAINTS and provides an explicit criterion substitution map — listing which tabular criteria are replaced by prose equivalents and what form those equivalents take. A format-mode declaration without a substitution map does not pass. (Conditional: applies only for non-tabular variants.) |
| C-46 | **SC-13 as named navigation entry in closed-chain paragraph** | format | REGISTER DECLARATION's closed-chain paragraph names SC-13 BASELINE CLOSURE as a navigation entry with a governing authority statement. A closed-chain paragraph that omits SC-13 or names it without a governing authority declaration does not pass. (Universal.) |
| C-47 | **SC-14 as named navigation entry in closed-chain paragraph (non-tabular)** | format | For non-tabular variants, REGISTER DECLARATION's closed-chain paragraph names SC-14 FORMAT MODE DECLARATION as a navigation entry with a governing authority statement for format-mode compliance failures. A closed-chain paragraph that omits SC-14 when it is active does not pass. (Conditional: applies only when SC-14 is active.) |
| C-48 | **Governed artifact tokens named in each SC closed-chain entry** | format | Each SC entry in the REGISTER DECLARATION closed-chain paragraph names by artifact token every artifact it governs (e.g., "governing authority for ... in [A-12] and [A-14]"). A closed-chain SC entry that names the SC without naming its governed artifact tokens does not pass. (Universal: applies to every SC listed in the closed-chain paragraph.) |
| C-49 | **Enforcement mechanism named in each SC closed-chain entry** | behavior | Each SC entry in the REGISTER DECLARATION closed-chain paragraph includes a named enforcement pathway — describing how the SC enforces compliance (e.g., "inline callbacks at both section headers enforce ... by token match without output-prose inspection"). A closed-chain entry that states authority without naming the enforcement mechanism does not pass. (Universal: applies to every SC listed in the closed-chain paragraph.) |
```
