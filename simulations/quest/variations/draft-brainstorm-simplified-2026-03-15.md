The simplified prompt looks clean and complete. Here is the full output:

---

## Simplified Prompt Body

The minimal golden prompt for `draft-brainstorm` (R20 V-05 → QU5) is written to:
`simulations/quest/golden/draft-brainstorm-variate-R20-QU5-simplified-2026-03-16.md`

---

## Simplification Report

**Word count: 1844 → 1474 (−370 words, 20.1% reduction)**

### What was removed (35 cuts)

Every cut removes text that either (a) restates a rule already enforced elsewhere, (b) explains the WHY of a rule rather than stating it, or (c) is a decorative label with no behavioral consequence.

| # | Text removed | Words | Why |
|---|---|---|---|
| 1 | "Do not advance to the next phase..." (opening) | 13 | Restated by per-phase precondition italics |
| 2 | Lens name example "(e.g., 'More Ambitious'...)" | 7 | "one phrase" is sufficient |
| 3 | "This is the most important entry in the pool..." | 22 | Motivation; Do Nothing instructions enforce the behavior |
| 4 | "Write the following four fields:" | 6 | Label before bolded fields — redundant |
| 5 | "(pool entry)" from Do Nothing | 2 | Context is clear |
| 6 | "Phase 1 opens below." from Phase 0 close | 3 | Phase 1 follows immediately |
| 7 | "You may add sections beyond the six required." | 8 | Permissive non-rule |
| 8 | "Aim for at least 6 lens-attributed ideas total." | 8 | ≥2/lens × 3 lenses = 6 already |
| 9 | "Marking as you write introduces sequential bias..." | 13 | Explains WHY; prohibition stated before it |
| 10 | "-- technically, organizationally, or for users?" (1a) | 7 | Parenthetical qualifier on a clear question |
| 11 | "A direction that shifts only emphasis..." (1c) | 17 | Negative restatement of the preceding positive test |
| 12 | "the strongest ideas surface across the whole run..." (Check A) | 13 | Explains WHY to rescan |
| 13 | "Output of Check A: 5 candidates advancing..." | 10 | Label-only |
| 14 | "Do not fill in Selected? during construction." | 8 | Covered by Selected? column rule |
| 15 | "Do not assess whether a row passes while other rows remain blank." | 13 | Covered by "Write all five sentences before evaluating" |
| 16 | "(scope, user group, cost, risk)" example | 4 | "actual constraints" is sufficient |
| 17 | "A partial Registry has no valid Selected? entries..." | 28 | Negative restatement of (a)/(b) |
| 18 | "This is a schema property of the Registry." | 7 | Decorative |
| 19 | "**Prohibition Battery:**" header | 2 | Prohibitions are self-labeled |
| 20 | "-- not on headings, inline, in notes, or in any other form." | 10 | "anywhere in your output" is exhaustive |
| 21 | Prohibition B last sentence ("If editing the candidate's rationale...") | 45 | Elaborate escalation of the preceding rule; no distinct criterion |
| 22 | "Output of Check C: final AMEND content." | 7 | Label-only |
| 23 | "Phase 3 may begin only when all four conditions are met simultaneously." (Phase 2 close) | 13 | Restates the four conditions just listed |
| 24 | GATE PRECONDITIONS trailing 3 sentences | 38 | Negative restatements of (a)/(b) |
| 25 | "(candidates confirmed in Check B...)" (Phase 3) | 13 | Parenthetical back-reference |
| 26 | "Name the specific direction the system, team, or product is already moving." | 12 | "What is happening right now" implies directionality |
| 27 | "Be specific: what is delayed, degraded, or foreclosed?" | 9 | "concretely accumulates" already enforces specificity |
| 28 | "(each must appear as a `##` section)" from dimensions header | 8 | Covered by "Each is a **mandatory `##` section**" above |
| 29 | "Generate the complete pool before selecting." | 6 | Restates "Do not mark top-5 yet" in positive form |
| 30 | "**Column rules:**" header | 2 | Bullets are self-labeled |
| 31 | "-- both must hold before Phase 3 may begin" from GATE header | 9 | Implied by GATE PRECONDITIONS |
| 32 | "Identify 5 top-5 candidates." (merged into Check A question) | 4 | Collapsed |
| 33 | "before any ideas" from 1a placement instruction | 3 | "First element" is sufficient |
| 34 | "while Phase 2 Check B is in progress" → "during Check B" | 5 | Compressed |
| 35 | "For each of the 5 candidates, write one row." → "Write one row per candidate." | 5 | Compressed |

**Essential criteria check: all PASS**

- C-01 Volume — pool instruction intact
- C-02 Idea Anatomy — idea template intact  
- C-03 Top-5 Marker — Phase 3 marking instruction intact
- C-04 Inertia Check — Phase 0 Do Nothing template intact
- C-05 AMEND Section — 1c and Check C intact

All lifecycle signals (C-35 to C-50 family), phase gate markers, registry gate conditions (C-49, C-50), and anti-pattern prohibitions preserved.

```json
{"simplified_word_count": 1474, "original_word_count": 1844, "all_essential_still_pass": true}
```
