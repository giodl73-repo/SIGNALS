`signal-check-variations-R12-2026-03-17.md` written — 5 complete variations.

---

**What's in R12:**

| V | Axis | C-33 | C-34 | C-35 |
|---|------|------|------|------|
| V-01 | C-33 only | YES | FAIL | FAIL |
| V-02 | C-34 grouped baseline | YES | FAIL (grouped) | FAIL |
| V-03 | C-35 only | FAIL | FAIL | YES |
| V-04 | All three combined, advisory canonical | YES | YES | YES |
| V-05 | All three combined, imperative | YES | YES | YES |

**Key structural additions over R10 V-04:**

- **C-32 baseline (locked in all)**: STEP D now closes with `Confirmed readiness: READY / CONDITIONALLY READY / NOT READY` and a forward arrow to STEP E
- **STEP E (new)**: Replaces the inline "Team summary" inside STEP D — STEP E is the dedicated final synthesis step; STEP B retains its early DRAFT function for C-11 compliance
- **C-33**: STEP A closes with `Inertia case: BUILT / PARTIAL / OPEN` + forward arrow to STEP E
- **C-34**: STEP E opens with two separate per-input prohibitions — one for `Confirmed readiness`, one for `Inertia case`
- **C-35**: ARCHITECTURE table advances from 9 rows (R10) to 11 rows — adds `Inertia case` and `Confirmed readiness` as declared PART 2 internal handoffs

**Three research questions isolating the gaps**:
1. Does C-33's named binary close a gap that prose inertia-case conclusions leave open at STEP E? (V-01)
2. Does per-input prohibition at STEP E (C-34) close the partial-compliance trap where grouped annotation allows `Inertia case` re-derivation while `Confirmed readiness` is structurally consumed? (V-02)
3. Does ARCHITECTURE extension to PART 2 internal rows (C-35) make the compliance gap *visible* before execution but require C-33+C-34 to actually *close* it? (V-03)
