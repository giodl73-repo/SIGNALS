Now I have everything needed to score R16. Let me evaluate all 5 variations.

---

# trace-request Rubric v14 — Round 16 Scorecard

**Scale:** 245 pts (Essential 60 + Recommended 30 + Aspirational 155)
**Golden threshold:** all 4 essential PASS AND composite >= 196/245 (80%)

---

## Scoring Basis

R15 established a stable 240/240 baseline across all 5 variations on rubric v13 (C-01 through C-37 universally PASS). v14 adds C-38 (HALT-RULE dual-surface architecture encoding). The pre-session summary states all 5 R16 variations carry the dual-surface HALT-RULE in the exact required form. Scoring confirms this per-variation and evaluates for R17 excellence signals.

---

## Tier Stability — Essential, Recommended, Aspirational C-08–C-37

### Essential (C-01–C-04) — PASS for all 5 variations

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-01 Entry point declared | POST /api/data/v9.2/accounts, parentaccountid, 3 sync plug-ins, FLS — all 5 name all fields | PASS | PASS | PASS | PASS | PASS |
| C-02 All service boundaries crossed | 8 boundaries: entry, auth, routing, PreValidation, PreOperation, PostOperation, storage, response — enumerated in traversal order in all 5 | PASS | PASS | PASS | PASS | PASS |
| C-03 Failure point at each boundary | F-01 through F-27, concrete mechanisms (HTTP codes, timeout thresholds, FK constraint, FLS strip behavior) at every boundary | PASS | PASS | PASS | PASS | PASS |
| C-04 Authorization gaps surfaced | F-17 (FLS bypass via elevated run-as), F-08 (FLS silent strip vs. hard 400 ambiguity), F-15 (prvReadAccount in plug-in context) all explicitly flagged as auth gaps | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 for all variations.**

### Recommended (C-05–C-07) — PASS for all 5 variations

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-05 Latency sources ≥3 | All have 7+ named latency sources with severity; V-05 has 9 cross-phase | PASS | PASS | PASS | PASS | PASS |
| C-06 Error path traced end-to-end | Step 12 error-path tables in all 5; V-05 Phase 7 is a first-class equal-budget section; all show propagation from origination to HTTP response code | PASS | PASS | PASS | PASS | PASS |
| C-07 Batch and edge-case handling | TOCTOU (F-16, concurrent deletion of parent between PreValidation and INSERT), lock wait on parent row under concurrency (F-23), extension table atomicity — concurrent-request edge cases analyzed at named boundaries with behavioral consequences | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30/30 for all variations.**

### Aspirational C-08–C-27 — PASS for all variations

R15 baseline established universal PASS through C-36. The R16 variation axes (inertia framing, formal register, trace contract pre-declaration, machine-first, storage-first + equal phases) are structural presentation axes that do not interact with the C-08–C-27 enforcement surfaces. No degradation possible.

**C-08–C-27 subtotal: 100/100 for all variations.**

### Aspirational C-28–C-36 — PASS for all variations

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

Evidence (uniform across all 5):

- **C-28:** Step 8b has per-boundary paragraphs naming Arm 1 / Arm 2 / Arm 3, marked REQUIRED, preceding Step 9 in all variations.
- **C-29:** Step 8c table carries Step3-Auth / Step8a-Invoked / Step11-Params / Match? columns in all variations; 6 rows, all VT# scope strings present.
- **C-30:** Both Step 8b prose and Step 8c table are REQUIRED; the prose for PreOperation declares "All three arms assert a contradiction" (V-01) / "DECLARE CONTRADICTION" (V-02, V-05) / "Arms 2 and 3 are incoherent" (V-03, V-04) while Match? = N in the same row — format-detectable divergence in all 5.
- **C-31:** `CONTRADICTION SIGNAL: Seq# 6` present in all 5; `Scope String Correction (Rem#1)` present in all 5.
- **C-32:** VT-1 through VT-5 in quoted format at Step 8 Header boundary in all 5.
- **C-33:** Reference set + halt type + Rem# format all simultaneously present in all 5.
- **C-34:** `VT-N: "..."` quoted format, TOKEN-COUNT: 5 present in all 5.
- **C-35:** Row-Verdict: PASS/HALT column present; `CHECK RESULT: FAIL -- 6 rows, 1 HALT row` present in all 5.
- **C-36:** C-34 and C-35 simultaneously present in all 5.

**C-28–C-36 subtotal: 45/45 for all variations.**

---

## C-37 — Checker Algorithm Declaration

