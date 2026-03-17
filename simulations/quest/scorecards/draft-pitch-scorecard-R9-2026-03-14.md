I have enough context from the rubric and variations to score all five. Let me evaluate each against the full 40-criterion rubric.

---

## draft-pitch — Round 9 Scorecard

### Baseline

All five variations inherit **R8 V-05** as their base. R8 V-05 passed all 30 prior criteria (C-01–C-37). R9 adds three new aspirational criteria: **C-38** (phase-level envelopment), **C-39** (pre-committed anchor), **C-40** (gate converts advisories). The only scoring differences across variations are which subset of {C-38, C-39, C-40} each passes.

---

### C-01 through C-37 — All Variations

| ID | Result | Notes |
|----|--------|-------|
| C-01 through C-04 | **PASS** (all) | Essential criteria. Inherited from R8 V-05. Exec opening gate, feature-free hook, three audience versions, proof audit. |
| C-05 through C-07 | **PASS** (all) | Recommended criteria. Inherited from R8 V-05. Signal intake, scout signal fallback, anti-positioning. |
| C-08 through C-37 | **PASS** (all) | Aspirational criteria. Inherited from R8 V-05. Covers depth, process, and resilience for Phases 1–5 including BINDING DECLARATION, INERTIA PROFILE, DIFFERENTIATION GATE, Maker-first order, position labels, per-audience inertia, inline provenance, etc. |

Inherited aspirational pass count: **30 of 33**.

---

### C-38 — Phase-level envelopment

**Pass condition**: All three elements (INERTIA PROFILE, Maker-first order, DIFFERENTIATION GATE) present AND their sequential pre-commit/fill/close relationship stated explicitly before any drafting step, mirroring prior phase patterns.

| Variation | Result | Evidence |
|-----------|--------|---------|
| **V-01** | **PASS** | Named PHASE 5 STRUCTURE block present before INERTIA PROFILE. Names all three elements with explicit labels (pre-commit step / constrained-fill step / post-verify step). States: "These three elements form a coherent pre-commit/fill/close envelope. All three must be present and executed in sequence. Having any two of three does not pass. Phase 5 is auditable from skill structure alone: the sequence is explicit before any draft is written." Mirrors Phase 2 BINDING DECLARATION pattern by name. |
| **V-02** | **FAIL** | No PHASE 5 STRUCTURE block. Three elements are structurally present (INERTIA PROFILE, Maker-first, DIFFERENTIATION GATE) but no named block states their sequential relationship or the pre-commit/fill/close pattern. Presence ≠ auditability. |
| **V-03** | **FAIL** | Same as V-02. No envelope declaration block added. |
| **V-04** | **PASS** | Same PHASE 5 STRUCTURE block as V-01. Inherited from V-01 component. |
| **V-05** | **PASS** | Same PHASE 5 STRUCTURE block. Inherited from V-01 component. |

---

### C-39 — Pre-committed anchor preserves order integrity

**Pass condition**: Constraint-ascending draft order declaration accompanied by explicit naming of a prior-phase pre-committed output AND explicit statement that the draft order cannot weaken that output.

| Variation | Result | Evidence |
|-----------|--------|---------|
| **V-01** | **FAIL** | Draft order declared (Maker first, then Dev, then Exec) but no draft-order integrity statement. EXEC OPENING SENTENCE is cited by name in the Exec Hook instruction with provenance, but no statement connects the Phase 4 lock to the Maker-first constraint — does not assert that Maker-first cannot weaken the pre-committed output. |
| **V-02** | **PASS** | Draft-order integrity statement present: "EXEC OPENING SENTENCE is locked at Phase 4, before Phase 5 begins. The Maker-first constraint-ascending order cannot weaken the exec version: EXEC OPENING SENTENCE is pre-committed by Phase 4's binary gate and the Exec Hook must use exact text regardless of draft order. Maker-first affects only which version is drafted first — it does not change any locked output from Phases 2, 3, or 4." Named anchor = EXEC OPENING SENTENCE. Explicit statement that order cannot affect it. Both pass conditions satisfied. |
| **V-03** | **FAIL** | Same as V-01. No draft-order integrity statement. |
| **V-04** | **PASS** | Same draft-order integrity statement as V-02. Inherited from V-02 component. |
| **V-05** | **PASS** | Same draft-order integrity statement. Inherited from V-02 component. |

---

### C-40 — Gate converts pre-existing advisory constraints into structural stops

**Pass condition**: Every gate YES/NO question enforces a constraint that already appears as an advisory instruction elsewhere in the skill. Gate invents no new constraints.

Baseline gate questions (R8 V-05 and V-01/V-02/V-04):
- Q1: "Are the three Core Belief summaries substantively distinct?" — Phase 2 Core Belief definition says only "The one thing this audience must believe before any other argument can land." **No prior advisory about distinctness**. Q1 introduces a new constraint at the gate.
- Q2: "Does the Maker version contain any unexplained acronym?" — Maker Hook instruction: "Zero unexplained acronyms. Zero namespace references. Zero CLI terminology." Advisory exists. ✓
- Q3: "Does the Dev version open with a scenario?" — Dev Hook instruction: "A scenario the developer is in right now." Advisory exists. ✓

