**v15 written** to `simulations/quest/rubrics/scout-size-rubric-v15-2026-03-17.md`.

---

**What changed from v14**

Two new aspirational criteria added. Scoring denominator updated from 29 to 31.

---

**C-38 — Phase 0 gate encoded as a formal precondition table with STATUS and CLOSED-LABEL columns per precondition row**

Derived from R14: V-03 and V-04 satisfy C-36 with prose and checklist formats; V-05 promotes the entire Phase 0 to a formal two-row table with STATUS and CLOSED-LABEL columns. The table schema co-locates each precondition's status and failure reason at the row level — the CLOSED reason is readable from the row without parsing prose. This is the gate-level application of the structural-encoding family (C-18, C-22, C-26): the constraint content moves from prose cross-reference to schema co-location. The distinction from C-36: a prose "CLOSED — Precondition B: …" satisfies C-36 by naming the failure; the table satisfies C-38 by making the failure legible at the schema level without consulting a definition block.

**C-39 — Three-field diagnostic block enclosed in a named section header that labels its architectural role as a diagnostic pattern**

Derived from R14: V-01 through V-04 embed the C-37 three-field block in a CHECKPOINT or WRONG section without a named container; V-05 wraps it in `── DIAGNOSTIC PATTERN ──`. The named container signals the block's architectural role at the document-structure level before the model enters the block — the same principle as C-32 (confidence gap promoted to named standalone section with visual delimiter). The distinction from C-37: C-37 is satisfied when the three fields are present as labeled entries regardless of container; C-39 requires the entire block to be wrapped in a named section with a visual delimiter that identifies it as a diagnostic pattern rather than a generic example block.
