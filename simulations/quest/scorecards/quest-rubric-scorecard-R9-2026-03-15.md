## quest-rubric — Round 9 Scoring (v9 Rubric, Batch 2)

---

### Rubric Criteria in Scope

| ID | Criterion | Tier | Notes |
|----|-----------|------|-------|
| C-01 | Essential criteria block present | essential | FM-01 |
| C-02 | Calibration pair discrimination | essential | STATUS-QUO/GENERIC vs GROUNDED distinct |
| C-03 | Severity ranking (C-01 = rank-1 failure) | essential | M-01 |
| C-04 | Named-blocks present (M-02 satisfied) | essential | scannable heading structure |
| C-05 | Weighted formula, not binary | essential | FM-02 |
| C-23 | Per-criterion PARTIAL-CONDITION block | recommended | per-criterion partial-credit boundary |
| C-24 | Formula consistency across structural positions | aspirational | no SA-1/FINAL divergence |
| C-25 | Anti-collapse formula guard (v9 form) | recommended | "verbatim at every structural position" |
| C-26 | Verdict tier declaration (evaluator-facing) | recommended | band table + gate |
| C-27 | Per-criterion DISCRIMINATES-BETWEEN block | aspirational | boundary-scan detectability |
| C-28 | Per-criterion DEPENDS_ON / INDEPENDENT | aspirational | dependency graph |

Essential = C-01–C-05 (5); Recommended = C-23, C-25, C-26 + others (3 counted); Aspirational = C-24, C-27, C-28 + inherited pool (20 denominator)

---

### V-01 — Role Sequence: Auditor Pre-Declaration

**Axis:** role-sequence (single)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | INERTIA-RECORD / CALIBRATION-PAIR / CRITERION blocks in template; Phase 0 skeleton declares all |
| C-02 | PASS | CALIBRATION-PAIR has STATUS-QUO vs GROUNDED — named competitor present at top |
| C-03 | PASS | SEVERITY RANK + DEFINITION (most critical) present; C-01 MUST target rank-1 |
| C-04 | PASS | Named-block headings `### INERTIA-RECORD [C-NN]` etc. preserved verbatim |
| C-05 | PASS | Weighted formula in FINAL RUBRIC; DO NOT collapse guard present |
| C-23 | **PASS** | CALIBRATION-PAIR has PARTIAL-CONDITION grounded in `### AUDITOR-PRE [C-NN]` (lines 313–315); PARTIAL-CONDITION must not be inferrable from PASS condition without independent judgment |
| C-24 | PASS | Single formula position (FINAL RUBRIC); no SA-1 to create inconsistency |
| C-25 | PASS | "DO NOT collapse to binary counting — reproduce this formula verbatim at every structural position" — v9 form, no SA-1 reference (lines 520–523) |
| C-26 | PASS | AUDITOR GATE checklist + Golden/Acceptable/Marginal/Fail band table in FINAL RUBRIC |
| C-27 | PASS | AUDITOR-PRE blocks carry PASS/PARTIAL/FAIL evidence with boundary marker; `### AUDITOR-PRE [C-NN]` heading is scannable; C-28-inherited from R8 V-05 |
| C-28 | PASS | Pre-Dec Alignment column in Audit Table verifies AUDITOR-PRE → PARTIAL-CONDITION chain; dependency ordering from R8 V-05 inherited |

**E = 5/5 → 60 | R = 3/3 → 30 | A ≈ 20/20 → 10**
**Composite: 100.0 — Golden**

**C-35 candidate signal:** `### AUDITOR-PRE [C-NN]` pre-declaration step makes the PARTIAL-credit boundary auditable *before* the Author Phase commits to a criterion — partial interpretation is locked in at declaration time, not at evaluation time. If this pre-declaration consistently produces tighter PARTIAL-CONDITION blocks than post-hoc review, it is a new structural guarantee not present in R8 V-05.

---

### V-02 — Phrasing Register: Conversational Imperative

