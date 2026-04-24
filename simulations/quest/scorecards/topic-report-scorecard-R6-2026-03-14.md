## Round 6 Scorecard — `topic-report`

### Summary Rankings

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-03 Inertia propagated | 5/5 | 3/3 | 14/14 | **100** | YES |
| 1 | V-04 Minimal golden | 5/5 | 3/3 | 14/14 | **100** | YES |
| 1 | V-05 Ceiling | 5/5 | 3/3 | 14/14 | **100** | YES |
| 4 | V-01 Inertia only | 5/5 | 3/3 | 13/14 | **99.3** | YES |
| 4 | V-02 Header only | 5/5 | 3/3 | 13/14 | **99.3** | YES |

---

### Per-Variation Scoring

**V-01** (C-21 YES, C-22 NO) — **99.3**
- C-01–C-21: all PASS. Full essential/recommended/aspirational foundation carries through.
- C-22 **FAIL**: No `=== THREE-LAYER WRITE POINT ===` header at SLOT 3. All three layers structurally present (C-18 PASS), but unnamed — structural convergence without named convergence.

**V-02** (C-21 NO, C-22 YES) — **99.3**
- C-01–C-20, C-22: all PASS.
- C-21 **FAIL**: SLOT 4 `[RULE NEXT-CONCRETE G-5]` names skill only. Branch B NEXT STEP has no "Leaving this open holds the topic at Not Ready." line. Skill label, not a commitment.

**Discriminator note**: V-01 and V-02 score identically. C-21 and C-22 are symmetric at design time — neither is structurally harder to satisfy alone. Live-run variance data will reveal which is the harder compliance target in practice.

**V-03** (C-21 YES, C-22 YES + persistence framing) — **100**
- All 14 aspirational criteria PASS. G-4 and G-5 at register updated to reflect stall-cost and blocking-signal obligations.
- Additional pattern beyond rubric: `[RULE G-7a COMPLETENESS]` requires "topic stays here until both are resolved" in the readiness sentence. No R6 criterion governs this. Live-run risk: G-4 calibration degrades if model appends persistence framing to the "Ready" branch when BLOCKERS is none.

**V-04** (C-21 YES, C-22 YES — minimal golden) — **100**
- All 14 PASS. C-21 added as one clause to `[RULE NEXT-CONCRETE]` with a violation example. C-22 added as a 4-line `=== THREE-LAYER WRITE POINT ===` header at SLOT 3 entry. No new phases, no new mechanisms, no Branch B structural change.

**V-05** (C-21 YES via G-9, C-22 YES with Branch B own header) — **100**
- All 14 PASS. G-9 INERTIA at the contract register makes the stall-cost invariant chain-traceable (register → `[RULE G-9 INERTIA]` → output), mirroring the G-7a/G-7b pattern. Branch B gets its own `=== THREE-LAYER WRITE POINT (BRANCH B) ===` for independent attention recovery on the `--format teams` path.
- **Golden document discrepancy noted**: The discriminator table claims "Inertia at READINESS sentence: YES" for V-05, but the actual V-05 spec does not implement it. V-03's persistence framing is absent from V-05 as written. No rubric impact; C-22 is the R6 criterion, not inertia-at-readiness.

---

### Prediction vs Actual

All 5 predictions confirmed. 5/5.

---

### Excellence Signals

1. **Violation example in [RULE NEXT-CONCRETE C-21]** (V-04): "Run /scout:feasibility (scout)." marked as `(no stall cost -- C-21 violation)` at the exact governed slot. Worked-example-as-failure-mode is more reliable than worked-example-as-correct-pattern alone.

2. **G-9 contract label for inertia invariant** (V-05): Elevating stall-cost to a named register entry (G-9 INERTIA) makes it chain-traceable at three levels without a scan step. Correct structural treatment for single-position output invariants vs. bidirectional list constraints.

3. **Branch B independent recovery point** (V-05): `=== THREE-LAYER WRITE POINT (BRANCH B) ===` self-contained header for `--format teams` execution. Model in Branch B reconstructs enforcement sequence without cross-branch lookup.

---

