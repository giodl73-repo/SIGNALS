## R14 Scorecard — discover-literature

### Scoring Framework (v14)

| Tier | Criteria | Points each | Max |
|------|----------|-------------|-----|
| Essential | C-01..C-05 | 12 | 60 |
| Recommended | C-06..C-08 | 10 | 30 |
| Aspirational | C-09..C-31 | 5 | 115 |
| **Total** | | | **205** |

---

### Baseline — C-01 through C-30 (all five variations)

All five variations carry the complete R13 V-05 baseline. No variation modifies any structure outside the C-29 Operationalization Verification block. Every criterion from C-01 through C-30 is PASS across all variations.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Claims extracted | PASS | PASS | PASS | PASS | PASS | Phase 1 instructs 3-5 claims as propositions with counter-evidence per claim |
| C-02 Citation table | PASS | PASS | PASS | PASS | PASS | Phase 2 specifies required columns; non-placeholder values mandated by OBLIGATION A |
| C-03 Four-tier map | PASS | PASS | PASS | PASS | PASS | Phase 3 requires FOUNDATIONAL/RECENT/CONTRARY/METHODOLOGICAL headings with entries |
| C-04 Gap analysis | PASS | PASS | PASS | PASS | PASS | Phase 4 produces supported/unsupported claim counts, contrary evidence list, recommendation keyword |
| C-05 Artifact + frontmatter | PASS | PASS | PASS | PASS | PASS | Phase 5 writes to `signals/discover/literature/...` with required YAML fields |
| C-06 Contrary mapped | PASS | PASS | PASS | PASS | PASS | CONTRARY entries require Claim # [n]; Phase 5 Q2 requests named contrary paper + rebuttal strategy |
| C-07 WebSearch visible | PASS | PASS | PASS | PASS | PASS | Phase 2 specifies six WebSearch angle queries; OBLIGATION A blocks placeholders |
| C-08 High-risk flagged | PASS | PASS | PASS | PASS | PASS | Phase 4 Q4: "Are any claims HIGH RISK? For each: scope / qualify / drop?" |
| C-09 Threshold met | PASS | PASS | PASS | PASS | PASS | Depth mode table present; THRESHOLD NOT MET: token with PASS annotation |
| C-10 Precedent chain | PASS | PASS | PASS | PASS | PASS | METHODOLOGICAL: "[year confirmation: predates current work]" required in entry |
| C-11 Interrogative obligation | PASS | PASS | PASS | PASS | PASS | PHASE 1 COMPLETE: carries `evidence_type_mapped` and `counter-evidence-noted` confirmation fields |
| C-12 Anti-placeholder recovery | PASS | PASS | PASS | PASS | PASS | OBLIGATION A with typed schema; RECOVERY NOTE: token with C-12 PASS annotation |
| C-13 Empty-tier acknowledgment | PASS | PASS | PASS | PASS | PASS | OBLIGATION B with typed schema; TIER EMPTY: token; PHASE 3 COMPLETE: carries `tiers_empty_acknowledged` |
| C-14 Inertia guard | PASS | PASS | PASS | PASS | PASS | INERTIA SCENARIO: in Phase 1, INERTIA RISK: in Phase 4, both required before recommendation keyword |
| C-15 Dual-domain preamble | PASS | PASS | PASS | PASS | PASS | ENFORCEMENT CONTRACT opens with both OBLIGATION A and B as non-optional constraints |
| C-16 Template-label checkability | PASS | PASS | PASS | PASS | PASS | INERTIA SCENARIO:, INERTIA RISK:, THRESHOLD NOT MET:, RECOVERY NOTE:, TIER EMPTY:, PHASE N COMPLETE: all named |
| C-17 Contract-to-token binding | PASS | PASS | PASS | PASS | PASS | OBLIGATION A names RECOVERY NOTE: with schema; OBLIGATION B names TIER EMPTY: with schema |
| C-18 Multi-criterion token reuse | PASS | PASS | PASS | PASS | PASS | THRESHOLD NOT MET: annotated as covering C-09 + C-16; RECOVERY NOTE: covering C-12 + C-16 |
| C-19 Typed token schema block | PASS | PASS | PASS | PASS | PASS | Both OBLIGATION A and B use Token/Schema/Fields/Required when/Unacceptable format |
| C-20 Dual multi-criterion synthesis | PASS | PASS | PASS | PASS | PASS | Pair 1 (failure/recovery): C-09, C-12, C-16; Pair 2 (lifecycle): C-09, C-13, C-16; each independently C-20 |
| C-21 Symmetric dual-schema | PASS | PASS | PASS | PASS | PASS | Both obligations declare independent typed schema blocks with verbatim field name propagation |
| C-22 Unconditional lifecycle tokens | PASS | PASS | PASS | PASS | PASS | PHASE 2 COMPLETE: and PHASE 3 COMPLETE: both annotated as unconditional boundary tokens |
| C-23 Full-phase instrumentation | PASS | PASS | PASS | PASS | PASS | All four PHASE N COMPLETE: tokens present; each names boundary and confirms unconditional emission |
| C-24 Redundant dual-path | PASS | PASS | PASS | PASS | PASS | C-24 Independence Verification block present; remove-either-pair test; C-24 PASS declared |
| C-25 N-of-4 counter | PASS | PASS | PASS | PASS | PASS | Each PHASE token carries "Token N of 4 required for C-23 ... C-23 in progress at N/4" annotation |
| C-26 Named independence block | PASS | PASS | PASS | PASS | PASS | "C-24 Independence Verification" labeled section with (a)-(d) structural elements; C-24 PASS declared |
| C-27 Inertia status integration | PASS | PASS | PASS | PASS | PASS | PHASE 1 COMPLETE: carries `inertia_committed=[yes]`; PHASE 4 COMPLETE: carries `inertia_verified=[yes]` |
| C-28 Annotation explicitness | PASS | PASS | PASS | PASS | PASS | Phase 1 annotation: C-27(a) named, single-grep verifiable. Phase 4 annotation: C-27(b) named, additive design confirmed |
| C-29 Attestation operationalization | PASS | PASS | PASS | PASS | PASS | Sub-clause (a)/(b) designation, self-declaring signal ID, grep instruction at both boundaries; six-cell block present |
| C-30 Named verification block | PASS | PASS | PASS | PASS | PASS | "C-29 Operationalization Verification" present in all; six cells confirmed; both grep instructions verbatim; C-29 PASS |

