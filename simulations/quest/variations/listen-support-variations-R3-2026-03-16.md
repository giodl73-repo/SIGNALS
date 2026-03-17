Written to `simulations/quest/golden/listen-support-variate-R3-2026-03-16.md`.

---

## R3 Variations — listen-support

### Variation axes (3 single-axis, then combined)

| ID | Axis | Rubric target | Core change |
|----|------|--------------|-------------|
| **V-01** | Output format (card template) | C-14 | `Title:` promoted from markdown heading to explicit named field; `Phase:` kept on metadata line; STEP 9 checks both fields coexist on every card |
| **V-02** | Lifecycle emphasis (mechanical severity) | C-15 | STEP 2 "severity norm" language removed; replaced with day-window lookup table (`Phase 1 → P2/P3`, `Phase 2 → P1/P2`, `Phase 3 → P0/P1`); no override path; STEP 9 adds mechanical compliance check |
| **V-03** | Inertia framing (prior-tool citation) | C-16 | STEP 1B gains `Prior tool exact name:` field; vocab table gains `Prior-tool ref?` column; STEP 9 adds 4th check: count of bodies naming prior tool by exact string, PASS (>= 2) / FAIL |
| **V-04** | Output format + lifecycle | C-14 + C-15 | V-01 + V-02 combined; the `Phase:` named field becomes the lookup key for the severity table — the two fixes share a structural anchor |
| **V-05** | Full synthesis (R3 golden candidate) | C-14 + C-15 + C-16 | V-01 + V-02 + V-03; STEP 9 gains a dedicated **Pass 3** block covering all three R3 criteria |

### Structural insight

The R2 regression had a displacement shape: adding Phase evicted Title (or vice versa) because both were competing for the same syntactic position in the `## T-NN — {Title}` header. The fix isn't just adding both fields — it's **separating Title from the heading entirely**, so the T-NN ID and the descriptive subject line are structurally distinct. V-04 adds a second benefit: the `Phase: Phase N (day X-Y)` named field is now the input to the severity lookup, making C-15 enforcement visible at the card level.

**Expected V-05 composite:** 130/130 — ceiling on the v3 rubric.