**Axis:** phrasing-register (single)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Named blocks present; template structure intact |
| C-02 | PASS | CALIBRATION-PAIR has GENERIC vs GROUNDED; named competitor ("generic rubric") referenced throughout |
| C-03 | PASS | Severity ranking and "most critical" definition preserved; conversational framing only |
| C-04 | PASS | `### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`, `### CRITERION [C-NN]` heading patterns explicitly preserved (design note lines 568–568) |
| C-05 | PASS | Weighted formula in FINAL RUBRIC |
| C-23 | **FAIL** | CALIBRATION-PAIR template has GENERIC and GROUNDED only — no PARTIAL-CONDITION field (lines 749–753). R8 V-05 had PARTIAL-CONDITION; V-02 drops it. Structural contract claim ("identical to R8 V-05") is violated at this field. Conversational register either inadvertently dropped PARTIAL-CONDITION or lacks the AUDITOR-PRE grounding mechanism needed to anchor it independently. |
| C-24 | PASS | Single formula position; no inconsistency |
| C-25 | PASS | Formula guard present verbatim (lines 925–926) |
| C-26 | PASS | Checklist gate + band table present |
| C-27 | PASS | Design note explicitly preserves `### INERTIA-RECORD [C-NN]` heading patterns; Rule A/B replace INVARIANT A/B but structural heading structure intact; DISCRIMINATES-BETWEEN blocks inherited from R8 V-05 not degraded |
| C-28 | PASS | Dependency structure from R8 V-05 preserved; conversational framing doesn't affect DEPENDS_ON declarations |

**E = 5/5 → 60 | R = 2/3 → 20 (C-23 FAIL) | A ≈ 19/20 → 9.5** (C-23-adjacent aspirational sub-criteria also weakened)
**Composite: 89.5**

**Finding:** Conversational register does NOT regress C-27 (DISCRIMINATES-BETWEEN) or C-28 (DEPENDS_ON) — structural heading patterns survive label-vocabulary substitution. But C-23 regresses: without AUDITOR-PRE, PARTIAL-CONDITION loses its independent grounding anchor and is dropped entirely. Vocabulary is navigational; the grounding mechanism (AUDITOR-PRE) is structural.

---

### V-03 — Inertia Framing: Implicit Competitor / Unnamed Status-Quo

**Axis:** inertia-framing (single, minimal direction)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Named blocks intact |
| C-02 | PASS | CALIBRATION-PAIR has GENERIC vs GROUNDED; prose note instructs "formulate the weakest acceptable condition" even without named competitor (lines 1161–1164); discrimination criterion still functional |
| C-03 | PASS | Severity ranking preserved; DEFINITION (most critical) present |
| C-04 | PASS | Named block heading patterns unchanged |
| C-05 | PASS | Weighted formula |
| C-23 | **FAIL** | CALIBRATION-PAIR has GENERIC and GROUNDED only — no PARTIAL-CONDITION (lines 1154–1158). Without AUDITOR-PRE and without a named competitor anchor, PARTIAL-CONDITION has no grounding source. Probe confirmed: named-competitor framing is NOT load-bearing for GROUNDED field quality, but the absence of a pre-declaration mechanism leaves PARTIAL-CONDITION unanchored. |
| C-24 | PASS | Single formula; no inconsistency |
| C-25 | PASS | Guard present (lines 1339–1340) |
| C-26 | PASS | AUDITOR GATE + band table |
| C-27 | PASS | Structural blocks inherited; unnamed competitor doesn't affect heading detectability |
| C-28 | PASS | Dependency declarations inherited from R8 V-05; unnamed competitor doesn't affect them |

**E = 5/5 → 60 | R = 2/3 → 20 (C-23 FAIL) | A ≈ 19/20 → 9.5**
**Composite: 89.5**

