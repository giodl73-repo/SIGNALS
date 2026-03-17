---

## Simplification Report

**Original (V-05 prompt body):** 2,900 words
**Simplified:** 2,316 words
**Reduction:** 584 words / **20.1%**

### What was removed and why

| # | Location | Removed | ~Words | Why |
|---|----------|---------|--------|-----|
| 1 | STATUS QUO | 5-step list → 1-sentence summary | 42 | Framing only; foil items carry the load |
| 2 | STATUS QUO | 3 softening filler sentences | 28 | Pure padding |
| 3 | SPAN DEFINITION ×4 | `Function:` label in each block | 48 | Stated in preamble; 4 repetitions add nothing |
| 4 | SPAN DEFINITION ×4 | `TRANSCRIPTION STOP: foil item must list...` in each block | 48 | Covered by the general TRANSCRIPTION STOP above all blocks |
| 5 | SPAN DEFINITION ×4 | `— computes pass-side enumeration for the foil item below:` subtitle | 32 | Redundant with Function label removal |
| 6 | ROLE: CRITERION DEFINER | Opening sequencing sentence + "no criterion fields" line | 18 | Implied by phase structure and gate |
| 7 | ROLE: CRITERION DEFINER | DEFINER OUTPUT GATE satisfaction paragraph (3 sentences) | 38 | Gate header + STOP CONDITION are operative; restatement is dead weight |
| 8 | PHASE 4 | Duplicate PREREQUISITE header | 15 | Phase 3's prerequisite covers it |
| 9 | PHASE 5 | Consumer explanation sentence | 20 | Restates Consumer field |
| 10 | ROLE: MECHANISM DEFINER | `**Input:**` line + "Produces independence map" sentence | 33 | Both restated elsewhere |
| 11 | ROLE: BUILDER ASPIRATIONAL | "This role's entry is gated..." entry sentence | 26 | Redundant with PREREQUISITE headers above it |
| 12 | TIER-BLIND CATEGORIZER | 2 illustrative trailing sentences | 44 | Derivation instruction covers the gap |
| 13 | EVALUABILITY ARCHITECTURE COMPETITOR | Verbose reasoning prose → condensed | 55 | Labels + criterion IDs are load-bearing; reasoning is not |
| 14 | PHASE 8.5 STOP block | Extended SV-bypass explanation (5 sentences) | 92 | V-05 ceiling-form addition; the co-located STOP is what satisfies C-51 |
| 15 | PHASE 8.5 ×2 | Detection-failure consequence paragraphs | 56 | V-05 ceiling form; operative gate is the STOP line |

### Criteria verification: all essential criteria PASS

- **C-51** (co-located STOP gate): `STOP — NOTE-COMPLETION GATE` present immediately after PER-NOTE FORMAT TEMPLATE instruction, co-located per note, blocks until [C-NN] filled ✓
- **C-52** (SPAN DEFINITION pre-step): 4× SPAN DEFINITION with all 3 fields, immediately before each foil item ✓
- **C-49** (FORMAT TEMPLATE [C-NN] slot): PER-NOTE FORMAT TEMPLATE with `[C-NN]` slot present ✓
- **C-43/C-44** (dual evaluability paths): EVALUABILITY ARCHITECTURE COMPETITOR condensed but both criterion IDs cited; Phase 8.5 NON-REDUNDANCY DECLARATION intact ✓
- **C-48** (TIER-BLIND CATEGORIZER): Competitor + derivation instruction preserved; only 2 illustrative trailing sentences removed ✓
- **C-01–C-42**: All phases and structural sections intact ✓

Written to: `simulations/quest/golden/quest-rubric-QU5-simplified-2026-03-16.md`

```json
{"simplified_word_count": 2316, "original_word_count": 2900, "all_essential_still_pass": true}
```
