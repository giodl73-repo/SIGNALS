Written to `simulations/quest/variations/campaign-brief-variations-R17-2026-03-17.md`.

---

# Variations -- campaign-brief / Round 17

**R16 recap:** V-01/V-02/V-03 confirmed the three C-35 PARTIAL bands. V-04 confirmed C-35 PASS minimum-sufficient (350/350). V-05 (350/350 + above-ceiling) extended the absent-state rule to declare the absent companion's mandate as "independently operative," which was extracted as C-36.

**R17 rubric:** v16, 36 criteria, 360 pts max. Sole new criterion: C-36.

---

## Variation summary

| Var | Axis | C-35 | C-36 | Expected |
|-----|------|------|------|----------|
| V-01 | C-36 PARTIAL Band 1 — absent-state bounded to single-clause authority (R16 V-04 verbatim) | PASS | PARTIAL | 350/360 |
| V-02 | C-36 PARTIAL Band 2 — companion mandate "structurally valid," operative status absent | PASS | PARTIAL | 350/360 |
| V-03 | C-36 PARTIAL Band 3 — companion mandate operative but conditionally scoped ("where it intersects with this clause's execution") | PASS | PARTIAL | 350/360 |
| V-04 | C-36 PASS minimum-sufficient — R16 V-05 verbatim ("independently operative -- the companion mandate is in effect even when its execution note is not present in this context") | PASS | PASS | 360/360 |
| V-05 | C-36 PASS + explicit obligation-honoring instruction naming the companion's specific requirements (R17 investigation probe) | PASS | PASS | 360/360 + above-ceiling |

---

## C-36 PARTIAL band structure (three bands)

| Band | Variation | What the absent-state rule says about the companion's mandate | Gap |
|------|-----------|--------------------------------------------------------------|-----|
| 1 | V-01 | Nothing — single-clause authority only; companion mandate not addressed | Mandate operability entirely open |
| 2 | V-02 | "Structurally valid part of the contract; validity not revoked" | Valid != operative; no behavioral claim |
| 3 | V-03 | "Operative where it intersects with this clause's execution" | Scoped/conditional operative; model must determine intersection |

---

## R17 investigation framing

The single-axis isolation across all five variations is the **absent-state rule depth** in the companion execution-note clause bodies. Everything above the execution notes is identical across all variations.

**R17 behavioral investigation (V-04 vs V-05 under double-elision):**
- V-04: declares companion's mandate "independently operative -- the companion mandate is in effect" without naming specific obligations → model may acknowledge operative status without executing obligations
- V-05: adds "honor the companion's [X] obligations: [specific requirement]" → model receives obligation specification that may drive actual execution output

The probe question: does a model encountering only the STORY clause body under simulated double-elision (STATUS execution note absent, preamble absent) produce per-signal-date-isolated output in `found` because V-05 explicitly named that timestamp isolation obligation -- vs V-04 whose mandate is declared operative but whose specific requirements were not restated? This is the distinction between declarative operative status and imperative obligation specification.