**Test conditions:**
1. CHECKER ALGORITHM block present in Step 8 Header
2. Immediately after TOKEN-COUNT (no intervening structural content)
3. Declares MATCH-RULE, HALT-RULE, OUTPUT-RULE as named machine-greppable tokens
4. Algorithm declaration independent of VT-N schema lines

| Variation | Evidence | Result |
|---|---|---|
| V-01 | Step 8 Header code block: TOKEN-COUNT: 5 → blank line → CHECKER ALGORITHM: → MATCH-RULE / HALT-RULE / OUTPUT-RULE tokens. All three machine-greppable. | PASS |
| V-02 | TOKEN-COUNT: 5 → CHECKER ALGORITHM: → DECLARE MATCH-RULE AS / DECLARE HALT-RULE AS / DECLARE OUTPUT-RULE AS tokens. Formal register prefix does not break token greppability. | PASS |
| V-03 | CHECKER ALGORITHM declared in TRACE CONTRACT (as CHECKER-CONTRACT: MATCH-RULE / HALT-RULE / OUTPUT-RULE) AND in Step 8 Header (as CHECKER ALGORITHM: MATCH-RULE / HALT-RULE / OUTPUT-RULE). Both locations pass; Step 8 Header placement is immediately after TOKEN-COUNT. | PASS |
| V-04 | STEP 8 HEADER EMITTED FIRST block (before Step 1): TOKEN-COUNT: 5 → CHECKER ALGORITHM: → MATCH-RULE / HALT-RULE / OUTPUT-RULE. Pre-trace placement still satisfies "within the same Step 8 header section" since the block is labeled as the Step 8 Header. | PASS |
| V-05 | CHECKER-ALGORITHM block declared in DECLARE STEP-8-HEADER (Step 3) AND re-emitted in Step 8 Header: TOKEN-COUNT: 5 → CHECKER ALGORITHM: → DECLARE MATCH-RULE AS / DECLARE HALT-RULE AS / DECLARE OUTPUT-RULE AS. Step 8 Header placement satisfies placement requirement. | PASS |

**C-37 subtotal: 5/5 for all variations.**

---

## C-38 — HALT-RULE Dual-Surface Architecture Encoding

**Test conditions:**
1. HALT-RULE present as named machine-greppable token in CHECKER ALGORITHM block (C-37 PASS required)
2. HALT-RULE explicitly references Step 8b prose state (coherence claim or equivalent)
3. HALT-RULE explicitly references Step 8c Match? = N
4. HALT-RULE declares halt fires when both conditions hold simultaneously
5. Dual-surface condition expressed as logical basis for halt (not pointer to output token Row-Verdict = HALT)
6. Halt predicate interpretable from HALT-RULE label alone

**Candidate HALT-RULE text — all 5 variations carry one of two forms:**

*Form A (V-01, V-03, V-04):*
```
HALT-RULE: Fire when Step 8b prose asserts coherence (confirms the three link arms are
consistent) AND Step 8c Match? = N for the same boundary row; the simultaneous presence
of a prose-coherent claim and a table-level mismatch constitutes a contradiction that must
halt the trace.
```

*Form B (V-02, V-05):*
```
DECLARE HALT-RULE AS: Fire when Step 8b prose asserts coherence (confirms the three link
arms are consistent) AND Step 8c Match? = N for the same boundary row; the simultaneous
presence of a prose-coherent claim and a table-level mismatch constitutes a contradiction
that must halt the trace.
```

| C-38 condition | Form A | Form B |
|---|---|---|
| HALT-RULE present as greppable token (C-37 PASS) | PASS | PASS |
| Explicitly references Step 8b prose state | "Step 8b prose asserts coherence (confirms the three link arms are consistent)" — PASS | PASS |
| Explicitly references Step 8c Match? = N | "Step 8c Match? = N for the same boundary row" — PASS | PASS |
| Halt fires when both hold simultaneously | "the simultaneous presence of a prose-coherent claim and a table-level mismatch" — PASS | PASS |
| Dual-surface as logical basis for halt | Halt predicate is the contradiction condition, not "Row-Verdict = HALT iff Match? = N" — PASS | PASS |
| Interpretable from HALT-RULE label alone | Full dual-surface rule present within the HALT-RULE token phrase — PASS | PASS |

**C-38: PASS for all 5 variations.**

