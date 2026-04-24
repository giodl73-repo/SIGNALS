# campaign-specify — Round 9 Scorecard (Rubric v9)

## Scoring Formula

```
composite = (essential_pass / 5 * 60) + (rec_pass / 3 * 30) + (asp_pass / 27 * 10)
```

All five variations inherit the base structure from R8. Essential and recommended criteria are structural invariants — all pass across all variations.

---

## Per-Variation Analysis

### V-01 — Lifecycle Emphasis: Explicit C-35 Instruction Block

**Axis**: Instruction paragraph before audit row template. Gate anchor absent.

| Tier | ID | Result | Evidence |
|------|----|--------|----------|
| Essential | C-01 | PASS | Three artifacts: spec, proposal, pitch — write gates present |
| Essential | C-02 | PASS | Six sections: Overview, User Problem, Proposed Solution, Constraints, Open Questions, Self-Review |
| Essential | C-03 | PASS | Do Nothing option + two others; Recommendation with Defeating Do Nothing and Defeating [Other] blocks |
| Essential | C-04 | PASS | Exec, Dev, Maker versions + Anti-Positioning |
| Essential | C-05 | PASS | Feature scope consistent across all three artifacts |
| Recommended | C-06 | PASS | Self-Review requires "at least one named gap; No gaps found fails" |
| Recommended | C-07 | PASS | Anti-Positioning section present and structurally separate |
| Recommended | C-08 | PASS | Recommendation cites specific trade-off traceable to risk/effort fields |
| Aspirational | C-09–C-26 | PASS (18) | Inherited; base structure unchanged from R8 |
| Aspirational | C-27 | PASS | `### Voice Compliance Audit` present; COMPLETION INDEX preamble enumerates four named sections |
| Aspirational | C-28 | PASS | Step 3 has Exec gate / Dev gate / Maker gate each with independent Pass/Fail |
| Aspirational | C-29 | PASS | Gate questions name "the Step 0c exec/dev/maker voice contract" — contract attribution in gate label text |
| Aspirational | C-32 | PASS | COMPLETION INDEX preamble: "Each section classifies a distinct category of compliance state" |
| Aspirational | C-33 | PASS | Three per-audience bullet rows; instruction reinforces "Record one verdict row per audience" |
| Aspirational | C-34 | **FAIL** | Pass parenthetical: `Pass (opening names a business cost, risk, or revenue consequence)` — bare behavioral criterion, no Step 0c contract attribution |
| Aspirational | C-35 | PASS | Instruction names requirement in prose: "A row that records only `[Audience] verdict: [Pass / Fail]` without inline contract attribution does not satisfy this section." Row template: `— Step 0c exec voice contract verified` |

**Asp earned**: C-09–C-33, C-35 = **26/27** (misses C-34)

```
Composite = (5/5 × 60) + (3/3 × 30) + (26/27 × 10) = 60 + 30 + 9.63 = 99.6
```

---

### V-02 — Output Format: Table Audit Rows with Contract Column

**Axis**: Table replaces bullet rows in Voice Compliance Audit. Gate anchor preserved (C-34 targeted).

| Tier | ID | Result | Evidence |
|------|----|--------|----------|
| Essential | C-01–C-05 | PASS | Same base structure |
| Recommended | C-06–C-08 | PASS | Unchanged |
| Aspirational | C-09–C-26 | PASS (18) | Inherited |
| Aspirational | C-27 | PASS | `### Voice Compliance Audit` with COMPLETION INDEX preamble enumerating four named sections |
| Aspirational | C-28 | PASS | Per-audience gates in Step 3 |
| Aspirational | C-29 | PASS | `Pass (Step 0c exec voice contract satisfied: ...)` names contract |
| Aspirational | C-32 | PASS | Categorization declaration unchanged |
| Aspirational | C-33 | PASS | Table has one row per audience (exec, dev, maker) — individual verdicts recorded separately |
| Aspirational | C-34 | PASS | Gate parenthetical: `Pass (Step 0c exec voice contract satisfied: opening names...)` — contract attributed |
| Aspirational | C-35 | PASS* | Table column `Step 0c Contract Verified` with value `Step 0c exec voice contract` — attribution IS within the same row record. Rubric says "inline within the row" (not "inline in the same cell"); table rows satisfy this. The `(e.g., ...)` in the pass condition marks the bullet form as illustrative, not mandatory. |

