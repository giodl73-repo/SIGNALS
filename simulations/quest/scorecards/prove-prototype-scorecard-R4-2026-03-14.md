# Quest Score — prove-prototype (Round 4)

**Rubric**: v4 (130 pts) | **Variations**: V-01 through V-05
**Date**: 2026-03-15

---

## Scoring Key

| Result | Credit |
|--------|--------|
| PASS | Full points |
| PARTIAL | ~half points |
| FAIL | 0 |

**Point weights** (from rubric):
- Essential C-01–C-05: 12 pts each (60 total)
- Recommended C-06–C-08: 10 pts each (30 total)
- Aspirational C-09, C-10, C-16–C-19: 5 pts each (30 total)
- Excellence C-11–C-15: 2 pts each (10 total)

---

## V-01 — Table-Dominant with Inline Gate Labels

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Section 1 carries `*[Gate: this section must be the first element of your output. Nothing precedes it...]*`; hypothesis precedes all build/result content |
| C-02 | PASS | 12 | Table requires ≥2 Out-of-Scope rows; col 3 is titled the test-validity question; "It wasn't needed" explicitly rejected |
| C-03 | PASS | 12 | Section 3 gate: "complete every row before any build output exists...stop and complete this table first"; output contract item 2 verifies 3 before 4 |
| C-04 | PASS | 12 | Results table has Predicted, Actual, Delta, and "Why the delta is what it is" columns; all required |
| C-05 | PASS | 12 | Section 7 table: Verdict + Verdict Rationale in same row; pass |
| C-06 | PASS | 10 | Col 3 "Why the test remains valid without this exclusion" enforces test-validity reasoning per exclusion; bars bare labels |
| C-07 | PASS | 10 | Actual column: "include one concrete data point — a number, a time, a count, or a direct quote from output" |
| C-08 | PASS | 10 | Section 8 table: Limitation + Next Step both required |
| C-09 | PASS | 5 | Section 6 Disposition A handles counter-interpretation + evidence-grounded rebuttal |
| C-10 | PASS | 5 | Section 9: numbered list, "No implicit steps. Configuration files named." |
| C-11 | PASS | 2 | Output contract rule 5: "Every table cell is populated. Write 'N/A' only where genuinely not applicable — with an inline reason." |
| C-12 | PASS | 2 | Section 3 inline gate + output contract item 2 make temporal ordering structurally visible without inference |
| C-13 | PASS | 2 | Delta column header is "Delta (predicted − actual)"; "do not leave this for the reader to infer" explicit |
| C-14 | PASS | 2 | Section 7: verdict rationale must be "the reasoning that connects the observed delta to the verdict"; "not a restatement of Section 5" |
| C-15 | PASS | 2 | Col 3 header answers the test-validity question per row; "It wasn't needed" and "outside scope" explicitly barred |
| C-16 | PASS | 5 | Section 6: "must close with exactly one of the following two dispositions...as the terminal element"; both A and B defined |
| C-17 | PASS | 5 | Output contract items 8–9 verify rationale in same row as delta and verdict; tables enforce co-location throughout |
| C-18 | PASS | 5 | Sections 6, 8, and 9 each carry Disposition A/B terminal elements; output contract item 6 verifies all three |
| C-19 | **PARTIAL** | **3** | Sections 1–7 carry `*[Gate: ...]*` inline markers; **Sections 8 and 9 have no opening gate markers**; output contract item 10 references "Sections 1–7" only; trailing-section coverage gap |

**V-01 Total: 128 / 130**

---

