**flow-trigger-rubric-v12** written to `simulations/quest/rubrics/flow-trigger-rubric-v12-2026-03-16.md`.

---

**Two new aspirational criteria (C-38–C-39), N_aspirational: 29 → 31, max (raw): 137.5 → 142.5:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-38 | V-04 "Formal imperative" pattern — obligation text carries role + modal verb + artifact + temporal constraint as a self-contained specification clause | Obligation statement self-containment: reading the obligation text column alone (without opening producing role, activation event, or refutation columns) yields a complete specification of who must do what with what content by when. Labels and category names in the obligation text are a weak pass even when other columns are fully populated. | C-32 (unified registry adds "how stated" requirement to "what columns present"), C-30 (temporal anchors per prohibition — extends to all Phase 0 obligation statements), C-31 (role is in the statement text, not only in a dedicated column) |
| C-39 | V-05 dual-time attribution self-documentation — narrative note confirming "role attribution exists at both declaration time (ARTIFACT MANIFEST) and detection time (CLOSURE CHECK counter)" | Attribution chain design rationale: the output explicitly documents that both attribution layers exist, names the artifact where each operates, and explains why both are required — so that removing either layer is understood to break remediation self-sufficiency, not merely reduce coverage. | C-31 (manifest-layer attribution), C-37 (closure-check-layer attribution), C-26 (INERTIA CONTRAST — rationale co-located with mechanism) |

**Structural relationships:** C-38 is the specification-completeness counterpart to C-32's column-completeness requirement — C-32 requires all metadata types to be present as columns; C-38 requires the obligation statement text itself to be a complete specification clause, eliminating the need to consult other columns for who, what, and when. C-39 is the design-rationale counterpart to the C-31+C-37 chain — C-31 and C-37 establish that attribution exists at both time points; C-39 requires the output to document *why* both points are required, converting an incidental structural correlation into a named design commitment that resists silent regression in future variations.