*C-35 interpretation note: The table column places the contract attribution in a different cell than the verdict, but remains within the same row. The rubric's pass condition is format-agnostic ("inline within the row"), making this a PASS. If a future rubric revision tightens the form requirement to the em-dash bullet specifically, V-02 would drop to 26/27.

**Asp earned**: All 27 = **27/27**

```
Composite = (5/5 × 60) + (3/3 × 30) + (27/27 × 10) = 60 + 30 + 10.0 = 100.0
```

---

### V-03 — Phrasing Register: "Satisfied" Verb in Audit Rows

**Axis**: `verified` → `satisfied` in audit rows. Gate anchor preserved. No other changes.

| Tier | ID | Result | Evidence |
|------|----|--------|----------|
| Essential | C-01–C-05 | PASS | Unchanged |
| Recommended | C-06–C-08 | PASS | Unchanged |
| Aspirational | C-09–C-26 | PASS (18) | Inherited |
| Aspirational | C-27 | PASS | Formal section, preamble enumerating four sections |
| Aspirational | C-28 | PASS | Per-audience gates |
| Aspirational | C-29 | PASS | `Pass (Step 0c exec voice contract satisfied: ...)` |
| Aspirational | C-32 | PASS | Categorization declaration |
| Aspirational | C-33 | PASS | Three per-audience bullet rows |
| Aspirational | C-34 | PASS | `Pass (Step 0c exec voice contract satisfied: ...)` — contract attributed in parenthetical |
| Aspirational | C-35 | PASS | `- Exec verdict: [Pass / Fail] — Step 0c exec voice contract satisfied`. Attribution is inline within each row. C-35 is verb-agnostic; "satisfied" is structurally equivalent to "verified" for purposes of this criterion. |

**Asp earned**: All 27 = **27/27**

```
Composite = (5/5 × 60) + (3/3 × 30) + (27/27 × 10) = 100.0
```

**Diagnostic finding**: C-35 is verb-agnostic. "Verified" and "satisfied" both earn it. Lexical consistency between gate parenthetical ("satisfied") and audit rows ("satisfied") is a structural bonus — not required but creates cleaner traceability.

---

### V-04 — Combined: Instruction + "Satisfied" Rows, No Gate Anchor

**Axis**: V-01 instruction + V-03 "satisfied" verb. C-34 intentionally absent.

| Tier | ID | Result | Evidence |
|------|----|--------|----------|
| Essential | C-01–C-05 | PASS | Unchanged |
| Recommended | C-06–C-08 | PASS | Unchanged |
| Aspirational | C-09–C-26 | PASS (18) | Inherited |
| Aspirational | C-27 | PASS | Formal section header + four-section preamble |
| Aspirational | C-28 | PASS | Per-audience gates in Step 3 |
| Aspirational | C-29 | PASS | Gate question text: "the Step 0c exec voice contract" names the contract |
| Aspirational | C-32 | PASS | Categorization declaration |
| Aspirational | C-33 | PASS | Per-audience rows with explicit instruction: "Record one verdict row per audience" |
| Aspirational | C-34 | **FAIL** | Parenthetical: `Pass (opening names a business cost, risk, or revenue consequence)` — bare, no Step 0c contract name |
| Aspirational | C-35 | PASS | Instruction with explicit non-passing form cited + "satisfied" rows: `— Step 0c exec voice contract satisfied`. Both instruction + template independently earn C-35; combined form is the strongest C-35 signal without C-34. |

**Confirmation**: C-35 is structurally independent from C-34 — earned here without the gate anchor.

**Asp earned**: 26/27 (misses C-34)

```
Composite = (5/5 × 60) + (3/3 × 30) + (26/27 × 10) = 60 + 30 + 9.63 = 99.6
```

---

### V-05 — Full Traceability: Instruction + "Satisfied" + Gate Anchor + Cross-Reference Pointer

**Axis**: All winning mechanisms combined. Bidirectional pointer added after Step 4.

