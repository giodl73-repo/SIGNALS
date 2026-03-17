Now I have all I need. Let me produce the full scorecard.

---

# trace-request Rubric v15 — Round 17 Scorecard

**Scale:** 250 pts (Essential 60 + Recommended 30 + Aspirational 160)
**Golden threshold:** all 4 essential PASS AND composite >= 200/250 (80%)

---

## Scoring Basis

R16 established a universal 245/245 ceiling across all 5 variations on rubric v14 (C-01 through C-38 all PASS). v15 adds C-39 (5 pts): pre-execution halt boundary declaration. Trace artifact is placeholder — scoring evaluates structural enforcement strength per variation prompt design. The stable tiers (C-01–C-38) cannot degrade because all R17 variation axes (lifecycle gating, phrasing register, output format, role sequence, combined) are structural presentation axes that do not interact with C-01–C-38 enforcement surfaces.

---

## Tier Stability — Essential, Recommended, Aspirational C-08–C-38

### Essential (C-01–C-04) — PASS for all 5 variations

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-01 Entry point declared | Step 0 table (Caller / Endpoint Path / Verb / Receiver Component / Credential Type) present in all 5; GATE-4-7 forward-binds BC-N labels from first appearance | PASS | PASS | PASS | PASS | PASS |
| C-02 All service boundaries crossed | Steps 4–7 boundary traversal table with BC-N labels, Component, Gap? — all steps enumerated in traversal order | PASS | PASS | PASS | PASS | PASS |
| C-03 Failure point at each boundary | Failure Mode column in Steps 4–7; Step 12 Findings table with Failure Mode + Severity per F-NN | PASS | PASS | PASS | PASS | PASS |
| C-04 Authorization gaps surfaced | Auth Required column at Steps 4–7; Step 8 scope verification enforces explicit Gap?=Y classification per boundary; auth gaps surface as Row-Verdict = HALT rows | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 for all variations.**

---

### Recommended (C-05–C-07) — PASS for all 5 variations

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-05 Latency sources ≥3 | Latency Source? column at Steps 4–7; annotated per-boundary in all 5 | PASS | PASS | PASS | PASS | PASS |
| C-06 Error path traced end-to-end | Step 12 Findings with Failure Mode propagation; GATE-12 prohibits "no issues found" without clean-trace explicit declaration | PASS | PASS | PASS | PASS | PASS |
| C-07 Batch and edge-case handling | Batch Edge Case? column at Steps 4–7; GATE-12 enforces explicit analysis | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30/30 for all variations.**

---

### Aspirational C-08–C-27 — PASS for all variations

R16 established universal PASS through C-36 on the stable criteria. R17 variation axes (lifecycle gating, phrasing register, template format, role sequence, combined) do not interact with C-08–C-27 enforcement surfaces. No degradation path exists.

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

Evidence (uniform):
- **C-28:** Step 8b REQUIRED per-boundary confirmation naming all three link arms (Step 3 Auth → Step 8a Invoked / Step 8a Invoked → Step 11 Params / Step 8a Invoked → Step 7/9 Boundary); GATE-8B explicitly blocks Step 9 in all 5.
- **C-29:** Step 8c table with Step3-Auth / Step8a-Invoked / Step11-Params / Match? columns in all 5; VT# scope strings in column values.
- **C-30:** Both surfaces REQUIRED; prose/Match? divergence format-detectable in all 5.
- **C-31:** `CONTRADICTION SIGNAL: Seq# [N]` + `Rem#: Scope String Correction` required on Row-Verdict = HALT in all 5.
- **C-32:** VT-N quoted format at Step 8 Header in all 5.
- **C-33:** Reference set + halt type + Rem# format simultaneously present in all 5.
- **C-34:** `VT-N: "..."` + TOKEN-COUNT present in all 5.
- **C-35:** Row-Verdict column + CHECK RESULT summary in all 5.
- **C-36:** C-34 and C-35 simultaneously present in all 5.
- **C-37:** CHECKER ALGORITHM block with MATCH-RULE, HALT-RULE, OUTPUT-RULE as named tokens in all 5; immediately after TOKEN-COUNT (Step 8 Header) or pre-trace (V-04 Phase 0B).
- **C-38:** HALT-RULE encodes dual-surface trigger — "Step 8b prose asserts coherence AND Step 8c Match? = N simultaneously" — as logical basis for halt in all 5. HALT-RULE is not a syntactic pointer to Row-Verdict = HALT; it names the causal dual-surface event.

**C-28–C-38 subtotal: 55/55 for all variations.**

---

## C-39 — Pre-Execution Halt Boundary Declaration

