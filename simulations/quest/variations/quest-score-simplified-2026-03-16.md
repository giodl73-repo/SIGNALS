---

## Simplified Prompt Body

```
[see: simulations/quest/golden/quest-score-golden-QU5-simplified-2026-03-16.md]
```

---

## Simplification Report

### What was removed and why

| Cut | Words saved | Rationale |
|-----|-------------|-----------|
| Intro description paragraph ("quest-score scores N skill outputs...") | ~47 | Describes what the skill does; all sections it mentions are already specified in SYNTHESIS. No criterion requires this meta-description. |
| Conflict clause ("If a conflict exists between this prompt and a rubric file...") | ~17 | No rubric criterion checks for this. Zero behavioral effect. |
| `Example: "N_aspirational changed from 14 (v7) to 16 (v8)."` in 1b | ~9 | Template line above already has `[prior value]` / `[current value]` placeholders. Example is noise once the template is clear. |
| 4-bullet 1d verdict rules → 2-bullet condensed | ~50 | YES and NO rules collapsed into one bullet. Two PARTIAL examples collapsed to one. PARTIAL violation rule merged into the PARTIAL bullet. All rules preserved, no content lost. |
| `PHASE 1 COMPLETE.` 35-word gate → 20-word gate | ~15 | Opening gate already states all conditions. Closing gate is informational shorthand, not a new requirement. |
| `After the bilateral audit, verify that every...` → `Verify that every...` | ~15 | Same instruction, shorter form. No criterion specifies the exact preamble. |
| `Criteria absent from all rows is a coverage gap.` | ~8 | Directly redundant with "For any criterion not appearing: add it to DEFERRED." The first sentence covers the action; the second re-states the implication. |
| `"A NO declaration requires rewriting the evidence before Phase 2 proceeds."` | ~12 | The locatability template already says "rewrite before proceeding" in the NO branch. Exact duplicate of information. |
| `After writing, write this required labeled field:` × 7 → `Required field:` × 7 | ~35 | Shortened preamble preserves "required" keyword and co-locates with each Inertia block. C-17 and C-20 require the Inertia labels exist; no criterion requires the preamble wording. |
| 1a Inertia verbose tail → compact form | ~20 | Original: "A scorer who skips produces a matrix missing C-23 and C-24 rows and computes all composites using /14 -- both errors invisible until Phase 3." Simplified: "C-23/C-24 rows missing and composites use /14." Same failure modes named. |
| 1b Inertia condensation | ~8 | "Both sides required to confirm the transition" → absorbed into dash clause. |
| 1d Inertia Reason-column explanation trim | ~15 | Removed "Reason phrases make each PARTIAL as auditable as its YES/NO verdicts." -- the preceding sentence already establishes the ambiguity problem. |
| Locatability field format shortening | ~25 | Full: "a reader can find [the quoted or referenced material] in [output ID] at [named section or structural location] without searching the full output". Simplified: "findable at [section] in [output ID] without searching the full output". Same constraint, fewer filler words. |
| Inertia (C-11, C-14, C-23) trim | ~25 | Removed "The binary field makes locatability status scannable without re-reading the evidence text." The preceding two sentences already cover C-11/C-14/C-23 failure modes. |
| ENTRY LOCK elaboration cut | ~30 | Removed "Write 'Confirmed' if... Write 'Violated...' if..." The template [Confirmed | Violated -- first verdict row at: ___] already specifies both branches. Only the required-field note retained. |
| `Score all N outputs before proceeding to Phase 3.` | ~10 | Phase 3 comes after Phase 2 by structure. Implied. |
| `If a discrepancy is found, update the SYMMETRIC DELTA REGISTER Arithmetic Discrepancy row.` | ~17 | Aspirational-only cross-reference (connects 3a to 1c). No essential criterion checks for it. |
| `Write the following sections in order.` before SYNTHESIS | ~6 | Implied by the section headers that immediately follow. |
| Intro description sentence in FORMULA CHANGE ALERT ("The v8 rubric changes...") | ~14 | The `N_aspirational: 14 (v7) -> 16 (v8)` line directly below makes the same statement. |

**Total removed: ~364 words**

### Essential criteria verification

| Criterion | Covered in simplified? | Location |
|-----------|----------------------|----------|
| C-01 | YES | 1a load block + Inertia (C-01) |
| C-02 | YES | "No row blank or missing. Include rows for all criteria C-01 through C-24." |
| C-03 | YES | "Evidence: must quote, paraphrase with location... Criterion restatement is not evidence." |
| C-04 | YES | Composite formula block with explicit calculation template in Phase 2 |
| C-05 | YES | `Required even when empty: "No failure patterns..."` in SYNTHESIS |

All 5 essential criteria: **still PASS**. All 3 recommended criteria (C-06, C-07, C-08): **still PASS**. All 16 aspirational criteria that were PASS in V-05: **still PASS** -- every structural mechanism (SYMMETRIC DELTA REGISTER, BILATERAL SYMMETRY AUDIT, COVERAGE ASSERTION, MODEL CELL + LOCATABILITY ASSERTION, ENTRY LOCK, Inertia labels with criterion-ID anchoring, NON-ADDITIVITY ANALYSIS) is preserved intact.

```json
{"simplified_word_count": 1397, "original_word_count": 1761, "all_essential_still_pass": true}
```
