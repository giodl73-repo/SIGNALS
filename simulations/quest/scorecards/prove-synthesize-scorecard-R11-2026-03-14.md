| | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | Sequential: SYNTHESIST → ADVERSARY → ANALYST |
| V-02 | **PASS** | "Three cognitive roles execute concurrently in your reasoning" + "output contains no labeled role sections and no visible role seams" |
| V-03 | **FAIL** | "Roles (Sequential)" heading |

### C-36 — Dual-exemplar adversarial gate (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "Exemplar (invalid): … [Applies to every investigation — fails the gate.]" + "Exemplar (valid): … [Hypothesis-specific — passes the gate.]" co-located in ADVERSARY section |
| V-02 | **PASS** | "Exemplar (fail)" + "Exemplar (pass)" co-located in ADVERSARY gate block entry |
| V-03 | **FAIL** | Incomplete |

### C-37 — Slot-indexed self-containment check (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Six questions each mapped to named paragraph: "→ Verdict/Confidence paragraph", "→ Key Evidence paragraph", etc. |
| V-02 | **PASS** | Same six-question mapping pattern with named paragraphs |
| V-03 | **FAIL** | No self-containment check present |

### C-38 — Role-to-output closure attribution (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "Attribute each to the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST)" in Open Questions output spec; C-11/C-30 prerequisites now satisfied |
| V-02 | **PASS** | Same attribution instruction plus "If a question was raised by the ADVERSARY challenge, acknowledge that attribution" — strengthened; C-11/C-30 prerequisites confirmed |
| V-03 | **FAIL** | Incomplete |

### C-39 — Phase-gated confidence ceiling (Aspirational, NEW v11)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Phase classification table (Explore/Test/Validate → ceilings 25/50/72/none) in pre-synthesis step; "State before proceeding: 'Evidence phase coverage: … Confidence ceiling: …'" enforces declaration before reasoning begins |
| V-02 | **FAIL** | No evidence-phase categories or confidence ceiling mechanism defined |
| V-03 | **FAIL** | Incomplete |

### C-40 — Concurrent synthesis gate block (Aspirational, NEW v11)

| | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | Sequential execution — gates are attached to sequential steps, no unified post-role block |
| V-02 | **PASS** | Named "Gate Block" section positioned after role definitions and before output instructions; all three roles' failure modes + dual exemplars co-located and indexed by role name |
| V-03 | **FAIL** | Incomplete |

### C-41 — Slot-indexed revision mandate (Aspirational, NEW v11)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "If any question cannot be answered from the named paragraph, revise that paragraph before outputting" — trigger (question fails against slot) + corrective action (revise that paragraph) both named; C-37 prerequisite satisfied |
| V-02 | **PASS** | Same instruction present |
| V-03 | **FAIL** | Incomplete |

---

## Composite Score Computation

**Anchors from R10 calibration:**
- R10 V-01 (v11): ~82.5 — fails all of C-35/C-36/C-37/C-38/C-39/C-40/C-41 and C-11/C-13/C-30 essential cluster
- R10 V-02 (v11): ~100.0 — fails C-11/C-13/C-30 (essentials) and cascading C-35/C-38/C-40; earns C-36/C-37/C-41

Each criterion (essential and aspirational) treated as 2.5 pts for composite delta computation.

### V-01 — Phase-gated confidence ceiling

| Criterion | Base (R10 V-01) | R11 | Delta |
|-----------|----------------|-----|-------|
| C-11 | FAIL | PASS | +2.5 |
| C-13 | FAIL | PASS | +2.5 |
| C-30 | FAIL | PASS | +2.5 |
| C-36 | FAIL | PASS | +2.5 |
| C-37 | FAIL | PASS | +2.5 |
| C-38 | FAIL | PASS | +2.5 |
| C-39 | FAIL | PASS | +2.5 |
| C-41 | FAIL | PASS | +2.5 |
| C-35 | FAIL | FAIL | 0 |
| C-40 | FAIL | FAIL | 0 |

**R11 V-01 = 82.5 + 20.0 = ~102.5**

