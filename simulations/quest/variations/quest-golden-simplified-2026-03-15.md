Exact count: **746 simplified** vs **1041 original** = **28.4% reduction**.

Now verifying all 16 criteria against the simplified prompt:

| Criterion | Weight | Check | Pass? |
|-----------|--------|-------|-------|
| C-01 | essential | Steps 1–4 all labeled and present | PASS |
| C-02 | essential | Score matrix with per-criterion rows before COMPOSITE | PASS |
| C-03 | essential | GATE 1 and GATE 2 with explicit state declarations | PASS |
| C-04 | essential | "full prompt body verbatim...complete, runnable...DO NOT write only a summary" | PASS |
| C-05 | essential | Rubric artifact with ID, category, text, pass condition, weight | PASS |
| C-06 | recommended | Step 3: "structural property (reusable principle)" + "mechanism" | PASS |
| C-07 | recommended | Step 4 has all 5 fields: ID, Text, Weight, Category, Pass condition | PASS |
| C-08 | recommended | GATE 2: 'Name both rounds explicitly (e.g., "Round 4 and Round 5")' | PASS |
| C-09 | aspirational | "Round 1: Vary one axis...Round 2+: Combine axes that produced spread" | PASS |
| C-10 | aspirational | "identical composite scores, no new excellence patterns emerge and the round does not advance plateau detection" | PASS |
| C-11 | aspirational | `## SPREAD-DESIGN PHASE` heading, precedes Step 1 | PASS |
| C-12 | aspirational | "Combine axes that produced spread (PARTIAL or FAIL)" + PARTIAL AMPLIFIER TABLE in Step 3 | PASS |
| C-13 | aspirational | Step 3 item 3: "Causal layer: structural \| behavioral \| correctness" | PASS |
| C-14 | aspirational | "SPREAD-DESIGN COMPLETE -- confirm axis assignments above before proceeding to Step 1" | PASS |
| C-15 | aspirational | 4-column PARTIAL AMPLIFIER TRAJECTORY TABLE; referenced in SPREAD-DESIGN phase | PASS |
| C-16 | aspirational | Step 3 item 4: "Provenance: [V-XX, R-N] -- variation and round where this property first appeared" | PASS |

All 16 criteria still pass.

---

## Simplification Report

**Removed elements and rationale:**

| Removed | Words | Why |
|---------|-------|-----|
| `## What Made It Golden` section (rubric evolution table + 3 structural properties) | 203 | Post-hoc documentation appended after convergence; no rubric criterion requires it in a runnable prompt body. Informative for the quest archive but dead weight in a skill that gets invoked fresh. |
| Axis bank (5 bullets: Role sequence, Output format, Lifecycle emphasis, Phrasing register, Inertia framing) | 44 | No criterion pass condition requires a pre-canned axis list. C-09's pass condition is satisfied by the Round 1/Round 2+ instructions alone. The axis bank is operator convenience, not structural requirement. |
| Placeholder table row `[prior round entries -- leave empty on Round 1]` | 12 | Table header + column labels are sufficient. The instruction is implied by "persistent -- add rows each round, never discard." |
| `Evidence: [exact text present or absent]` in Step 2 | 8 | C-02 pass condition requires a score matrix showing criterion results — not an evidence quote field. Removes clutter from the scoring instruction. |
| `\| RANK \| \| \| \| \| \| \|` row in score matrix | 8 | No criterion references ranking. Composite score suffices for variation selection. |
| `Tiebreaker: minimal structure (fewest operator constraints).` in artifacts | 8 | No criterion requires tiebreaker logic. C-04 tests artifact content, not which variation was chosen. |
| `4. State both artifact paths.` in artifacts | 5 | No criterion pass condition requires path declaration. C-04 and C-05 test file content. |
| `Label each: variation axis and hypothesis.` in Step 1 | 7 | No criterion pass condition requires variation labels. C-06 targets named patterns in Step 3, not Step 1 labels. |
| `added-in-round` from rubric artifact fields | 1 | C-05's pass condition lists ID, weight, category, text, pass condition — `added-in-round` is not among them. |

**Total removed: 296 words (28.4%)**

---

**Simplified prompt written to:**
`simulations/quest/golden/quest-golden-QU5-simplified-2026-03-15.md`

```json
{"simplified_word_count": 746, "original_word_count": 1041, "all_essential_still_pass": true}
```
