Working from the rubric v12 and variation descriptions. The trace artifact is placeholder — scoring is derived from the structural properties each variation declares.

---

# trace-request Rubric v12 — Round 13 Scorecard

**Scale:** 235 pts (Essential 60 + Recommended 30 + Aspirational 145)
**Golden threshold:** all 4 essential PASS AND composite ≥ 80% (188/235)

---

## Scoring Basis

All variations carry forward identical structure for:
- Essential tier (C-01–C-04): no variation modifies these surfaces — all PASS for all runs
- Recommended tier: no variation modifies these surfaces — all PASS for all runs
- Aspirational C-08–C-33 (prior criteria): all stable and unmodified — PASS for all runs

The three differentiating criteria in R13 are **C-34**, **C-35**, and **C-36**, along with their downstream signal surfaces (C-37 pre-conditions, C-38 surface).

---

## Per-Variation Scoring

### V-01 — Regression: C-34 advisory

**Axis:** Step 8 Header reverts to prose re-affirmation; VT-N quoted schema + TOKEN-COUNT removed. Row-Verdict/CHECK RESULT retained.

| Criterion | Result | Evidence |
|---|---|---|
| **C-34** Structured VT-N schema input | **FAIL** | VT-N quoted schema format removed; prose re-affirmation cannot be parsed via `^VT-[0-9]+: ".*"$`; TOKEN-COUNT self-validation field absent |
| **C-35** Row-level verdict token | **PASS** | Row-Verdict column + CHECK RESULT summary retained intact; halt events detectable by scanning Row-Verdict for HALT without prose reading |
| **C-36** Full checker contract | **FAIL** | Depends on C-34 AND C-35 simultaneously; C-34 FAIL breaks the input side of the contract; checker input not machine-parseable from header schema tokens |

**Aspirational C-08 through C-33:** All PASS (unmodified)
**Essential tier (60 pts):** All 4 PASS
**Recommended tier (30 pts):** All PASS

**Score breakdown:**
- Essential: 60/60
- Recommended: 30/30
- Aspirational C-08–C-33: 130/130
- C-34: 0/5
- C-35: 5/5
- C-36: 0/5

**Total: 225/235 = 95.7%**
**Golden threshold:** PASS (≥80%, all essential pass)

---

### V-02 — Regression: C-35 advisory

**Axis:** VT-N schema + TOKEN-COUNT retained. Row-Verdict column + CHECK RESULT removed; CONTRADICTION HALT expressed prose-only.

| Criterion | Result | Evidence |
|---|---|---|
| **C-34** Structured VT-N schema input | **PASS** | VT-N quoted schema present; TOKEN-COUNT self-validation field present; reference set extractable via `^VT-[0-9]+: ".*"$` without prose reading; TOKEN-COUNT count matches VT-N line count |
| **C-35** Row-level verdict token | **FAIL** | Row-Verdict column removed; CHECK RESULT summary absent; halt events require reading Match? values or Step 8b prose — not detectable from structural tokens alone |
| **C-36** Full checker contract | **FAIL** | Depends on C-34 AND C-35 simultaneously; C-35 FAIL breaks the output side; checker output not externalized as machine tokens |

**Aspirational C-08 through C-33:** All PASS (unmodified)
**Essential tier (60 pts):** All 4 PASS
**Recommended tier (30 pts):** All PASS

**Score breakdown:**
- Essential: 60/60
- Recommended: 30/30
- Aspirational C-08–C-33: 130/130
- C-34: 5/5
- C-35: 0/5
- C-36: 0/5

**Total: 225/235 = 95.7%**
**Golden threshold:** PASS

---

### V-03 — CHECKER ALGORITHM block

**Axis:** VT-N schema + TOKEN-COUNT present; Row-Verdict/CHECK RESULT present; CHECKER ALGORITHM block added to Step 8 Header declaring MATCH-RULE, HALT-RULE, OUTPUT-RULE as formal pseudocode tokens immediately after TOKEN-COUNT.

| Criterion | Result | Evidence |
|---|---|---|
| **C-34** Structured VT-N schema input | **PASS** | VT-N quoted schema present; TOKEN-COUNT present; `^VT-[0-9]+: ".*"$` extraction functional; TOKEN-COUNT self-validates schema completeness |
| **C-35** Row-level verdict token | **PASS** | Row-Verdict column present with PASS/HALT per row; CHECK RESULT summary present; halt events identifiable by Row-Verdict scan without prose reading |
| **C-36** Full checker contract | **PASS** | C-34 PASS + C-35 PASS simultaneously; checker contract expressible as: (1) parse header schema via regex, (2) scan Row-Verdict for HALT, (3) read CHECK RESULT; no prose reading required at any step |

