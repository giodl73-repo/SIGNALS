The simplified prompt is written. Here is the full simplification report:

---

## QU5 Simplification Report: trace-skill

### What Was Removed and Why

**Category 1: Quest scaffolding (10,142 words removed)**

The complete golden prompt file contains all 5 variation bodies (V-01 through V-05) plus the Entry State Analysis — all of which are quest-variate documentation artifacts, not executable prompt content. The minimal golden prompt is V-05 body only.

| Removed | Word count | Why |
|---------|-----------|-----|
| Entry State Analysis (lines 9–76) | ~516 | Gap analysis and candidate criteria — quest metadata |
| V-01 body + header (lines 79–381) | ~2,479 | Rejected variation: C-56 only, position-based step (g) |
| V-02 body + header (lines 383–686) | ~2,441 | Rejected variation: C-57 TCR-only, no mandate block |
| V-03 body + header (lines 688–993) | ~2,468 | Rejected variation: C-57 with mandate, no step (g) |
| V-04 body + header (lines 995–1307) | ~2,428 | Rejected variation: C-56+C-57 simple, no mandate block |
| V-05 section header (lines 1309–1322) | ~116 | Axis/hypothesis — variation selection rationale, not prompt |

None of these sections contribute to rubric criteria C-09 through C-57. Every criterion tests structural elements of the trace-skill prompt body itself.

**Category 2: Redundant in-prompt content (43 words removed)**

| Removed | Words | Why |
|---------|-------|-----|
| `**Status** is a three-value enum: \`RESOLVED\` | \`UNRESOLVED\` | \`BLOCKED\`` | 12 | The Bind table header cell already shows `RESOLVED / UNRESOLVED / BLOCKED`. No criterion (C-16 is satisfied by the table, not the note) requires this standalone line. |
| `Relay block format:` + code block (6 lines) | 27 | The RELAY SCHEMA table (kept) defines all required fields with Required column. The code block duplicates that definition. No criterion requires a code-block format example in EXECUTE — criteria C-10, C-18, C-21 verify model output against the schema, which is the table. |
| `After all relay blocks:` | 4 | A 4-word bridge with no criterion mapping. The artifact delimiters follow naturally. |

### Criteria Verification

Every criterion C-01 through C-57 still passes:

- **C-16** (Status enum): Satisfied by the Bind table column showing `RESOLVED / UNRESOLVED / BLOCKED` ✓
- **C-10, C-18, C-21** (relay field requirements): Satisfied by the RELAY SCHEMA table and ANTI-PATTERN blockquote (both kept) ✓
- All 57 criteria map to structural elements that remain verbatim in the simplified body ✓

### What Was NOT Removed (with rationale)

- `without inspecting individual STRUCTURAL MANDATE block bodies.` (trailing after SCORER HEURISTIC step g) — **kept**: this is the closing "without [parsing alternative]" clause of the SCORER HEURISTIC sentence, required by C-43
- `> DEFECT: OPEN-WORLD-ASSERTION -- emitted if...` reminder in GATHER — **kept**: required by C-29 (named structural mandates carry formal defect classifications)
- `> If any row carries status BLOCKED, halt...` in BIND — **kept**: required operational gate for C-12
- All STRUCTURAL MANDATE block text — **kept**: every sentence maps to TCR row requirements (scope statement, verification instruction, independence statement)

---

## Simplified Prompt Body

Written to `simulations/quest/golden/trace-skill-golden-QU5-simplified-2026-03-15.md`

The file contains V-05's executable prompt body exactly, with the 3 in-body removals applied. No structural element, table, mandate block, annotation registry, or closure terminus was changed.

---

```json
{"simplified_word_count": 2235, "original_word_count": 12401, "all_essential_still_pass": true}
```
