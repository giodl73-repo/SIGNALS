Written to `simulations/quest/golden/corps-committee-variate-R17-2026-03-17.md`.

---

## corps-committee -- Prompt Variations R17

### Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | C-46 only -- FAILS template extended with C-44/C-45 self-referential entries | Template carries entries for C-44 and C-45 (recursive C-40 pattern). No BEFORE YOU START pre-flights added. C-47 and C-48 not satisfied. |
| **V-02** | C-47 only -- BEFORE YOU START pre-flight halt for FAILS template currency | Imperative halt fires at session-open if template lacks entries for any aspirational pair after C-39. Tagged `[C-47]`. FAILS template unchanged (no C-44/C-45 entries). C-46 and C-48 not satisfied. |
| **V-03** | C-48 only -- BEFORE YOU START pre-flight halt for CO-DEPENDENCY PREAMBLE completeness | Imperative halt fires at session-open if preamble omits the C-43/C-41 three-leg row. Tagged `[C-48]`. Parallel to C-47 on the C-45 axis. C-46 and C-47 not satisfied. |
| **V-04** | Combination: C-46 + C-47 | FAILS template gets C-44/C-45 entries + BEFORE YOU START gets C-44 pre-flight. Minimum change from R16 V-04 baseline that satisfies both. C-48 not satisfied. |
| **V-05** | Full integration: C-46 + C-47 + C-48 | All three mechanisms present. C-47 pre-flight text updated to name C-44/C-45 in the aspirational pair list, citing C-46 miss rather than C-44 miss. FAILS template additionally carries C-46/C-47/C-48 self-referential entries. Remove any one mechanism and a gap reopens. |

### Key design decisions

**C-46 vs C-47 are independent.** A skill can have C-44/C-45 entries in the FAILS template (C-46 satisfied) without any BEFORE YOU START pre-flight (C-47 not satisfied) — V-01. A skill can have the pre-flight (C-47 satisfied) without template entries for C-44/C-45 (C-46 not satisfied) — V-02. V-05 is the only variation where both mechanisms fire independently.

**V-05 C-47 text evolution.** In V-02/V-04, the C-47 pre-flight names `C-42, C-43` as the aspirational pair list and cites "C-44 miss." In V-05, it names `C-42, C-43, C-44, C-45` and cites "C-46 miss" — because V-05 has satisfied C-46 and the template must now carry entries for the extended pair list.

**INERTIA CONTINUITY BRIDGE criteria** (currently labeled `C-46-ICB` and `C-49-ICB` in the fill rules) are distinguished with suffixes to avoid collision with the rubric's new C-46. These should be reconciled in the quest-score phase.