## V-02 — Phase Gates with Execute-Before Inline Markers

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1: `*Execute before anything else. This phase must appear as the first element of your output.*` |
| C-02 | PASS | 12 | Phase 2 per-exclusion pair; "Why the test remains valid without it" required inline; "bare labels without rationale fail this phase" |
| C-03 | PASS | 12 | Phase 3: `*Execute before any build activity*` + `*Do not proceed to Phase 4 until every metric...written down*`; gate line "PHASE 3 COMPLETE — measurement protocol established before build" is model-written artifact |
| C-04 | PASS | 12 | Phase 5 labeled fields: Predicted, Actual, Delta ("do not merge"), "Why the delta is what it is" in same block |
| C-05 | PASS | 12 | Phase 7: Verdict + Verdict rationale labeled fields; rationale explicitly distinct from Phase 5 restatement |
| C-06 | PASS | 10 | Phase 2: per-exclusion "why remains valid" inline; "it wasn't needed" explicitly fails the phase |
| C-07 | PASS | 10 | Phase 5: "must include at least one concrete data point — a number, a time, a count, or a direct quote from output" |
| C-08 | PASS | 10 | Phase 8: Limitation + Next Step labeled fields; "do more testing" explicitly fails |
| C-09 | PASS | 5 | Phase 6 Disposition A: counter-interpretation + "explain why it does not hold, using evidence from Phase 5" |
| C-10 | PASS | 5 | Phase 9: numbered list, "No implicit steps. Every tool, input, and command must be named." |
| C-11 | PASS | 2 | Gate check lines ("PHASE N COMPLETE") require each phase to be substantially written before the next begins; structural enforcement via completion artifact |
| C-12 | PASS | 2 | Phase 3 gate line "PHASE 3 COMPLETE — measurement protocol established before build" is model-written temporal evidence; ordering explicitly visible in output |
| C-13 | PASS | 2 | Phase 5 Delta: "do not merge this into Predicted or Actual; it is its own labeled field" |
| C-14 | PASS | 2 | Phase 7: "not a restatement of Phase 5 — it is the reasoning connecting the observed delta to the verdict; it appears here in the same block as the verdict" |
| C-15 | PASS | 2 | Per-exclusion "why remains valid" inline; explicit failure condition on "bare labels without rationale" |
| C-16 | PASS | 5 | Phase 6 closes with "PHASE 6 COMPLETE — DISPOSITION [A/B] SELECTED"; binary disposition + gate artifact combined |
| C-17 | PASS | 5 | Labeled-pair blocks: "Why the delta is what it is" in same block as Delta; Verdict rationale in same block as Verdict; co-location enforced throughout |
| C-18 | PASS | 5 | Phases 6, 8, and 9 each close with A/B disposition "written as the terminal element of this phase, before the gate line"; gate-completion line verifies disposition was selected |
| C-19 | **PASS** | **5** | All 9 phases carry inline execute-before/after markers: Phase 8 `*Execute after Phase 7 gate is present in your output.*`; Phase 9 `*Execute after Phase 8 gate is present in your output.*`; complete coverage including trailing optional sections |

**V-02 Total: 130 / 130**

---

