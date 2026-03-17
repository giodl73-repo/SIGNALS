## Round 3 Scorecard — prove-analysis

**Rubric:** v3 (130 pts) | **Trace artifact:** placeholder (structural scoring)

---

### Scores

| Rank | Variation | Essential (60) | Recommended (30) | Aspirational (40) | Total |
|------|-----------|---------------|-----------------|------------------|-------|
| 1 | **V-05** Full Stack | 60 | 30 | 40 | **130** |
| 2 | **V-01** Pre-Reg Mechanism Column | 60 | 30 | 30 | **120** |
| 2 | **V-02** Per-Source Falsification Chain | 60 | 30 | 30 | **120** |
| 2 | **V-03** Two-Phase Vocabulary Audit | 60 | 30 | 30 | **120** |
| 2 | **V-04** Mechanism + Falsification Blocks | 60 | 30 | 30 | **120** |

---

### Criterion differentiators (aspirational tier only)

| | C-11 | C-13 | C-14 | C-15 | C-16 |
|--|------|------|------|------|------|
| V-01 | ✓ | ✓ | **✓** | — | — |
| V-02 | ✓ | ✓ | — | — | **✓** |
| V-03 | ✓ | ✓ | — | **✓** | — |
| V-04 | ✓ | — | **✓** | — | **✓** |
| V-05 | ✓ | ✓ | ✓ | ✓ | ✓ |

---

### Key scoring decisions

**V-01: +5 vs predicted (115→120).** Passes C-13 on R2 continuity — its compliance review covers "mechanism entries, counter-pattern sentences, and narrative paragraphs," which exceeds R2 V-05's coverage that passed C-13. The C-13/C-15 boundary holds: named-section-by-heading is C-15; reaching non-table narrative is C-13.

**V-04: +5 vs predicted (115→120).** C-11 PASS — eight labeled fields per block satisfies "numbered block with labeled fields qualifies." C-13 FAIL confirmed — Phase 1 mechanism prediction text is not listed in the compliance review scope (Phase 2 + Phase 3 are covered, but Phase 1 is absent). V-04 is the only non-full-stack variation achieving both C-14 and C-16.

**Research questions resolved:**
- C-14 column adjudication (V-01): sufficient — explicit reference instruction in the column header passes the per-source requirement
- C-16 chain-before-table (V-02) vs block embedding (V-04): both pass; V-02 has a traceability advantage via the copy instruction
- C-15 Phase B (V-03): structural pass; execution quality deferred to model run

---

### Excellence signals from V-05

**1. Chain-to-table copy instruction** — `"Source null verdict (C-16): Copy from Falsification Chain. Do not rewrite."` Prevents post-hoc drift: the model cannot soften a null verdict after observing the pattern because the cell is constrained to copy, not re-derive. No other variation uses this pattern. → Candidate **C-17** (falsification chain traceability).

