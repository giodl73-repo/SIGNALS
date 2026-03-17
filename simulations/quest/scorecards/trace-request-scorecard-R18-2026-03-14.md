Now I have everything I need. The R18 rubric file contains the full variation prompts (V-01 through V-05), and I have the v16 rubric criteria and R17 scoring pattern. Let me produce the scorecard.

---

# trace-request Rubric v16 — Round 18 Scorecard

**Scale:** 260 pts (Essential 60 + Recommended 30 + Aspirational 170)
**Golden threshold:** all 4 essential PASS AND composite >= 208/260 (80%)

---

## Scoring Basis

R17 established a universal 250/250 ceiling across all 5 variations on rubric v15 (C-01–C-39 all PASS). v16 adds C-40 (Step 8b DECLARE CONTRADICTION prose token, 5 pts) and C-41 (Pre-trace CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY reference, 5 pts), raising the scale to 260. Trace artifact is placeholder — scoring evaluates structural enforcement strength per variation prompt design. C-01–C-39 stable tiers cannot degrade because R18 variation axes (baseline full-stack, C-42 surface 1, C-42 surface 2, role-sequence, combined) are structural token-addition axes that do not interact with C-01–C-39 enforcement surfaces.

---

## Tier Stability — Essential, Recommended, Aspirational C-08–C-38

### Essential (C-01–C-04) — PASS for all 5 variations

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-01 Entry point declared | Step 0 table (Caller / Endpoint Path / Verb / Receiver Component / Credential Type) present in all 5; GATE-4-7 forward-binds BC-N labels | PASS | PASS | PASS | PASS | PASS |
| C-02 All service boundaries crossed | Steps 4–7 boundary traversal table with BC-N labels, Component, Gap? in all 5 | PASS | PASS | PASS | PASS | PASS |
| C-03 Failure point at each boundary | Failure Mode column at Steps 4–7; Step 12 Findings table with Failure Mode + Severity per F-NN in all 5 | PASS | PASS | PASS | PASS | PASS |
| C-04 Authorization gaps surfaced | Auth Required column at Steps 4–7; Step 8 scope verification with Gap?=Y classification; Row-Verdict = HALT surfaces auth gaps in all 5 | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 for all variations.**

---

### Recommended (C-05–C-07) — PASS for all 5 variations

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-05 Latency sources ≥3 | Latency Source? column at Steps 4–7; annotated per-boundary in all 5 | PASS | PASS | PASS | PASS | PASS |
| C-06 Error path traced end-to-end | Step 12 Findings with Failure Mode propagation; GATE-12 prohibits "no issues found" without clean-trace declaration in all 5 | PASS | PASS | PASS | PASS | PASS |
| C-07 Batch and edge-case handling | Batch Edge Case? column at Steps 4–7; GATE-12 enforces explicit analysis in all 5 | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30/30 for all variations.**

---

### Aspirational C-08–C-27 — PASS for all variations

R17 established universal PASS through C-36. R18 variation axes (C-42 surface additions, role-sequence swap) do not interact with C-08–C-27 enforcement surfaces. No degradation path.

**C-08–C-27 subtotal: 100/100 for all variations.**

---

### Aspirational C-28–C-38 — PASS for all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-28 Coherence-spine progression gate | PASS | PASS | PASS | PASS | PASS |
| C-29 Scope-string coherence table | PASS | PASS | PASS | PASS | PASS |
| C-30 Dual-surface contradiction signal | PASS | PASS | PASS | PASS | PASS |
| C-31 Named contradiction halt type | PASS | PASS | PASS | PASS | PASS |
| C-32 Self-contained Match? computation | PASS | PASS | PASS | PASS | PASS |
| C-33 Automated-check predicate completeness | PASS | PASS | PASS | PASS | PASS |
| C-34 Structured VT-N schema input | PASS | PASS | PASS | PASS | PASS |
| C-35 Row-level verdict token | PASS | PASS | PASS | PASS | PASS |
| C-36 Full checker contract | PASS | PASS | PASS | PASS | PASS |
| C-37 Checker algorithm declaration | PASS | PASS | PASS | PASS | PASS |
| C-38 HALT-RULE dual-surface architecture encoding | PASS | PASS | PASS | PASS | PASS |