## V-03 — Labeled-Pair Block Architecture

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Block 1: `**[Gate: this block must appear as the first element of your output, before any description of what was built or what happened]**` |
| C-02 | PASS | 12 | Block 2 per-exclusion labeled pairs; "Why the test remains valid without it" required; "bare labels do not satisfy this field" |
| C-03 | PASS | 12 | Block 3: `**[Gate: this block must be complete before Block 4. Every metric, success condition, and failure condition must be established here before any build content is written...]*` |
| C-04 | PASS | 12 | Block 5 labeled pairs: Predicted, Actual, Delta ("own labeled field — do not embed"), "Why the delta is what it is" in same block |
| C-05 | PASS | 12 | Block 7: Verdict + Verdict rationale labeled pair |
| C-06 | PASS | 10 | Block 2 per-exclusion "Why the test remains valid without it"; "it wasn't needed" explicitly fails |
| C-07 | PASS | 10 | Block 5 Actual: "must include at least one concrete data point" |
| C-08 | PASS | 10 | Block 8: Limitation + Next step; "do more testing" fails |
| C-09 | PASS | 5 | Block 6 terminal pair A: Counter-interpretation + Rebuttal |
| C-10 | PASS | 5 | Block 9: numbered list, no implicit steps |
| C-11 | PASS | 2 | Structural rule 1: "Every labeled field must be populated. Write 'N/A' only where genuinely not applicable — with an inline reason." |
| C-12 | PASS | 2 | Block 3 gate explicitly states "before any build content is written"; block ordering enforced by structural rule 3 |
| C-13 | PASS | 2 | Block 5 Delta: "this is its own labeled field — do not embed it in Predicted or Actual; do not leave it for the reader to compute" |
| C-14 | PASS | 2 | Block 7: "not a restatement of Block 5"; verdict rationale connects evidence to conclusion |
| C-15 | PASS | 2 | Per-exclusion "Why the test remains valid without it" labeled pair; "bare labels do not satisfy this field" |
| C-16 | PASS | 5 | Block 6: two-path terminal pair; "No other closing form is permitted"; both A (counter + rebuttal) and B (None + reason) defined |
| C-17 | PASS | 5 | Structural rule 4 explicitly enumerates all co-location requirements; labeled-pair format confirmed as satisfying C-17 |
| C-18 | PASS | 5 | Blocks 6, 8, 9 each close with terminal labeled pairs A or B; "No other closing form is permitted" in blocks 6 and 8; status field in block 9 |
| C-19 | **PARTIAL** | **2** | Blocks 1–6 carry `**[Gate: ...]*` inline markers; **Blocks 7, 8, and 9 have no opening gate markers**; structural rule 3 covers 3→4, 5→6, 6→7 ordering but as a separate rules section, not co-located inline markers; three trailing sections ungated |

**V-03 Total: 127 / 130**

---

## V-04 — Conversational Imperative

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | "Before you write anything else: Restate the hypothesis...It goes first. It appears before any description of what you built..." |
| C-02 | PASS | 12 | Step 1: ≥2 exclusions with per-item reason answering "without this, can the prototype still test the hypothesis?" |
| C-03 | PASS | 12 | Step 2 gate line written by model: `Measurement protocol established before build.`; final rule: "must appear in your output before the build description in Step 3"; ordering enforced by model-written artifact |
| C-04 | PASS | 12 | Step 4: "I predicted [X]. I observed [Y]. The gap is [Z]." explicit three-element structure; gap required |
| C-05 | PASS | 12 | Step 6: "Confirmed? Refuted? Inconclusive? Say it plainly." |
| C-06 | PASS | 10 | Step 1 per-item reason must answer "without this, can the prototype still test the hypothesis? If yes, why?" |
| C-07 | PASS | 10 | Step 4: "Include at least one concrete data point: a number, a measured output, a time, a direct quote" |
| C-08 | PASS | 10 | Step 7: one limitation + one specific next step; "Name the specific thing to test, build, or change" |
| C-09 | PASS | 5 | Step 5 Option A: "Counter-interpretation: [state it]. Rebuttal: [explain why it does not hold using the evidence from Step 4]" |
| C-10 | PASS | 5 | Step 8: numbered list, "No implicit steps. Configuration files named." |
| C-11 | **PARTIAL** | **1** | No table cells or structural rules explicitly prohibit blank steps; "Follow them in order" implies content but structural enforcement weaker than table/labeled-pair formats; gate lines don't force substantive content per step |
| C-12 | PASS | 2 | Step 2 gate line + Final Rule enforce that measurement protocol appears before build description; temporal ordering structurally visible via model-written line |
| C-13 | PASS | 2 | Step 4: "compute the gap explicitly — do not leave it for the reader to infer. Write: 'I predicted [X]. I observed [Y]. The gap is [Z].'"; gap as dedicated sentence |
| C-14 | PASS | 2 | Step 6: "This explanation is not the results again. It is the reasoning that bridges the evidence to the conclusion" |
| C-15 | PASS | 2 | Step 1: per-item reason answers test-validity question; "It wasn't needed is not a reason" |
| C-16 | PASS | 5 | Step 5: "End this step with exactly one of the following two closing sentences...No other form of closing is permitted" |
| C-17 | **PARTIAL** | **3** | Step 4 co-locates delta reason "in the same paragraph as the gap — not in a separate section later"; Step 6 has verdict rationale in same step. But conversational paragraphs don't constitute "table row, labeled pair, or immediately adjacent labeled element"; softer enforcement than structured formats |
| C-18 | PASS | 5 | Steps 5, 7, 8 each close with exactly one of two named sentences; "No other form of closing is permitted" in all three |
| C-19 | **PARTIAL** | **1** | Only Step 2 carries an inline gate (model-written line `Measurement protocol established before build.`); all other ordering constraints are stated in the preamble or in the Final Rule at end of document; per C-19, a requirement stated only in preamble or end-of-document contract without co-located inline marker does not pass; weakest C-19 coverage of all five variations |

