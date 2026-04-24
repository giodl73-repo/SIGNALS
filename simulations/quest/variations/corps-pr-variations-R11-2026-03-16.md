`corps-pr-variate-R11-2026-03-16.md` written. Here is the summary of what was built and why.

---

## R11 Variation Axes

| Axis | Used In | R11 Focus |
|------|---------|----------|
| Lifecycle emphasis (C-33: C2 scoped as receipt completeness) | V-01, V-04, V-05 | C2 checks receipt fields (a)-(e), not Phase B ledger content |
| Output format (C-34: F-01 typed IA-RESPONSE) | V-02, V-04, V-05 | Type column required; F-01 Description = IA verdict + role mechanism in same entry |
| Role sequence (C-35: receipt precedes C2 RESULT) | V-03, V-04, V-05 | Explicit ordering constraint in pipeline declaration; violation detectable by line scan |

---

## What each variation does

**V-01 (C-33 axis)** — Replaces the C2 compliance block with a receipt field checklist: one line per field (a)-(e), each marked present/absent. C2 RESULT: SATISFIED means all five fields are populated. Removes the old WORSE/BETTER verbatim citation check (which was a Phase B re-check, not a receipt check). Adds an explicit note: "C2 does NOT re-check Phase B content — that is C1's scope."

**V-02 (C-34 axis)** — Adds a Type column to the findings table. F-01 must have `Type = IA-RESPONSE`; its Description must contain the IA verdict/cost position AND the role's disagreeing mechanism in the same cell. Subsequent findings use `Type = DOMAIN`. A table without the Type column or an F-01 with any other type fails the template.

**V-03 (C-35 axis)** — Makes the per-role ordering explicit by labeling each step: STEP 1 (READ RECEIPT) must appear in the output before STEP 2 (C2 RESULT). The pipeline Phase C exit conditions name "READ RECEIPT precedes C2 RESULT per role in the output text" as a named invariant. Detectable by scanning for the receipt block header and C2 RESULT line in output order.

**V-04 (C-33 + C-35)** — Wires the two causally. C-35 ordering guarantee is what makes C-33's completeness check independently verifiable: C2 cannot confirm receipt completeness if the receipt has not yet been written at that point in the output. The C2 block template is the field checklist from V-01; the per-role template uses the step-labeled ordering from V-03. Both exit conditions are named in the pipeline: (a) C2 verified receipt field completeness, not Phase B; (b) READ RECEIPT precedes C2 RESULT per role.

**V-05 (C-33 + C-34 + C-35)** — Full integration. Per-role output sequence is a four-step invariant: (1) READ RECEIPT with fields (a)-(e); (2) C2 RECEIPT CHECK confirming field completeness, following the receipt in the output; (3) PRE-COMMITMENT SEALED before diff content; (4) Findings table with F-01 Type=IA-RESPONSE and Description containing both IA verdict and role mechanism. Seven Phase C exit conditions are enumerated, one per mechanism. The mechanisms are independent and non-overlapping: satisfying two of three still fails the third.
