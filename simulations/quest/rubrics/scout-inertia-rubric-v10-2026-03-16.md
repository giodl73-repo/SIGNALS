`scout-inertia-rubric-v10-2026-03-17.md` written.

---

**v9 -> v10: two new criteria, ceiling 155 -> 165**

| # | Criterion | Source signal |
|---|-----------|---------------|
| A-21 | **Inline falsifiability example in defeat condition threshold column** | R9 V-02 A-20 FAIL: "Measurable threshold" column in Stage 5B had no inline example; V-04/V-05 provide `(e.g., >10MB, >3 failures/week)` in the label. A-20 covers quantity/unit columns; A-21 extends the inline-example pattern to DC threshold columns. The two are independent -- a template can fail A-20 while passing A-21, and vice versa. Both required for full inline coverage. |
| A-22 | **Mid-template bridge completion status check** | R9 V-02 excellence signal: Q3/Q4 echoed as named status checks in Stage 2, between FM Inventory and DC section. A-12 requires the artifacts to be *named*; A-22 requires a *completion gate* positioned before DC authoring begins. Parallel to how A-16 enforces FM row assignment before DC citation, A-22 enforces bridge completion before DC rows are written. A-22 implies A-12. |

**Implication chain updated**: A-22 implies A-12. A-21 requires A-20 and A-13. A-19 implies A-16 implies A-14 implies A-08. A-18 implies A-15. A-17 implies A-11.

**R10 target**: First 165/165 candidate. Requires satisfying A-21 (DC threshold inline example) and A-22 (mid-template bridge gate) on top of the full R9 scaffold. The untested combination is A-10 + A-11/A-17 + A-12/A-22 + A-13 + A-14 + A-15/A-18 + A-16 + A-19 + A-20 + A-21 simultaneously. V-02 at 150/155 is the current high-water mark; a variation that keeps V-02's structure and adds the DC threshold inline example (A-21) + bridge status check gate (A-22) is the minimal delta to 165.