---

### C-31 — C-30 Block Placement Citation

This is the only criterion that differentiates the five variations.

**C-31 pass condition:** The C-30 named block must contain: (a) a labeled field naming the Phase 4 lifecycle token it follows, (b) a labeled field confirming all six cells draw from already-emitted content with no forward-references, and (c) both declarations as labeled fields within the block, not as prose in surrounding context.

#### V-01 — Control (R13 V-05 base, no C-31 additions)

The C-29 Operationalization Verification block closes with: "All six cells confirmed. Both grep instructions stated verbatim in cells (iii) and (vi) above. Dependency chain ... C-30 complete. C-29 PASS."

No PLACEMENT field. No CELL-SOURCE field. The block makes no declaration about its own placement or cell-source provenance.

**C-31: FAIL** — Both (a) and (b) absent. A reviewer cannot confirm from within the block that (a) the block appears after PHASE 4 COMPLETE: or (b) no cell is a forward-reference. C-31 requires self-attestation; distributed correctness without in-block declaration does not satisfy it.

#### V-02 — PLACEMENT only (C-31(a) present, C-31(b) absent)

After "C-29 PASS.", a PLACEMENT field is appended within the block:

> `PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above). C-31(a) status: placement citation present -- the Phase 4 lifecycle token is named explicitly within this block.`

The PLACEMENT field is structurally within the block (before the `---` separator). C-31(a) is satisfied: the Phase 4 lifecycle token is named as a labeled field. However, no CELL-SOURCE field appears. A reviewer reading the block can confirm chronological placement but cannot confirm that cell (vi) is not a forward-reference to unemitted content.