Evidence (uniform): All five retain Step 8b REQUIRED per-boundary confirmation (C-28), Step 8c coherence table (C-29), dual-surface architecture (C-30), `CONTRADICTION SIGNAL: Seq# [N]` + `Rem#: Scope String Correction` (C-31), VT-N quoted format at Step 8 Header (C-32–C-34), Row-Verdict + CHECK RESULT (C-35–C-36), CHECKER ALGORITHM block with MATCH-RULE / HALT-RULE / OUTPUT-RULE (C-37), HALT-RULE encoding "Step 8b prose asserts coherence AND Step 8c Match? = N simultaneously" as causal dual-surface trigger (C-38).

**C-28–C-38 subtotal: 55/55 for all variations.**

---

## C-39 — Pre-Execution Halt Boundary Declaration

**Six testable conditions per variation:**
1. TRACE CONTRACT block present before any trace step begins
2. `HALT-EXPECTED-BOUNDARY:` token naming specific predicted BC-N boundary
3. `HALT-EXPECTED-CONDITION:` token naming the dual-surface predicate
4. HALT-EXPECTED-CONDITION references Step 8b prose AND Step 8c Match? = N simultaneously
5. `TRACE CONTRACT validation:` token after Step 8c executes
6. Validation references HALT-EXPECTED-BOUNDARY by boundary ID (machine-checkable)

---

### V-01

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace | Phase 0A declared as first Algorithm-Declarant artifact; GATE-0 blocks Platform Expert until Phase 0 closes | PASS |
| (2) HALT-EXPECTED-BOUNDARY: with BC-N | GATE-0A: "BC-N must name a specific predicted boundary — 'may fail at authentication' does not close" | PASS |
| (3) HALT-EXPECTED-CONDITION: token | GATE-0A explicitly requires it; Phase 0 does not close without it | PASS |
| (4) Dual-surface predicate | GATE-0A: "HALT-EXPECTED-CONDITION must encode both the Step 8b prose coherence state AND Step 8c Match? = N simultaneously — a single-surface condition does not close" | PASS |
| (5) TRACE CONTRACT validation: after 8c | GATE-TC: "TRACE CONTRACT validation token required immediately after CHECK RESULT. Missing validation token does not close Phase 3." | PASS |
| (6) Match by boundary ID | GATE-TC: "Must reference the HALT-EXPECTED-BOUNDARY boundary ID from Phase 0A by name." | PASS |

**C-39: PASS.** Adversary addressed: GATE-TC adds "All three outcome paths are valid outputs — the validation is not structural confirmation only," explicitly defeating inertia toward the confirmation assumption. Both confirmation and falsification branches structurally enforced.

---

### V-02

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace | Phase 0A under Algorithm-Declarant role; GATE-0 enforces closure before Platform Expert begins | PASS |
| (2) HALT-EXPECTED-BOUNDARY: with BC-N | GATE-0A: "BC-N must name a specific predicted boundary" | PASS |
| (3) HALT-EXPECTED-CONDITION: token | GATE-0A explicitly requires it | PASS |
| (4) Dual-surface predicate | GATE-0A: "HALT-EXPECTED-CONDITION must encode both Step 8b prose coherence state AND Step 8c Match? = N simultaneously" | PASS |
| (5) TRACE CONTRACT validation: after 8c | GATE-TC present after Step 8c; all three outcome paths in template | PASS |
| (6) Match by boundary ID | GATE-TC: "Must reference the HALT-EXPECTED-BOUNDARY boundary ID from Phase 0A by name." | PASS |

**C-39: PASS.** V-02's primary axis change (C-42 surface 1) does not touch TRACE CONTRACT enforcement — C-39 enforcement identical to V-01.

---