**2. Pre-write verdict audit (write-gate pattern)** — Phase B audits planned verdict language *before* the VERDICT section is written: `"VERDICT (pre-audit before writing)."` Write-gate is stronger than post-hoc correction. Pattern appears independently in both V-03 and V-05 — structural stability indicator. → Candidate **C-18** (pre-write verdict audit).

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["chain-to-table copy instruction creates explicit traceability: V-05's 'Source null verdict (C-16): Copy from Falsification Chain. Do not rewrite.' prevents post-hoc drift between preamble falsification commitments and table verdicts -- a model cannot soften a null verdict after observing the pattern when the table cell is constrained to copy, not re-derive", "pre-write verdict audit (write-gate pattern): V-05 Phase B audits planned verdict language before the VERDICT section is written, using 'VERDICT (pre-audit before writing)' framing -- this write-gate provides a stronger vocabulary guarantee than post-hoc correction; the pattern appears independently in both V-03 and V-05, suggesting structural stability as a candidate v4 criterion"]}
```
15 requires explicit per-section coverage naming sections like "MECHANISM VERDICT," "COUNTER-PATTERN SUMMARY," "VERDICT paragraphs." Vague "narrative paragraphs" does not satisfy the structural guarantee C-15 requires. |
| C-16 | Per-source falsification | FAIL | Single shared null expectation ("Null expectation: [What would the data look like if this hypothesis were false? One sentence.]") applied uniformly to all sources via the "Null expectation met?" column. C-16 explicitly disqualifies "a single shared null expectation applied uniformly to all sources." No per-source null condition block exists. |

**Score: 60 + 30 + (5+5+5+5+5+5+0+0) = 120/130**

**vs predicted:** 115 predicted; 120 actual. Delta +5. Source: C-13 scored PASS based on R2 continuity — R2 V-05 passed C-13 with equivalent or less compliance coverage; V-01 (R3) adds "narrative paragraphs" to the audit scope, meeting the same standard.

---

#### V-02: Per-Source Falsification Chain

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Source named | PASS | "Exact source name from the FALSIFICATION CHAIN above. Do not add rows for sources not listed in the chain." |
| C-02 | Pattern stated | PASS | "Pattern found" column: "No pattern detected" if none; "Do not hedge." |
| C-03 | Hypothesis connection | PASS | "Hypothesis bearing" column: "Explicit link. For 'Null met' rows: explain the disconfirmation." |
| C-04 | Correlation vs causal labeled | PASS | "Relationship type" column: "ONLY vocabulary contract terms. No forbidden terms." |
| C-05 | Strength assessed | PASS | "Strength" column: "weak / moderate / strong + at least one number, rate, count, or logical argument." |
| C-06 | Multiple sources | PASS | FALSIFICATION CHAIN: "Add one block per accessible source. Minimum two blocks required." |
| C-07 | Counter-patterns | PASS | COUNTER-PATTERN SUMMARY [Required] collects all "Null met" rows and no-pattern sources. |
| C-08 | Quantified claims | PASS | QUANTIFIED CLAIMS [Required]: "N of M sources met their source-specific null condition." |
| C-09 | Causal mechanism proposed | PASS | MECHANISM ANALYSIS [Required] with three sentence templates; mechanism verdict ("Mechanism established / plausible / ruled out / untestable") required. |
| C-10 | Scope and validity | PASS | VERDICT.Scope (C-10): "at least one explicit boundary condition." |
| C-11 | Per-source structured format | PASS | Six-column analysis table (Source, Pattern found, Source null verdict, Hypothesis bearing, Relationship type, Strength); each essential obligation in a named column. |
| C-12 | Null/falsification framing | PASS | FALSIFICATION CHAIN provides per-source null conditions; "Source null verdict" column copies chain verdicts to the table. C-12 pass condition requires "at least one pattern has an explicit falsification sentence" — all sources have one via the chain. |
| C-13 | Vocabulary precision | PASS | Vocabulary contract (forbidden terms + required replacements) + compliance review covering "all Relationship type cells, mechanism sentences, all counter-pattern entries, and synthesis narrative" — explicitly mentions "synthesis narrative" as an outside-table audit target. |
| C-14 | Pre-registered mechanism | FAIL | MECHANISM ANALYSIS section fires AFTER the analysis table — mechanism sentences are written per source post-analysis, not pre-registered before any source is named. The section says "For each source with a pattern, write one mechanism sentence" — this is post-hoc mechanism proposal, not pre-registration. No preamble mechanism prediction gate. No column or field requires adjudication of a pre-stated prediction. MECHANISM VERDICT renders a verdict but it synthesizes post-hoc sentences, not per-source adjudications of a locked prediction. C-14 requires the prediction to appear BEFORE the first per-source analysis. |
| C-15 | Document-wide vocabulary audit | FAIL | Compliance review covers "mechanism sentences, counter-pattern entries, and synthesis narrative" — lists content categories but does not name each prose section individually by document heading. Does not explicitly audit "verdict text" or name MECHANISM VERDICT, HYPOTHESIS, COUNTER-PATTERN SUMMARY as discrete audit sections. Per-section-by-heading naming is the C-15 structural requirement. |
| C-16 | Per-source falsification | PASS | FALSIFICATION CHAIN: each block requires "Source null condition: [specific to this artifact, not a generic expectation shared across all sources]" + Observed + "Source null verdict: [Null met / Null not met / Ambiguous + explanation]." Minimum two blocks, each with an independent null condition. The chain-before-table structure commits to source-specific null conditions before any pattern analysis. |

**Score: 60 + 30 + (5+5+5+5+5+0+0+5) = 120/130**

**vs predicted:** 120 predicted; 120 actual. Delta 0. Prediction confirmed.

---

#### V-03: Two-Phase Narrative Vocabulary Audit

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Source named | PASS | "Specific named artifact. Not 'the data.' If you cannot name it, no row." |
| C-02 | Pattern stated | PASS | "Pattern found" column: "No hedging." |
| C-03 | Hypothesis connection | PASS | "Hypothesis bearing" column: "Explicit link. One to two sentences." |
| C-04 | Correlation vs causal labeled | PASS | "Relationship type" column: "ONLY vocabulary contract terms. Forbidden terms = error." |
| C-05 | Strength assessed | PASS | "Strength" column: "Tier + at least one number, rate, count, or argument." |
| C-06 | Multiple sources | PASS | "Minimum two rows." |
| C-07 | Counter-patterns | PASS | COUNTER-PATTERN SUMMARY [Required] collects "Null met" rows and no-pattern sources. |
| C-08 | Quantified claims | PASS | QUANTIFIED CLAIMS [Required]: "N of M analyzed sources met the null expectation." |
| C-09 | Causal mechanism proposed | PASS | "Proposed mechanism" in HYPOTHESIS AND FALSIFICATION SETUP + MECHANISM ANALYSIS [Required] with sentence templates + mechanism verdict term. |
| C-10 | Scope and validity | PASS | VERDICT.Scope (C-10): "at least one explicit boundary condition...do not omit." |
| C-11 | Per-source structured format | PASS | Six-column table (Source, Pattern found, Null expectation met?, Hypothesis bearing, Relationship type, Strength); each essential obligation in a named column. |
| C-12 | Null/falsification framing | PASS | "Null expectation" pre-stated in setup section; "Null expectation met?" column per row. C-12 requires "at least one pattern has an explicit falsification sentence" — satisfied by shared null + per-row column. |
| C-13 | Vocabulary precision | PASS | Vocabulary contract (forbidden terms + required replacements) + Phase A table column audit + Phase B naming each prose section individually: PROPOSED MECHANISM, MECHANISM ANALYSIS, COUNTER-PATTERN SUMMARY, VERDICT paragraphs. Strongest C-13 structural guarantee of any variation. |
| C-14 | Pre-registered mechanism | FAIL | "Proposed mechanism" in HYPOTHESIS AND FALSIFICATION SETUP is unlocked — it can be revised after observing sources. No explicit pre-registration GATE ("do not name any data source until mechanism is locked"). MECHANISM ANALYSIS section prompts per-source mechanism sentences in forms like "A plausible cause is X" and "This could be explained by X" — these are post-hoc per-source mechanism proposals, not adjudications of a pre-stated prediction. No "Mechanism adjudication" column or field requiring comparison to the pre-stated mechanism. The mechanism verdict in MECHANISM ANALYSIS is a synthesis of post-hoc sentences. C-14 pass condition requires "a mechanism prediction appears before the first per-source analysis" with a gate, and each source "explicitly references the pre-stated mechanism and reports a confirmation verdict." Neither is present. |
| C-15 | Document-wide vocabulary audit | PASS | VOCABULARY COMPLIANCE AUDIT Phase A + Phase B. Phase A audits the Relationship type table column. Phase B explicitly names and audits each prose section by document heading: "PROPOSED MECHANISM (HYPOTHESIS AND FALSIFICATION SETUP):", "MECHANISM ANALYSIS -- each mechanism sentence and verdict:", "COUNTER-PATTERN SUMMARY -- each entry:", "VERDICT paragraphs (pre-audit before writing)." Phase B status report is required before VERDICT. The VERDICT.Vocabulary field must confirm both phases complete. C-15 pass condition satisfied in full. |
| C-16 | Per-source falsification | FAIL | "Null expectation: [What would the data look like if this hypothesis were false? One sentence.]" — a single shared null expectation applied to all sources via the "Null expectation met?" column. C-16 requires "at least two data sources each carry an explicit source-specific falsification sentence." No per-source null condition block exists. The COUNTER-PATTERN SUMMARY collects disconfirming rows but does not constitute per-source falsification setup. |

**Score: 60 + 30 + (5+5+5+5+5+0+5+0) = 120/130**

**vs predicted:** 120 predicted; 120 actual. Delta 0. Prediction confirmed.

---

#### V-04: Mechanism Chain + Per-Source Falsification Blocks

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Source named | PASS | "Specific named artifact -- file, table, schema, scenario set, log, test suite. Not 'the data.' If you cannot name it, do not use this source block." |
| C-02 | Pattern stated | PASS | "Pattern found (C-02)" labeled field: "No pattern detected" if none; "Do not hedge." |
| C-03 | Hypothesis connection | PASS | "Hypothesis bearing (C-03)" labeled field: "start with 'This bears on the hypothesis because...'" |
| C-04 | Correlation vs causal labeled | PASS | "Relationship type (C-04)" labeled field: vocabulary contract terms only; three options printed. |
| C-05 | Strength assessed | PASS | "Strength (C-05)" labeled field: "Tier: weak / moderate / strong + at least one number, rate, N of M, effect size, p-value, or logical argument." |
| C-06 | Multiple sources | PASS | "Minimum two blocks required." |
| C-07 | Counter-patterns | PASS | "Counter-evidence (C-07)" labeled field per source: "Data in this source that weakens or contradicts the pattern." |
| C-08 | Quantified claims | PASS | QUANTIFIED CLAIMS [Required]: "N of M sources met their source-specific null condition." |
| C-09 | Causal mechanism proposed | PASS | Phase 1 requires mechanism prediction. Phase 3 MECHANISM VERDICT renders one of four permitted verdict terms. Mechanism analysis is the organizing frame across all three phases. |
| C-10 | Scope and validity | PASS | PHASE 3 Overall Synthesis.Scope (C-10): "at least one explicit boundary condition." |
| C-11 | Per-source structured format | PASS | Per-source blocks with eight labeled fields (**Source**, **Falsification block**, **Pattern found**, **Hypothesis bearing**, **Relationship type**, **Mechanism adjudication**, **Strength**, **Counter-evidence**). Rubric pass condition: "A table with labeled columns or a numbered block with labeled fields qualifies." Eight labeled fields per block satisfies this. |
| C-12 | Null/falsification framing | PASS | Per-source **Falsification block** includes "Source null condition," "Observed," and "Source null verdict." Source-specific null condition is required. Minimum two blocks. C-12 requires "at least one pattern has an explicit falsification sentence" — satisfied by all blocks. |
| C-13 | Vocabulary precision | FAIL | Phase 1 MECHANISM PREDICTION text is not covered by the compliance review. VOCABULARY COMPLIANCE REVIEW scans "all Relationship type fields from Phase 2, all mechanism adjudication entries, all counter-evidence entries, and all Phase 3 synthesis paragraphs" — Phase 1 mechanism prediction is absent from this list. The mechanism prediction format ("If [hypothesis] is true, [mechanism M] operates: [X causes Y]...") can contain relationship language. Without Phase 1 audit coverage, hedged terms can slip through the mechanism prediction unchanged. This is the same gap flagged in R2 V-04 ("PHASE 1, PHASE 3, and SYNTHESIS narrative have no vocabulary contract or compliance check") applied now to Phase 1 specifically, even though Phase 3 is covered. |
| C-14 | Pre-registered mechanism | PASS | PHASE 1 GATE: "Hypothesis and mechanism prediction locked. Do not name or analyze any source until this gate is complete." Phase 2 "Mechanism adjudication (C-14)" field: "Reference the pre-registered prediction explicitly. Write one of: Confirmed / Not confirmed / Silent." Phase 3 MECHANISM VERDICT section renders verdict using permitted terms. All three C-14 pass conditions satisfied. |
| C-15 | Document-wide vocabulary audit | FAIL | Compliance review names "Phase 2 fields" and "Phase 3 synthesis paragraphs" as categories, not each section individually by document heading. No Phase B structure naming PHASE 1 MECHANISM PREDICTION, FALSIFICATION TALLY, OVERALL SYNTHESIS, or individual Phase 3 verdict fields. Phase 1 is unaudited (see C-13). Per-section-by-heading naming is the C-15 structural bar. |
| C-16 | Per-source falsification | PASS | Per-source **Falsification block**: "Source null condition: [specific to this artifact, not a generic null. What would THIS source show, specifically, if the hypothesis does not hold?]" + Observed + Source null verdict. Minimum two blocks. Phase 3 FALSIFICATION TALLY aggregates verdicts. |

**Score: 60 + 30 + (5+5+5+5+0+5+0+5) = 120/130**

**vs predicted:** 115–120 predicted; 120 actual. Delta 0 to +5. C-11 awarded (labeled blocks qualify per rubric); C-13 fails due to Phase 1 audit gap (design note was partially wrong about Phase 3 coverage, but Phase 1 gap is real and decisive).

---

#### V-05: Full 130/130 Stack

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Source named | PASS | "Exact artifact name from Falsification Chain. Not 'the data.'" Falsification chain gate prevents unnamed sources from entering the table. |
| C-02 | Pattern stated | PASS | "Pattern found" column: "No pattern detected" if none; no hedging. |
| C-03 | Hypothesis connection | PASS | "Hypothesis bearing" column: "Explicit link. One to two sentences. For 'Null met' rows: explain what the disconfirmation means for the hypothesis." |
| C-04 | Correlation vs causal labeled | PASS | "Relationship type" column: "ONLY vocabulary contract terms. No forbidden terms." |
| C-05 | Strength assessed | PASS | "Strength" column: "weak/moderate/strong + number, rate, count, or logical argument." |
| C-06 | Multiple sources | PASS | Falsification chain minimum two blocks; table constrained to chain sources. |
| C-07 | Counter-patterns | PASS | COUNTER-PATTERN SUMMARY [Required] collects all "Null met" rows from the table. |
| C-08 | Quantified claims | PASS | QUANTIFIED CLAIMS [Required]: "N of M sources met their source-specific null condition" and "N of M sources produced Mechanism adjudication: Confirmed." Two structural quantification floors. |
| C-09 | Causal mechanism proposed | PASS | Mechanism prediction in HYPOTHESIS AND PRE-REGISTRATION SETUP + MECHANISM VERDICT requires one of four permitted verdict terms. Mechanism verdict restated in VERDICT.Mechanism verdict (C-14). |
| C-10 | Scope and validity | PASS | VERDICT.Scope (C-10): "at least one explicit boundary condition...do not omit." |
| C-11 | Per-source structured format | PASS | Seven-column table (Source, Pattern found, Source null verdict, Hypothesis bearing, Relationship type, Strength, Mechanism adjudication); each essential obligation in a named column. Table format preserved despite three pre-table structural layers. |
| C-12 | Null/falsification framing | PASS | FALSIFICATION CHAIN + "Source null verdict" column copies chain verdict to table. Every table row has an explicit null verdict referencing a pre-analysis commitment. |
| C-13 | Vocabulary precision | PASS | Vocabulary contract (forbidden terms + required replacements) + Phase A table column audit + Phase B explicitly audits: "HYPOTHESIS AND PRE-REGISTRATION SETUP -- mechanism prediction" (covers Phase 1 text), "FALSIFICATION CHAIN -- null condition sentences (all blocks)," "MECHANISM VERDICT -- verdict sentence and rationale," "COUNTER-PATTERN SUMMARY -- all entries," "VERDICT (pre-audit)." Phase 1 mechanism prediction is the explicit gap closed by V-05 vs V-01 and V-04. |
| C-14 | Pre-registered mechanism | PASS | PRE-REGISTRATION GATE: "Mechanism prediction locked. Do not name any data source before this gate. Proceed to the FALSIFICATION CHAIN." Mechanism adjudication column: "Compare pattern to pre-registration in HYPOTHESIS AND PRE-REGISTRATION SETUP. Reference the pre-stated prediction explicitly." MECHANISM VERDICT renders final verdict using permitted terms. |
| C-15 | Document-wide vocabulary audit | PASS | Phase A audits Relationship type column. Phase B names five sections individually: HYPOTHESIS AND PRE-REGISTRATION SETUP (mechanism prediction), FALSIFICATION CHAIN (all blocks), MECHANISM VERDICT (verdict sentence), COUNTER-PATTERN SUMMARY (all entries), VERDICT (pre-audit before writing). Phase B status report required. VERDICT.Vocabulary (C-15): "Phase A table column audit and Phase B prose section audit complete." |
| C-16 | Per-source falsification | PASS | FALSIFICATION CHAIN: "each null condition must be specific to that source -- not a generic expectation shared across sources." Source null verdict: "Copy from Falsification Chain. Do not rewrite." Table column copies from chain (explicit traceability instruction). VERDCT.Falsification summary (C-16) restates tally. |

**Score: 60 + 30 + (5+5+5+5+5+5+5+5) = 130/130**

**vs predicted:** 130 predicted; 130 actual. Delta 0. Prediction confirmed.

---

### Composite Scores and Ranking

| Rank | Variation | Essential (60) | Recommended (30) | Aspirational (40) | Total | vs Predicted |
|------|-----------|----------------|------------------|-------------------|-------|-------------|
| 1 | V-05 Full 130/130 Stack | 60 | 30 | 40 | **130** | = 130 |
| 2 | V-01 Pre-Registered Mechanism Column | 60 | 30 | 30 | **120** | +5 vs 115 |
| 2 | V-02 Per-Source Falsification Chain | 60 | 30 | 30 | **120** | = 120 |
| 2 | V-03 Two-Phase Narrative Vocabulary Audit | 60 | 30 | 30 | **120** | = 120 |
| 2 | V-04 Mechanism Chain + Per-Source Falsification Blocks | 60 | 30 | 30 | **120** | +5 vs 115 |

**V-01 re-score note:** Predicted 115; scored 120. V-01 passes C-13 because its compliance review covers "mechanism entries, counter-pattern sentences, and narrative paragraphs" — coverage equivalent to or exceeding R2 V-05 (which passed C-13 with "mechanism entries and counter-pattern sentences"). R2 continuity applies: the C-13 structural bar is vocabulary contract + compliance review reaching non-table sections, not per-section-by-heading naming (which is C-15).

**V-04 re-score note:** Predicted 115–120; scored 120. C-11 awarded: eight labeled fields per per-source block satisfies "numbered block with labeled fields qualifies." C-13 fails due to Phase 1 mechanism prediction text not being covered by the compliance review (Phase 2 + Phase 3 are covered, but Phase 1 is not listed). This is consistent with R2's C-13 failure mode: Phase 1/MECHANISM section text unaudited.

**All-essential-pass:** True. All five variations pass C-01 through C-08 (essential + recommended floors) without exception. The aspiration tier is where differentiation occurs.

**Four-way tie at 120:** Four variations each achieve 30/40 aspirational, but with different criterion profiles:

| | C-11 | C-13 | C-14 | C-15 | C-16 |
|--|------|------|------|------|------|
| V-01 | ✓ | ✓ | ✓ | — | — |
| V-02 | ✓ | ✓ | — | — | ✓ |
| V-03 | ✓ | ✓ | — | ✓ | — |
| V-04 | ✓ | — | ✓ | — | ✓ |
| V-05 | ✓ | ✓ | ✓ | ✓ | ✓ |

V-04 is the only non-full-stack variation that achieves both C-14 (pre-registered mechanism) and C-16 (per-source falsification). It uniquely combines the two strongest new criteria — but sacrifices C-13 because its compliance review omits Phase 1 mechanism prediction text from the audit scope.

---

### C-14 Structural Test Result

**Research question:** Does column-based adjudication (V-01) produce adequate C-14 per-source coverage, or does cell-space compression disqualify it?

**Finding:** V-01 PASSES C-14. The "Mechanism adjudication" column instruction is explicit: "Reference the pre-registered prediction explicitly. Write one of: Confirmed: [how the observed pattern matches the pre-registered mechanism prediction] / Not confirmed: [how the observed pattern diverges from the prediction; be specific] / Silent: [why this source cannot speak to the mechanism]." The preamble GATE locks the prediction before any source is named. The MECHANISM VERDICT section aggregates per-source verdicts into a synthesis. Column-cell adjudication is structurally sufficient for C-14 — the column header enforces the pass condition with the same guarantee as V-04's embedded block field.

---

### C-15 Structural Test Result

**Research question:** Does V-03's Phase B audit produce genuine per-section C-15 coverage, or does the model produce pro-forma "Clear" entries?

**Scoring finding:** V-03 passes C-15 structurally — the template names each section by document heading and requires a per-section verdict. Whether model execution produces meaningful review vs. pro-forma "Clear" is an execution risk, not a structural gap. The structural guarantee is present. The open question deferred to a future run-with-model evaluation round.

---

### C-16 Structural Test Result

**Research question:** Does V-02's chain-before-table produce equivalent C-16 coverage to V-04's embedded block fields?

**Finding:** Both PASS C-16 with different structural profiles. V-02 separates the falsification chain from the analysis — the chain commits first, the table copies verdicts. V-04 co-locates the falsification block inside the source block — the model commits per-source in sequence. Both satisfy C-16's "at least two data sources each carry an explicit source-specific falsification sentence." V-02's chain-before-table has a traceability advantage: the copy instruction in the table ("Copy from Falsification Chain. Do not rewrite.") prevents post-hoc adjustment of null verdicts after observing patterns.

---

### Excellence Signals from V-05

These are structural patterns from V-05 that are not codified in the v3 rubric and represent candidate v4 aspirational criteria:

**1. Chain-to-table copy instruction creates explicit traceability**
V-05's table column instruction: "Source null verdict (C-16): Copy from Falsification Chain. Do not rewrite." The COPY instruction is a structural guarantee against post-hoc drift: the model cannot re-derive or soften a null verdict after observing the pattern. The chain commits first; the table references the commitment. No other variation uses this pattern. V-02 has a falsification chain but does not instruct the table to copy from it (the table column description redescribes the verdict format independently). V-05's copy instruction closes a potential drift gap: a model could fill V-02's table column with a softened verdict that diverges from the chain.

Candidate v4 criterion: **C-17 -- Falsification chain traceability** — the analysis table must explicitly reference the pre-stated falsification chain verdict for each source (e.g., "Copy from Falsification Chain: do not rewrite") rather than independently filling the null verdict column. A table that re-derives the null verdict without referencing the chain does not qualify.

**2. Phase B pre-write verdict audit (write-gate pattern)**
V-05's Phase B includes "VERDICT (pre-audit before writing): [Clear -- planned verdict language uses vocabulary contract terms.] OR [Planned use of '[forbidden term]' -- will use '[contract term]' instead.]" The model must plan and audit verdict language BEFORE writing the VERDICT section. This is a write-gate: the compliance check precedes the section it applies to, not follows it. V-03 has a similar structure but does not use the same pre-write framing; its Phase B says "VERDICT paragraphs (pre-audit before writing)" — same pattern, independently developed in parallel.

This is the first round where both V-03 and V-05 exhibit the pre-write verdict audit pattern. The recurrence suggests it is a stable structural pattern, not a one-off design choice.

Candidate v4 criterion: **C-18 -- Pre-write verdict audit** — the vocabulary compliance check must audit planned verdict language before the VERDICT section is written, using explicit pre-write framing ("pre-audit before writing" or equivalent). A compliance check that runs only after the VERDICT is written, or that does not name the VERDICT section in Phase B, does not qualify.

---

### Round 3 Research Question Resolutions

| Question | Answer |
|----------|--------|
| Does V-01's column adjudication produce adequate C-14 depth? | YES — column cell adjudication with explicit reference instruction passes C-14. |
| Does V-02's chain-before-table produce equivalent C-16 to V-04's block embedding? | YES — both pass. V-02 has a traceability advantage via copy instruction. |
| Does V-03's Phase B produce genuine per-section C-15 coverage? | STRUCTURALLY YES — execution quality deferred to model run. |
| Does V-05's preamble density cause essential criterion failures? | NOT STRUCTURALLY — all essential/recommended criteria pass across all variations. |
| What is V-04's C-11 verdict with eight labeled fields? | PASS — "numbered block with labeled fields qualifies" applies; eight fields is sufficient. |

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["chain-to-table copy instruction creates explicit traceability: V-05's 'Source null verdict (C-16): Copy from Falsification Chain. Do not rewrite.' prevents post-hoc drift between preamble falsification commitments and table verdicts -- a model cannot soften a null verdict after observing the pattern when the table cell is constrained to copy, not re-derive", "pre-write verdict audit (write-gate pattern): V-05 Phase B audits planned verdict language before the VERDICT section is written, using 'VERDICT (pre-audit before writing)' framing -- this write-gate provides a stronger vocabulary guarantee than post-hoc correction; the pattern appears independently in both V-03 and V-05, suggesting structural stability as a candidate v4 criterion"]}
```