**C-31: FAIL** — C-31(a) PASS, C-31(b) absent. Both-or-nothing property applies identically to the pattern established by C-28/C-29: one element alone does not constitute a both-required pass condition. C-31(b) is independently necessary.

#### V-03 — CELL-SOURCE only (C-31(b) present, C-31(a) absent)

After "C-29 PASS.", a CELL-SOURCE field is appended within the block:

> `CELL-SOURCE: All six cells above draw from already-emitted content -- no cell contains a forward-reference to output not yet produced at block-emission time; all sub-clause designations, self-declaring signal field names, and grep instructions were established in earlier lifecycle token annotations and are restated verbatim here. C-31(b) status: cell-source provenance confirmed within this block.`

C-31(b) is satisfied: cell-source provenance is confirmed as a labeled field within the block. However, no PLACEMENT field appears. A reviewer reading the block knows the six cells do not forward-reference, but cannot confirm from within the block that the block itself was emitted after PHASE 4 COMPLETE:.

**C-31: FAIL** — C-31(b) PASS, C-31(a) absent. Symmetric failure to V-02: cell-source provenance without placement citation leaves the block's chronological position unverifiable from within. Neither element can substitute for the other.

#### V-04 — Both elements as surrounding prose (C-31(c) failure)

A bracketed prose note appears immediately BEFORE the `## C-29 Operationalization Verification` heading:

> `[This operationalization verification block follows the PHASE 4 COMPLETE: lifecycle token above. All six cells draw from already-emitted content in the Phase 1 and Phase 4 lifecycle token annotations; no forward-references are present in any cell.]`

Both C-31(a) and C-31(b) content is present in this prose note. However, the note appears OUTSIDE the block — it precedes the heading that marks the block's opening. The block itself contains no PLACEMENT or CELL-SOURCE labeled fields. C-31(c) is explicit: declarations must "appear as labeled fields or an explicit sub-block within the C-30 block (not as prose in surrounding context)."

A reviewer reading the block alone (from `## C-29 Operationalization Verification` through C-29 PASS) cannot confirm C-31 compliance without reading the preceding prose. This defeats the self-attesting property C-31 is designed to create.

**C-31: FAIL** — C-31(c) binding. Both elements present as surrounding prose but absent as labeled fields within the block. The pre-block note is context, not self-attestation. The parallel is exact: a reviewer auditing only the block has no evidence of placement or cell-source provenance from within the block itself.

#### V-05 — Full ceiling synthesis (C-31 PASS)

The C-29 Operationalization Verification block opens with two labeled fields BEFORE the six cells:

> `PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above) -- the Phase 4 / gap-analysis lifecycle token has been declared before this block emits; no forward-reference to future Phase 4 content is possible. C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block.`
>
> `CELL-SOURCE: All six cells below draw from already-emitted content -- Phase 1 and Phase 4 lifecycle token annotations have both been written before this block; no cell contains a forward-reference to output not yet produced at block-emission time; all sub-clause designations, self-declaring signal field names, and grep instructions were established in earlier annotations and are restated verbatim here. C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block.`

The block closes with explicit C-31 sub-clause confirmation:

> `C-31 PASS: PLACEMENT labeled field (within this block) names PHASE 4 COMPLETE: as the Phase 4 lifecycle token emitted above this block -- C-31(a) satisfied; CELL-SOURCE labeled field (within this block) confirms all six cells draw from already-emitted content with no forward-references -- C-31(b) satisfied; both declarations appear as labeled fields within this structural block, not as prose in surrounding context -- C-31(c) satisfied.`

And the dependency chain: "C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 complete."

**C-31: PASS** — All three sub-clauses independently satisfied:
- (a): PLACEMENT field names PHASE 4 COMPLETE: explicitly as a labeled field within the block
- (b): CELL-SOURCE field confirms no forward-references, explicitly as a labeled field within the block
- (c): Both appear within the block structure (after the heading, before the separator), not as surrounding prose
- Explicit C-31(a)/(b)/(c) sub-clause declaration present at closing

---

