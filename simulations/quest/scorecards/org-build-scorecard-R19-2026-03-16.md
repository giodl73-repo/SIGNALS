step 1-D: "FORBIDDEN: writing both verdicts. FORBIDDEN: writing neither." inline; Phase 3 sub-step 3-F same pattern.

**Aspirational: 27/30 (fails C-19, C-29, C-30)**

**Score:** 60 + 30 + (27/30 × 10) = **99.00**

---

### Summary

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 5/5 | 3/3 | 26/30 | **98.67** |
| V-02 | 5/5 | 3/3 | 26/30 | **98.67** |
| V-03 | 5/5 | 3/3 | 26/30 | **98.67** |
| **V-04** | **5/5** | **3/3** | **28/30** | **99.33** |
| V-05 | 5/5 | 3/3 | 27/30 | **99.00** |

**Winner: V-04** at 99.33

---

### Ranking

1. V-04 — 99.33 (fixes C-19/C-29; Phase 3 task step 5 is the last interleaving failure)
2. V-05 — 99.00 (fixes C-22; "is an error" prose prevents C-19/C-29)
3. V-01/V-02/V-03 — 98.67 (four shared failures)

---

### Excellence Signals from V-04

**Signal 1 — MUST-only task step bodies, Constraints-housed FORBIDDENs:**  
V-04 relocates ALL FORBIDDEN directives — including sub-step ordering guards — to the Constraints section. Task step bodies contain only MUST directives and descriptive prose. This achieves C-19 and C-29 compliance (no "is an error" forms anywhere) while satisfying C-37 (ordering guards in Constraints still name both blocked and prerequisite sub-steps by name). Phases 1, 2, and 4 achieve perfect structural separation. Phase 3 task step 5 breaks the pattern — the verdict guard FORBIDDENs remain inline — revealing the one remaining gap to fully satisfy C-30.

**Signal 2 — Content FORBIDDENs relocated to Constraints section:**  
V-04 moves "FORBIDDEN: paraphrasing the CONST-1 template" from inline inside the FILE task step (V-01/V-02 pattern) into Phase 2's Constraints section alongside other content guards. This reinforces the pattern: the Constraints section is the single auditable location for all constraint declarations, content or ordering.

**Emerging pattern (candidate C-39):** Task step bodies should contain ONLY task-execution instructions (MUST + descriptive). ALL FORBIDDEN directives — sub-step ordering guards AND content guards — belong exclusively in the Constraints section. A phase where any task step body contains a FORBIDDEN directive fails. This is the logical completion of C-30 × C-37: C-37 names the sub-steps; C-30 governs location; C-39 would require the location to be the Constraints section. V-04 demonstrates this for 3 of 4 phases; a future variation must extend it to Phase 3 by moving the verdict guard FORBIDDENs out of task step 5.

---

```json
{"top_score": 99.33, "all_essential_pass": true, "new_patterns": ["MUST-only task step bodies: relocating ALL FORBIDDEN directives (sub-step ordering guards and content guards) to the Constraints section — not embedded inline in task step bodies — enables C-19, C-29, and C-30/C-37 co-satisfaction; task step bodies become MUST-only execution instructions; Constraints section becomes the single auditable location for all constraint declarations"]}
```
