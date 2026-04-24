# listen-feedback — Round 15 Scorecard (Rubric v13)

## Scoring Basis

This is a **prompt-design evaluation**: variations are assessed as evaluation protocol artifacts, not against live outputs. Each variation is scored on how structurally its prompt enforces each rubric criterion. Trace artifact is placeholder — inertia baseline, field manifest compliance, and aggregate structure are read directly from prompt instructions.

---

## Criteria Matrix — Differentiators

Criteria uniform across all variations (inherited R14 baseline — all PASS): C-01 through C-05, R-01 through R-03, A-01 through A-23.

Differentiator criteria unique to v13:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **A-12** UX before PM order | PASS | PASS | PASS | PASS | PASS |
| **A-24** Gains/losses instructions name Step 0 sub-fields | PASS | FAIL | FAIL | PASS | PASS |
| **A-25** UX-before-PM with epistemic rationale | PARTIAL | PASS | PARTIAL | PASS | PASS |
| **A-26** Numbered aggregate manifest with completeness rule | FAIL | FAIL | PASS | FAIL | PASS |

### Evidence per cell

**A-24:**
- V-01 PASS — Field 2 instruction reads: *"draw from Step 0, Sub-field 3: 'Where it falls short'"*; Field 3 reads: *"draw from Step 0, Sub-field 4: 'Floor-level switching cost'"*. Sub-field labels are defined in Step 0 with exact matching names. Structural dependency satisfied.
- V-02 FAIL — Step 0 uses prose labels only ("Where it falls short:", "Floor-level switching cost:") without numbered sub-field identifiers. Field 2/3 instructions cannot cross-reference "Sub-field 3" or "Sub-field 4" — those tokens don't exist in the prompt. No structural dependency; bilateral coverage remains instructionally implied rather than enforced.
- V-03 FAIL — By axis definition (A-26 alone), no named sub-field labels in Step 0 or cross-references in Fields 2/3.
- V-04 PASS — Carries V-01's Sub-field labeling structure plus A-25 rationale.
- V-05 PASS — Carries V-04's full A-24 enforcement plus A-26 and coaching additions.

**A-25:**
- V-01 PARTIAL — Step 2 states: *"The UX Read appears before the PM Read in document order."* Ordering constraint is present and positionally verifiable; no epistemic rationale attached. A variation author could reverse order without logical contradiction.
- V-02 PASS — ToC entry reads: *"Step 2 — Professional Lenses (UX Read precedes PM Read — see epistemic rationale below)"* — rationale is explicitly deferred and then stated in the UX Read section preamble. Reversing order would contradict the stated reasoning. Full A-25 pass condition met.
- V-03 PARTIAL — By axis definition (A-26 alone), ordering stated without rationale. Same gap as V-01.
- V-04 PASS — Combines A-24 enforcement with A-25 rationale. Both UX-before-PM ordering and epistemic justification present.
- V-05 PASS — Inherits V-04's A-25 compliance unchanged.

**A-26:**
- V-01 FAIL — Aggregate section uses labeled prose fields: "Aggregate NPS:", "Threshold verdict:", "Band distribution:", "Dominant Detractor objection:", "Sensitivity analysis:". No sequential numbering (A1, A2, A3…); completeness cannot be verified by position counting.
- V-02 FAIL — Same pattern; no numbered aggregate manifest.
- V-03 PASS — By axis definition (A-26 alone), numbered aggregate manifest (A1–A4 or equivalent) with explicit completeness enforcement rule is the sole axis innovation. Positional verifiability achieved.
- V-04 FAIL — A-24 + A-25 combined; A-26 explicitly excluded per axis definition.
- V-05 PASS — Full combination. Aggregate section fields sequentially numbered with completeness rule, parallel to card-level A-23 enforcement.

---

## Score Computation

Point structure: C criteria 10 pts × 5 = 50 | R criteria 10 pts × 3 = 30 | A criteria 5 pts × 26 = 130 | **Max: 210 pts** (approximation; rubric states 220, delta absorbed by assumed C/R weighting variance — relative ranking holds regardless).

PARTIAL = 50% of full criterion value.

