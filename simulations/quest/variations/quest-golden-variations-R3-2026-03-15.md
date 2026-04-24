Here are the 5 Round 3 variations for `quest-golden` against rubric v2.

---

## Round 3 Variation Map

| V | Axis | Type | Target | Key Change |
|---|------|------|--------|------------|
| V-01 | output-format | single | C-11 | Phase 0 counts criteria per tier; formula in Step 2 requires concrete denominators substituted + arithmetic shown inline |
| V-02 | phrasing-register | single | C-12 | Dual-gate section restructured as two labeled blocks with explicit anti-conflation prohibition per gate |
| V-03 | inertia-framing | single | C-12 | Status-Quo Scorer named as competitor; each scorecard must pass the "anti-conflation test" and record a "beats SQS because..." statement |
| V-04 | output-format x phrasing-register | combo (P1) | C-11 + C-12 | V-01 inline formula + V-02 gate labels — targets both gaps simultaneously via non-overlapping mechanisms |
| V-05 | lifecycle-emphasis x output-format | combo (P2) | C-11 + C-12 | Scoring split into PHASE A (verdicts + formula resolution) and PHASE B (threshold evaluation) — lifecycle separation reinforces both formula resolution and anti-conflation |

---

**Variation axis analysis:**

- **V-01 vs V-02**: The two gaps are structurally independent — a scorecard can have concrete denominators (C-11 PASS) while still conflating the gates (C-12 FAIL), or vice versa. Single-axis variations should be evaluated independently.

- **V-03 vs V-02**: Both target C-12, but by different mechanisms. V-02 uses structural prohibition language; V-03 uses competitive framing that requires the anti-conflation distinction to be argued. If V-03 achieves C-12 PASS at a lower structural cost than V-02, the framing-first approach is preferable for the golden prompt.

- **V-04 priority**: V-01's Phase 0 count block and V-02's gate labels operate in adjacent non-overlapping sections of the scoring block. Combination adds no redundancy.

- **V-05 rationale**: The lifecycle split means formula resolution (Step 2A) must be complete before threshold evaluation begins (Step 2B). This creates a temporal dependency that prevents the formula from being copied symbolically — it has to be resolved in the step that precedes the gate. The phase boundary also makes anti-conflation natural: the two gates already inhabit separate structural sections.

**Anchor:** V-01. Detectable failure condition: Phase 0 declares `N_e = 5` but the formula still shows `/ N_essential` — a visible mechanical inconsistency auditable without prose evaluation.

Written to: `simulations/quest/golden/quest-golden-variate-R3-2026-03-16.md`