Essential status: C-11 ✓ C-13 ✓ C-30 ✓ — R10 calibration identified only these three as the blocking essentials; likely all-essential PASS.
Golden: 102.5 ≥ 90 ✓ — **likely GOLD**

### V-02 — Concurrent execution with unified gate block

| Criterion | Base (R10 V-02) | R11 | Delta |
|-----------|----------------|-----|-------|
| C-11 | FAIL | PASS | +2.5 |
| C-13 | FAIL | PASS | +2.5 |
| C-30 | FAIL | PASS | +2.5 |
| C-35 | FAIL | PASS | +2.5 |
| C-36 | PASS | PASS | 0 |
| C-37 | PASS | PASS | 0 |
| C-38 | FAIL | PASS | +2.5 |
| C-39 | FAIL | FAIL | 0 |
| C-40 | FAIL | PASS | +2.5 |
| C-41 | PASS | PASS | 0 |

**R11 V-02 = 100.0 + 15.0 = ~115.0**

Essential status: R10 calibration confirms C-11/C-13/C-30 were the **only** three failing essentials in R10 V-02. All three now PASS → **confirmed all-essential PASS**.
Golden: 115.0 ≥ 90 ✓ — **GOLD** (first confirmed gold in series)

### V-03 — Inertia framing (incomplete)

Incomplete variation; roles section stubs out with "placeholder". No gate instructions, no output spec, no self-containment check. Earns basic structural framing points only.

**R11 V-03 ≈ ~8.0** (consistent with R10 V-03 pattern)

---

## Ranking

| Rank | Variation | Score | Gold |
|------|-----------|-------|------|
| 1 | V-02 Concurrent + Unified Gate Block | ~115.0 | **GOLD (confirmed)** |
| 2 | V-01 Phase-gated Confidence Ceiling | ~102.5 | likely GOLD |
| 3 | V-03 Inertia Framing | ~8.0 | ✗ |

---

## Excellence Signals — R11 V-02

**E-01 — Unified gate block as essential-cluster fix mechanism.** Moving from per-step role gates to a named structural section (positioned after roles, before output) simultaneously resolves C-11 (SYNTHESIST/ANALYST NOT: gates), C-13 (NOT: format), C-30 (failure modes named), and C-40 (concurrent-compatible unified block). The placement is load-bearing: concurrent roles have no execution steps to attach gates to; the block as a discrete section solves the C-35/C-11 architectural tension in one move. Six criteria are activated by one structural change.

**E-02 — Failure mode labeling as pre-gate first-class construct.** Each role carries "Failure mode: [name]" as a labeled construct in the role definition, separate from the gate entry. This separates concept from enforcement: the role definition names what can go wrong (C-30 satisfaction site), the gate block names how to detect and prevent it (C-11 satisfaction site). The two-location pattern is what enables concurrent execution — the role definition survives without execution-step attachment; the gate block handles enforcement.

**E-03 — Concurrent execution paired with output format contract.** C-35 requires both: concurrent reasoning AND seamless output. R11 V-02 specifies both together in a single instruction block: "Three cognitive roles execute concurrently in your reasoning" (execution model) + "output contains no labeled role sections and no visible role seams" (output format contract). Neither alone satisfies C-35. The dual specification is the minimum sufficient form.

---

## Series Note

R11 V-02 achieves the first confirmed all-essential PASS. R12 natural target: combine V-02's gate block architecture with V-01's phase ceiling (C-39) — the one aspirational V-02 currently misses. That variation would earn all eleven tracked criteria simultaneously.

---

```json
{"top_score": 115.0, "all_essential_pass": true, "new_patterns": ["unified gate block resolves C-11/C-13/C-30 essential cluster and enables C-35/C-38/C-40 simultaneously — one structural section replaces scattered per-step gates in concurrent-compatible form", "explicit Failure mode: [name] labeling in role definitions as pre-gate declaration separates concept from enforcement, enabling C-30 satisfaction independent of gate structure", "concurrent execution paired with output format contract (no labeled role sections, no visible role seams) satisfies C-35 dual requirement — execution model and output format must both be specified in the same instruction"]}
```
