Written to:
- `simulations/quest/golden/campaign-evidence-variate-R5-2026-03-16.md`
- `simulations/quest/variations/campaign-evidence-variations-R5-2026-03-16.md`

---

**What R5 does and why:**

R5's two new criteria both trace back to R4 V-04 — the 100-point gold standard. But V-04 has a latent defect:

**C-18 (peer tier parity)**: SEQUENCING RULE in R4 V-04 contains "This is a declared governance rule — not an unnamed structural convention." The other three rules make no such claim about themselves. Under the C-18 test (remove all rule labels — if prose treats any rule differently, parity is absent), R4 V-04 *fails*. This is the defect C-18 was designed to encode.

**C-17 (prospective commitment)**: R4 V-04's coverage map is placed before Stage 1, which satisfies C-17 structurally. The question is whether *explicit* pre-execution lock language adds anything over placement.

**Variation design:**

| Variation | Axis | C-17 mechanism | C-18 mechanism | Expected score |
|-----------|------|----------------|----------------|----------------|
| V-01 | C-18 single | Placement (structural) | Strip SEQUENCING meta-commentary | 100 |
| V-02 | C-17 single | Explicit temporal lock | Intentional miss (control) | 99 |
| V-03 | C-17 inline | Rule-embedded annotations | Uniform annotation format | 100 |
| V-04 | Combined | Explicit lock | Prose parity | 100 |
| V-05 | Full stack | Inline + lock + audit | Uniform annotations | 100 |

The key diagnostic: V-01 vs V-02 on C-17 — does placement before Stage 1 satisfy the criterion, or does the semantic commitment declaration matter?
C-17 via placement only.

---

### V-02 — Single axis: C-17 (explicit pre-execution temporal lock)

**Hypothesis**: Explicit "finalized before Stage 1 begins / cannot be modified after
any stage executes" language in the coverage map header makes the prospective intent
unmistakable. Tests whether semantic declaration adds value over structural placement
for C-17 compliance.

SEQUENCING RULE retains R4 V-04 meta-commentary (intentional C-18 miss — control
variation). Coverage map block renamed "PRE-EXECUTION RULE COVERAGE COMMITMENT" with
explicit temporal lock text.

**Targets**: C-01–C-17. **Intentional miss**: C-18. **Diagnostic**: gap between
V-01 and V-02 on C-17 calibrates whether placement (V-01) or explicit lock (V-02)
is load-bearing.

---

### V-03 — Single axis: C-17 via inline coverage annotations

**Hypothesis**: Stage applicability embedded in each rule annotation — "CALIBRATION
RULE [invoked at: Stage 4, Stage 5]" — satisfies C-17 via a mechanism that makes
the commitment inseparable from reading the rule. A model cannot encounter the rule
without also reading its applicability scope. Also addresses C-18 via uniform
annotation format across all four rules (no rule receives special treatment).

No separate RULE COVERAGE MAP block. Coverage committed through rule annotations
before Stage 1.

**Targets**: C-01–C-18. **Risk**: C-16 zero-gap invocation relies entirely on
per-stage invocation tags without a separate map for cross-reference.

---

### V-04 — Combined: C-18 prose parity + C-17 explicit lock

**Hypothesis**: V-01's prose parity fix + V-02's temporal lock language are mutually
reinforcing. The coverage map is declared as a pre-execution commitment (C-17 semantic
strength), and all four rules make behavioral demands in the same prose register
(C-18 parity). Cleanest full-18-criteria design with no redundant mechanism.

**Targets**: C-01–C-18 (all). **Risk**: Preventive only — no retrospective loop.

---

### V-05 — Full stack: inline annotations + explicit lock + dual enforcement + inertia

**Hypothesis**: Combining inline annotations (C-17 inseparable from rule reading) with
an explicit "cannot be modified retroactively" lock and a retrospective audit table
creates triple C-17 enforcement. All four rules receive uniform annotation format
(C-18). Inertia framing adds decision-trajectory depth above the criteria ceiling.

**Targets**: C-01–C-18 (all), with structural depth on C-04, C-08, and C-17 via
dual enforcement + inertia.

---

### Predicted leaderboard

| Rank | Variation | Criteria | Key advantage |
|------|-----------|----------|---------------|
| 1 | V-05 | 18/18 + depth | Triple C-17 enforcement + inertia |
| 2 | V-04 | 18/18 | Cleanest C-17+C-18 combination, no overhead |
| 3 | V-03 | 18/18 | Inline mechanism — smaller prompt, C-17 inseparable |
| 4 | V-01 | 18/18 | Minimal R4→R5 delta — tests prose parity alone |
| 5 | V-02 | 17/18 | C-18 intentional miss — control for C-17 isolation |

**Diagnostic value**: V-01 vs V-02 on C-17: does placement satisfy C-17, or does
explicit lock language add measurable value? V-03 vs V-04 on C-16/C-17: is the
separate map block necessary for zero-gap invocation checking, or do inline
annotations carry the same structural weight?