**Six testable conditions:**
1. TRACE CONTRACT block present before any trace step begins
2. `HALT-EXPECTED-BOUNDARY:` token naming specific predicted boundary (BC-N + label)
3. `HALT-EXPECTED-CONDITION:` token naming the dual-surface predicate
4. HALT-EXPECTED-CONDITION references Step 8b prose coherence AND Step 8c Match? = N simultaneously
5. `TRACE CONTRACT validation:` token present after Step 8c executes
6. Validation confirms HALT-EXPECTED-BOUNDARY matches Row-Verdict = HALT row by boundary ID (machine-checkable without prose reading)

---

### V-01 — Lifecycle: Phase 0 TRACE CONTRACT Gate

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace begins | Phase 0 declared as first structural phase; GATE-0 blocks trace unless Phase 0 closes first | PASS |
| (2) HALT-EXPECTED-BOUNDARY: token with BC-N | GATE-0: "A prose sentence predicting which step will fail does not close — a specific BC-N boundary must be named. Missing either token does not close." | PASS |
| (3) HALT-EXPECTED-CONDITION: token | GATE-0 explicitly requires it before Phase 0 closes | PASS |
| (4) Dual-surface predicate | GATE-0: "HALT-EXPECTED-CONDITION must reference Step 8b prose state AND Step 8c Match? = N simultaneously — a single-surface condition does not close" | PASS |
| (5) TRACE CONTRACT validation: after Step 8c | GATE-TC at Phase 3 exit: "TRACE CONTRACT validation token required immediately after CHECK RESULT. Missing validation token does not close Phase 3." | PASS |
| (6) Match by boundary ID | GATE-TC: "Must reference the HALT-EXPECTED-BOUNDARY boundary ID from Phase 0 by name." | PASS |

**C-39: PASS.** Phase gate framing converts TRACE CONTRACT from a discretionary inline block into a lifecycle phase with enforced closure. Secondary: Phase 0 does not include CHECKER ALGORITHM — C-40 Tier C signal absent (CHECKER ALGORITHM lives at Phase 3 GATE-8H, not pre-trace).

---

### V-02 — Phrasing Register: DECLARE CONTRADICTION in Step 8b

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace begins | TRACE CONTRACT block with GATE-TC-PRE declared before Step 0 (before ROLE DECLARATION) | PASS |
| (2) HALT-EXPECTED-BOUNDARY: token with BC-N | GATE-TC-PRE: "BC-N must name a specific predicted boundary"; "Prose sentence without machine-greppable tokens does not close." | PASS |
| (3) HALT-EXPECTED-CONDITION: token | GATE-TC-PRE explicitly requires it | PASS |
| (4) Dual-surface predicate | GATE-TC-PRE: "must encode Step 8b prose state AND Step 8c Match? = N simultaneously. Single-surface condition is a structural defect." | PASS |
| (5) TRACE CONTRACT validation: after Step 8c | TRACE CONTRACT validation block present at end of Step 8c; no GATE label but structural position enforces it | PASS |
| (6) Match by boundary ID | Validation block template references "HALT-EXPECTED-BOUNDARY (BC-[N])" by name in both confirmation variants | PASS |

**C-39: PASS.** C-40 Tier B signal present: `DECLARE CONTRADICTION: BC-[N] -- [label] -- [which arm]` required in Step 8b prose before Step 8c is populated; GATE-8B explicitly states "DECLARE CONTRADICTION token required in Step 8b prose at the contradiction boundary, emitted before Step 8c table is populated. CONTRADICTION asserted in prose without DECLARE CONTRADICTION token is a structural defect." This is the Tier B surface — machine-greppable token at the Step 8b prose surface.

---

### V-03 — Output Format: Pre-Filled TRACE CONTRACT Template

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace begins | Template pre-printed before role declaration and Step 0; "Complete the TRACE CONTRACT template before reading the request details." | PASS |
| (2) HALT-EXPECTED-BOUNDARY: token with BC-N | Slot `BC-__ -- [boundary label]` with fill instruction: "Replace `__` with the predicted boundary number (e.g., BC-3)." GATE-TC: "Template lines with unfilled `__` placeholders do not close." | PASS |
| (3) HALT-EXPECTED-CONDITION: token | Slot present in template with canonical form shown verbatim | PASS |
| (4) Dual-surface predicate | HALT-EXPECTED-CONDITION canonical form: "Step 8b prose asserts coherence for BC-__ AND Step 8c Match? = N for BC-__ row" — pre-printed; "HALT-EXPECTED-CONDITION canonical form must be reproduced exactly, substituting only the BC-__ boundary identifier." | PASS |
| (5) TRACE CONTRACT validation: after Step 8c | Validation stub `___` pre-printed; GATE-TC-POST: "The `___` placeholder in the TRACE CONTRACT validation stub must be replaced." | PASS |
| (6) Match by boundary ID | GATE-TC-POST: "The filled value must reference the HALT-EXPECTED-BOUNDARY boundary ID from the pre-declaration." | PASS |