### Composite Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01..C-05 (essential, 60 pts) | PASS | PASS | PASS | PASS | PASS |
| C-06..C-08 (recommended, 30 pts) | PASS | PASS | PASS | PASS | PASS |
| C-09..C-30 (aspirational, 110 pts) | PASS | PASS | PASS | PASS | PASS |
| C-31 (aspirational, 5 pts) | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |
| **Total** | **200/205** | **200/205** | **200/205** | **200/205** | **205/205** |

---

### Ranking

| Rank | Variation | Score | C-31 verdict |
|------|-----------|-------|--------------|
| 1 | V-05 | 205/205 | PASS — both elements as labeled fields within block |
| 2 (tie) | V-01 | 200/205 | FAIL — no elements present |
| 2 (tie) | V-02 | 200/205 | FAIL — (a) only; (b) absent |
| 2 (tie) | V-03 | 200/205 | FAIL — (b) only; (a) absent |
| 2 (tie) | V-04 | 200/205 | FAIL — both elements outside block as surrounding prose |

---

### Failure Mode Analysis

C-31 probed three independent failure axes. All three confirmed:

**Axis (a)/(b) independence:** V-02 and V-03 demonstrate the symmetric both-or-nothing property:
- V-02 (placement only): reviewer can confirm chronological position but not cell-source provenance
- V-03 (cell-source only): reviewer can confirm no forward-references but not whether block follows PHASE 4 COMPLETE:
- Either element alone is necessary but not sufficient — the same pattern as C-28 at Phase 1 only / Phase 4 only (V-02/V-03 R11)

**Axis (c) inside-block requirement:** V-04 demonstrates that content placed before the block heading is not within the block. Both elements were present and accurate; they failed solely because their location was prose context rather than labeled fields within the block. A reviewer auditing the block alone (from heading to separator) would find no placement or cell-source declarations. Self-attestation requires in-block placement — the self-attesting property is defeated by any requirement to read surrounding context.

**Full synthesis (V-05):** Three structural decisions made V-05 the ceiling:
1. PLACEMENT and CELL-SOURCE placed BEFORE the six cells — declares validity before presenting evidence
2. Both fields self-identify their compliance ("C-31(a) satisfied:" / "C-31(b) satisfied:") inline
3. Closing declaration names all three sub-clauses explicitly and extends the dependency chain to C-31

---

### Excellence Signals from V-05

**Signal 1: Declarations precede evidence within the block.** PLACEMENT and CELL-SOURCE appear at the top of the C-29 Operationalization Verification block, before the six cells. This is structurally superior to V-02's end-of-block placement: a reviewer encounters the placement and cell-source confirmations before auditing the six cells, making the audit context self-contained from the first line of the block.

**Signal 2: CELL-SOURCE references cells "below."** The CELL-SOURCE field says "All six cells *below* draw from already-emitted content" — using directional language within the block to distinguish between where the cells live (within the block, below) and where their source data lives (already-emitted annotations, above). This is more precise than V-03's "All six cells *above* draw from already-emitted content" (V-03's placement at end of block reverses the direction).

**Signal 3: Explicit C-31(a)/(b)/(c) sub-clause naming at closing.** The final sentence enumerates all three sub-clauses with their status, mirroring the C-28 annotation pattern applied one level higher. A reviewer reading the closing line alone can confirm all three C-31 requirements without re-reading PLACEMENT and CELL-SOURCE fields.

**Signal 4: Dependency chain terminates at C-31.** "C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 complete" makes the full lineage traceable from the closing declaration. Prior variations (V-01 through V-04) terminate at C-30. V-05 extends the chain to the new ceiling, making C-31 compliance visible in the chain declaration itself.

---

```json
{"top_score": 205, "all_essential_pass": true, "new_patterns": ["Declare placement and cell-source as labeled fields before the six cells, not after C-29 PASS, so the block is self-contained from its first line", "Use directional language within the block (cells 'below' vs source data 'above') to distinguish block-internal content from already-emitted annotations", "Enumerate all sub-clauses (a)/(b)/(c) explicitly in the closing declaration of a self-attestation block, mirroring the C-28 pattern at the C-31 level", "Extend the dependency chain declaration to the new ceiling criterion so the full lineage is traceable from the closing line"]}
```
