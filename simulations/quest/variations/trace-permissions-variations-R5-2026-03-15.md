Written to `simulations/quest/golden/trace-permissions-variate-R5-2026-03-16.md`.

---

## Round 5 — trace-permissions (Rubric v5)

**New criteria targeted:** C-18 (NOT POSSIBLE verdict closure mechanism citation) + C-19 (per-role escalation roll-up assertion)

### Variation map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Output format — dedicated `Closing Mechanism` column (C-18 single-axis) | Round 4 V-02 buried the mechanism hint inside the Evidence column as optional text. Splitting into four columns makes `Closing Mechanism` a distinct cell: a NOT POSSIBLE row with a blank cell is a visible format error, not a missing phrase |
| **V-02** | Role sequence — mandatory ESCALATION ROLL-UP block (C-19 single-axis) | Round 4's one-sentence "Summary for [Role]" was too loose. A named block with declared fields (`Vectors assessed:`, `POSSIBLE count:`, `NOT POSSIBLE count:`, `Mechanisms cited:`, `Composite verdict:`) makes each field independently checkable; a blank `Composite verdict:` is an incomplete block, not a missing sentence |
| **V-03** | Lifecycle emphasis — Phase 3 pre-declaration commitment (C-18 + C-19 via phase discipline) | Before tracing any vectors, each role declares exactly what it will check and commits to: (a) mechanism citations for every NOT POSSIBLE, (b) a roll-up block at the end. Phase 3 gate verifies every commitment was honored. Incompleteness is detectable at declaration time and gate time |
| **V-04** | Combined: dedicated closing mechanism column (C-18) + mandatory roll-up block (C-19) | Direct stack of V-01 + V-02 mechanics; the two failure modes are independent so the structures reinforce without overlapping |
| **V-05** | Combined: phrasing register (audit evidence standard) + inertia framing (hypothesis-per-vector) | Each vector opens with a stated design assumption; NOT POSSIBLE becomes "Assumption confirmed" requiring a cited structural basis; the ROLE ESCALATION AUDIT VERDICT provides the C-19 roll-up naturally as an audit section verdict |

**Single-axis variations:** V-01 (output format), V-02 (role sequence), V-03 (lifecycle emphasis)
**Combined variations:** V-04 (V-01 + V-02), V-05 (phrasing register + inertia framing)
