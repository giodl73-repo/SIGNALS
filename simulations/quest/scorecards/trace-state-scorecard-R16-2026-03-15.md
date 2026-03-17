## trace-state · Round 16 Scoring — Rubric v14

**Scoring parameters:** 5 essentials × 10 pts = 50 | 35 aspirationals × 50/35 ≈ 1.43 pts each | Max 100 | Golden ≥ 80

---

## Essential Criteria — All Variations

All five variations provide: complete state triple structure (C-01), explicit preconditions + postconditions (C-02), two non-trivial invariants per operation (C-03), labeled defect with type/triggering-op/reason (C-04), and domain-recognizable Sales/CS/Finance vocabulary (C-05).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 State triple | PASS | PASS | PASS | PASS | PASS |
| C-02 Pre/post conditions | PASS | PASS (sub-steps 1+3) | PASS | PASS | PASS |
| C-03 Two domain invariants | PASS | PASS (sub-step 4) | PASS | PASS | PASS |
| C-04 Labeled defect | PASS | PASS | PASS | PASS | PASS |
| C-05 Domain plausibility | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 50 pts for all variations.** All essential pass = ✓ all five.

---

## Aspirational Criteria (C-09–C-44)

### Format-constraint rulings (applied before scoring)

| Criterion | Format restriction | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------------|------|------|------|------|------|
| C-38 step-label criterion fusion | Step-block only | FAIL | PASS | FAIL | PASS | FAIL |
| C-39 step-block disqualification fusion | Step-block only | FAIL | PASS | FAIL | PASS | FAIL |
| C-30 column-header criterion fusion | Tabular only | PASS | PARTIAL | PASS | PARTIAL | PASS |
| C-34 column-header FAILS-if patterns | Tabular only | PASS | FAIL | PASS | FAIL | PASS |
| C-40 per-pass labeled defect | Multi-pass only | PASS | FAIL | PASS | FAIL | PASS |
| C-41 cross-domain precondition chain | Multi-pass only | PASS | FAIL | FAIL | PASS | PASS |
| C-42 domain-ordering hypothesis | Multi-pass only | PASS | FAIL | PASS | FAIL | PASS |
| C-36 pass-level defect hypothesis | Multi-pass only | PASS | FAIL | PASS | FAIL | PASS |
| C-37 consequence clause at pass headings | Multi-pass only | PASS | FAIL | PASS | FAIL | PASS |
| C-43 lifecycle-phase state annotation | Format-neutral | FAIL | PASS | FAIL | PASS | PASS |
| C-44 sub-step decomposition | Format-neutral | FAIL | PASS | FAIL | FAIL | PASS |

---

### Core aspirationals — structural verification

| Criterion | Evidence basis | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|---------------|------|------|------|------|------|
| C-09 Negative path | Section 6 / Negative-Step block with correct columns | PASS | PASS | PASS | PASS | PASS |
| C-10–C-11, C-15, C-22 (R1–R5 accumulated) | In target lists, no structural counter-evidence | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-12, C-14 | Not in any target list | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-13 Row source linkage | "Derived From (Pass N Row #)" in every registry | PASS | PASS | PASS | PASS | PASS |
| C-16 No-prose prohibition | HARD RULES: "Prose is not a valid format" | PASS | PASS | PASS | PASS | PASS |
| C-17 Minimum row counts | ≥5 per pass, ≥15 total enforced | PASS | PASS | PASS | PASS | PASS |
| C-18 | Not in any target list | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-19 Hard-rules invalidation block | HARD RULES with "any violation invalidates" | PASS | PASS | PASS | PASS | PASS |
| C-20 Valid invariant example | Qualifying example present in invariant sections | PASS | FAIL | PASS | FAIL | PASS |
| C-21 Ordering-2 independence | "Do not write 'same as above'" instruction | PASS | PASS | PASS | PASS | PASS |
| C-23 Silent-omission warning | "silent omissions invalidate this section" | PASS | PASS | PASS | PASS | PASS |
| C-24 Reference row not reproduced | "do not reproduce this row/record in output" | PASS | PASS | PASS | PASS | PASS |
| C-25 Cross-domain invariant register | Section 4 with cross-pass derivation | PASS | PARTIAL | PASS | PASS | PASS |
| C-26 Total-row verification | "Verify: total ≥ 15" / "≥ 10" | PASS | FAIL | PASS | PASS | PASS |
| C-27 Invariant exclusion list | Explicit "does not qualify" patterns | PASS | PASS | PASS | PASS | PASS |
| C-28 Both race-condition ops named | "Name both concurrent operations explicitly" | PASS | PASS | PASS | PASS | PASS |
| C-29 Mutation verification sentence | "write one explicit confirmation sentence" | PASS | PASS | PASS | PASS | PASS |
| C-31–C-33 (R10–R13 accumulated) | In V-02, V-04 target lists | FAIL | PARTIAL | FAIL | PARTIAL | FAIL |
| C-35 Per-pass invariant registry | Load-bearing sub-section heading required | PASS | PASS | PASS | PASS | PASS |