| Tier | ID | Result | Evidence |
|------|----|--------|----------|
| Essential | C-01–C-05 | PASS | Unchanged |
| Recommended | C-06–C-08 | PASS | Unchanged |
| Aspirational | C-09–C-26 | PASS (18) | Inherited |
| Aspirational | C-27 | PASS | `### Voice Compliance Audit` + COMPLETION INDEX preamble enumerating four named sections |
| Aspirational | C-28 | PASS | "Each audience gate must independently pass" — exec/dev/maker gates with Pass/Fail |
| Aspirational | C-29 | PASS | `Pass (Step 0c exec voice contract satisfied: ...)` in Step 3; Step 4 names "Step 0c voice contract for that audience" as rewrite anchor |
| Aspirational | C-32 | PASS | COMPLETION INDEX preamble: "Each section classifies a distinct category of compliance state" |
| Aspirational | C-33 | PASS | Three per-audience rows; instruction paragraph reinforces "Record one verdict row per audience" |
| Aspirational | C-34 | PASS | `Pass (Step 0c exec voice contract satisfied: opening names a business cost...)` — contract named in parenthetical for all three audiences |
| Aspirational | C-35 | PASS | Triple-layer: (1) instruction paragraph naming the form, (2) "satisfied" verb matching gate language, (3) bidirectional cross-reference note: "The Voice Compliance Audit rows in the COMPLETION INDEX below record the outcome of each gate above. Each audit row names the same Step 0c contract verified by its gate." All three layers converge on inline per-row contract attribution. |

**Asp earned**: All 27 = **27/27**

```
Composite = (5/5 × 60) + (3/3 × 30) + (27/27 × 10) = 100.0
```

---

## Summary

| Variation | Essential | Rec | Asp | Composite | C-34 | C-35 |
|-----------|-----------|-----|-----|-----------|------|------|
| V-01 | 5/5 | 3/3 | 26/27 | **99.6** | FAIL | PASS |
| V-02 | 5/5 | 3/3 | 27/27 | **100.0** | PASS | PASS (table) |
| V-03 | 5/5 | 3/3 | 27/27 | **100.0** | PASS | PASS |
| V-04 | 5/5 | 3/3 | 26/27 | **99.6** | FAIL | PASS |
| V-05 | 5/5 | 3/3 | 27/27 | **100.0** | PASS | PASS |

**Predicted vs Actual:**

| Variation | Predicted | Actual | Match |
|-----------|-----------|--------|-------|
| V-01 | 26/27 (99.6) | 26/27 (99.6) | Exact |
| V-02 | 27/27 (100.0) | 27/27 (100.0) | Confirmed (table format earns C-35) |
| V-03 | 27/27 (100.0) | 27/27 (100.0) | Exact |
| V-04 | 26/27 (99.6) | 26/27 (99.6) | Exact |
| V-05 | 27/27 (100.0) | 27/27 (100.0) | Exact |

---

## Excellence Signals

**From V-05 (maximum traceability density):**

**E-01: Verb lexical consistency between gate enforcement and audit record.** Using "satisfied" in both the gate parenthetical (`Pass (Step 0c exec voice contract satisfied: ...)`) and the audit row (`— Step 0c exec voice contract satisfied`) creates a self-consistent chain — a model reading the gate parenthetical and then writing the audit row uses the same verb without needing to translate. This is a zero-cost improvement over "verified": same C-35 outcome, cleaner traceability narrative.

**E-02: Bidirectional cross-reference pointer bridging Phase 3 and COMPLETION INDEX.** The note after Step 4 — "The Voice Compliance Audit rows in the COMPLETION INDEX below record the outcome of each gate above. Each audit row names the same Step 0c contract verified by its gate" — makes the structural relationship self-documenting. Without this pointer, the connection between gate verdicts and audit rows is implicit (the model must infer it). With the pointer, it is declared. This adds C-35 evidence density at the gate enforcement location, not just at the audit section — creating forward and backward traceability.

**E-03: Table format is a valid C-35 form (V-02 diagnostic confirmation).** C-35's "inline within the row" requirement is format-agnostic. A dedicated table column satisfies it as well as the em-dash bullet form. The rubric's example was illustrative; the criterion is structural. This opens table format as an alternative for the audit section without rubric penalty.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Verb lexical consistency between gate parenthetical and audit rows: using 'satisfied' in both locations creates a self-consistent traceability chain without requiring the model to translate between enforcement and audit vocabulary", "Bidirectional cross-reference pointer after Step 4 explicitly declares the structural link between Phase 3 gate verdicts and COMPLETION INDEX audit rows, adding C-35 evidence density at the gate location and making the connection self-documenting rather than implicit"]}
```
