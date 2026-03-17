v18 rubric written to `simulations/quest/rubrics/prove-prototype-rubric-v18-2026-03-15.md`.

**Two new aspirational criteria extracted from R18:**

**C-49** (table-enforced thread co-equality, 5 pts) — Thread 1 and Thread 2 declared as rows in a two-row table with identical column schema (Scope | Key structural markers | Terminal discharge obligation). V-03 demonstrated that identical schema makes subordination structurally impossible by construction — both thread rows must fill every column with equivalent depth, so co-equality cannot be accidentally violated by register drift. Advances C-47 from assertion-enforced to construction-enforced. Requires C-47.

**C-50** (structural marker inventory, 5 pts) — A dedicated `## Structural Marker Inventory` section placed before any container executes, containing a four-column table (Marker type | Required by | Location | Form) for all four C-43/C-44/C-45 marker types, closed with an explicit REQUIRED statement. V-04 demonstrated this establishes C-48 compliance as a verifiable document property before a reader encounters any container body — auditable from the document's opening rather than discovered by scanning through it. Advances C-48 from scannable markers to pre-declared markers. Requires C-48.

**Updated ceiling**: 347 → **357** (Aspirational 247 → 257). R19 seed: combine C-49 + C-50 on the R18 base.