---

### Per-variation aspirational summary

**PASS weight = 1.43 pts | PARTIAL weight = 0.72 pts**

#### V-01 (Tabular 3-pass Finance→Sales→CS | targets C-40, C-41, C-42)

| Pool | PASS criteria | Count |
|------|--------------|-------|
| Prior (C-09–C-39) | C-09, C-13, C-16, C-17, C-19, C-20, C-21, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-32, C-34, C-35, C-36, C-37 | 20 |
| New (C-40–C-44) | C-40, C-41, C-42 | 3 |
| **PASS total** | | **23** |
| PARTIAL | C-10, C-11, C-15, C-22 (in targets, unverifiable from prompt) | 4 |
| FAIL | C-12, C-14, C-18, C-31, C-33, C-38, C-39, C-43, C-44 | 9 |

**V-01 score: 50 + 23 × 1.43 + 4 × 0.72 = 50 + 32.89 + 2.88 = 85.8**

---

#### V-02 (Step-block single-pass Sales | targets C-43, C-44)

| Pool | PASS criteria | Count |
|------|--------------|-------|
| Prior (C-09–C-39) | C-09, C-13, C-16, C-17, C-19, C-21, C-23, C-24, C-27, C-28, C-29, C-35, C-38, C-39 | 14 |
| New (C-40–C-44) | C-43, C-44 | 2 |
| **PASS total** | | **16** |
| PARTIAL | C-10, C-15, C-22, C-25 (single-pass aggregate), C-30 (registry table headers partial), C-31, C-32, C-33 | 8 |
| FAIL | C-11, C-12, C-14, C-18, C-20, C-26, C-34, C-36, C-37, C-40, C-41, C-42 | 12 |

**V-02 score: 50 + 16 × 1.43 + 8 × 0.72 = 50 + 22.88 + 5.76 = 78.6**
*Below golden threshold — single-pass format structurally excludes C-36, C-37, C-40–C-42.*

---

#### V-03 (Tabular 3-pass CS→Finance→Sales | targets C-40, C-42; no bridge table)

| Pool | PASS criteria | Count |
|------|--------------|-------|
| Prior (C-09–C-39) | C-09, C-13, C-16, C-17, C-19, C-20, C-21, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-32, C-34, C-35, C-36, C-37 | 20 |
| New (C-40–C-44) | C-40, C-42 | 2 |
| **PASS total** | | **22** |
| PARTIAL | C-10, C-11, C-15, C-22 | 4 |
| FAIL | C-12, C-14, C-18, C-31, C-33, C-38, C-39, C-41, C-43, C-44 | 10 |

**V-03 score: 50 + 22 × 1.43 + 4 × 0.72 = 50 + 31.46 + 2.88 = 84.3**

*V-03 loses C-41 vs V-01 (no bridge table). The different ordering is the axis, not additional bridge structure.*

---

#### V-04 (Step-block 2-pass Sales→CS | targets C-41, C-43)

| Pool | PASS criteria | Count |
|------|--------------|-------|
| Prior (C-09–C-39) | C-09, C-13, C-16, C-17, C-19, C-21, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-35, C-38, C-39 | 16 |
| New (C-40–C-44) | C-41, C-43 | 2 |
| **PASS total** | | **18** |
| PARTIAL | C-10, C-15, C-22, C-30 (registry table headers), C-31, C-32, C-33 | 7 |
| FAIL | C-11, C-12, C-14, C-18, C-20, C-34, C-36, C-37, C-40, C-42, C-44 | 11 |

**V-04 score: 50 + 18 × 1.43 + 7 × 0.72 = 50 + 25.74 + 5.04 = 80.8**

*Above golden but structurally constrained by 2-pass limit: C-40 excluded (no per-pass defect enforcement), C-42 excluded (no ordering hypothesis at pass headings).*

---

#### V-05 (Tabular 3-pass Finance→Sales→CS | all five C-40–C-44)

