Written to `simulations/quest/rubrics/flow-integration-rubric-v17-variations-R17-2026-03-15.md`.

---

## flow-integration R17 Variations — Summary

**Five complete prompts, single-axis first then combined.**

---

### V-01 — SHOULD Modal Failure Probe
**Axis**: Phrasing register — SHOULD replaces indicative in WHY anchor  
**Hypothesis**: ~157/182 aspirational. SHOULD = "recommended but not required" → cascade fail C-37, C-39, C-40, C-42, C-43 (−25 pts minimum). Answers **Q1** for SHOULD.

WHY anchor: *"Undocumented integration calls **SHOULD** become ship-blockers at integration review..."*

---

### V-02 — MAY Modal Failure Probe
**Axis**: Phrasing register — MAY replaces indicative in WHY anchor  
**Hypothesis**: ~157/182 aspirational. MAY = "optional" → same cascade via discretionary weakening, different failure mechanism than SHOULD. Closes **Q1** independently for MAY.

WHY anchor: *"...authentication, rate limits, retry behavior, and error propagation gaps **MAY** become ship-blockers at integration review if not documented."*

---

### V-03 — C-44 Clean Ceiling Probe
**Axis**: Inertia framing — explicit 3-sentence inertia prefix + C-42 anchor-close  
**Hypothesis**: 182/182 aspirational. Resolves **Q2**: sentences labeled as (1) implicit SDK undercounting, (2) delegation chain gap, (3) undefined obligation scope → single declarative anchor-close with concern enumeration → C-44 PASS, C-41 PASS, C-42 PASS simultaneously.

---

### V-04 — C-43 × C-44 Interaction: MUST + Inertia-Dominant
**Axis**: Combined — MUST modal (C-43) + three-sentence inertia prefix (C-44)  
**Hypothesis**: 182/182 aspirational. Orthogonal surfaces — C-43 tests modal strength, C-44 tests inertia sentence count. MUST anchor-close with five-concern enumeration activates both. No conflict expected.

---

### V-05 — Full 272-pt Ceiling Attempt
**Axis**: Combined — all of V-04 + five-row non-standard obligation table  
**Non-standard substitutions**: `spec-invisible`, `underspecified`, `unresolvable`, `proxy-relay` replace the four canonical terms; `cold-start-init` is a new 5th row (no canonical equivalent → outside C-34 scope). YOU MUST NOT block enumerates all four substituted canonical tokens inline.  
**Hypothesis**: 272/272 — first attempt at the new R17 ceiling. Activates C-35, C-38, C-43, C-44, C-27/C-30/C-31/C-34 in a single form.

---

**Open questions forward to R18:**
- Q1 (R18): Does V-04 confirm C-43 + C-44 compose without interaction penalty?
- Q2 (R18): Does V-05 achieve 272/272 empirically?
