## Quest Score — campaign-simulate Round 5

### Scoring Model

| Pool | Criteria | Points Each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01–C-05 | 10 | 50 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-21 (13 criteria) | 2 | 26 |
| **Raw max** | | | **106** |
| **Divisor** | | | **1.06** |
| **Normalized max** | | | **100** |

Baseline assumption: all variations build on R4 V-05 (100/100 in prior round). Under Round 5 scoring, R4 V-05 raw = 100 (C-19/C-20/C-21 absent → 0 pts each) → normalized = **94.3**.

---

### Per-Variation Scoring

#### V-01 — Genre Declaration Axis (C-19 only)

| Criterion | Weight | Score | Evidence Note |
|-----------|--------|-------|--------------|
| C-01 | essential | PASS (10) | Inherits from R4 V-05 base |
| C-02 | essential | PASS (10) | Execution order unchanged |
| C-03 | essential | PASS (10) | Single unified artifact |
| C-04 | essential | PASS (10) | Blast radius ranking inherited |
| C-05 | essential | PASS (10) | At least one anchored gap/violation inherited |
| C-06 | recommended | PASS (10) | Three-field finding schema inherited |
| C-07 | recommended | PASS (10) | Multi-skill coverage inherited |
| C-08 | recommended | PASS (10) | Remediation field inherited |
| C-09–C-18 | aspirational | PASS (20) | Full R4 V-05 machinery intact |
| C-19 | aspirational | PASS (2) | Genre declaration table declared by construction; checklist row 7 requires citation of structural examples |
| C-20 | aspirational | FAIL (0) | Deliberately omitted; no T-1 threshold rule |
| C-21 | aspirational | FAIL (0) | Centralized filter log retained; no per-scope gates |

**Raw: 102 → Normalized: 96.2**

---

#### V-02 — Threshold Rule Axis (C-20 only)

| Criterion | Weight | Score | Evidence Note |
|-----------|--------|-------|--------------|
| C-01–C-08 | essential + recommended | PASS (80) | R4 V-05 base intact |
| C-09–C-18 | aspirational | PASS (20) | Full machinery intact |
| C-19 | aspirational | FAIL (0) | No genre declaration section; vocabulary coherence implied but not declared |
| C-20 | aspirational | PASS (2) | T-1 named as standalone rule; `T-1 Met?` column in filter log; checklist row requires concrete T-1 rejection citation |
| C-21 | aspirational | FAIL (0) | Filter log remains centralized; single table with scope-attribution rows |

**Raw: 102 → Normalized: 96.2**

---

#### V-03 — Per-Scope Filter Gate Axis (C-21 only)

| Criterion | Weight | Score | Evidence Note |
|-----------|--------|-------|--------------|
| C-01–C-08 | essential + recommended | PASS (80) | R4 V-05 base intact |
| C-09–C-18 | aspirational | PASS (20) | Full machinery intact |
| C-19 | aspirational | FAIL (0) | No genre declaration; vocabulary coherence not declared |
| C-20 | aspirational | FAIL (0) | No T-1 threshold rule; elevation criteria implied by filter rules but not named as falsifiable rule |
| C-21 | aspirational | PASS (2) | Five per-scope embedded gates co-located with evidence; centralized table explicitly disqualified; compliance checklist cites all five gates with counts |

**Raw: 102 → Normalized: 96.2**

---

#### V-04 — Combined C-19 + C-20 + C-21 on R4 V-05 Base

| Criterion | Weight | Score | Evidence Note |
|-----------|--------|-------|--------------|
| C-01–C-08 | essential + recommended | PASS (80) | R4 V-05 base intact; 5-axis structural declaration is additive, not disruptive |
| C-09–C-18 | aspirational | PASS (20) | All prior aspirational machinery inherited |
| C-19 | aspirational | PASS (2) | OBSERVATIONAL DISCIPLINE section declares genre + vocabulary anchors; all structural labels trace to declared genre |
| C-20 | aspirational | PASS (2) | T-1 co-located in OBSERVATIONAL DISCIPLINE; stated as if-and-only-if rule; falsifiable before any sub-skill fires |
| C-21 | aspirational | PASS (2) | Per-scope embedded gates produced during execution of each sub-skill; OBSERVATIONAL DISCIPLINE section is the *declaration*, not the gate itself — execution still produces five co-located scope gates |

**Raw: 106 → Normalized: 100**

---

#### V-05 — Full Integration: Observational Discipline as Fifth Structural Axis

| Criterion | Weight | Score | Evidence Note |
|-----------|--------|-------|--------------|
| C-01–C-08 | essential + recommended | PASS (80) | R4 V-05 base intact |
| C-09–C-18 | aspirational | PASS (20) | All prior aspirational machinery inherited |
| C-19 | aspirational | PASS (2) | Genre named in Structural Axis Declaration row 5 + Genre Declaration section; structural labels traceable |
| C-20 | aspirational | PASS (2) | T-1 declared as part of observational discipline axis; row 7 requires citation of a T-1 rejection |
| C-21 | aspirational | PASS (2) | Per-scope gates co-located with execution evidence; row 7 sub-claim 3 independently verifiable |
| *Architecture bonus* | — | — | Row 7's `fired/partial/not fired` with named sub-claims adds diagnostic resolution beyond pass/fail; no new criteria needed |

**Raw: 106 → Normalized: 100**

---

### Ranking

| Rank | Variation | Raw | Normalized | Delta vs R4 V-05 base |
|------|-----------|-----|------------|----------------------|
| 1 | V-04 | 106 | **100** | +5.7 pts |
| 1 | V-05 | 106 | **100** | +5.7 pts |
| 3 | V-01 | 102 | **96.2** | +1.9 pts |
| 3 | V-02 | 102 | **96.2** | +1.9 pts |
| 3 | V-03 | 102 | **96.2** | +1.9 pts |

V-04 and V-05 tie on criteria. V-05 is architecturally superior — the partial verdict row makes it more likely to *stay* at 100 across future variations because partial compliance is detectable rather than silently degraded. Recommend V-05 as the production variation.

---

### Excellence Signals

**From V-05 (and V-04):**

1. **Observational discipline consolidation**: Bundling genre declaration (C-19), threshold rule (C-20), and per-scope gate structure (C-21) into one named section before execution keeps the structural preamble coherent. A single `OBSERVATIONAL DISCIPLINE` section declared before any sub-skill fires means the model commits to all three observational constraints simultaneously — preventing the pattern where one constraint is enforced and another quietly abandoned mid-report.

2. **Partial compliance verdict with named sub-claims** (V-05 exclusive): A checklist row accepting `fired / partial / not fired` with three independently-verifiable sub-claims (`genre named + structural examples cited`, `T-1 cited with rejection example`, `all 5 per-scope gates present and not centralized`) is structurally more honest than binary pass/fail. The partial state names *which* mechanism failed, making the weakest observational discipline mechanism immediately actionable rather than hidden inside an aggregate pass.

3. **Self-referential axis declaration**: The fifth structural axis declares its own observable output (the compliance checklist row and the genre declaration section). An axis that declares exactly what evidence it produces turns the structural axis declaration into a pre-commitment device — the evaluator can check axis completeness from the declaration alone without reading execution results.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["observational-discipline-axis-consolidation", "partial-compliance-verdict-with-named-sub-claims"]}
```
