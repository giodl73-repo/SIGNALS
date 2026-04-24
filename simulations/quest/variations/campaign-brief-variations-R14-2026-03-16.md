`simulations/quest/golden/campaign-brief-variate-R14-2026-03-17.md` written.

---

**R14 summary — what each variation isolates:**

| | C-32 | STATUS header | STORY header | Other axis | Expected |
|---|---|---|---|---|---|
| V-01 | PASS | bare | bare | — | 320/330 (C-33 PARTIAL baseline) |
| V-02 | PASS | **with parenthetical** | bare | — | 320/330 (asymmetric, weakest-link) |
| V-03 | PASS | bare | **with parenthetical** | — | 320/330 (asymmetric reversed) |
| V-04 | PASS | with parenthetical | with parenthetical | `current_date:` field in STATUS | 330/330 (C-33 PASS ceiling) |
| V-05 | PASS | with parenthetical | with parenthetical | self-declaring bodies + VERDICT inertia-first | 330/330 (C-33 PASS + double-elision max) |

**Key investigation structure:**

- V-01 vs V-04/V-05: confirms C-33 is independently necessary (bare headers do not achieve C-33 even with C-32 PASS)
- V-02 vs V-03: confirms weakest-link symmetry across C-29/C-30 domains (neither domain alone satisfies C-33)
- V-05 beyond V-04: not rubric-scorable above ceiling, but observable — V-05's self-declaring clause bodies instruct the model to activate the contract from the clause alone without locating the preamble, testing the upper bound of partial double-elision recovery behavior