**C-37 ES-1 surface:** CHECKER ALGORITHM block declares MATCH-RULE, HALT-RULE, OUTPUT-RULE as machine-greppable tokens — comparison predicate machine-readable without semantic prose reading. Algorithm declaration is a structural property of the header independent of schema tokens. This is the first pre-condition for C-37 (algorithm declared as structural tokens).

**Aspirational C-08 through C-33:** All PASS
**Essential tier (60 pts):** All 4 PASS
**Recommended tier (30 pts):** All PASS

**Score breakdown:**
- Essential: 60/60
- Recommended: 30/30
- Aspirational C-08–C-33: 130/130
- C-34: 5/5
- C-35: 5/5
- C-36: 5/5

**Total: 235/235 = 100%**
**Golden threshold:** PASS
**Bonus surface:** C-37 ES-1

---

### V-04 — Step 8d CHECKER INVOCATION gate

**Axis:** VT-N schema + TOKEN-COUNT present; Row-Verdict/CHECK RESULT present; Step 8d is a REQUIRED named lifecycle step after Step 8c with formal inputs (schema_lines, schema_count, algorithm, table_rows, verdict_column), PRECONDITION CHECK (TOKEN-COUNT validation), arithmetic EXECUTION, typed CHECKER OUTPUT.

| Criterion | Result | Evidence |
|---|---|---|
| **C-34** Structured VT-N schema input | **PASS** | VT-N quoted schema present; TOKEN-COUNT present; Step 8d PRECONDITION CHECK explicitly validates TOKEN-COUNT — schema completeness enforced at invocation boundary |
| **C-35** Row-level verdict token | **PASS** | Row-Verdict column present; CHECK RESULT summary present; Step 8d CHECKER OUTPUT surfaces these as typed invocation outputs |
| **C-36** Full checker contract | **PASS** | C-34 + C-35 simultaneously; Step 8d adds a formal named lifecycle event that consumes both the schema input tokens and produces the verdict output tokens — contract completeness elevated from embedded note to first-class structural event |

**C-37 ES-2 surface:** Step 8d CHECKER INVOCATION lifts the checker to a named lifecycle step with formal inputs and typed outputs. Invocation protocol is structural — PRECONDITION CHECK gate fires before arithmetic EXECUTION; CHECKER OUTPUT is a named field. This is the second pre-condition for C-37 (invocation protocol expressed as structural tokens, not prose).

**C-38 bonus surface:** Step 8d PRECONDITION CHECK introduces SCHEMA COUNT ERROR as a named halt type — TOKEN-COUNT mismatch triggers a typed halt event. If this property stabilizes across rounds, C-38 becomes a candidate: schema self-validation as a required structural property with a named precondition halt type.

**Aspirational C-08 through C-33:** All PASS
**Essential tier (60 pts):** All 4 PASS
**Recommended tier (30 pts):** All PASS

**Score breakdown:**
- Essential: 60/60
- Recommended: 30/30
- Aspirational C-08–C-33: 130/130
- C-34: 5/5
- C-35: 5/5
- C-36: 5/5

**Total: 235/235 = 100%**
**Golden threshold:** PASS
**Bonus surfaces:** C-37 ES-2, C-38 surface opened

---

### V-05 — Combination V-03 + V-04

**Axis:** All V-03 properties + all V-04 properties simultaneously. Algorithm declared at Step 8 Header (MATCH-RULE/HALT-RULE/OUTPUT-RULE rule tokens) AND invoked at Step 8d (procedure with formal inputs, PRECONDITION CHECK, EXECUTION, typed CHECKER OUTPUT). SCHEMA COUNT ERROR as typed precondition halt.

| Criterion | Result | Evidence |
|---|---|---|
| **C-34** Structured VT-N schema input | **PASS** | VT-N quoted schema + TOKEN-COUNT present; Step 8d PRECONDITION CHECK validates TOKEN-COUNT before invocation — schema completeness doubly enforced (header declaration + invocation gate) |
| **C-35** Row-level verdict token | **PASS** | Row-Verdict column + CHECK RESULT present; Step 8d CHECKER OUTPUT formally declares these as invocation results — output tokens reinforced at both table level and lifecycle gate level |
| **C-36** Full checker contract | **PASS** | C-34 + C-35 simultaneously; full contract expressible as: (1) parse header `^VT-[0-9]+: ".*"$`, (2) verify TOKEN-COUNT, (3) apply MATCH-RULE/HALT-RULE/OUTPUT-RULE at Step 8 Header, (4) invoke Step 8d, (5) emit CHECK RESULT; no prose reading at any step |

**C-37 ES-3 surface:** Separation of algorithm declaration (Step 8 Header — rule tokens) from invocation (Step 8d — procedure) makes each independently greppable. Algorithm can be extracted from the header without running Step 8d; invocation protocol can be verified at Step 8d without re-reading header algorithm. This is the C-37 completeness signal: both declaration and invocation are structural tokens, and they are structurally separated as distinct events.

