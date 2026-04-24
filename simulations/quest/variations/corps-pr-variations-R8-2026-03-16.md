`corps-pr-variate-R8-2026-03-16.md` written. Here is the summary of what was produced:

---

## Variation Axes Selected

| Axis | Used In | R8 Focus |
|------|---------|----------|
| Inertia framing (C-25 string-matchable Budget verdict) | V-01, V-04, V-05 | Three labeled lines at line boundary; each independently string-matchable |
| Lifecycle emphasis (C-26 exact named result tokens) | V-02, V-04, V-05 | `C1 RESULT: ALL CLEAR` / `C1 RESULT: BLOCKED -- [item]` and `C2 RESULT: SATISFIED` / `C2 RESULT: UNSATISFIED -- [citation missing]` as terminal-line tokens |
| Role sequence (C-27 PRE-COMMITMENT labeled block) | V-03, V-05 | Distinct `PRE-COMMITMENT:` block structurally precedes findings table; initial position is not a receipt field |

---

## What changed from R7

**V-01 (C-25 gap):** R7 V-01 required `WORSE rows:` and `BETTER rows:` as indented fields under a single `Budget verdict:` label — readable but not independently string-matchable per clause. R8 V-01 requires each clause on its own labeled line at consistent indent, so `grep "^WORSE rows:"` retrieves it without prose parsing. The technical role IA cost anchor must now copy all three lines verbatim, making the citation a direct quotation rather than a paraphrase.

**V-02 (C-26 gap):** R7 V-02 appended supplementary text to the result token (`C1 RESULT: ALL CLEAR — Phase C may begin`), which breaks literal string matching. R8 V-02 strips the suffix — the token line is the entire compliance signal. The double-dash separator (`BLOCKED -- [item]`, `UNSATISFIED -- [citation missing]`) is the diagnostic boundary, making the pass/fail token independently scannable.

**V-03 (C-27 gap):** R7 V-03 required the READ RECEIPT including the initial position to be written before re-reading the diff, but the initial position was one field within the receipt template — no structural separation from findings. A role could fill it post-hoc. R8 V-03 moves the initial position into a distinct `PRE-COMMITMENT:` labeled block that appears in the output text after the receipt and before the findings table. Ordering is independently verifiable by reading top-to-bottom. Post-findings, the delta names the code artifact that held or changed the committed position.

**V-04 (C-25 + C-26):** B3 in the C1 checklist now explicitly scans for three labeled lines (not just "three-clause present"). C2 per-role compliance requires verbatim quotation of the `WORSE rows:` and `BETTER rows:` lines, making C2 a direct traceable verification of B3 structure.

**V-05 (C-25 + C-26 + C-27):** Full integration: three-clause labeled lines → C1 verifies those lines with `ALL CLEAR` token → PRE-COMMITMENT block written before diff read → C2 cites those lines verbatim with `SATISFIED` token → findings table with Domain-Lens column → post-commitment delta. Closes all three R8 gaps in one pipeline.
