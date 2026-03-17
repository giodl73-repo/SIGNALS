Written to `simulations/quest/golden/campaign-evidence-variate-R4-2026-03-16.md`.

---

## Variations — campaign-evidence / Round 4

**What R4 adds**: C-15 requires SEQUENCING to be a **named rule** in the preamble rule block (same tier as CALIBRATION, FALSIFICATION, ATTRIBUTION), not an unnamed convention or narrative principle. C-16 requires **zero-gap invocation**: every declared rule at every applicable stage — ATTRIBUTION at evidence-gathering stages, CALIBRATION at analysis + synthesis, FALSIFICATION at hypothesis + synthesis, SEQUENCING at all stages whose ordering it governs.

---

### V-01 — Single axis: C-15 (SEQUENCING as formal named rule)

**Hypothesis**: The minimal change that crosses C-15 is placement — moving SEQUENCING from a structural label to the preamble rule block at the same tier as the other three rules. Tests whether naming and placement alone produce behavioral change, or whether C-15 is purely a criterion about document structure.

Complete prompt with 4 named rules (CALIBRATION, FALSIFICATION, ATTRIBUTION, **SEQUENCING RULE**) in the preamble. Evidence-first ordering. SEQUENCING RULE invoked at Stages 1, 2, 3, and 5. All other R3 V-04 machinery preserved.

**Targets**: C-01–C-16. **Risk**: No coverage map — C-16 compliance is still behavioral.

---

### V-02 — Single axis: C-16 via pre-declared coverage matrix (hypothesis-first)

**Hypothesis**: A coverage matrix pre-declared before Stage 1 — specifying which rules apply at which stages — makes zero-gap invocation a verifiable contract. Gaps become visible violations. Tests C-16 independently of C-15 (no SEQUENCING RULE, no evidence-first).

Coverage matrix:
```
| Rule               | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
| CALIBRATION RULE   | —       | —       | —       | invoke  | invoke  |
| FALSIFICATION RULE | invoke  | —       | —       | —       | invoke  |
| ATTRIBUTION RULE   | —       | invoke  | invoke  | —       | invoke  |
| EVIDENCE RULE      | —       | invoke  | invoke  | —       | —       |
```

**Targets**: C-01–C-13, C-16. **Intentional misses**: C-10, C-14, C-15. **Risk**: Map enforcement is still behavioral — model may skip the header.

---

### V-03 — Single axis: Output format (post-brief invocation audit table)

**Hypothesis**: A retrospective audit table — required after Stage 5 — makes C-16 gaps visible as blank cells and forces correction before submission. Differs from V-02 (preventive map) in causality: this is retrospective verification. Tests whether self-checking after the fact is sufficient on its own.

Stage prompts say "apply all rules that govern this stage; mark with [RULE_NAME invoked]." After the brief, the model fills an audit table with expected pattern (`CALIBRATION at 4, 5 | FALSIFICATION at 1, 5 | ATTRIBUTION at 2, 3, 5 | EVIDENCE RULE at 2, 3`). Blank cells require correction.

**Targets**: C-01–C-13, C-16. **Intentional misses**: C-10, C-14, C-15. **Risk**: Audit may be filled performatively rather than by verification.

---

### V-04 — Combined: C-15 + C-16 (SEQUENCING as named rule + coverage matrix)

**Hypothesis**: C-15 provides the rule identifier; C-16's coverage map enforces that SEQUENCING RULE is invoked at every governed stage, not merely declared. Without C-15, the map has no SEQUENCING row. Without the map, SEQUENCING RULE may be declared but invoked only at synthesis. The combination is mutually reinforcing. C-14 rationale encoded at Stage 3 and synthesis.

Four rules in preamble including SEQUENCING RULE. Coverage matrix with SEQUENCING at Stages 1, 2, 3, 5. Evidence-first ordering. Per-stage invocations matching the map exactly.

**Targets**: C-01–C-16 (all). **Risk**: Preventive only — no retrospective audit loop.

---

### V-05 — Full stack: All 16 criteria + inertia framing + dual enforcement

**Hypothesis**: Combining preventive (coverage map) and retrospective (audit table) mechanisms for C-16 — plus SEQUENCING RULE (C-15), evidence-first (C-10), reordering rationale (C-14), and inertia framing — makes every criterion either structurally enforced or self-checked. No criterion relies solely on the model following a prose instruction.

Adds an INERTIA POSITION at the top, an inertia column in the findings table, an inertia verdict section, and a post-brief RULE INVOCATION AUDIT table. Dual enforcement: coverage map (before Stage 1) + audit table (after Stage 5).

**Targets**: C-01–C-16 (all), with independent structural depth on C-04 and C-08 via inertia framing. **Risk**: Longest variation; audit may be performative; inertia position must be carried through all stages.

---

### Predicted leaderboard

| Rank | Variation | Criteria | Key advantage |
|------|-----------|----------|---------------|
| 1 | V-05 | 16/16 + depth | Dual C-16 enforcement + inertia framing |
| 2 | V-04 | 16/16 | Cleanest C-15 + C-16 combination, no audit overhead |
| 3 | V-01 | 16/16 | Minimal R3→R4 delta — tests whether formal declaration alone is sufficient |
| 4 | V-03 | 11/16 | Retrospective audit isolated |
| 5 | V-02 | 11/16 | Preventive map isolated |

**Diagnostic value**: If V-02 and V-03 score close to V-04, C-16 mechanisms work independently of SEQUENCING RULE — the coverage tools do the work. If V-02 and V-03 score close to V-01, the formal rule declaration is the dominant intervention, not the enforcement mechanisms.
