Written to `simulations/quest/golden/mock-ns-variate-R9-2026-03-16.md`.

---

## mock-ns -- Round 9 Variations (rubric v9, C-29 + C-30 target)

**Three single-axis, two combined. Each is a complete, runnable skill body.**

---

### Variation axes chosen

| Axis | Rationale |
|------|-----------|
| **Predicative-identity declarative** | C-25 explicitly names "S-0 is the emit step" as equivalent to "This step emits first" -- but has that form been tested against C-28/C-29/C-30? |
| **Modal-obligation declarative** | "must emit" vs "emits" -- does mood matter for C-25's "role-asserting declaration"? |
| **Tier-carry compound with named consumers** | "carries tier into S-2 and S-3" in the declarative compound directly names the C-18 handoff consumers -- tests whether the declarative alone satisfies C-18, and whether C-20's "terminal sentence" is position-sensitive |

---

### Variate summary

**V-01 (Predicative-identity declarative)**
```
S-0 is the emit step. Write the TOPICS.md status line before any other work begins.
```
- Axis: Identity-predicate ("is the emit step") vs action-predicate ("emits first")
- Hypothesis: C-25 lists "S-0 is the emit step" as an equivalent form; "S-0" is direct nominative step-label satisfying C-28/C-29/C-30
- Predicted: **124/124**

---

**V-02 (Modal-obligation declarative)**
```
This step must emit first. Write the TOPICS.md status line before any other work begins.
```
- Axis: Modal-obligation mood ("must emit") vs indicative ("emits first")
- Hypothesis: "Must emit" may be obligation-imposition rather than role-declaration -- C-25 requires a "present-tense declaration asserting the step's ROLE"; a modal imposes a norm rather than declaring the step's nature. Predicted C-25/C-28 failure.
- Predicted: **120/124** (C-25 FAIL -2, C-28 FAIL -2)

---

**V-03 (Tier-carry compound, no standalone terminal sentence)**
```
This step emits first and carries tier into S-2 and S-3. Write the TOPICS.md status line
before any other work begins.
```
- Axis: Compound predicate names consumers ("carries tier into S-2 and S-3"); standalone tier-carry sentence deliberately omitted
- Hypothesis: Tests C-18 (does the declarative compound satisfy "explicit handoff sentence"?) and C-20 (does C-20's "standalone terminal sentence" require it to be terminal, i.e., after the resolution bullets?)
- Predicted: **122 or 124/124** depending on whether C-20 is position-sensitive

---

**V-04 (Two-axis: identity + tier-carry compound, no terminal sentence)**
```
S-0 is the emit step and carries tier into S-2 and S-3. Write the TOPICS.md status line
before any other work begins.
```
- Axes: V-01 (identity predicate) + V-03 (tier-carry with consumers, no terminal sentence)
- Hypothesis: Identity compound -- "S-0 is the emit step and carries tier into S-2 and S-3." Tests whether the identity-form compound satisfies C-18 (does "is the emit step and carries tier..." count as an explicit handoff sentence?), plus repeats the C-20 position-sensitivity test in identity form
- Predicted: **120-124/124** depending on C-18 and C-20 rulings

---

**V-05 (Synthesis: tier-carry compound + full dual-register C-18/C-20 coverage)**
```
This step emits first and carries tier into S-2 and S-3. Write the TOPICS.md status line
before any other work begins.
```
(+ standalone terminal sentence retained: "Carry the resolved tier into S-2 and S-3 before any further action.")
- Axes: V-03 compound + standalone terminal sentence kept for C-20 dual-register
- Hypothesis: Maximum redundancy -- tier-carry appears in three registers (declarative compound, table cell, standalone terminal sentence). C-18 and C-20 are both satisfied independent of position-sensitivity ruling. C-27 unaffected (standalone sentence is NOT in the preamble gate). Predicted **124/124**.

---

### Three discriminators targeted by R9

| # | Discriminator | Variates that test it |
|---|---------------|-----------------------|
| 1 | C-25/C-28 mood-sensitivity: does "must emit" assert role or impose obligation? | V-02 vs V-01/V-05 |
| 2 | C-20 terminal-position: does "standalone terminal sentence" require post-resolution position? | V-03/V-04 (no terminal) vs V-05 (terminal kept) |
| 3 | C-18 identity-form: does "is the emit step and carries tier" constitute an explicit handoff sentence? | V-04 vs V-03 |
