`topic-story-rubric-v11-2026-03-15.md` written.

---

**Three new criteria added (C-37, C-38, C-39):**

**C-37 -- Repair Operation Item Template Substitution Variables Are Labeled with Their Source Declarations**
From R10 Signal 1 (C-34 PASS note on V-01, V-04, V-05). C-34 fires on whether the repair operation contains a quotable parameterized template; C-37 fires on whether each substitution variable is annotated with its artifact source. V-01's block named the sources inline and closed instantiation with "Do not derive -- substitute directly from these two sources." Without source declarations the extension author must infer where `[Section name]` and `[field name]` originate; with them, instantiation is fully prescribed and auditable against named artifact locations. C-34 passes on any substitutable template; C-37 passes only when each variable is labeled with its named source and instantiation is described as a substitution-only operation.

**C-38 -- Section Template Anti-Consolidation Directive Cross-Reference Resolves to an Exact Inventory Cell**
From R10 Signal 2 (C-35 PASS note on V-02, V-04, V-05). C-35 fires on any inventory-designating cross-reference (column-level suffices); C-38 fires on whether the cross-reference names both the axis row and the constraint column and designates that cell as the single point of update. V-02's directive named "Structural Constraint column, Inertia-framing axis row -- that cell is the single point of update for this constraint." A column-level reference requires a scan for the relevant row; a cell-level reference terminates at an unambiguous, locatable, updatable artifact position. C-35 passes on any canonical inventory reference; C-38 passes only when the reference resolves to an exact cell (row x column) named as the single point of update.

**C-39 -- Checklist Constraint-Reference Footer States the Propagation Rule and Explicitly Denies Independent Authority**
From R10 Signal 3 (C-36 PASS note on V-03, V-05). C-36 fires on the explicit canonical designation; C-39 fires on two additional operational properties: (a) the propagation rule -- "updating the inventory propagates to these items" -- states the maintenance implication directionally so a diligent maintainer does not redundantly update the checklist; and (b) the authority denial -- "the checklist is not separately authoritative for constraint content" -- forecloses future elevation of the checklist to co-canonical standing. Together, the two statements close both maintenance questions a reader might ask when encountering the footer. C-36 passes on the canonical designation; C-39 passes only when the propagation rule and authority denial are both explicitly stated.

**Scoring updated**: 32 aspirational criteria (C-08--C-39) sharing 10 pts, 0.3125 pts each (10/32). R10 baseline under v11: V-05 passes all 32 → 100.0.