**Finding:** Named-competitor framing is NOT load-bearing for CALIBRATION-PAIR structural quality (C-27, C-28) or formula integrity (C-24, C-25). C-02 survives because the prose instruction compensates. C-23 fails for the same reason as V-02: the absence of AUDITOR-PRE leaves PARTIAL-CONDITION without an independent anchor. The named competitor was a grounding crutch for PARTIAL-CONDITION, not a structural requirement.

---

### V-04 — Role Sequence × Phrasing Register (Combination)

**Axes:** V-01 + V-02

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Named blocks in template; Phase 0 skeleton includes AUDITOR-PRE |
| C-02 | PASS | CALIBRATION-PAIR has STATUS-QUO vs GROUNDED; named competitor at top |
| C-03 | PASS | Severity ranking preserved; conversational framing doesn't change structure |
| C-04 | PASS | `### AUDITOR-PRE [C-NN]`, `### INERTIA-RECORD [C-NN]`, etc. heading patterns retained (lines 1494–1500) |
| C-05 | PASS | Weighted formula |
| C-23 | **PASS** | CALIBRATION-PAIR has STATUS-QUO, GROUNDED, PARTIAL-CONDITION (lines 1589–1593); AUDITOR-PRE provides pre-declared boundary; conversational register does NOT cause PARTIAL-CONDITION to drop |
| C-24 | PASS | Single formula; no inconsistency |
| C-25 | PASS | "DO NOT collapse to binary counting — reproduce this formula verbatim at every structural position" (lines 1756–1757) |
| C-26 | PASS | Checklist gate + band table |
| C-27 | PASS | `### AUDITOR-PRE [C-NN]` heading preserved despite conversational surrounding prose; DISCRIMINATES-BETWEEN blocks inherited |
| C-28 | PASS | DEPENDS_ON structure intact; Pre-Dec Alignment column in Audit Table |

**E = 5/5 → 60 | R = 3/3 → 30 | A ≈ 20/20 → 10**
**Composite: 100.0 — Golden**

**Key compound result:** The Auditor Pre-Declaration structural value is independent of formal CONSTRAINT/INVARIANT vocabulary. V-04 demonstrates that `### AUDITOR-PRE [C-NN]` heading patterns survive conversational framing — the grounding mechanism is preserved even when the imperative prose is plain. Formal labels (INVARIANT C, PRECONDITION for Author Phase entry) are navigational, not structural.

---

### V-05 — Full Accumulation: Role Sequence × Phrasing Register × Inertia Framing

**Axes:** V-01 + V-02 + V-03 (all three)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Named blocks, Phase 0 skeleton with AUDITOR-PRE; all structural |
| C-02 | PASS | CALIBRATION-PAIR has GENERIC vs GROUNDED; unnamed competitor handled by AUDITOR-PRE threshold taking the anchoring role |
| C-03 | PASS | Severity ranking intact |
| C-04 | PASS | All named-block heading patterns preserved |
| C-05 | PASS | Weighted formula |
| C-23 | **PASS** | CALIBRATION-PAIR has GENERIC, GROUNDED, PARTIAL-CONDITION (lines 2002–2008); note explicitly states: "the acceptance threshold declared before this criterion was drafted" — AUDITOR-PRE compensates for absent named competitor |
| C-24 | PASS | Single formula; no inconsistency |
| C-25 | PASS | Guard present verbatim (lines 2181–2182) |
| C-26 | PASS | Gate + band table |
| C-27 | PASS | AUDITOR-PRE blocks provide FAILS-AT/PASSES-AT/Boundary equivalent; `### AUDITOR-PRE [C-NN]` heading scannable without reading content |
| C-28 | PASS | Pre-Dec Alignment column + convergence check in Auditor Phase; DEPENDS_ON inherited |

**E = 5/5 → 60 | R = 3/3 → 30 | A ≈ 20/20 → 10**
**Composite: 100.0 — Golden**

