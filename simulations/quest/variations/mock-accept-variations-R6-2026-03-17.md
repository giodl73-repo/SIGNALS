Written to `simulations/quest/golden/mock-accept-variate-R6-2026-03-17.md`.

---

## mock-accept Variate — Round 6 Summary

**Baseline:** R5 V-04 (18/20 against v6 — has C-23 Standing Rule halt, C-24 gate traceability, C-25/C-28 Slot 2 table; missing C-26 halt co-location and C-27 dedicated GATE F step)

**Axis-Assignment Plan:**

| Plan | Axis | Target | Predicted |
|------|------|--------|-----------|
| V-01 | lifecycle-emphasis | C-27 | GATE F promoted to standalone STEP 9, separate from Write call | 19/20 |
| V-02 | output-format | C-26 | Three-step HALT appended to every CONSTRAINT block; GATE F stays in STEP 8 | 19/20 |
| V-03 | inertia-framing | C-29 candidate | DEFAULT DECISION POSITION block + Cost-of-MOCK field; full V-05 base | 20/20 + signal |
| V-04 | lifecycle + output-format | C-26 + C-27 | V-01 STEP 9 + V-02 halt co-location; closes both V-04 gaps | **100.0** |
| V-05 | lifecycle + output-format + inertia-framing | C-26 + C-27 + C-29 | Full combination | **100.0 or rubric-update trigger** |

**Key structural differences per variation:**

- **V-01 vs V-02 independence test**: V-01 has `STEP 9 — GATE F COMPLETENESS CHECK` as its own step (C-27) but no HALT at CONSTRAINT sites. V-02 has HALT at every CONSTRAINT block (C-26) but GATE F embedded in STEP 8. Confirms the two criteria are independently achievable.

- **V-03 new axis**: Introduces `DEFAULT DECISION POSITION` block before STEP 1 and a `Cost-of-MOCK:` field on every MOCK-ACCEPTED evaluation record — a structural candidate for C-29.

- **V-04 minimal path**: Exactly the two single-axis changes needed to close the V-04 gap. No extra overhead. The tightest 100-point path.

- **V-05 golden candidate**: V-04 + inertia framing. If `Cost-of-MOCK:` appears as a distinct output field structurally separate from Slot 2, it triggers a v7 rubric update with C-29.