**V-04 Total: 123 / 130**

---

## V-05 — Hybrid Phase-Table

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1: `*[Phase gate: this phase must produce the first element of your output. Nothing precedes it.]*` |
| C-02 | PASS | 12 | Phase 2 table col 3 "Why this exclusion does not invalidate the test"; ≥2 rows required; "It wasn't needed fails" |
| C-03 | PASS | 12 | Phase 3 gate: "complete every row...before Phase 4 begins...A measurement protocol must exist in the output before any build content can appear"; output contract item 2 verifies |
| C-04 | PASS | 12 | Phase 5 table: Predicted, Actual, Delta, "Why the delta is what it is" columns with explicit "do not leave this for the reader to infer" |
| C-05 | PASS | 12 | Phase 7 table: Verdict + Verdict Rationale; "not a restatement of Phase 5" |
| C-06 | PASS | 10 | Phase 2 col 3 per exclusion; "must answer: why does the hypothesis remain testable without this?"; "It wasn't needed fails" |
| C-07 | PASS | 10 | Phase 5: "one concrete data point — a number, a time, a count, or a direct quote" required in Actual |
| C-08 | PASS | 10 | Phase 8 table: Limitation + Next Step; "do more testing fails" |
| C-09 | PASS | 5 | Phase 6 phase-close A: counter-interpretation + evidence-grounded rebuttal |
| C-10 | PASS | 5 | Phase 9: numbered list, no implicit steps |
| C-11 | PASS | 2 | Output contract rule 5: "Every table cell is populated. Write 'N/A' only where genuinely not applicable — with an inline reason." |
| C-12 | PASS | 2 | Phase 3 gate + output contract item 2 make temporal sequence structurally visible |
| C-13 | PASS | 2 | Phase 5: Delta column, "computed gap; write '0 — prediction confirmed' if match; do not leave this for the reader to infer" |
| C-14 | PASS | 2 | Phase 7: "not a restatement of Phase 5 — it is the reasoning connecting the evidence to the conclusion; it appears in this row" |
| C-15 | PASS | 2 | Col 3 per exclusion: "must answer: why does the hypothesis remain testable without this?" |
| C-16 | PASS | 5 | Phase 6 phase-close: "write exactly one of the following as the terminal element of this phase"; A and B both defined |
| C-17 | PASS | 5 | Tables enforce same-row co-location; output contract items 8–9 verify delta reason and verdict rationale in same row |
| C-18 | PASS | 5 | Phases 6, 8, and 9 each close with A/B phase-close block "as the terminal element"; output contract item 6 verifies all three |
| C-19 | **PARTIAL** | **3** | Phases 1–7 carry `*[Phase gate: ...]*` inline markers; **Phases 8 and 9 have no opening gate markers**; output contract item 10 says "every inline phase gate marker is present" but no markers are defined for phases 8–9; same trailing-section gap as V-01 |

**V-05 Total: 128 / 130**

---

## Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (12) | 12 | 12 | 12 | 12 | 12 |
| C-02 (12) | 12 | 12 | 12 | 12 | 12 |
| C-03 (12) | 12 | 12 | 12 | 12 | 12 |
| C-04 (12) | 12 | 12 | 12 | 12 | 12 |
| C-05 (12) | 12 | 12 | 12 | 12 | 12 |
| C-06 (10) | 10 | 10 | 10 | 10 | 10 |
| C-07 (10) | 10 | 10 | 10 | 10 | 10 |
| C-08 (10) | 10 | 10 | 10 | 10 | 10 |
| C-09 (5) | 5 | 5 | 5 | 5 | 5 |
| C-10 (5) | 5 | 5 | 5 | 5 | 5 |
| C-11 (2) | 2 | 2 | 2 | **1** | 2 |
| C-12 (2) | 2 | 2 | 2 | 2 | 2 |
| C-13 (2) | 2 | 2 | 2 | 2 | 2 |
| C-14 (2) | 2 | 2 | 2 | 2 | 2 |
| C-15 (2) | 2 | 2 | 2 | 2 | 2 |
| C-16 (5) | 5 | 5 | 5 | 5 | 5 |
| C-17 (5) | 5 | 5 | 5 | **3** | 5 |
| C-18 (5) | 5 | 5 | 5 | 5 | 5 |
| C-19 (5) | **3** | **5** | **2** | **1** | **3** |
| **Total** | **128** | **130** | **127** | **123** | **128** |

**Rank**: V-02 (130) > V-01 = V-05 (128) > V-03 (127) > V-04 (123)

---

## Excellence Signals — V-02

V-02 is the sole variation to achieve 130/130. Its two differentiating mechanisms:

**1. All-phases-gated including trailing optional sections**

Every other variation gates the main sequence (phases 1–7) but leaves the trailing optional sections (Limitations, Replication) without inline gate markers, relying on a structural-rules section or output contract to state the ordering constraint. V-02 is the only variation that writes `*Execute after Phase 7 gate is present in your output.*` and `*Execute after Phase 8 gate is present in your output.*` inline at Phases 8 and 9 respectively. The implicit assumption that "obviously last sections don't need gates" is the specific C-19 failure mode for V-01, V-03, and V-05.

**2. Phase-completion line as dual-criterion artifact**

V-02's gate completion lines — e.g., `"PHASE 3 COMPLETE — measurement protocol established before build"` and `"PHASE 6 COMPLETE — DISPOSITION [A/B] SELECTED"` — serve two functions simultaneously: they satisfy C-19 (inline co-located ordering gate, written at the point of the constrained action) and C-12 (measurement ordering made explicit, structurally visible in the actual output). A model-written artifact in the output is verifiable after the fact in a way that a template-only gate marker is not. V-02 is the only variation where the gate exists both as a template directive and as an output-embedded artifact.

---

## New Patterns

Two patterns emerge from this round that are not covered by existing criteria:

**`trailing-section-gate-completeness-enforces-full-c19`**
Three of five variations (V-01, V-03, V-05) share the same C-19 gap: the main sequence (phases/sections 1–7) is fully gated inline, but the trailing optional sections (Limitations, Replication Path) carry no opening gate markers, with their ordering constraints delegated to a structural-rules section or output contract. The pattern identifies this as a systematic failure mode: a prompt that gates "all the important sections" but treats optional trailing sections as self-evidently ordered does not achieve full C-19 compliance. Complete C-19 requires gating every sequentially constrained section, including those that appear to be obviously final.

**`gate-completion-line-as-dual-criterion-artifact`**
V-02's phase completion lines (model-written into the output, not merely present in the template) satisfy C-19 and C-12 simultaneously. A model-written gate artifact — e.g., "PHASE 3 COMPLETE — measurement protocol established before build" — is structurally stronger than a template-only marker because it appears in the actual output and can be independently reviewed. This distinguishes *ordering instruction* (C-19 partially satisfied) from *ordering evidence* (C-19 and C-12 fully satisfied). The dual-criterion artifact pattern is currently not captured by any rubric criterion and could be a candidate for C-20 in v5.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["trailing-section-gate-completeness-enforces-full-c19", "gate-completion-line-as-dual-criterion-artifact"]}
```