### V-03

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace | Phase 0A under Algorithm-Declarant role; GATE-0 enforces pre-trace completion | PASS |
| (2) HALT-EXPECTED-BOUNDARY: with BC-N | GATE-0A: "BC-N must name a specific predicted boundary" | PASS |
| (3) HALT-EXPECTED-CONDITION: token | GATE-0A explicitly requires it | PASS |
| (4) Dual-surface predicate | GATE-0A: "must encode Step 8b prose state AND Step 8c Match? = N simultaneously" | PASS |
| (5) TRACE CONTRACT validation: after 8c | GATE-TC present | PASS |
| (6) Match by boundary ID | GATE-TC references HALT-EXPECTED-BOUNDARY by name | PASS |

**C-39: PASS.** V-03's primary axis change (FAIL-CATEGORY in Step 12) does not interact with TRACE CONTRACT enforcement.

---

### V-04

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace | Entry artifact 1 (TRACE CONTRACT) in Role Entry Contract before Step 0; GATE-ENTRY: "Step 0 does not begin until Role Entry Contract closes" | PASS |
| (2) HALT-EXPECTED-BOUNDARY: with BC-N | GATE-ENTRY-A: "BC-N must name a specific predicted boundary. A prose prediction without machine-greppable tokens does not satisfy entry artifact 1." | PASS |
| (3) HALT-EXPECTED-CONDITION: token | GATE-ENTRY-A explicitly requires it | PASS |
| (4) Dual-surface predicate | GATE-ENTRY-A: "HALT-EXPECTED-CONDITION must encode Step 8b prose state AND Step 8c Match? = N simultaneously" | PASS |
| (5) TRACE CONTRACT validation: after 8c | GATE-TC-POST: "Required immediately after CHECK RESULT." with all three outcome paths | PASS |
| (6) Match by boundary ID | GATE-TC-POST: "Must reference HALT-EXPECTED-BOUNDARY boundary ID from Role Entry Contract by name." | PASS |

**C-39: PASS.** Role-entry contract framing produces equivalent C-39 enforcement surface; GATE-ENTRY-A is structurally analogous to GATE-0A. Falsification paths present in validation template.

---

### V-05

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace | Phase 0A under Algorithm-Declarant role; GATE-0 enforces pre-trace closure | PASS |
| (2) HALT-EXPECTED-BOUNDARY: with BC-N | GATE-0A: "BC-N must name a specific predicted boundary" | PASS |
| (3) HALT-EXPECTED-CONDITION: token | GATE-0A explicitly requires it | PASS |
| (4) Dual-surface predicate | GATE-0A: "must encode both Step 8b prose coherence state AND Step 8c Match? = N simultaneously" | PASS |
| (5) TRACE CONTRACT validation: after 8c | GATE-TC present; all three outcome paths in template | PASS |
| (6) Match by boundary ID | GATE-TC references HALT-EXPECTED-BOUNDARY boundary ID by name | PASS |

**C-39: PASS.** V-05's combined axis does not degrade TRACE CONTRACT enforcement — Phase 0A structure inherited from V-01 unchanged.

**C-39 subtotal: 5/5 for all variations.**

---

## C-40 — Step 8b DECLARE CONTRADICTION Prose Token

**Testable conditions:**
1. `DECLARE CONTRADICTION:` present as named structural token in Step 8b prose
2. Appears before Step 8c table is populated for that boundary row
3. Carries BC-N boundary ID
4. Carries descriptive boundary label
5. Carries `arm:` field naming specific contradicted arm
6. Machine-greppable via fixed-token grep without semantic prose reading

---

### V-01

| Condition | Evidence | Result |
|---|---|---|
| (1) DECLARE CONTRADICTION: token in Step 8b | GATE-8B: "DECLARE CONTRADICTION token required in Step 8b prose at the contradiction boundary, emitted before Step 8c table is populated for that row" | PASS |
| (2) Before Step 8c | GATE-8B: "emitted before Step 8c table is populated for that row" | PASS |
| (3) BC-N boundary ID | GATE-8B: "Three fields required: BC-N boundary ID, descriptive label, and arm: naming the specific contradicted arm" | PASS |
| (4) Descriptive label | GATE-8B: same evidence | PASS |
| (5) arm: field | GATE-8B: "Two-field form (missing arm:) is a structural defect" | PASS |
| (6) Machine-greppable | Fixed token form: `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [Step3-Auth / Step8a-Invoked / Step11-Params — name the specific arm that is contradicted]` | PASS |