**Compound signal (C-35 batch-2 candidate):** Auditor Phase gate in V-05 adds a convergence check absent from V-01 and V-04 individually (lines 2127–2130): "does the Auditor Pre-Declaration threshold appear in the CALIBRATION-PAIR PARTIAL-CONDITION field *without being simply copied* from the AUDITOR-PRE block?" This tests that the PARTIAL boundary is both pre-declared (independent of Author interpretation) AND re-grounded criterion-specifically (not mechanically copied). This two-property test only surfaces when all three axes combine: pre-declaration (role-sequence) + implied generic-rubric contrast (unnamed competitor) + plain prose detection. Neither V-01 nor V-04 tests this independently.

---

### Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | all_essential_pass |
|-----------|---------------|-----------------|-------------------|-----------|-------------------|
| V-01 | 60.0 | 30.0 | 10.0 | **100.0** | ✓ |
| V-02 | 60.0 | 20.0 | 9.5 | **89.5** | ✓ |
| V-03 | 60.0 | 20.0 | 9.5 | **89.5** | ✓ |
| V-04 | 60.0 | 30.0 | 10.0 | **100.0** | ✓ |
| V-05 | 60.0 | 30.0 | 10.0 | **100.0** | ✓ |

**Rank:** V-01 = V-04 = V-05 (100.0 Golden) > V-02 = V-03 (89.5)

Among 100.0 scorers: V-05 has the richest new structural signal (convergence check); V-04 confirms conversational register is structurally neutral for C-27/C-28; V-01 establishes the AUDITOR-PRE pre-declaration mechanism.

---

### Excellence Signals from Top-Scoring Variations

**From V-01 (root signal, inherited by V-04 and V-05):**

The `### AUDITOR-PRE [C-NN]` block inserted before the Author Phase is a structurally load-bearing grounding mechanism for PARTIAL-CONDITION. V-02 and V-03 both regress on C-23 — different axes, same root cause: without a pre-declaration mechanism, PARTIAL-CONDITION has no independent anchor and is dropped. This makes AUDITOR-PRE the enabling structure for C-23, not CALIBRATION-PAIR field formatting or named-competitor vocabulary.

**From V-04 (vocabulary independence):**

Conversational register (plain imperative prose replacing CONSTRAINT/INVARIANT labels) does not degrade C-27 (DISCRIMINATES-BETWEEN) or C-28 (DEPENDS_ON) because structural guarantee depends on `### heading` patterns, not on surrounding label vocabulary. V-04 isolates this cleanly: AUDITOR-PRE plus conversational framing still scores 100.0. Formal vocabulary is navigational.

**From V-05 (compound convergence signal):**

At three-axis combination, a new structural check emerges: the AUDITOR-PRE acceptance threshold must appear in CALIBRATION-PAIR PARTIAL-CONDITION without being mechanically copied. This convergence test is absent from V-01 and V-04 individually — it only appears when (a) there's a pre-declared boundary, (b) there's no named competitor providing an external discrimination anchor, and (c) the boundary must be expressed in plain prose. The result: two independent quality guarantees for PARTIAL credit — pre-declared (AUDITOR-PRE) and criterion-specific grounding (CALIBRATION-PAIR independent formulation). Whether this is a C-35 candidate depends on whether V-05 M-06 probe (boundary × dependency consistency check) shows divergence from C-28 in at least one case.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["AUDITOR-PRE pre-declaration block grounds CALIBRATION-PAIR PARTIAL-CONDITION independently of named-competitor framing — without it, PARTIAL-CONDITION loses its anchor and is dropped (C-23 regression confirmed across V-02 and V-03)", "Conversational register does not degrade C-27 or C-28 when named structural heading patterns (### AUDITOR-PRE [C-NN]) are explicitly preserved — formal CONSTRAINT/INVARIANT vocabulary is navigational not structural", "Convergence check at three-axis combination: AUDITOR-PRE threshold must appear in CALIBRATION-PAIR PARTIAL-CONDITION without mechanical copy — two-property guarantee emerges only when pre-declaration and unnamed-competitor axes combine"]}
```