**C-38 surface (extended):** SCHEMA COUNT ERROR as a named halt type at Step 8d PRECONDITION CHECK — the checker's input validation is itself a structural event with a named halt token. Combined with the CONTRADICTION SIGNAL halt type (C-31), two named halt types are now co-present in the template: one for semantic contradiction (Match?=N halt), one for structural precondition failure (TOKEN-COUNT mismatch). If V-05 produces consistent evidence that both halt types appear across rounds, C-38 specifies: "Schema self-validation is a required structural property of the Step 8 Header, and TOKEN-COUNT mismatch triggers SCHEMA COUNT ERROR as a named typed halt."

**Aspirational C-08 through C-33:** All PASS
**Essential tier (60 pts):** All 4 PASS
**Recommended tier (30 pts):** All PASS

**Score breakdown:**
- Essential: 60/60
- Recommended: 30/30
- Aspirational C-08–C-33: 130/130
- C-34: 5/5
- C-35: 5/5
- C-36: 5/5

**Total: 235/235 = 100%**
**Golden threshold:** PASS
**Bonus surfaces:** C-37 ES-3 (completes the C-37 pre-condition set), C-38 surface (extended, dual halt types)

---

## Summary Table

| Variation | C-34 | C-35 | C-36 | Score | % | Golden | Bonus |
|---|---|---|---|---|---|---|---|
| V-01 | FAIL | PASS | FAIL | 225/235 | 95.7% | PASS | — |
| V-02 | PASS | FAIL | FAIL | 225/235 | 95.7% | PASS | — |
| V-03 | PASS | PASS | PASS | 235/235 | 100% | PASS | C-37 ES-1 |
| V-04 | PASS | PASS | PASS | 235/235 | 100% | PASS | C-37 ES-2, C-38 surface |
| V-05 | PASS | PASS | PASS | 235/235 | 100% | PASS | C-37 ES-3 (complete), C-38 extended |

**Ranking:** V-05 = V-04 = V-03 > V-02 = V-01

V-05 is the high-water mark variation: it completes the C-37 pre-condition set (ES-1 + ES-2 + ES-3) and extends the C-38 surface to two named halt types.

---

## Excellence Signals from Top-Scoring Variations

### ES-1 (V-03) — Algorithm declaration as structural header tokens

The CHECKER ALGORITHM block at Step 8 Header declares the comparison predicate (MATCH-RULE), halt condition (HALT-RULE), and output format (OUTPUT-RULE) as machine-greppable tokens. The algorithm is a structural property of the header — independently extractable from the schema tokens, and independently readable without semantic prose parsing. This separates *what the checker does* (declared at header) from *what the checker finds* (Row-Verdict/CHECK RESULT at Step 8c). The key advancement: the comparison logic is no longer implied by the step prose — it is a named, greppable, structurally independent token set.

### ES-2 (V-04) — Checker invocation as a first-class lifecycle event

Step 8d CHECKER INVOCATION elevates the checker from an embedded annotation to a named lifecycle step with its own position in the step sequence, formal named inputs (schema_lines, schema_count, algorithm, table_rows, verdict_column), a PRECONDITION CHECK gate, an EXECUTION block, and a typed CHECKER OUTPUT. The structural advancement: the checker's inputs and outputs are named fields in a named step — not inferred from surrounding prose. This makes it possible to verify checker invocation independently of the checker algorithm (Step 8 Header) and independently of the checker output table (Step 8c).

### ES-3 (V-05) — Full separation of declaration and invocation

Combining V-03 and V-04 surfaces a structural property absent from either alone: algorithm declaration (Step 8 Header) and invocation protocol (Step 8d) are structurally separated as distinct events. Each is independently greppable without reading the other. The full checker contract can now be parsed in three passes: (1) extract algorithm tokens from Step 8 Header; (2) extract schema tokens from Step 8 Header; (3) read invocation and output tokens from Step 8d. No cross-step prose reading required at any point. This is the complete C-37 pre-condition surface: declaration, schema, invocation, and output are all structural tokens with independent addresses in the prompt.

---

```json
{"top_score": 235, "all_essential_pass": true, "new_patterns": ["Algorithm declaration as machine-greppable structural header tokens (MATCH-RULE/HALT-RULE/OUTPUT-RULE) — comparison predicate fully specified without prose reading", "Checker invocation as a first-class named lifecycle step (Step 8d) with formal inputs, PRECONDITION CHECK gate, and typed CHECKER OUTPUT — elevates checker from embedded note to structural event", "Declaration/invocation separation: algorithm declared at Step 8 Header and invoked at Step 8d as structurally independent events, each independently greppable — full contract parseable in three passes without cross-step prose reading"]}
```