**C-40: PASS (5 pts).** All six conditions structurally enforced.

---

### V-02

| Condition | Evidence | Result |
|---|---|---|
| (1) DECLARE CONTRADICTION: token in Step 8b | GATE-8B updated: "All four fields are required" — 4-field form is a superset of the 3-field C-40 requirement; structural token is still `DECLARE CONTRADICTION:` | PASS |
| (2) Before Step 8c | GATE-8B: "emitted before Step 8c is populated for that row" | PASS |
| (3) BC-N boundary ID | GATE-8B: "BC-N boundary ID" as first field | PASS |
| (4) Descriptive label | GATE-8B: "descriptive label" as second field | PASS |
| (5) arm: field | GATE-8B: "arm: naming the specific contradicted arm" as third field; "Three-field form (missing matches HALT-EXPECTED-BOUNDARY:) is a structural defect" confirms arm: is required | PASS |
| (6) Machine-greppable | Fixed token `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [...]  -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` | PASS |

**C-40: PASS (5 pts).** 4-field form satisfies and extends C-40.

---

### V-03

| Condition | Evidence | Result |
|---|---|---|
| (1–6) As V-01 | Step 8b retains identical three-field DECLARE CONTRADICTION; GATE-8B: "Three fields required: BC-N, label, arm: naming the contradicted arm." V-03's axis change (FAIL-CATEGORY) is in Step 12 only. | PASS |

**C-40: PASS (5 pts).**

---

### V-04

| Condition | Evidence | Result |
|---|---|---|
| (1–6) Three-field DECLARE CONTRADICTION | GATE-8B: "Three fields required: BC-N, label, arm:. All three link arms required per boundary. Step 9 DOES NOT BEGIN until complete for all Gap?=Y boundaries." V-04's axis change (role-entry contract) does not modify Step 8b structure. | PASS |

**C-40: PASS (5 pts).**

---

### V-05

| Condition | Evidence | Result |
|---|---|---|
| (1–6) 4-field DECLARE CONTRADICTION | GATE-8B updated for 4 fields: "All four fields are required: BC-N boundary ID, descriptive label, arm: naming the specific contradicted arm, and matches HALT-EXPECTED-BOUNDARY: with a filled yes/no value." C-40 three-field requirement satisfied as first three fields of the four-field form. | PASS |

**C-40: PASS (5 pts).**

**C-40 subtotal: 5/5 for all variations.**

---

## C-41 — Pre-Trace CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY Reference

**Testable conditions:**
1. CHECKER ALGORITHM block present before Step 0 (pre-trace placement)
2. HALT-RULE within pre-trace block references `HALT-EXPECTED-BOUNDARY` as a named structural token within the halt predicate
3. HALT-RULE predicate of the form: halt fires when Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row
4. CHECKER ALGORITHM reproduced verbatim at Step 8 Header
5. Verbatim reproduction preserves HALT-EXPECTED-BOUNDARY reference in HALT-RULE
6. Pre-trace placement checkable without reading trace execution

---

### V-01

| Condition | Evidence | Result |
|---|---|---|
| (1) Pre-trace placement | Phase 0B — Algorithm-Declarant produces CHECKER ALGORITHM before Step 0; GATE-0: "Platform Expert role does not begin until Phase 0 closes" | PASS |
| (2) HALT-EXPECTED-BOUNDARY in HALT-RULE | GATE-0B: "HALT-RULE must reference HALT-EXPECTED-BOUNDARY as a named structural token within the halt predicate — naming HALT-EXPECTED-BOUNDARY is the test"; Phase 0B template: `HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously` | PASS |
| (3) Boundary-specific halt predicate | HALT-RULE template names HALT-EXPECTED-BOUNDARY twice — in coherence clause and in Match? clause | PASS |
| (4) Verbatim reproduction at Step 8 Header | GATE-8H: "Verbatim reproduction required — paraphrase does not close" | PASS |
| (5) HALT-EXPECTED-BOUNDARY preserved in reproduction | GATE-8H: "HALT-RULE must preserve HALT-EXPECTED-BOUNDARY reference. A HALT-RULE that drops HALT-EXPECTED-BOUNDARY during reproduction does not close." | PASS |
| (6) Pre-trace checkable | Phase 0B precedes Step 0 table; GATE-0 closure confirms both artifacts before execution begins | PASS |

