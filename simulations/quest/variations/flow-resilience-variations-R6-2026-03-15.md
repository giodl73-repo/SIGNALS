Written to `simulations/quest/golden/flow-resilience-variate-R6-2026-03-15.md`.

---

**R6 variations summary:**

| Variation | Axis | New criteria targeted |
|-----------|------|-----------------------|
| V-01 | Typed nil-finding identifiers | C-22 |
| V-02 | Scope declaration closure bracket | C-23 |
| V-03 | Template-embedded conditional linkage rules | C-24 |
| V-04 | Typed nil IDs + scope closure bracket | C-22 + C-23 |
| V-05 | Full R6 formalization on R5 gate infrastructure | C-22 + C-23 + C-24 + C-15–C-21 |

**Key mechanisms introduced:**

- **C-22** (V-01, V-04, V-05): `OEG-NIL-1` / `DCV-NIL-1` / `MRF-NIL-1` — typed prefix + unique run-level suffix; supersession notation `DCV-NIL-1: SUPERSEDED — DCV-CR-01 added` enables cross-referencing when Gate 4 amends a nil section.

- **C-23** (V-02, V-04, V-05): `SCOPE BRACKET: OPENING` before Gate 1 + `SCOPE BRACKET: CLOSING` terminal block after Gate 4 — both named, paired, independently auditable; terminal block names each OP-NN with coverage outcome.

- **C-24** (V-03, V-05): `RULE CR-DCV` and `RULE BARRED-CG` declared as named blocks before Gate 1; cited by rule ID in every amendment record they produce; No-Amendment Confirmation required when RULE CR-DCV is not triggered.
