**Round 3 variations for rubric v2 written** to `simulations/quest/golden/flow-trigger-variate-R3-v2-2026-03-15.md`.

---

## Summary

**5 variations generated** targeting the three new rubric v2 criteria (C-11/C-12/C-13):

| Variation | Axis | Primary Target | Structural Mechanism |
|-----------|------|----------------|----------------------|
| **V-01** | Role sequence | C-11, C-12, C-13 | Scanner role completes before any enumeration; pre-numbered manifest slots must be populated or gap-tokened; Verdict Writer format string has mandatory row-citation field |
| **V-02** | Output format | C-11, C-12, C-13 | Two-pass numbered ledger — Pass 1 allocates rows (IS the denominator), Pass 2 populates every allocated row; verdict format strings have no closing tag without row range |
| **V-03** | Phrasing register | C-11, C-12, C-13 | Failure mode catalog FM-11/FM-12/FM-13 names the exact defect each criterion prevents; SHALL language + detection signals make each criterion checkable in-output |
| **V-04** | Lifecycle + output format | C-11, C-12, C-13 | Three phase gates: Gate 0 blocks Phase 1 without denominator count, Gate 1 blocks Phase 2 without full candidate disposal, Gate 2 requires row citations in verdicts |
| **V-05** | Inertia framing + role sequence | C-11, C-12, C-13, C-09, C-10 | Names the DEFAULT behavior that produces each defect + explains why it fails; understanding the failure mode produces deeper compliance than rules alone |

**Key design insight**: C-12 (inline gap tokens) is structurally distinct from a reconciliation table at the end — the token must appear at the candidate's position in the numbered sequence. V-01 and V-02 enforce this most directly by pre-allocating slots before any conditions are evaluated.