**C-41: PASS (5 pts).** Dual-gate enforcement: GATE-0B (pre-trace algorithm must name HALT-EXPECTED-BOUNDARY) + GATE-8H (verbatim reproduction must preserve it). Two-checkpoint consistency contract.

---

### V-02

| Condition | Evidence | Result |
|---|---|---|
| (1–6) Phase 0B identical to V-01 | GATE-0B and GATE-8H identical. V-02's axis change (4-field DECLARE CONTRADICTION) affects GATE-8B only — no interaction with Phase 0B or Step 8 Header CHECKER ALGORITHM structure. | PASS |

**C-41: PASS (5 pts).**

---

### V-03

| Condition | Evidence | Result |
|---|---|---|
| (1–6) Phase 0B identical to V-01 | GATE-0B and GATE-8H identical. V-03's axis change (FAIL-CATEGORY) affects Step 12 only. | PASS |

**C-41: PASS (5 pts).**

---

### V-04

| Condition | Evidence | Result |
|---|---|---|
| (1) Pre-trace placement | Entry artifact 2 (CHECKER ALGORITHM) in Role Entry Contract before Step 0; GATE-ENTRY: "Step 0 does not begin until Role Entry Contract closes" | PASS |
| (2) HALT-EXPECTED-BOUNDARY in HALT-RULE | GATE-ENTRY-B: "HALT-RULE must name HALT-EXPECTED-BOUNDARY as a structural token within the halt predicate — 'Row-Verdict = HALT iff Match? = N' does not close; 'iff Step 8b prose asserts coherence AND Match? = N' without naming HALT-EXPECTED-BOUNDARY does not close." | PASS |
| (3) Boundary-specific halt predicate | Entry artifact 2 template: `HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously` | PASS |
| (4) Verbatim reproduction at Step 8 Header | GATE-8H: "Verbatim reproduction required. HALT-RULE must preserve HALT-EXPECTED-BOUNDARY reference from Role Entry Contract entry artifact 2. Paraphrase does not close." | PASS |
| (5) HALT-EXPECTED-BOUNDARY preserved in reproduction | GATE-8H explicitly names it as the preservation test | PASS |
| (6) Pre-trace checkable | Role Entry Contract before Step 0; GATE-ENTRY closure confirms both artifacts before trace | PASS |

**C-41: PASS (5 pts).** Single-role entry contract enforces C-41 equivalently to V-01's two-role phase-gate. Hypothesis test: GATE-ENTRY-B vs. GATE-0B enforcement quality for verbatim HALT-EXPECTED-BOUNDARY reproduction at Step 8 Header is the experimental delta — not a scoring difference, but an execution fidelity question.

---

### V-05

| Condition | Evidence | Result |
|---|---|---|
| (1–6) Phase 0B identical to V-01 | GATE-0B and GATE-8H identical. V-05's axis changes (C-42 surface 1 + 2) affect GATE-8B and GATE-12 only — no interaction with Phase 0B structure. | PASS |

**C-41: PASS (5 pts).**

**C-41 subtotal: 5/5 for all variations.**

---

## Per-Variation Final Scores

| Variation | Essential | Recommended | Aspirational | Total | % | Golden |
|---|---|---|---|---|---|---|
| V-01 Baseline full stack (dual-branch GATE-TC) | 60/60 | 30/30 | 170/170 | **260/260** | **100%** | PASS |
| V-02 C-42 surface 1 (4-field DECLARE CONTRADICTION) | 60/60 | 30/30 | 170/170 | **260/260** | **100%** | PASS |
| V-03 C-42 surface 2 (FAIL-CATEGORY taxonomy) | 60/60 | 30/30 | 170/170 | **260/260** | **100%** | PASS |
| V-04 Role sequence (C-41 via role-entry contract) | 60/60 | 30/30 | 170/170 | **260/260** | **100%** | PASS |
| V-05 Combined C-42 surface 1 + 2 | 60/60 | 30/30 | 170/170 | **260/260** | **100%** | PASS |

