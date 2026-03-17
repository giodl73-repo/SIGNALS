Written to `simulations/quest/golden/mock-accept-variate-R3-2026-03-16.md`.

---

## mock-accept Variate — Round 3 Summary

**Baseline carried forward:** R2 champion (SKIP table + Slot-2-first + bypass-error-code fields)

### Axis-Assignment Plan

| Variation | Axis | Target Criterion | Key Change |
|-----------|------|-----------------|------------|
| **V-01** | lifecycle-emphasis | C-14 (CANARY SUPPRESSED branch) | Step 8 restructured as BRANCH A / BRANCH B gate; CANARY SUPPRESSED named as correct suppression path, not an error; CANARY-FALSE-POSITIVE defined distinctly |
| **V-02** | output-format | C-15 (empty blocked-lists explicit) | STEP 3 + STEP 4 guard records require unconditional output — `"Arch-blocked: [] (none)"` required even when empty; format constraint not logic change |
| **V-03** | phrasing-register | C-16 (VERDICT-ECHO as parseable code) | Step 6 REAL-REQUIRED template promotes VERDICT-ECHO from prose instruction to structured `Error-code:` field; becomes a checkable artifact field |
| **V-04** | lifecycle-emphasis + output-format | C-14 + C-15 | V-01 two-branch CANARY gate + V-02 explicit empty-list records; non-overlapping steps |
| **V-05** | lifecycle-emphasis + output-format + phrasing-register | C-14 + C-15 + C-16 | Full R3 integration: all three new aspirational criteria plus all R2 bases |

### Design rationale per criterion

**C-14 (CANARY SUPPRESSED branch):** The baseline has CANARY SUPPRESSED as an inline else-clause adjacent to CANARY-FALSE-POSITIVE. The two-branch gate structure makes suppression a named, affirmative path rather than a fallback, preventing a model from treating suppression as an error condition or conflating it with a false-positive.

**C-15 (empty blocked-list explicit):** Without a format constraint, models skip the guard record entirely when no namespaces are blocked. Adding `"If empty: 'Arch-blocked: [] (none)'"` forces the output unconditionally — the presence of the record is the signal, not just its contents.

**C-16 (VERDICT-ECHO as parseable code):** Moving VERDICT-ECHO from a prose parenthetical to a structured `Error-code:` field in the template schema makes it a parseable, checkable output field. The scorer can look for `Error-code: VERDICT-ECHO` as a concrete artifact signal.
