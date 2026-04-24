Written to `simulations/quest/rubrics/review-design-rubric-v17-2026-03-15.md`.

**Changes from v16 to v17:**

| | |
|---|---|
| **C-50** | BLOCK 2.7 Registry Inbound Integrity Halt — F-29 fires when any registry row has no corresponding BLOCK 2 P1 finding (inbound direction; F-28 was outbound). Closes the F-28+F-29 bidirectional pair, mirroring the F-13+F-18 pattern on BLOCK 0. |
| **C-51** | BLOCK 2.7 Registry Structural Position Named Halt — F-30 fires when BLOCK 2.7 is not positioned after BLOCK 2.5 and before BLOCK 3. Introduces the seventh enforcement class: **position integrity** (prior classes: structural presence, content completeness, count parity, identity integrity, vocabulary integrity, catalogue disposition). |
| **C-47** | R17 signal added: V-01 PASS confirmed with canonical form; C-47/C-48 orthogonality confirmed. |
| **C-48** | R17 signal added: BLOCK 2.7 is the gap block (F-29, F-30 absent in V-01). Canonical BLOCK 2.7 SEALED requires three F-IDs: **F-28, F-29, F-30**. |
| **C-49** | R17 signal added: V-02 near-miss form documented — tie-prohibition present, sort keys present, but numbered tier steps, rank-range declaration, and non-conformance prohibition absent. |
| **Formula** | Denominator 42 → 44. Each aspirational criterion ~0.227 pts. |