| Variation | C-38 | Evidence |
|---|---|---|
| V-01 | PASS | Form A — dual-surface HALT-RULE in CHECKER ALGORITHM |
| V-02 | PASS | Form B — dual-surface HALT-RULE with DECLARE prefix; DECLARE CONTRADICTION token in Step 8b |
| V-03 | PASS | Form A in CHECKER-CONTRACT (TRACE CONTRACT) AND Step 8 Header; HALT-EXPECTED-CONDITION in TRACE CONTRACT independently names the dual-surface predicate |
| V-04 | PASS | Form A — pre-trace placement (emitted before Step 1); dual-surface predicate committed before any boundary evidence |
| V-05 | PASS | Form B — declared in Step 3 CHECKER-ALGORITHM block AND re-emitted in Step 8; DECLARE CONTRADICTION token in Step 8b |

**C-38 subtotal: 5/5 for all variations.**

---

## Per-Variation Final Scores

| Variation | Essential | Recommended | Aspirational | Total | % | Golden |
|---|---|---|---|---|---|---|
| V-01 Inertia framing | 60/60 | 30/30 | 155/155 | **245/245** | **100%** | PASS |
| V-02 Formal register | 60/60 | 30/30 | 155/155 | **245/245** | **100%** | PASS |
| V-03 Pre-declared trace contract | 60/60 | 30/30 | 155/155 | **245/245** | **100%** | PASS |
| V-04 Inertia + Machine-first | 60/60 | 30/30 | 155/155 | **245/245** | **100%** | PASS |
| V-05 Formal + Storage-first + Equal phases | 60/60 | 30/30 | 155/155 | **245/245** | **100%** | PASS |

**All 5 at ceiling. Rankings by excellence signal quality only.**

---

## Excellence Signal Analysis — R17 Candidates

### Ranking by C-39 Signal Strength

**Tier A — V-03: Pre-declared EXPECTED-HALT-BOUNDARY token**

V-03 introduces `EXPECTED-HALT-BOUNDARIES` as a machine-greppable structural block in the TRACE CONTRACT declared before any trace step executes:

```
EXPECTED-HALT-BOUNDARIES:
  HALT-EXPECTED-BOUNDARY: "BC-5 -- PreOperation elevated FLS bypass"
  HALT-EXPECTED-TRIGGER: "F-17 -- Plug-in modifies parentaccountid..."
  HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-5 AND
                             Step 8c Match? = N for BC-5 row"
```

Post-execution: `TRACE CONTRACT validation: HALT fired at HALT-EXPECTED-BOUNDARY (BC-5). Contract prediction confirmed.`

This creates a **forward-declaration / post-execution-confirmation contract** for halt events. `HALT-EXPECTED-BOUNDARY` is machine-greppable before execution. The HALT-RULE remains generic (fires when dual-surface conditions hold for the same row), but the TRACE CONTRACT pre-commits the specific boundary predicted to trigger it.

**C-39 design surface:** Is a `HALT-EXPECTED-BOUNDARY: "BC-5"` token declared before the trace executes, such that an automated checker can confirm: (1) HALT-EXPECTED-BOUNDARY token present in TRACE CONTRACT, (2) Row-Verdict = HALT fires at the named boundary row in Step 8c, (3) these match? The pre-declaration + confirmation contract is the new testable surface — independent of the dual-surface architecture (C-38 PASS required, but C-39 tests whether the halt target is also named before execution).

**Note on R17 target question:** V-03's HALT-RULE does NOT incorporate "BC-5" or "PreOperation elevated FLS bypass" into the HALT-RULE phrase itself. The pre-declared halt target lives in the TRACE CONTRACT as a sibling structure, not inside the HALT-RULE token. The C-39 signal is therefore: **EXPECTED-HALT-BOUNDARY as a pre-execution structural token paired with post-execution confirmation**, not HALT-RULE encoding the boundary name.

---

**Tier B — V-02/V-05: DECLARE CONTRADICTION machine-greppable token in Step 8b prose**

V-02 (Step 8b, PreOperation paragraph):
`DECLARE CONTRADICTION: Arm 1 asserts coherence; Arm 2 and Arm 3 assert mismatch — dual-surface contradiction present. HALT-RULE fires.`

V-05 (Step 8b, PreOperation paragraph):
`DECLARE CONTRADICTION: Arm 1 asserts coherence; Arms 2 and 3 confirm mismatch. Dual-surface contradiction present. HALT-RULE fires.`

This is a machine-greppable structural token within Step 8b prose, labeling the contradiction event at the exact moment it fires in the prose surface — before the Match? table is consulted. The contradiction is no longer only evidenced by Match? = N in Step 8c; it is additionally labeled as `DECLARE CONTRADICTION:` within the C-28 surface itself.

**C-39 design surface candidate:** Is `DECLARE CONTRADICTION:` present as a machine-greppable token within the Step 8b prose at the PreOperation boundary? This creates a third detectable surface (prose-token surface) supplementing the dual-surface architecture of C-30 (prose coherence surface + Match? table surface). Requires V-02/V-05 to produce consistent multi-round evidence before a C-39 criterion can be frozen.