**All predictions confirmed. Three variations at 100 (V-03, V-04, V-05). V-04 is the R6 recommended production design. Three R7 discriminator candidates identified.**

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["G-9 contract label chaining for stall-cost invariant mirrors G-7a/G-7b pattern at register level", "Branch B independent THREE-LAYER WRITE POINT header for --format teams attention recovery"]}
```
lden**: YES

---

#### V-02 -- Explicit THREE-LAYER header only (C-21 NO, C-22 YES)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01--C-08 | All essential + recommended | PASS | Same foundation as V-01 |
| C-09--C-20 | All aspirational base | PASS | Same foundation as V-01 |
| C-21 | Inertia framing at NEXT STEP | FAIL | SLOT 4 [RULE NEXT-CONCRETE G-5] names skill only -- no stall-cost clause. Branch B NEXT STEP: "| Run /{namespace}:{skill-type} ({namespace})." with no "Leaving this open..." line |
| C-22 | Explicit THREE-LAYER WRITE POINT header | PASS | === THREE-LAYER WRITE POINT === at SLOT 3 entry with LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY + Recovery instruction |

**Aspirational**: 13/14 | **Score**: 60 + 30 + (13/14 * 10) = **99.3** | **Golden**: YES

**Discriminator note**: V-01 and V-02 isolate C-21 vs C-22. Both reach 99.3 -- neither criterion is harder than the other at design time. Live-run variance data from R6 runs will reveal whether attention-recovery (C-22) or commitment framing (C-21) is the harder live compliance target.

---

#### V-03 -- Inertia propagated to READINESS sentence (C-21 YES, C-22 YES + persistence framing)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01--C-20 | All essential + recommended + aspirational base | PASS | Full foundation; G-4 at register updated to require naming blocking signals; G-5 updated to include stall cost |
| C-21 | Inertia framing at NEXT STEP | PASS | [RULE NEXT-CONCRETE C-21] with stall-cost clause and form template; Branch B NEXT STEP carries "Leaving this open holds the topic at Not Ready." |
| C-22 | Explicit THREE-LAYER WRITE POINT header | PASS | === THREE-LAYER WRITE POINT === at SLOT 3 entry with full LAYER 1/2/3 enumeration and Recovery instruction |

**Additional pattern**: [RULE G-7a COMPLETENESS] requires persistence framing in the readiness sentence -- "topic stays here until both are resolved." No v6 rubric criterion governs this. Live-run risk: G-4 calibration degrades if the model appends persistence framing to the "Ready -- all planned signals complete." branch when BLOCKERS is none.

**Aspirational**: 14/14 | **Score**: 60 + 30 + (14/14 * 10) = **100** | **Golden**: YES

---

#### V-04 -- C-21 + C-22 combined, R6 minimal golden (C-21 YES, C-22 YES)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01--C-20 | All essential + recommended + aspirational base | PASS | G-5 at register updated: "naming the specific skill to run and the stall cost of deferring it" -- stall cost now a first-class G-5 guarantee |
| C-21 | Inertia framing at NEXT STEP | PASS | [RULE NEXT-CONCRETE C-21] at SLOT 4 with correct/violation examples; violation explicitly calls out "no stall cost -- C-21 violation"; Branch B template includes "Leaving this open holds the topic at Not Ready." |
| C-22 | Explicit THREE-LAYER WRITE POINT header | PASS | === THREE-LAYER WRITE POINT === at SLOT 3 with LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY and Recovery line; header appears before any enforcement layer is encountered |

**Design quality**: Both additions slot into V-04(R5) at minimum overhead. C-21 is a one-clause addition with a violation example. C-22 is a 4-line header block at SLOT 3 entry. No new phases, no new contract labels at register, no Branch B structural change. Cleanest 14/14 path.

**Aspirational**: 14/14 | **Score**: 60 + 30 + (14/14 * 10) = **100** | **Golden**: YES

---

#### V-05 -- Ceiling: G-9 contract label + Branch B own THREE-LAYER header (C-21 YES, C-22 YES)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01--C-20 | All essential + recommended + aspirational base | PASS | Same as V-04 |
| C-21 | Inertia framing at NEXT STEP | PASS | [RULE G-9 INERTIA] at SLOT 4 with correct/violation examples; G-9 at register makes stall-cost chain-traceable at register -> [RULE G-9 INERTIA] -> output, matching G-7a/G-7b pattern |
| C-22 | Explicit THREE-LAYER WRITE POINT header | PASS | Branch A SLOT 3: === THREE-LAYER WRITE POINT === with LAYER 1/2/3 and Recovery. Branch B Section 3: === THREE-LAYER WRITE POINT (BRANCH B) === with independent LAYER 1/2/3 and Recovery note: "re-read this Branch B header... without referencing Branch A" |

**Golden document discrepancy**: The discriminator table in the golden file lists "Inertia at READINESS sentence: YES" for V-05, but the actual V-05 spec's readiness template is "Not ready -- missing {names from LOCKED BLOCKERS list}." without persistence framing. The V-03 persistence pattern is NOT present in V-05 as written. Does not affect v6 rubric score; no R6 criterion governs inertia at readiness.

**Aspirational**: 14/14 | **Score**: 60 + 30 + (14/14 * 10) = **100** | **Golden**: YES

---

### Prediction vs Actual

| Variation | Predicted | Actual | Match? |
|-----------|-----------|--------|--------|
| V-01 | 13/14 = 99.3 | 13/14 = 99.3 | YES |
| V-02 | 13/14 = 99.3 | 13/14 = 99.3 | YES |
| V-03 | 14/14 = 100 | 14/14 = 100 | YES |
| V-04 | 14/14 = 100 | 14/14 = 100 | YES |
| V-05 | 14/14 = 100 | 14/14 = 100 | YES |

All 5 predictions confirmed. C-21 and C-22 are symmetric discriminators at design time.

---

### Excellence Signals

**From V-04 (minimal golden):**

1. **Violation example in [RULE NEXT-CONCRETE C-21]**: The annotation carries an explicit violation -- `"Run /scout:feasibility (scout)." (no stall cost -- C-21 violation)` -- making the missing pattern concrete at the exact governed position, not just the correct pattern. Worked-example-as-failure-mode is more reliable than worked-example-as-correct-pattern alone.

2. **G-5 register update for stall cost**: V-04 upgrades the G-5 register entry to include "the stall cost of deferring it." The stall-cost obligation is now at the top-level contract, not just as a [RULE] annotation at SLOT 4. Two rules govern the same slot -- [RULE NEXT-CONCRETE] for no-generic-step and [RULE NEXT-CONCRETE C-21] for stall cost -- each catching a distinct failure mode.

3. **Minimum overhead proof**: C-21 + C-22 achieve 14/14 with no new phases, no new mechanisms, no Branch B structural change. This establishes the lower bound for integrating both criteria into any existing v5 golden design.

**From V-05 (ceiling):**

4. **G-9 contract label mirrors G-7a/G-7b pattern**: Elevating the stall-cost invariant to named G-9 at the register makes it chain-traceable at three levels (register -> annotation -> output) without a scan step. Correct structural treatment for invariants governing a single output position rather than a bidirectional list constraint.

5. **Branch B independent recovery point**: === THREE-LAYER WRITE POINT (BRANCH B) === provides self-contained attention recovery for the --format teams execution path. A model entering Branch B can reconstruct the enforcement sequence without backtracking to Branch A. This addresses the highest-risk live-run failure mode for format-branched skills.

---

### R7 Discriminator Candidates

| Pattern | Source | Hypothesis |
|---------|--------|------------|
| Inertia at READINESS sentence | V-03 | Does "topic stays here until resolved" in the Not Ready sentence reduce developer ambiguity, or introduce G-4 calibration noise when BLOCKERS is empty? |
| G-9 contract label for stall cost | V-05 | Does register-level chaining for C-21 reduce live-run inertia omissions the same way G-7a/G-7b chaining reduced COMPLETENESS/EXCLUSIVITY omissions? |
| Branch B own THREE-LAYER header | V-05 | Do --format teams runs show lower C-22 compliance variance with a Branch B-local header vs Branch A header only? |

---

### Round 6 Findings

1. **C-21 and C-22 are symmetric at design time**: V-01 (13/14, misses C-22) and V-02 (13/14, misses C-21) score identically. The discriminator between them is live-run variance, not design-time analysis.

2. **V-04 is the R6 minimal golden**: C-21 + C-22 at zero new mechanism overhead over V-04(R5). Recommended production design.

3. **V-03 persistence framing is rubric-safe**: Adding "topic stays here until all are resolved" to the readiness sentence passes all C-01--C-22 criteria. Live-run risk is confined to the BLOCKERS-none edge case. Worth promoting to R7 candidate if developer-value data supports it.

4. **V-05 golden document inconsistency**: Discriminator table claims "Inertia at READINESS sentence: YES" for V-05 but the actual spec does not implement it. Documentation gap, not a rubric failure. V-05 scores 14/14 correctly without it.
