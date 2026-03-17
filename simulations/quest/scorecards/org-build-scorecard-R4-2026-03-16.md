## Quest Score — org-build Round 4

### Criterion Matrix

| ID | Category | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|----------|------|------|------|------|------|
| **C-01** | essential | PASS | PASS | PASS | PASS | PASS |
| **C-02** | essential | PASS | PASS | PASS | PASS | PASS |
| **C-03** | essential | PASS | PASS | PASS | PASS | PASS |
| **C-04** | essential | PASS | PASS | PASS | PASS | PASS |
| **C-05** | essential | PASS | PASS | PASS | PASS | PASS |
| **C-06** | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-07** | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-08** | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-09** | aspirational | PASS | FAIL | FAIL | FAIL | PASS |
| **C-10** | aspirational | PASS | FAIL | FAIL | PASS | PASS |
| **C-11** | aspirational | PASS | PASS | FAIL | FAIL | PASS |
| **C-12** | aspirational | PASS | PASS | FAIL | FAIL | PASS |
| **C-13** | aspirational | PASS | PASS | FAIL | PASS | PASS |
| **C-14** | aspirational | PASS | PASS | FAIL | FAIL | PASS |
| **C-15** | aspirational | PASS | PASS | FAIL | PASS | PASS |
| **C-16** | aspirational | PASS | FAIL | FAIL | PASS | PASS |
| **C-17** | aspirational | PASS | PASS | FAIL | FAIL | PASS |
| **C-18** | aspirational | PASS | PASS | FAIL | PASS | PASS |
| **C-19** | aspirational | **FAIL** | FAIL | FAIL | PASS | PASS |
| **C-20** | aspirational | PASS | FAIL | FAIL | FAIL | PASS |

---

### Evidence Notes

**V-01 — C-19 FAIL:** The hypothesis states advisory phrasing is still present. Inspecting the text confirms: `"Scan the repository"`, `"Show at least two hierarchy levels"`, `"Use box-and-line notation"`, `"Include at least two area rows"` — all constraint statements without MUST prefix. C-19 pass condition requires every constraint to use MUST or FORBIDDEN; plain imperatives without explicit MUST fail. All other criteria pass on the text as written.

**V-02 — basis for PASS set:** Hypothesis explicitly lists C-08/C-11/C-12/C-17/C-18 as structural guarantees from inertia-first Phase 1. Phase 1 gate emits T1-VERDICT and T1-FLAT-CASE-PRESSURE as named typed variables. Downstream phases reference them by name → C-14 PASS (at least one pair). Verdict guard in Phase 1 uses bidirectional FORBIDDEN → C-13, C-15 PASS. Fails C-09 (row-type constraint not in this axis), C-10 (MUST in anti-pattern not addressed), C-16 (mitigation-cell remediation rule not in this axis), C-19 (phrasing not addressed), C-20 (not all phases have gates and input contracts).

**V-03 — all aspirationals FAIL:** Axis is sequencing only (roles before chart). Structural guarantees land on C-02, C-04, C-06 — all already passing. No axis-generated content addresses any aspirational. Score reflects that sequencing discipline produces zero aspirational gains.

**V-04 — PASS set from register sweep:** Converting advisory → MUST/FORBIDDEN activates: C-10 (`MUST` in anti-pattern Watch), C-13 (FORBIDDEN: writing both verdicts), C-15 (FORBIDDEN: omitting both verdicts), C-16 (FORBIDDEN: format guidance in Mitigation), C-18 (FORBIDDEN: wrong category set per verdict path), C-19 (uniform register). Fails C-09 (row-type requires structural instruction, not phrasing), C-11/C-12/C-17 (require inertia-first derivation), C-14 (no phase gate machinery), C-20 (no systematic gate coverage).

**V-05 — all 12 aspirationals PASS:** Combines lifecycle gates (V-01), inertia-first verdict propagation (V-02), and uniform MUST/FORBIDDEN register (V-04). The single C-19 failure in V-01 is closed by the V-04 axis. C-20 achieved by V-01's full gate architecture. All structural guarantees from V-02 preserved.

---

### Composite Scores

| Variation | Essential (5→60) | Recommended (3→30) | Aspirational (N/12→10) | **Total** |
|-----------|------------------|---------------------|------------------------|-----------|
| **V-01** | 5/5 → 60 | 3/3 → 30 | 11/12 → 9.17 | **99.17** |
| **V-02** | 5/5 → 60 | 3/3 → 30 | 7/12 → 5.83 | **95.83** |
| **V-03** | 5/5 → 60 | 3/3 → 30 | 0/12 → 0.00 | **90.00** |
| **V-04** | 5/5 → 60 | 3/3 → 30 | 6/12 → 5.00 | **95.00** |
| **V-05** | 5/5 → 60 | 3/3 → 30 | 12/12 → 10.00 | **100.00** |

---

### Ranking

1. **V-05 — 100.00** — Combined lifecycle + inertia-first + uniform register. All 20 criteria pass.
2. **V-01 — 99.17** — Lifecycle emphasis alone reaches 99+. Single gap: C-19 from advisory imperatives.
3. **V-02 — 95.83** — Inertia-first structural guarantees buy 7 aspirationals. Gate machinery is partial, register unaddressed.
4. **V-04 — 95.00** — Register sweep buys 6 aspirationals. Structural depth criteria (C-11, C-12, C-14, C-17, C-20) unreachable by phrasing alone.
5. **V-03 — 90.00** — Sequencing discipline is correct but contributes zero aspirational gains. Guarantees things already passing.

---

### Excellence Signals from V-05

**1. Closed constraint system via axis composition.** V-01 alone reaches 99.17 because lifecycle gates handle C-09 through C-20 — except C-19, which requires a separate axis. The joint application of lifecycle (typed variables in every gate) and register (MUST/FORBIDDEN for every constraint statement) creates a property stronger than either alone: every constraint is simultaneously *strongly worded* and *structurally enforced*. Neither axis alone could close C-20 and C-19 simultaneously.

**2. Inertia-first as a derivation lock.** V-02's contribution in V-05 is that C-11/C-12/C-17/C-18 stop being instruction-compliance requirements and become structural consequences of Phase 1. The verbatim scope template, the category-to-verdict mapping, and the exclusion FORBIDDEN statements are all keyed to T1-FLAT-CASE-PRESSURE and T1-VERDICT at Phase 1 gate. The model cannot produce incoherent downstream artifacts without explicitly violating a named variable binding.

**3. V-03 teaches by contrast: sequencing discipline without gate machinery is invisible to the rubric.** Bottom-up role writing is a valid development pattern but it operates entirely within criteria that are already passing. A sequencing-only variation cannot activate aspirational criteria without adding typed output declarations. The lesson: structural guarantees for already-passing criteria score nothing; structural guarantees for failing criteria (phase gates, verbatim templates) score everything.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["constraint-completeness-seal: uniform MUST/FORBIDDEN register combined with all phase gates declaring typed outputs produces a closed constraint system where no rule is advisory and no data is implicit — a compound property not testable by C-19 or C-20 individually", "pre-print skeleton: V-05 description names a filled-in output template with placeholder slots as the highest-gain device — this constrains output shape beyond what typed variable declarations achieve and is not captured by any current criterion"]}
```
