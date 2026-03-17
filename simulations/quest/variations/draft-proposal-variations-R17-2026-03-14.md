Written to `simulations/quest/golden/draft-proposal-variate-R17-2026-03-15.md`.

---

# draft-proposal Variate — Round 17

**Rubric**: v17 · Formula: `(E/4×60) + (R/3×30) + (A/36×10)` · 43 trigger rows · New criteria: C-42, C-43

---

## Summary

| Variation | Axis | Designed fail | Cascade? | Predicted score |
|-----------|------|---------------|----------|-----------------|
| V-01 | Lifecycle emphasis | C-42 → C-43 | Yes (invariant) | 99.44 |
| V-02 | Output format | C-43 only | No | 99.72 |
| V-03 | Phrasing register | C-41 only | No | 99.72 |
| V-04 | Lifecycle + Role sequence | C-42, C-43, C-46 | C-42→C-43; C-46 independent | 99.17 |
| V-05 | Role sequence + cascade | C-23, C-26, C-31..C-43 | Full chain | 95.83 |

---

## V-01 — C-42→C-43 Cascade | Lifecycle Emphasis | T-40 CONDITION Abstract

**Axis**: AMENDMENT TABLE SPECIFICATION includes T-40 with its trigger description (`fires if Domain 2 per-column enumeration lacks "Risk row:" anchor`) but provides no guidance about T-40 CONDITION content.

**Hypothesis**: Without CONDITION content guidance, an LLM writes T-40 CONDITION as an abstract restatement of the trigger text — naming the deficiency category without quoting a deficient T-38 CONDITION form. T-42 fires (C-42 FAIL) → T-43 cascades (C-43 FAIL). All other 34 A-tier criteria PASS.

**Key structural element**: T-40 in the AMENDMENT TABLE SPECIFICATION:
```
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix before the column list)
```
No CONDITION guidance → LLM writes abstract CONDITION → C-42 FAIL → C-43 FAIL.

---

## V-02 — C-43 Isolated | Output Format | T-40 CONDITION Exemplar-Only

**Axis**: AMENDMENT TABLE SPECIFICATION provides explicit guidance to quote a deficient T-38 CONDITION form in T-40 CONDITION (exemplar). No prescription guidance ("a passing T-38 CONDITION reads...") is provided.

**Hypothesis**: LLM follows the exemplar instruction (C-42 PASS) but stops there. T-43 fires alone (C-43 FAIL). Isolates C-43 as a single independent fail, verifying the cascade invariant is one-directional: C-42 PASS does not force C-43 PASS.

**Key structural element**: T-40 in the AMENDMENT TABLE SPECIFICATION:
```
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix; T-40 CONDITION must quote a
                             deficient T-38 CONDITION form — e.g., a T-38 CONDITION that
                             reads "fires if per-site entries lack composite identifier"
                             is abstract-only: it names the category but does not quote
                             a deficient per-site entry, and this abstract form fires T-40)
```
Exemplar present → C-42 PASS. No prescription → C-43 FAIL.

---

## V-03 — C-41 Isolated | Phrasing Register | T-40 Fully Documented

**Axis**: T-40 CONDITION in the spec carries both (a) inline failure exemplar and (b) correct-format prescription. Domain 1 back-fill instructions in Phase 9b explicitly call for P×I compound scores only, omitting R-NN identifiers.

**Hypothesis**: C-42 and C-43 both PASS (T-40 fully documented). T-41 fires because Domain 1 after-state is P×I-only — the classic C-41 isolation survives the v17 rubric upgrade. Score identical to V-02 but through a completely different criterion path.

**Key structural element** — Phase 9b Domain 1:
```
Back-fill P×I compound scores only into Domain 1 RISK fields — do not include R-NN
identifiers in Domain 1 back-fill entries
```
Plus T-40 in spec with full two-part CONDITION (a)+(b) → C-42/C-43 PASS.

---

## V-04 — C-42+C-43+C-46 | Combined: Lifecycle Emphasis + Role Sequence

**Axes**: T-40 row in spec lists only `T-40 PHASE = FINALIZATION` (no description, no CONDITION guidance) **and** Phase 9 inverts the role order — Architect precedes PM.

**Hypothesis**: T-40 minimal entry gives LLM nothing to write for T-40 CONDITION → C-42 FAIL → C-43 cascade. Separately, Phase 9 Architect-first instruction fires T-46 (C-46 FAIL). Three fails: cascade pair (C-42, C-43) plus independent role-sequence fail (C-46). No cross-cascade between the two fault paths.

**Key structural elements**:
- T-40 in spec: `T-40 PHASE = FINALIZATION` (no text)
- T-46 in spec: `fires if Phase 9 PM output precedes Architect output — Architect must lead Phase 9`
- Phase 9 instruction: Architect leads, PM follows

---

## V-05 — C-23 Cascade Root | Combined: Role Sequence + Propagation

**Axis**: Phase 0 omits amendment table initialization entirely. No `ID | TRIGGER | CONDITION | STATUS | PHASE` table is created. No AMENDMENT TABLE SPECIFICATION section.

**Hypothesis**: C-23 FAIL (amendment table absent) → C-26 FAIL → C-31..C-43 all fire (13 amendment-table-dependent A-tier criteria cascade). New C-42 and C-43 join the cascade, extending the R16 V-05 path from 13 fails to 15. Score: 21/36 → 95.83.

**Cascade path**: C-23 → C-26 → C-31, C-32, C-33, C-34, C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-42, C-43 (15 A-tier fails).

**Key structural element**: Phase 0 body contains only the role sequence declaration — no `Initialize the amendment tracking table` instruction and no AMENDMENT TABLE SPECIFICATION section at the end of the prompt.
