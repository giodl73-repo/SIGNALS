Written to `simulations/quest/golden/quest-golden-variate-v2-R2-2026-03-15.md`.

---

## Round 2 Variations — quest-golden against rubric v2

**Variation map:**

| V | Axis | Type | Target | Mechanism |
|---|------|------|--------|-----------|
| V-01 | output-format | single | C-11 | COMPOSITE row template forces operator to write `E=[n], R=[n], A=[n]` with resolved formula in the evidence cell — formula appears at the point of use |
| V-02 | phrasing-register | single | C-12 | IS:/IS NOT: constitutive pair at gate section header defines conflation (IS NOT: merged paragraph) and the required form (IS: two labeled sections with independent evidence) |
| V-03 | lifecycle-emphasis | single | C-11 | Mandatory "Sub-step 2b — Denominator resolution" before COMPOSITE row: operator must write `E=[n], R=[n], A=[n]` as a named blocking step; COMPOSITE cannot be filled without it |
| V-04 | output-format × phrasing-register | combination | C-11 + C-12 | V-01's resolved-formula COMPOSITE row + V-02's IS/IS NOT anti-conflation pair; two sections, two mechanisms, no overlap |
| V-05 | inertia-framing × lifecycle-emphasis | combination | C-11 + C-12 | Status-Quo Golden competitor names both failure modes upfront (motivation); V-03's denominator sub-step closes Failure 1 mechanically; two-labeled-gate structure closes Failure 2 structurally |

**Design decisions:**

- **V-01 vs V-03** test the same criterion (C-11) via different mechanisms — template anchoring vs. lifecycle forcing. If both pass, prefer V-01 (simpler). If only V-03 passes, active computation is the causal requirement.
- **V-04 is the anchor** — orthogonal sections (scoring section for C-11, gate section for C-12), detectable failure mode (if one passes and the other fails, the axis that failed must be reinforced).
- **V-05 adds motivation layer** on top of V-03's mechanics — tests whether naming failure modes upfront increases C-12 compliance beyond what the IS/IS NOT form achieves alone.