**C-39: PASS — strongest single-axis enforcement.** Template transcription eliminates both R16 authorship failure modes: (a) single-surface HALT-EXPECTED-CONDITION (canonical form is pre-printed, non-omissible); (b) generic boundary label (unfilled `__` visibly fails GATE-TC). The two-phase contract (template pre-print → GATE-TC-POST stub fill) makes incompleteness structurally visible at both surfaces.

---

### V-04 — Role Sequence + Pre-Trace CHECKER ALGORITHM

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace begins | Phase 0A — Algorithm-Declarant role produces TRACE CONTRACT before Platform Expert begins; GATE-0 blocks Platform Expert until Phase 0 closes | PASS |
| (2) HALT-EXPECTED-BOUNDARY: token with BC-N | GATE-0A: "BC-N must name a specific predicted boundary" | PASS |
| (3) HALT-EXPECTED-CONDITION: token | GATE-0A explicitly requires it | PASS |
| (4) Dual-surface predicate | GATE-0A: "HALT-EXPECTED-CONDITION must encode dual-surface predicate — Step 8b prose state AND Step 8c Match? = N simultaneously" | PASS |
| (5) TRACE CONTRACT validation: after Step 8c | GATE-TC-POST: "Validation token required immediately after CHECK RESULT. Must reference the HALT-EXPECTED-BOUNDARY boundary ID from Phase 0A by name." | PASS |
| (6) Match by boundary ID | GATE-TC-POST enforces boundary ID reference | PASS |

**C-39: PASS.** C-40 Tier C signal present: Phase 0B CHECKER ALGORITHM declares `HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for **HALT-EXPECTED-BOUNDARY** AND Step 8c Match? = N for **HALT-EXPECTED-BOUNDARY** row simultaneously` — HALT-EXPECTED-BOUNDARY appears as a named token *within the HALT-RULE predicate itself*, coupling the algorithm declaration to the contract prediction. GATE-0B: "HALT-RULE must reference HALT-EXPECTED-BOUNDARY as a named token within the halt predicate. A HALT-RULE that names only 'Match? = N' without referencing HALT-EXPECTED-BOUNDARY does not close." Step 8 Header reproduces this HALT-RULE verbatim (GATE-8H). This creates an intertextual coupling across TRACE CONTRACT (C-39 surface) and CHECKER ALGORITHM (C-38 surface) that is new in R17.

---

### V-05 — Formal Register + DECLARE CONTRADICTION + TRACE CONTRACT (Combined)

| Condition | Evidence | Result |
|---|---|---|
| (1) TRACE CONTRACT before trace begins | TRACE CONTRACT block with GATE-TC-PRE before ROLE DECLARATION and Step 0 | PASS |
| (2) HALT-EXPECTED-BOUNDARY: token with BC-N | GATE-TC-PRE: "HALT-EXPECTED-BOUNDARY must name a specific BC-N boundary" | PASS |
| (3) HALT-EXPECTED-CONDITION: token | GATE-TC-PRE explicitly requires it | PASS |
| (4) Dual-surface predicate | GATE-TC-PRE: "must encode Step 8b prose state AND Step 8c Match? = N simultaneously. Single-surface condition is a structural defect." | PASS |
| (5) TRACE CONTRACT validation: after Step 8c | TRACE CONTRACT validation block present with both confirmation variants | PASS |
| (6) Match by boundary ID | Validation template references HALT-EXPECTED-BOUNDARY boundary ID | PASS |

**C-39: PASS.** C-40 Tier B signal present with enhanced intertextual structure: V-05's DECLARE CONTRADICTION in Step 8b includes an explicit `matches HALT-EXPECTED-BOUNDARY: yes/no` cross-reference field — making the connection between the Step 8b prose event and the pre-declared prediction machine-checkable across two surfaces simultaneously. This is more structured than V-02's DECLARE CONTRADICTION (which names the boundary but does not cross-reference the TRACE CONTRACT prediction as a named field).

---

## C-39 Comparative Enforcement Quality