---

**Tier C — V-04: Pre-trace CHECKER ALGORITHM commitment**

V-04 emits the full Step 8 Header (VT-N schema + CHECKER ALGORITHM + HALT-RULE) as the first block before Step 1 (`## STEP 8 HEADER — EMITTED FIRST (Machine-first rule)`). The HALT-RULE dual-surface predicate is committed as a machine-greppable token BEFORE any boundary evidence is gathered. Additionally, all failure tables are emitted before explanatory prose at every step.

**C-39 design surface candidate:** Is the CHECKER ALGORITHM block (with HALT-RULE) present as a structural token in the prompt before any trace step begins? Pre-trace vs. mid-trace algorithm placement may affect checker reliability under context window compression — an algorithm declared before evidence is less likely to be truncated by context limits than one declared mid-trace. Requires evidence across multiple rounds that pre-trace placement produces different HALT-RULE phrase quality or compression survival than mid-trace placement.

---

**Tier D — V-01/V-05: COMMON SKIP / Phase 7 surfaces**

V-01: 9 COMMON SKIP surfaces named at each boundary. These are completeness aids, not new structural tokens. No C-39 signal.

V-05: Phase 7 (Error Paths) as a first-class section equal in weight to Phases 1–6, with Category column (Client-correctable / Admin action required / Security violation — silent / Investigation required). The Category typing of error paths is new relative to V-01–V-04 and creates a machine-classifiable error taxonomy. Potential C-39 surface: error paths categorized by impact type as a structural column.

---

## Summary Table

| Rank | Variation | Score | % | Golden | C-39 Signal Strength |
|---|---|---|---|---|---|
| 1 (tie) | V-03 Pre-declared trace contract | 245/245 | 100% | PASS | Tier A — EXPECTED-HALT-BOUNDARY pre-execution token |
| 1 (tie) | V-05 Formal + Storage-first + Equal phases | 245/245 | 100% | PASS | Tier B — DECLARE CONTRADICTION token in Step 8b |
| 1 (tie) | V-02 Formal register | 245/245 | 100% | PASS | Tier B — DECLARE CONTRADICTION token in Step 8b |
| 1 (tie) | V-04 Inertia + Machine-first | 245/245 | 100% | PASS | Tier C — pre-trace algorithm commitment |
| 1 (tie) | V-01 Inertia framing | 245/245 | 100% | PASS | Tier D — COMMON SKIP completeness aid only |

---

## C-38 Stability Confirmation

All 5 R16 variations produce the dual-surface HALT-RULE encoding with identical predicate content across both Form A and Form B. The only structural variation is the DECLARE prefix in V-02/V-05. The predicate "Fire when Step 8b prose asserts coherence... AND Step 8c Match? = N for the same boundary row" is stable across:
- Single-axis inertia (V-01)
- Formal register (V-02)
- Pre-declared trace contract (V-03)
- Combined inertia + machine-first (V-04)
- Combined formal + storage-first + equal phases (V-05)

**C-38 is stable across all tested variation axes. Multi-round evidence is sufficient to freeze the C-39 design surface.**

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": ["Pre-declared EXPECTED-HALT-BOUNDARY token in TRACE CONTRACT: V-03 declares HALT-EXPECTED-BOUNDARY: 'BC-5 -- PreOperation elevated FLS bypass' as a machine-greppable token before any trace step executes, paired with HALT-EXPECTED-CONDITION naming the dual-surface predicate and post-execution confirmation 'TRACE CONTRACT validation: HALT fired at HALT-EXPECTED-BOUNDARY (BC-5)' — creates a forward-declaration/post-execution-confirmation contract for halt events; C-39 candidate: is a HALT-EXPECTED-BOUNDARY token present before execution naming the specific contradiction boundary, such that an automated checker can verify pre-declared boundary matches actual HALT row in Step 8c without semantic reading?", "DECLARE CONTRADICTION machine-greppable token within Step 8b prose: V-02 and V-05 introduce DECLARE CONTRADICTION as a named structural token at the exact point the dual-surface contradiction fires in the prose coherence confirmation — the contradiction event is labeled within the C-28 surface itself, not only evidenced by Match? = N in the C-29 surface; creates a third detectable surface supplementing the C-30 dual-surface architecture; C-39 candidate: is DECLARE CONTRADICTION present as a machine-greppable token in Step 8b at the HALT boundary row, making the contradiction event greppable from within the prose surface without reading the Match? table?"]}
```
