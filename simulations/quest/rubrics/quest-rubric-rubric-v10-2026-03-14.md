Written to `simulations/quest/rubrics/quest-rubric-rubric-v10-2026-03-15.md`.

**What changed v9 → v10:**

**C-31** (`checkpoint-row-for-novel-contract-element-prevents-silent-drop`) — R9 set-level finding. All 5 R9 variations added "Rubric Propagation Contract present" as an explicit Phase 2 SetCoherenceAuditor row. This technique was absent in all R8 variations. The pattern: whenever a role definition introduces a novel contract element, the per-variation checkpoint must have a named row for it — without that row, the element silently drops under token pressure and no rewrite gate fires.

**C-32** (`evolution-hook-dual-path-specification-reduces-compliance-fragility`) — promoted from the v10 candidate. R9 V-02 (notes-only) and V-03 (version-field-only) both pass C-10/C-29, delivering the ablation gradient the candidate required. Single-path compliance satisfies the literal OR gate but leaves the remaining path droppable invisibly. Dual-path (both version-tracking position AND mechanism-note position required) forces both to be constructed, making either absence immediately detectable.

**Structural updates:**
- Required Sections row 7 adds C-31 and C-32 to N/A scope list
- Scoring N/A paragraph adds C-31 and C-32
- Notes adds `**C-31 N/A scope**` and `**C-32 N/A scope**` blocks (both N/A for this document; C-32 self-applies PASS)
- v11 Candidates: `evolution-hook-dual-path-confirmation` retired (promoted); rejection-log count updated to 24 aspirational; new candidate `c31-checkpoint-row-minimum-count-scales-with-contract-depth` added
