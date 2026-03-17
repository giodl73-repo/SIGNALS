Original: **3,046 words**. Simplified: **2,851 words**. Removed: **195 words** (6.4%).

---

## Simplification report

**What was removed and why:**

| Removed | Location | Words | Why |
|---------|----------|-------|-----|
| "This target will be referenced at Step 5 (committed block) and re-verified at Step 5B and Pass 2 Part C Sub-check 3." | Step 1 | ~22 | Forward reference — enforcement exists at those steps regardless |
| "Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT" | Step 2C | ~9 | Cross-reference only — no gate behavior |
| "Do not proceed until filled with your own-words paraphrase." | Step 2C | ~10 | The field's own placeholder notation `[your paraphrase]` carries the instruction |
| "This table is re-verified at Step 5B Constraint 1B and Pass 2 Part B item 4." | Step 3A | ~18 | Cross-reference only — enforcement at those steps |
| "No third-person. Every old-tool reference: product name from Step 1b-ii." | Phase 1 body | ~10 | Covered by Step 4 Performance Mode Declaration |
| "No third-person. Product name for old tool." | Phase 2 body | ~8 | Covered by Step 4 |
| "No third-person. Product name for old tool." | Phase 3 body | ~8 | Covered by Step 4 |
| Entry-specific guidance block (label + entries 1–3) | Step 8 | ~45 | Entry 3's Trigger event rule already in its template; entries 1–2 are vague labels |
| "A NO in any cell is a concreteness failure for that ticket on that property." | Part B item 2 | ~17 | Structurally implied by the table — a NO cell value needs no prose clarification |
| "triple-clause verbatim (do not paraphrase, do not summarize, copy it verbatim word-for-word)" → "verbatim" | Sub-check 1 paraphrase consistency | ~12 | Redundant with the per-phase governing clause instructions above, which keep the full triple instruction |
| C-58/C-59/C-60 probe: complete (×3 lines); "C-57" → "C-60" | State final | ~25 | The probes are confirmed by their respective Part B items; updated ceiling reference |

**What was NOT removed:** All constraint gates, all correction instructions, all Prohibited sentinels, all table structures, all verbatim enforcement language in governing paraphrase clauses, "Confirmation: this rule applies to every severity assignment", all state and verification blocks, "If any fails, correct and re-run."

**Honest assessment of the 20–40% target:** V-05 is already a lean product of 20 rounds of rubric-driven tightening. Every structural element was added to close a specific failure mode. The only true redundancy is the cross-reference notes, trailing body reminders, and one prose explanation of an implied structural property — about 6% of the prompt. The 20–40% target is not achievable for this prompt without removing load-bearing criteria gates.

**Essential criteria verification:**

| Criterion class | Still passes? | Mechanism preserved |
|----------------|---------------|---------------------|
| C-01–C-08 (essential + recommended) | YES | All field requirements, vocabulary, persona grounding intact |
| C-45/C-48/C-50 (inference rule + phase distribution) | YES | Step 2C field, Step 5 Required items 1–3, Constraint 0, Sub-check 3 table all present |
| C-53/C-55/C-58 (role-phase cross-matrix) | YES | Step 3A table, Constraint 1B, Part B item 4 cross-matrix verification table |
| C-57/C-59 (all-phase verbatim quotes) | YES | Part B item 2 all three phases with verbatim + properties |
| C-60 (Phase 2 concreteness table) | YES | 5-column table in Part B item 2 preserved |
| C-13/C-15/C-17 (coverage gate + table + gap bridge) | YES | PASS 1 table with Phase and Gap traced to columns |
| C-51 (Phase 2 migration barrier + Prohibited sentinel) | YES | Entry 3 extended template with Prohibited sentinel and Disallowed expansion present |

```json
{"simplified_word_count": 2851, "original_word_count": 3046, "all_essential_still_pass": true}
```