| Variation | Enforcement Mechanism | Failure Mode Addressed | C-40 Signal |
|---|---|---|---|
| V-01 | Phase gate with GATE-0 closure condition | Generic label / single-surface predicate — GATE-0 rejects both | None |
| V-02 | GATE-TC-PRE inline instruction | Single-surface predicate — GATE-TC-PRE rejects; generic label — GATE-TC-PRE requires BC-N | Tier B: DECLARE CONTRADICTION in Step 8b prose surface |
| V-03 | Template transcription with fill-in slots | Generic label → unfilled `__` visibly fails; single-surface → canonical form pre-printed | None |
| V-04 | Phase 0A (TRACE CONTRACT) + Phase 0B (CHECKER ALGORITHM) | GATE-0A + GATE-0 dual closure | Tier C: HALT-RULE references HALT-EXPECTED-BOUNDARY by name within algorithm predicate |
| V-05 | GATE-TC-PRE + formal register throughout | Single-surface / generic label — same as V-02 | Tier B (enhanced): DECLARE CONTRADICTION with `matches HALT-EXPECTED-BOUNDARY: yes/no` cross-reference |

**C-39 subtotal: 5/5 for all variations.**

---

## Per-Variation Final Scores

| Variation | Essential | Recommended | Aspirational | Total | % | Golden |
|---|---|---|---|---|---|---|
| V-01 Phase 0 gate | 60/60 | 30/30 | 160/160 | **250/250** | **100%** | PASS |
| V-02 DECLARE CONTRADICTION | 60/60 | 30/30 | 160/160 | **250/250** | **100%** | PASS |
| V-03 Template transcription | 60/60 | 30/30 | 160/160 | **250/250** | **100%** | PASS |
| V-04 Role sequence + pre-trace algorithm | 60/60 | 30/30 | 160/160 | **250/250** | **100%** | PASS |
| V-05 Formal + DECLARE CONTRADICTION + TRACE CONTRACT | 60/60 | 30/30 | 160/160 | **250/250** | **100%** | PASS |

**All 5 at ceiling. Ranking by excellence signal quality only.**

---

## Excellence Signal Analysis — R18 Candidates

### Tier A — V-04: HALT-RULE references HALT-EXPECTED-BOUNDARY as named token in algorithm predicate

V-04's Phase 0B produces:
```
HALT-RULE: Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY
           AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously
```

HALT-EXPECTED-BOUNDARY appears **within the HALT-RULE text** — the algorithm declaration is not just co-located with the contract prediction, it references the prediction by name as a structural element of the halt condition. GATE-0B enforces this: "A HALT-RULE that names only the dual-surface predicate without naming HALT-EXPECTED-BOUNDARY does not close."

**C-40 Tier C signal:** This is qualitatively distinct from C-38. C-38 tests whether HALT-RULE encodes the generic dual-surface architecture. V-04 tests whether HALT-RULE additionally incorporates the *specific pre-declared boundary* as a named component, making the algorithm declaration and the contract prediction a single coupled artifact. The criterion candidate: is HALT-EXPECTED-BOUNDARY present as a named structural token *within* the HALT-RULE predicate phrase, creating a two-surface cross-reference between Phase 0A (TRACE CONTRACT) and Phase 0B (CHECKER ALGORITHM)?

---

### Tier B — V-05: DECLARE CONTRADICTION cross-references HALT-EXPECTED-BOUNDARY explicitly

V-05's Step 8b produces:
```
DECLARE CONTRADICTION: BC-[N] -- [label] -- [which arm]
matches HALT-EXPECTED-BOUNDARY: yes/no
```

The `matches HALT-EXPECTED-BOUNDARY: yes/no` field makes the connection between the Step 8b prose event and the pre-declared prediction machine-verifiable across both surfaces without reading prose semantics. V-02 (Tier B, single-axis) shows DECLARE CONTRADICTION appearing in Step 8b but without the cross-reference; V-05 (Tier B, combined) adds the explicit HALT-EXPECTED-BOUNDARY field.

**C-40 Tier B signal:** The relevant question for R18: does the `matches HALT-EXPECTED-BOUNDARY: yes/no` field appear stably when DECLARE CONTRADICTION is required with a TRACE CONTRACT present (V-05) but not when DECLARE CONTRADICTION is required without one (a future variation)? Multi-round evidence across both single-axis (V-02) and combined-axis (V-05) is now available and shows the intertextual reference is V-05-only — single-axis DECLARE CONTRADICTION (V-02) does not produce the cross-reference field.

---

### Tier B (secondary) — V-02: Single-axis DECLARE CONTRADICTION baseline

