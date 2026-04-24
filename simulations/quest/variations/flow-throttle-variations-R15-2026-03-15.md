Written to `simulations/quest/golden/flow-throttle-variate-R15-2026-03-16.md`.

---

## Round 15 — V-01 through V-05

**Baseline:** R14 best (235/235 under v14; 235/250 under v15 — C-38, C-39, C-40 all FAIL)

---

### Variation Axes

| V | Axis | C-38 | C-39 | C-40 | Predicted |
|---|------|------|------|------|-----------|
| V-01 | Output format | count at header | canonical two-sentence closure | absent | 245/250 |
| V-02 | Phrasing register | count at header | canonical two-sentence closure | PROHIBITED + inline annotation at inventory close | 250/250 |
| V-03 | Lifecycle emphasis | count at header | canonical two-sentence closure | PROHIBITED in named sub-block before FORMAT CONTRACT COMPLETE | 245/250 (contested) |
| V-04 | Role sequence + phrasing register | count at header + count at Role 2 activation | canonical closure | PROHIBITED + inline annotation | 250/250 |
| V-05 | All three axes | count at header + count at activation + per-row Dropout-prohibited? column | canonical closure | PROHIBITED clause + per-row dropout tokens + ANNOTATION SCAN GATE before TABLE F | 250/250 (excellence candidate) |

---

### What Each Variation Isolates

**V-01** separates C-38 + C-39 from C-40. If the scorecard shows 245 (not 250), it confirms C-40 is independently testable.

**V-02** is the minimal path to 250 — single-step addition of all three criteria with no structural reordering. If V-02 scores 250, the round is effectively decided; V-03–V-05 test whether deeper structures add scoring surface.

**V-03** tests the co-location question for C-40: does "annotation inventory includes a PROHIBITED clause" mean physically inside the Section C block, or anywhere within the FORMAT CONTRACT closure? V-03's **ANNOTATION DROPOUT PROHIBITION** is a named sub-block after Section C but before FORMAT CONTRACT COMPLETE — if this fails C-40, it establishes that the PROHIBITED clause must be co-located in the inventory section.

**V-04** adds the annotation count to Role 2 activation conditions, making dropout a role-entry failure rather than a contract-boundary violation. Tests whether this strengthens C-36.

**V-05** introduces the **ANNOTATION SCAN GATE** (parallel to TYPE SCAN GATE) positioned between TABLE E and TABLE F. This makes annotation dropout a construction-time blocking condition with 7 observable scan lines — the strongest possible structural enforcement. If the scorecard rewards it, it seeds C-41 ("annotation scan gate as role-activation observable").