| Variation | Result | Evidence |
|-----------|--------|---------|
| **V-01** | **FAIL** | Q1 (Core Belief distinctness) has no advisory counterpart in Phase 2. Core Belief column definition adds no distinctness requirement. Gate invents a constraint at Q1. Q2 and Q3 have advisories but Q1 failure is sufficient to fail C-40. |
| **V-02** | **FAIL** | Same. Phase 2 Core Belief column definition unchanged from R8 V-05 base. Q1 still introduces a new constraint with no prior advisory. |
| **V-03** | **PASS** | Phase 2 Core Belief column definition expanded: "Each Core Belief must be substantively distinct from the other two — naming a claim that belongs specifically to this audience and could not be the primary belief anchor for a different audience. A Core Belief that paraphrases another audience's Core Belief does not pass." Gate Q1 carries inline advisory citation: "*(This enforces the Core Belief distinctness advisory stated in Phase 2 Core Belief column definition.)*" All three gate questions now convert pre-existing advisories. Q2 and Q3 citations also added. Gate invents no new constraints. |
| **V-04** | **FAIL** | Same Phase 2 Core Belief definition as V-01/V-02/R8 base. No distinctness advisory added. Q1 still introduces a new constraint. |
| **V-05** | **PASS** | Phase 2 Core Belief definition includes distinctness advisory (from V-03 component). All three gate questions carry inline advisory citations. Gate converts, does not invent. |

---

### Per-Variation Summary

| Variation | C-38 | C-39 | C-40 | New Passes | Aspirational Total |
|-----------|------|------|------|------------|-------------------|
| V-01 | PASS | FAIL | FAIL | 1 | 31/33 |
| V-02 | FAIL | PASS | FAIL | 1 | 31/33 |
| V-03 | FAIL | FAIL | PASS | 1 | 31/33 |
| V-04 | PASS | PASS | FAIL | 2 | 32/33 |
| **V-05** | **PASS** | **PASS** | **PASS** | **3** | **33/33** |

---

### Score Computation

Formula: `Score = (essential_pass/4)*60 + (recommended_pass/3)*30 + (aspirational_pass/33)*10`

All variations: essential_pass = 4, recommended_pass = 3.

| Variation | Essential | Recommended | Aspirational | **Score** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | (4/4)*60 = 60.00 | (3/3)*30 = 30.00 | (31/33)*10 = 9.39 | **99.39** |
| V-02 | 60.00 | 30.00 | (31/33)*10 = 9.39 | **99.39** |
| V-03 | 60.00 | 30.00 | (31/33)*10 = 9.39 | **99.39** |
| V-04 | 60.00 | 30.00 | (32/33)*10 = 9.70 | **99.70** |
| **V-05** | **60.00** | **30.00** | **(33/33)*10 = 10.00** | **100.00** |

---

### Rankings

1. **V-05 — 100.00** (C-38+C-39+C-40 all pass)
2. **V-04 — 99.70** (C-38+C-39, C-40 fails)
3. **V-01 — 99.39** (C-38 only)
3. **V-02 — 99.39** (C-39 only)
3. **V-03 — 99.39** (C-40 only)

---

### Excellence Signals from V-05

**Pattern 1 — Phase-level structural declaration block (C-38)**
Before the first fill step of a multi-element phase, a named block explicitly states the phase's internal structure (element names, sequential labels, pass/fail rule for the set). This mirrors the BINDING DECLARATION pattern from Phase 2: auditability is stated as intent, not achieved silently. The block asserts the "having any two of three does not pass" rule — making the pattern testable from skill text alone before execution.

**Pattern 2 — Anchor integrity statement for constrained ordering (C-39)**
When a constraint-ascending execution order is declared, a dedicated anchor integrity statement names the pre-committed prior-phase output and explicitly asserts the constrained order cannot affect it. The statement separates two distinct claims: (a) the order is constrained, and (b) the pre-committed anchor is immune to that constraint. Without (b), the order declaration is structurally undefended against the objection that Maker-first weakens the exec version.

**Pattern 3 — Advisory-to-gate promotion with inline citation (C-40)**
Each gate YES/NO question carries an inline citation naming the advisory instruction it enforces and where it appears. This transforms the gate from an independent constraint list into a traceable enforcement layer. The gate invents nothing: every pass/fail stop is derivable from the skill's advisory instructions alone. This makes the gate's authority auditable — a reader can verify that the gate is tightening pre-stated requirements, not imposing novel ones.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Phase-level structural declaration block names all envelope elements with sequential labels and pass/fail rule before any fill step executes, mirroring the BINDING DECLARATION auditability pattern", "Anchor integrity statement separates order constraint from output immunity: explicitly names the pre-committed prior-phase output and asserts the constrained draft order cannot affect it", "Advisory-to-gate promotion with inline citation: each gate question carries a parenthetical naming the advisory instruction it enforces and its location, making the gate's authority derivable from skill structure alone"]}
```