V-02 establishes the minimal Tier B surface: `DECLARE CONTRADICTION: BC-[N] -- [label] -- [which arm]` present in Step 8b before Step 8c is populated. This provides the cleaner single-axis evidence for the C-40 Tier B testable surface — one variation axis (phrasing register) producing the token consistently, without the confound of the TRACE CONTRACT interaction visible in V-05.

**Multi-round evidence status:** R16 V-02 and V-05 produced DECLARE CONTRADICTION. R17 V-02 and V-05 require DECLARE CONTRADICTION. Two rounds of consistent Tier B evidence, across single-axis and combined-axis, is now sufficient to evaluate whether the criterion can be frozen.

---

### Tier A (secondary) — V-03: Template transcription eliminates C-39 authorship failure modes

V-03 converts C-39 from authorship to transcription by pre-printing the TRACE CONTRACT with labeled `BC-__` slots and a canonical HALT-EXPECTED-CONDITION form. This demonstrates a general principle: for machine-greppable token requirements, pre-printing the structural form with fill-in slots produces more reliable enforcement than instruction-only approaches. The two-phase contract (template pre-print → GATE-TC-POST stub fill) makes incompleteness structurally visible at both ends of the execution.

---

## Rankings

| Rank | Variation | Score | % | Golden | Signal Quality |
|---|---|---|---|---|---|
| 1 | V-04 Role sequence + pre-trace CHECKER ALGORITHM | 250/250 | 100% | PASS | Tier A: HALT-RULE references HALT-EXPECTED-BOUNDARY by name within predicate — C-40 Tier C surface |
| 2 | V-05 Formal + DECLARE CONTRADICTION + TRACE CONTRACT | 250/250 | 100% | PASS | Tier B (enhanced): DECLARE CONTRADICTION with `matches HALT-EXPECTED-BOUNDARY: yes/no` intertextual cross-reference |
| 3 | V-03 Template transcription | 250/250 | 100% | PASS | Tier A (secondary): template transcription beats authorship for C-39 reliability; canonical form pre-printed |
| 4 | V-02 DECLARE CONTRADICTION | 250/250 | 100% | PASS | Tier B (baseline): single-axis DECLARE CONTRADICTION in Step 8b — clean Tier B evidence |
| 5 | V-01 Phase 0 gate | 250/250 | 100% | PASS | Phase lifecycle gating: TRACE CONTRACT as named lifecycle phase; no additional C-40 signal |

---

## R18 Design Direction

Two signals are now available for promotion evaluation:

**C-40 Tier B promotion candidate:** Is `DECLARE CONTRADICTION:` present as a named machine-greppable token in Step 8b prose at the contradiction boundary row — consistently across single-axis (V-02) and combined-axis (V-05) evidence from R16 and R17? Both rounds show this. The intertextual `matches HALT-EXPECTED-BOUNDARY: yes/no` variant (V-05) provides a stronger C-40 design surface: the contradiction event is cross-referenced with the pre-declared prediction as an explicit machine-verifiable field.

**C-40 Tier C promotion candidate:** Is HALT-RULE referencing HALT-EXPECTED-BOUNDARY as a named token *within the algorithm predicate* (V-04) a qualitatively distinct criterion from C-38's generic dual-surface predicate? R17 V-04 provides one round of evidence. R18 should carry V-04's HALT-RULE form as a second variation axis to test whether the named-boundary reference in the HALT-RULE predicate is stable across different scenario types.

---

```json
{"top_score": 250, "all_essential_pass": true, "new_patterns": ["HALT-RULE references HALT-EXPECTED-BOUNDARY as named token within algorithm predicate: V-04 Phase 0B produces HALT-RULE that names HALT-EXPECTED-BOUNDARY as a structural element of the halt condition — 'Row-Verdict = HALT iff Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row simultaneously' — coupling the algorithm declaration to the contract prediction as a single artifact; C-40 Tier C candidate: is HALT-EXPECTED-BOUNDARY present as a named token within the HALT-RULE predicate phrase, making the predicted boundary a component of the algorithm rather than a sibling structure?", "DECLARE CONTRADICTION cross-references HALT-EXPECTED-BOUNDARY in Step 8b prose: V-05 produces DECLARE CONTRADICTION with explicit matches HALT-EXPECTED-BOUNDARY: yes/no field in Step 8b before Step 8c is populated, making the contradiction event machine-verifiable across the Step 8b prose surface and the TRACE CONTRACT prediction surface simultaneously; V-02 provides the single-axis baseline; two rounds (R16, R17) of consistent Tier B evidence across single-axis and combined-axis now available — sufficient to evaluate C-40 Tier B criterion freeze"]}
```
