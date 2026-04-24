`simulations/quest/golden/flow-throttle-variate-R11-2026-03-16.md` written.

---

## flow-throttle Variate — Round 11

**Rubric:** v11 (C-01–C-32) | **Max composite:** 210

### State Analysis

R10 V-05 under v11 scores **195/210** — C-32 already passes (escape-route demolisher is present), but three criteria are open:

| Gap | Root cause |
|-----|------------|
| **C-29** FAIL | Inertia annotation is unstructured prose, not C-18/C-26 labeled-field form |
| **C-30** FAIL | Depends on C-29's labeled annotation form; examples exist in prose but are not anchored to the labeled structure |
| **C-31** FAIL | Audit paths use general scan language ("scan for a named gate step") rather than artifact-identifier + structural-position observables |
| **C-32** PASS | Escape-route demolisher in R10 V-05 explicitly rebuts the C-22-redundancy argument; carries free |

### Variation Map

| V | Axes | C-29 | C-30 | C-31 | C-32 | Predicted |
|---|------|------|------|------|------|-----------|
| V-01 | Inertia framing: C-29 FAIL isolation (R10 V-05 prose baseline carry) | FAIL | FAIL | FAIL | PASS | 195/210 |
| V-02 | Inertia framing: C-29 minimal — two labeled fields, no example | PASS | FAIL | FAIL | PASS | 200/210 |
| V-03 | Lifecycle emphasis: C-31 named-observable audit paths (prose inertia baseline) | FAIL | FAIL | PASS | PASS | 200/210 |
| V-04 | Inertia framing + Lifecycle emphasis: three-field labeled annotation + named-observable audit paths | PASS | PASS | PASS | PASS | 210/210 |
| V-05 | Role sequence + all axes: three-role pipeline + three-field C-29 + named-observable C-31 | PASS | PASS | PASS | PASS | 210/210 |

### Single-axis questions

- **Q1 (V-01 vs V-02):** Does the labeled-field structure alone (without example) satisfy C-29 minimum pass? Two fields vs. prose paragraph — same content, different form.
- **Q2 (V-01 vs V-03):** Does artifact-ID anchoring satisfy C-31 independently of the inertia framing change? The five named observables (section header, three Y/N verdict lines, gate decision line, MR-01 anchor) are orthogonal to Section B.
- **Q3 (V-04 vs V-05):** Does the three-role pipeline produce architectural enforcement V-04's instructions cannot? Role 1's `FORMAT CONTRACT COMPLETE` exit condition closes the register before the Domain Expert can encounter an unregistered element type.

### Key structural changes per variation

**C-29/C-30 upgrade (V-02: two fields; V-04/V-05: three fields)** — Section B inertia annotation restructured from prose into labeled fields: `Failure mode prevented` / `Gap above C-25` / `Concrete example`. V-04/V-05's third field names "FLAT-LOAD: within nominal band" as the concrete unregistered type and traces the full classification ambiguity under open vs. closed register.

**C-31 upgrade (V-03/V-04/V-05)** — TYPE SCAN GATE audit test replaced with five named observables: (1) `TYPE SCAN GATE` section header at structural position after last R-NN row; (2–4) `Burst/Cascade/RetryAfter: [Y / N]` verdict lines; (5) `PROCEED/BLOCKED` gate decision line before MR-01. Gate-absent signature: no `[Category]: [Y / N]` lines between R-NN and MR-01.
