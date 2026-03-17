Written to `simulations/quest/rubrics/review-design-rubric-v18-2026-03-15.md`.

**Changes from v17 to v18:**

| | |
|---|---|
| **C-52** | Block-Level Inertia Note for Enforcement Class Scope Broadening — fires when an F-code's trigger class was deliberately broadened in a prior round but no inline note in the block names the prior form, the new scope, and why both are non-conformant. Converts a rubric-only historical record into self-defending inline text. Source: V-05 R18 BLOCK 2.7 inertia note. |
| **C-53** | SEALED Attestation Dual Non-Conformance Naming for Position-Integrity F-Codes — fires when a SEALED statement containing F-30 (or equivalent position-integrity F-code) names only the positive form ("block in conformant position") without explicitly naming both prohibited forms (absence AND wrong lifecycle position). Source: V-05 R18 BLOCK 2.7 SEALED "absence and wrong-position both non-conformant." |
| **Formula** | Denominator 44 → 46. Each aspirational criterion ~0.217 pts. |

The two new criteria are orthogonal to each other and to the C-51/C-46/C-48 cluster they extend: C-52 governs what the **block body** must explain; C-53 governs what the **SEALED attestation** must name. An output can declare F-30 correctly (C-51), enumerate it in SEALED (C-48), and still fail both C-52 (no inertia note) and C-53 (positive-form-only SEALED).
