# Scorecard: listen-adoption — Round 5

**Rubric version:** v5 (max 140, golden threshold 80)
**Variations evaluated:** V-01 through V-05
**Base scores inherited:** R4 V-04 and V-05 both scored 135/135; C-18 (5 pts) is the sole new criterion.

---

## Per-Criterion Legend

| Symbol | Meaning |
|--------|---------|
| **P** | PASS |
| **X** | FAIL |
| **~** | PARTIAL (noted where rubric does not define partial credit — treated as FAIL for scoring) |

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (12 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | All 16 stock roles mapped to Rogers archetype | P | P | P | P | P |
| C-02 | Month-by-month adoption sequence (≥3 months, no Rogers inversion) | P | P | P | P | P |
| C-03 | Chasm identification with bridging mechanism | P | P | P | P | P |
| C-04 | Interventions ranked by adoption delta (≥2) | P | P | P | P | P |
| C-05 | Champion network named (≥2 roles, rationale tied to archetype position) | P | P | P | P | P |

**Essential subtotal:** 60 / 60 all variations

Evidence note (C-01–C-05): All variations inherit Step 1 archetype table, Step 2 timeline, Step 3a/3b/3c chasm block, Step 4 churn register, and Step 5 interventions from their R4 bases. The Step 1 template explicitly requires all 16 roles; Step 2 requires Rogers-sequenced months; Step 3 requires "chasm" named with bridging mechanism; Step 4 structure contains the champion table; Step 5 requires ranked delta. No variation removes or conditionalizes any of these sections.

---

### Recommended Criteria (10 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Churn risk per archetype (≥2, trigger + mitigation) | P | P | P | P | P |
| C-07 | Spread mechanism named per transition (≥1 feature-specific) | P | P | P | P | P |
| C-08 | Tabular or structured month view | P | P | P | P | P |

**Recommended subtotal:** 30 / 30 all variations

Evidence note (C-06–C-08): Step 4 churn table is structurally required in all five prompt designs; Step 2 timeline table with spread mechanism column is inherited unchanged; Step 2 is explicitly a table by template. No variation removes these.

---

### Aspirational Criteria (5 pts each)

#### C-09 through C-12 (inherited from R4 bases)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Sensitivity analysis on chasm width (2 named scenarios, different levers) | P | P | P | P | P |
| C-10 | Feedback loop into signal readiness (≥2 measurable proceed signals) | P | P | P | P | P |
| C-11 | Named inertia per archetype (≥3 feature-specific, not attitude labels) | P | P | P | P | P |
| C-12 | No orphan or conditional sections | P | P | P | P | P |

Evidence note (C-09–C-11): Steps 6 and 7 are unconditional in all variations. Step 1 inertia ID format is explicitly required. C-12 requires careful attention: V-01 has a FAIL-path block and COMMIT CONFIRMATION block, both of which appear unconditionally in the output (they execute regardless of outcome, reporting differently). V-03 has a WRITE GATE but the gate section itself is always present; only the write instruction is conditional on the computed boolean. V-05's per-criterion revision log format always appears (REVISION LOG may be empty but the structural slot exists). None of the five variations introduce hedging language on section inclusion. All PASS C-12.

---

#### C-13 through C-15 (aspirational inertia backbone, double-anchor, action mitigations)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-13 | Named inertia as downstream backbone (cited by ID in ≥3 of 4 downstream sections) | P | P | P | P | P |
| C-14 | Champion rationale double-anchored (archetype position + named EM inertia per row) | P | P | P | P | P |
| C-15 | Churn mitigations are concrete actions, not surveillance-only | P | P | P | P | P |

Evidence note (C-13): Step 5.5 Propagation Ledger is the structural verification mechanism in all variations (inherited from R4 V-04/V-05 bases). It requires 4-row table with explicit inertia ID lists and a total, with a revision gate if total < 3. This gate appeared in R4 and is retained in all R5 variations. Step 3a explicitly requires citing EM inertia IDs; Step 3c champion table column 4 (EM Inertia Bridged) requires explicit ID; Step 4 churn trigger column uses "reverts to [I-xx]" format; Step 5 requires inertia ID column per intervention row.

Evidence note (C-14): Champion table column 4 ("EM Inertia Bridged: ID + named inertia") is a structural requirement inherited from R4 V-04/V-05. The template reads "Well-placed to influence the early majority without naming the inertia ID fails the fourth column even if column 3 passes." Both column 3 (archetype bridge rationale) and column 4 (EM inertia ID) are present as independent columns.

Evidence note (C-15): Step 4 mitigation column explicitly names action verbs (assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, escalate) and explicitly disallows surveillance-only verbs (monitor, track, watch, observe, measure). Inherited from R4 bases, retained in all R5 variations.

---

#### C-16 through C-18 (self-audit and revision obligation)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-16 | Self-audit pre-commit naming C-13, C-14, C-15 with criterion-specific checks | P | P | P | P | P |
| C-17 | Dedicated structural slot per aspirational criterion (C-13, C-14, C-15 each distinct) | P | P | P | P | P |
| C-18 | Revision obligation on self-audit deficiency | P | P | P | P | P |

---

**Detailed C-16 / C-17 / C-18 evidence per variation:**

---

**V-01 — Re-run mandate in Pre-Commit FAIL path**

- **C-16:** PASS. Inherits Pre-Commit audit block naming C-13, C-14, C-15 with criterion-specific pass conditions from V-04 base. Each check states the exact pass condition and produces a PASS/FAIL result label.
- **C-17:** PASS. Three distinct structural elements: (a) Step 5.5 Propagation Ledger for C-13 — a standalone table with its own header, explicitly prohibited from merging with champion table; (b) Step 3c champion table column 4 for C-14; (c) Step 4 churn table mitigation column for C-15. No two of the three share a parent block.
- **C-18:** PASS. The mechanism upgrades the FAIL path to two mandatory phases: Phase 1 produces an initial PASS/FAIL result; Phase 2 (triggered only on FAIL) requires the model to state which sections were revised and re-run the check, with the re-run showing PASS before the model can proceed to the COMMIT CONFIRMATION. The COMMIT CONFIRMATION block explicitly asks whether any revision occurred and requires all three final results to be PASS. A deficiency flagged in Phase 1 that is not corrected before COMMIT CONFIRMATION violates the structured format — the commit confirmation block cannot show PASS on a criterion whose Phase 1 showed FAIL unless the revision was executed. The correction transaction is structurally required to appear in the output. Evaluability: medium-high. An evaluator can check the COMMIT CONFIRMATION for revision history.

---

**V-02 — Behavioral contract header before SECTION A**

- **C-16:** PASS. Inherits criterion-specific audit block from V-05 base (which scored 135/135 on C-16 in R4).
- **C-17:** PASS. Inherits three distinct structural elements from V-05 base: Propagation Ledger (C-13), champion table column 4 (C-14), churn table action column (C-15).
- **C-18:** PASS — with the weakest structural guarantee among the five variations. The behavioral contract header makes the revision obligation visible before any content is produced, reducing the probability that a model rationalizes a deficiency as "close enough." However, the mechanism is framing-based rather than structural: the model sees the rule, names it in the audit block, and is expected to comply. A model that finds a deficiency in C-14 and writes the artifact anyway satisfies C-16 (audit exists, names criteria) but fails C-18. The behavioral contract increases compliance by anchoring the obligation in the opening terms — but it does not create a structural branch that forces the correction transaction to appear in the output. C-18 passes because the expected model behavior is to comply with the explicit stated obligation, but evaluators have lower surface to verify the correction (no dedicated SECTION K, no revision log format). Evaluability: lowest of the five.

---

**V-03 — Conditional WRITE GATE replaces terminal write instruction**

- **C-16:** PASS. Inherits criterion-specific audit block from V-04 base.
- **C-17:** PASS. Inherits three distinct structural elements from V-04 base.
- **C-18:** PASS. The WRITE GATE computes a COMMIT READY boolean. If NO, the model receives a revision directive rather than a write instruction — structurally, the model cannot proceed to write the artifact until COMMIT READY = YES. This creates a branching gate: a deficiency flagged in the audit that sets COMMIT READY = NO forces the model into a revision loop before any artifact is written. The correction must occur (the write instruction only fires when COMMIT READY = YES). The mechanism closes the gap from R4 where the FAIL path said "revise before proceeding" but the model could rationalize a marginal FAIL as sufficient. C-18 passes because the write gate structurally prevents committing an unrevised artifact. Evaluability: medium. The COMMIT READY = YES / NO toggle is visible in the output, but the correction transaction itself may not be logged in detail — only the final state is confirmed. An evaluator can verify the gate result but may not see what was changed.

---

**V-04 — SECTION K meta-gate tracking initial/final state**

- **C-16:** PASS. Inherits criterion-specific audit block from V-05 base. SECTION K supplements it by recording initial and final gate states per criterion.
- **C-17:** PASS. Three distinct structural elements: (a) Step 5.5 Propagation Ledger for C-13; (b) Step 3c champion table column 4 for C-14; (c) Step 4 churn table mitigation column for C-15. Additionally, SECTION K is a fourth, independently named structural element covering C-18 — the C-17 criteria are assessed before SECTION K appears, so SECTION K does not merge evidence for C-13/C-14/C-15; it only records their gate state. C-17 is satisfied by the three pre-SECTION K slots.
- **C-18:** PASS — strongest evaluability. SECTION K records: initial gate result (H/I/J = PASS or FAIL), whether a revision was executed, and final gate result. The behavioral commitment in SECTION K is explicit: "if initial result is FAIL and no revision entry appears, this artifact is incomplete." An evaluator checking C-18 goes directly to SECTION K without tracing individual gate histories — the correction transaction (or its absence) is reported in a single, named, independently identifiable structural location. Satisfies the C-18 pass condition through both the trivial path (all initial results PASS, SECTION K confirms no revision needed) and the revision path (SECTION K shows initial FAIL + revision description + final PASS). Evaluability: highest — SECTION K is a dedicated, evaluator-accessible verification point.

---

**V-05 — Per-criterion revision log format + conditional write gate**

- **C-16:** PASS. Inherits criterion-specific audit from V-04 base. Per-criterion revision log adds structured format: INITIAL RUN → REVISION LOG → RE-RUN → FINAL RESULT per criterion.
- **C-17:** PASS. Three distinct structural elements inherited: Propagation Ledger (C-13), champion table column 4 (C-14), churn table action column (C-15). The per-criterion revision log is a parallel verification structure for C-18, not a merged slot for C-13/C-14/C-15.
- **C-18:** PASS — second-highest evaluability. The per-criterion revision log makes the correction transaction visible *per criterion*: the format requires INITIAL RUN to state the check result, REVISION LOG to describe what was changed if a deficiency was found, RE-RUN to confirm the corrected version satisfies the pass condition, and FINAL RESULT to record the gate outcome. A model cannot populate FINAL RESULT = PASS without either showing INITIAL RUN = PASS (trivial) or showing REVISION LOG + RE-RUN (correction evidence). The conditional write gate additionally blocks commit until all three final results are PASS. Combined, V-05 provides both per-criterion transaction logs and a write gate. Evaluability: very high — correction transactions are visible per criterion. Slight edge goes to V-04 because SECTION K provides a single named structural location (evaluator scans one place); V-05 distributes revision evidence across three per-criterion sub-blocks, requiring the evaluator to check each one.

---

## Composite Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-02 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-03 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-04 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-05 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-06 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-08 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-09 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-11 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-13 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-14 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-15 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-16 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-17 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-18 | 5 | 5 | 5 | 5 | 5 | 5 |
| **Total** | **140** | **140** | **140** | **140** | **140** | **140** |

All five variations pass all 18 criteria. All essential criteria pass. All scores reach the maximum of 140.

---

## Ranking

All variations tie at 140. Within-score ordering by C-18 evaluability robustness (how easily an evaluator can verify the correction obligation was met):

| Rank | Variation | C-18 Mechanism | Evaluability |
|------|-----------|---------------|-------------|
| 1 | **V-04** | SECTION K meta-gate — single named location records initial/final state per criterion | Highest: one section to check |
| 2 | **V-05** | Per-criterion revision log — INITIAL RUN → REVISION LOG → RE-RUN per criterion + write gate | Very high: transaction visible per criterion, distributed across three sub-blocks |
| 3 | **V-01** | FAIL-path re-run mandate + COMMIT CONFIRMATION — re-run must show PASS before commit | Medium-high: COMMIT CONFIRMATION is checkable; correction evidence present if revision occurred |
| 4 | **V-03** | Conditional WRITE GATE — COMMIT READY boolean gates write instruction | Medium: gate result visible, correction transaction not logged in detail |
| 5 | **V-02** | Behavioral contract header — framing-based obligation, no structural gate | Lowest: reliant on model compliance with stated rule; correction transaction not structurally required in output |

---

## Excellence Signals

**From V-04 (top-ranked):**

1. **Meta-gate section as evaluator shortcut.** SECTION K consolidates initial/final gate states for all three aspirational check criteria into a single named structural location. An evaluator checking C-18 does not need to trace individual gate histories — they go to SECTION K. This pattern (dedicated summary gate section) is more robust than per-criterion logging because it provides one failure point: if SECTION K is absent or incomplete, C-18 fails cleanly.

2. **Behavioral commitment recorded in the section itself.** SECTION K's explicit "if initial result is FAIL and no revision entry appears, this artifact is incomplete" statement makes the obligation visible at the point of evaluation, not just at the point of writing. This reduces rationalization by anchoring the rule in the structural slot an evaluator inspects.

3. **Separation of gate state from content sections.** By recording gate state in SECTION K (a trailing section) rather than inline with content, V-04 prevents the common failure mode of a model conflating the audit check with the content it's checking — the structural separation enforces independence.

**From V-05:**

4. **Per-criterion revision log format.** The INITIAL RUN → REVISION LOG → RE-RUN → FINAL RESULT format makes the correction transaction visible and required by format. A model cannot skip the revision log for a failing criterion — the format requires it. This pattern is reusable as a general aspirational criterion verification template.

5. **Conditional write gate + per-criterion log combination.** V-05 combines two independent enforcement mechanisms: the revision log ensures the correction is documented, and the write gate ensures the artifact is not written before the correction. Neither mechanism alone is sufficient (a model could log a FAIL and still write; a model could pass the gate without logging the correction). The combination makes both gaps simultaneously harder to exploit.

**Pattern that distinguishes the top two from the bottom three:**

The distinguishing property of V-04 and V-05 over V-01/V-03/V-02 is **structural evidence of the correction transaction in the output.** V-01's COMMIT CONFIRMATION records whether revision occurred but not what changed. V-03's WRITE GATE records the boolean outcome but not the correction. V-02's behavioral contract records the obligation but not its execution. V-04 and V-05 require the *content* of the revision to appear in the output — not just the fact that a revision occurred. This makes C-18 evaluable against the artifact alone, without requiring trust in the model's self-reported compliance.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["Meta-gate section pattern: dedicated trailing section records initial/final gate states for all aspirational audit criteria in a single named structural location, enabling one-section C-18 verification without tracing individual gate histories", "Per-criterion revision log: INITIAL RUN -> REVISION LOG -> RE-RUN -> FINAL RESULT format makes the correction transaction visible and structurally required per criterion, preventing silent commit after flagged deficiency", "Conditional WRITE GATE: replacing the write instruction with a COMMIT READY boolean structurally branches the model into a revision loop when a deficiency is present, preventing artifact write before correction", "Correction transaction content requirement: top-ranked variations require the *content* of the revision to appear in the output, not just the fact that revision occurred -- enabling C-18 evaluation against the artifact alone without trusting model self-report"]}
```