| Pool | PASS criteria | Count |
|------|--------------|-------|
| Prior (C-09–C-39) | C-09, C-13, C-16, C-17, C-19, C-20, C-21, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-32, C-34, C-35, C-36, C-37 | 20 |
| New (C-40–C-44) | C-40, C-41, C-42, C-43, C-44 | 5 |
| **PASS total** | | **25** |
| PARTIAL | C-10, C-11, C-15, C-22 | 4 |
| FAIL | C-12, C-14, C-18, C-31, C-33, C-38, C-39 | 7 |

**V-05 score: 50 + 25 × 1.43 + 4 × 0.72 = 50 + 35.75 + 2.88 = 88.6**

*Ceiling variation. Inherits full prior multi-pass tabular pass profile (V-01 base) and adds C-43 + C-44. Remaining gap to 100: C-38/C-39 structurally excluded by tabular format; C-10, C-11, C-15, C-22 (R1–R5 accumulated) uncracked.*

---

## Rankings

| Rank | Variation | Score | Golden | New Criteria Earned |
|------|-----------|-------|--------|---------------------|
| 1 | V-05 | **88.6** | ✓ | C-40, C-41, C-42, C-43, C-44 |
| 2 | V-01 | **85.8** | ✓ | C-40, C-41, C-42 |
| 3 | V-03 | **84.3** | ✓ | C-40, C-42 |
| 4 | V-04 | **80.8** | ✓ | C-41, C-43 |
| 5 | V-02 | **78.6** | ✗ | C-43, C-44 |

---

## Excellence Signals — V-05

**Three patterns that separate V-05 from V-01:**

### Signal 1: Defect-Analysis sub-step triples extend C-44 into defect documentation

V-05 decomposes each Defect Analysis entry into three mandatory sub-steps — Pre-Defect State, Triggering Operation, Post-Defect State+Reason — each with its own state triple. This is the tabular analog of the operation-level sub-step decomposition: every finding is now independently verifiable as a mini state trace, not just a label on a row. The C-44 threshold (≥3 sub-steps each with independent state annotation) is met at a structurally distinct site (defect log) rather than within operation blocks, which would have created format conflict with the tabular trace rows.

### Signal 2: Phase-annotated tabular state cells as C-43 native structure

V-05 embeds `[phase: Authoring]` directly inside the Starting State and Ending State cells of every trace row, declared for all three domains before the trace begins. This puts lifecycle-phase context into the core tabular structure rather than alongside it. A state name alone (`Draft`) cannot surface a phase-boundary invariant violation; `Draft [phase: Authoring]` makes the lifecycle arc visible in every row and enables the scoring of invariants that span phase boundaries. The column-header FAILS FORMAT annotation (`FAILS FORMAT: no phase label [C-36][C-43]`) makes this enforceable, not advisory.

### Signal 3: Ordering hypothesis + bridge table + per-pass defect form a self-validating circuit

C-42 names what defect class each ordering should surface. C-41's bridge table makes the inter-pass postcondition→precondition dependency explicit and traceable to specific rows. C-40's per-pass defect log then confirms or disconfirms the hypothesis empirically. Together these three form a closed loop: predict the defect class via ordering annotation → expose the dependency chain via bridge → verify the class appears in the per-pass log. Without all three, the analysis is directional but not self-validating. V-01 has all three; V-03 has C-40 and C-42 but not C-41, leaving the hypothesis verifiable by class but not by traceability chain. V-05 inherits V-01's full circuit and adds lifecycle phase granularity and defect sub-step tracing.

---

## Persistent Block

C-09 through C-16 (8 criteria) and C-38/C-39 (format-locked to step-block) remain the uncracked ceiling barriers. C-38/C-39 and the tabular format are in structural tension — satisfying C-30/C-34 (tabular analogs) in multi-pass variations that also need C-40/C-41/C-42 (multi-pass only) is the achievable path. A hybrid step-block multi-pass format that combines C-38/C-39 (step-block criterion fusion) with C-40/C-41/C-42 (multi-pass) remains untried and is the likely R17 axis.

---

```json
{"top_score": 88.6, "all_essential_pass": true, "new_patterns": ["Defect-Analysis sub-step triples — decomposing each defect entry into pre-defect/triggering-op/post-defect state triples makes each finding independently traceable at state granularity, extending C-44 into defect documentation rather than only operation blocks", "Phase-annotated tabular state cells — embedding [phase: X] directly in Starting State and Ending State cells of multi-pass tabular trace rows makes lifecycle-phase boundary violations visible in the core trace structure, enabling invariant detection across phase transitions", "Three-signal defect-class confirmation circuit — ordering hypothesis (C-42) names the expected defect class, bridge table (C-41) makes the inter-pass dependency traceable to specific rows, per-pass defect log (C-40) confirms or disconfirms the hypothesis empirically — together forming a closed self-validating loop"]}
```