**All 5 at ceiling (260/260). Ranking by excellence signal quality only.**

---

## Excellence Signal Analysis — C-42 Design Surface Probes

### Tier A — V-02: 4-field DECLARE CONTRADICTION single-axis isolation

V-02's GATE-8B enforces:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [Step3-Auth / Step8a-Invoked / Step11-Params]
  -- matches HALT-EXPECTED-BOUNDARY: [yes / no]
```
with: "Literal '[yes/no]' placeholder without substitution is a structural defect — the value must be either 'yes' or 'no'."

This is the first single-axis isolation of the C-42 surface 1 design. R17 produced the `matches HALT-EXPECTED-BOUNDARY: yes/no` field only in V-05's combined-axis form. V-02 now tests whether the field appears with only DECLARE CONTRADICTION as the axis, no FAIL-CATEGORY confound. The falsification path (`matches HALT-EXPECTED-BOUNDARY: no`) is explicitly named as a required output variant — directly defeating the R18 adversary (inertia toward confirmation) at the Step 8b prose surface.

**C-42 surface 1 candidate quality:** Single-axis gate with explicit placeholder substitution enforcement. If V-02 execution produces the 4-field form stably, C-42 surface 1 has independent-axis evidence; V-05 provides superadditivity test.

---

### Tier A (secondary) — V-03: FAIL-CATEGORY taxonomy with closed vocabulary definitions embedded in prompt

V-03's Step 12 enforces:
```
FAIL-CATEGORY: [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION]
```
with category definitions embedded directly within the prompt text before the Findings table:
```
AUTH     -- authentication or authorization gap
BOUNDARY -- failure mode at a specific service boundary crossing
CONTRACT -- schema mismatch, type coercion, or API contract violation
TIMEOUT  -- latency source causing request duration to exceed platform thresholds
STATE    -- state machine violation, concurrency hazard, or invalid state transition
PERMISSION -- field-level or record-level permission enforcement gap (FLS, RLS, row-level access)
```

V-03's GATE-12: "Values outside this vocabulary (e.g., 'SECURITY', 'PERFORMANCE', 'SCHEMA') are structural defects that do not close." Clean trace handling: "Clean trace still carries FAIL-CATEGORY: N/A on the clean trace row."

**C-42 surface 2 candidate quality:** The embedded vocabulary definitions reduce out-of-vocabulary drift by giving the model the semantic mapping immediately before use. The N/A handling for clean traces covers the zero-finding edge case. If V-03 produces exclusively in-vocabulary values, C-42 surface 2 has single-axis evidence; vocabulary freezing is possible.

---

### Tier B — V-05: Combined superadditivity test

V-05 imposes both GATE-8B (4-field DECLARE CONTRADICTION) and GATE-12 (FAIL-CATEGORY taxonomy) simultaneously. Primary experimental claim: do both surfaces survive under combined token pressure? If Step 8b degrades (3-field form drops `matches HALT-EXPECTED-BOUNDARY:`), V-02's surface is the weaker under combination. If Step 12 degrades (out-of-vocabulary values), V-03's surface is the weaker under combination. If both surfaces survive at V-02/V-03 single-axis fidelity, C-42 surface 1 and surface 2 are independent.

**Superadditivity test quality:** Standard combined-axis design. V-05 provides the cross-validation signal needed before either C-42 surface advances to promotion.

---

### Tier C — V-04: Role-entry contract vs. phase-gate enforcement hypothesis

V-04's architectural test (C-41 via single-role role-entry contract, not Algorithm-Declarant Phase 0B) generates the comparison signal for R18: does GATE-ENTRY-B (self-declared by Platform Expert at entry) produce equivalent HALT-EXPECTED-BOUNDARY fidelity at Step 8 Header verbatim reproduction vs. GATE-0B (externally imposed by Algorithm-Declarant as phase-closure artifact)? The hypothesis predicts GATE-0B (external phase gate) may achieve higher Step 8 Header fidelity than GATE-ENTRY-B (self-declared entry condition). Execution result of V-01 vs. V-04 would resolve this.

---

### Tier C (secondary) — V-01: Explicit dual-branch GATE-TC adversary defeat

V-01's GATE-TC adds a previously absent adversary-defeat clause: "All three outcome paths are valid outputs — the validation is not structural confirmation only." This directly names and defeats the R18 adversary (planner assumes HALT fires at predicted boundary). Combined with the three-path template in the TRACE CONTRACT validation block, V-01 is the first variation to make the falsification paths structurally explicit at the gate level rather than implicitly present via template options.

---

## Rankings

| Rank | Variation | Score | % | Golden | Signal Quality |
|---|---|---|---|---|---|
| 1 | V-02 C-42 surface 1 single-axis | 260/260 | 100% | PASS | Tier A: First single-axis isolation of 4-field DECLARE CONTRADICTION with falsification path explicitly gated — clean evidence for C-42 surface 1 promotability |
| 2 | V-03 C-42 surface 2 single-axis | 260/260 | 100% | PASS | Tier A: FAIL-CATEGORY closed vocabulary with embedded definitions and N/A clean-trace handling — strongest single-axis C-42 surface 2 design |
| 3 | V-05 Combined | 260/260 | 100% | PASS | Tier B: Superadditivity test for C-42 surfaces 1 and 2 — determines independence under token pressure |
| 4 | V-01 Baseline full stack | 260/260 | 100% | PASS | Tier C: Explicit dual-branch GATE-TC adversary defeat; two-checkpoint C-41 enforcement (GATE-0B + GATE-8H) |
| 5 | V-04 Role sequence | 260/260 | 100% | PASS | Tier C: Single-role entry-contract C-41 hypothesis — execution fidelity comparison against V-01 two-role phase-gate |

---

## R19 Design Direction

**C-42 surface 1 — promotion readiness after R18:**
V-02 provides single-axis evidence. V-05 provides superadditivity test. If both produce the 4-field form with filled `yes/no` values: C-42 surface 1 achieves two-axis independent evidence (single + combined) in one round. Promotable if V-02 single-axis succeeds. If V-05 degrades the field while V-02 succeeds, surface 1 requires isolation from surface 2.

**C-42 surface 2 — promotion readiness after R18:**
V-03 provides single-axis evidence. V-05 provides superadditivity test. If V-03 produces exclusively in-vocabulary FAIL-CATEGORY values: vocabulary is freezable. Key failure mode to watch: model produces "SECURITY" (a natural synonym for AUTH) or "PERFORMANCE" (a natural synonym for TIMEOUT) — out-of-vocabulary synonyms are the primary risk.

**V-01 vs. V-04 C-41 enforcement comparison:**
If execution data were available, the HALT-EXPECTED-BOUNDARY fidelity at Step 8 Header (V-01 Phase-gate vs. V-04 role-entry) would determine whether two-role phase-gate architecture adds enforcement value over single-role entry-contract. No execution data in R18 — hypothesis remains open for next scored round with executed traces.

---

```json
{"top_score": 260, "all_essential_pass": true, "new_patterns": ["4-field DECLARE CONTRADICTION single-axis isolation: V-02 gates `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` as a four-field requirement with explicit placeholder-substitution enforcement ('Literal [yes/no] without substitution is a structural defect') and falsification path (`matches HALT-EXPECTED-BOUNDARY: no`) named as a required output variant — first single-axis isolation of C-42 surface 1, removing the combined-axis confound present when R17 V-05 produced this field", "FAIL-CATEGORY closed vocabulary with embedded definitions: V-03 embeds six-item vocabulary definitions (AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION) directly within the Step 12 prompt text before the Findings table, requiring a machine-greppable FAIL-CATEGORY token on every finding row including clean-trace (FAIL-CATEGORY: N/A), with out-of-vocabulary values named as structural defects — first single-axis isolation of C-42 surface 2 with embedded semantic mapping reducing out-of-vocabulary synonym drift"]}
```