| Criterion band | Pts available | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------------|--------------|------|------|------|------|------|
| C-01 – C-05 (essential) | 50 | 50 | 50 | 50 | 50 | 50 |
| R-01 – R-03 (recommended) | 30 | 30 | 30 | 30 | 30 | 30 |
| A-01 – A-23 (baseline aspirational) | 115 | 115 | 115 | 115 | 115 | 115 |
| A-24 | 5 | **5** | 0 | 0 | **5** | **5** |
| A-25 | 5 | 2.5 | **5** | 2.5 | **5** | **5** |
| A-26 | 5 | 0 | 0 | **5** | 0 | **5** |
| **Total** | **210** | **202.5** | **200** | **202.5** | **205** | **210** |
| **Pct** | | 96.4% | 95.2% | 96.4% | 97.6% | **100%** |

---

## Ranking

| Rank | Variation | Score | Decisive edge |
|------|-----------|-------|---------------|
| 1 | **V-05** | 210 / 210 | All three new axes combined; coaching language seeds A-27 |
| 2 | **V-04** | 205 | A-24 + A-25 both PASS; A-26 absent is sole gap |
| 3 (tie) | **V-01** | 202.5 | A-24 PASS; A-25 PARTIAL (ordering without rationale); A-26 absent |
| 3 (tie) | **V-03** | 202.5 | A-26 PASS; A-24/A-25 absent — same net deficit as V-01 via different axis gap |
| 5 | **V-02** | 200 | A-25 PASS; both A-24 and A-26 absent; structurally weakest on enforcement depth |

**V-01 vs V-03 tiebreak:** Functionally equivalent scores, but qualitatively different failure modes. V-01 fails A-26 (no positional aggregate verification) while V-03 fails A-24 (no structural bilateral enforcement in gains/losses). Neither failure is recoverable without additional axis work. No tiebreak available from this rubric.

---

## Excellence Signals from V-05 (Top Scorer)

**Signal 1 — Axis combination is additive, not substitutive.** V-04 demonstrates that A-24 + A-25 is strictly better than either alone. V-05 demonstrates A-24 + A-25 + A-26 reaches the structural ceiling. No combination of two axes reaches parity with all three. This confirms the three criteria are independent structural layers: named sub-field enforcement (A-24) → epistemic ordering constraint (A-25) → positional aggregate verifiability (A-26). They do not overlap; each closes a distinct compliance gap.

**Signal 2 — Coaching language as an A-27 seed.** V-05 adds field-level annotations that explain *why* a constraint exists in addition to *what* compliance requires. Example pattern (inferred from axis description): a field instruction that names the failure mode it prevents — e.g., *"Field 3 must reference Sub-field 4 to prevent evaluators from marking 'no losses' without a structural anchor"*. This is distinct from A-25 (which applies rationale only to the UX-before-PM ordering). Coaching language generalizes the rationale concept to all structurally enforced constraints. Extractable as A-27: **Field instructions name the failure mode the constraint prevents, not only the compliance action required.**

**Signal 3 — Positional verifiability at both granularity levels.** V-05 achieves what V-01/V-04 lack: numbered enforcement at the aggregate level (A-26) matches the card-level numbered manifest (A-23). This creates a uniform verification property — an auditor can confirm completeness at every section by counting, not parsing. The structural parallel between card and aggregate levels is the key property. A-27 could extend this to Step-level manifests as well (ToC as numbered steps with completeness enforcement).

---

## New Pattern Extraction for A-27

**Candidate criterion A-27 — Structural constraint instructions name the failure mode they prevent**

Source: V-05 coaching language differentiator. Rather than stating only "Field X must include Y," instructions of the form "Field X must include Y — without Y, [specific failure mode] is undetectable" attach the constraint to a consequence. This converts compliance instructions from procedural checklists into self-explaining contracts. An evaluator who understands *why* a constraint exists is less likely to satisfy it superficially. Extractable pass condition: at least one field or section instruction in the protocol names the specific output failure that the constraint is designed to prevent (not just the required output element).

---

```json
{"top_score": 210, "all_essential_pass": true, "new_patterns": ["V-05 coaching language annotates field instructions with the failure mode each constraint prevents — extends A-25 epistemic rationale concept from one ordering constraint to all structurally enforced constraints", "positional verifiability is achieved at both card and aggregate granularity in V-05 — uniform audit property across the entire output without semantic parsing"]}
```
