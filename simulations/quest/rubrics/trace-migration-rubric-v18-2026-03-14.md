Written to `simulations/quest/rubrics/trace-migration-rubric-v18-2026-03-15.md`.

**v17 → v18 summary:**

| New | Chain position | What it tests |
|-----|---------------|---------------|
| **C-51** | STATUS QUO COST FRAME pre-parse positioning | C-36 passes if the frame precedes Q1. C-51 passes only if it precedes the parse phase itself — before the CONSTRAINT TYPE REGISTRY, before any phase architecture is built. The baseline becomes an entry condition for the entire analytical pipeline, not just Phase A. |
| **C-52** | B2 as explicit STATUS QUO COST FRAME closure | C-39 passes if B2 names a cross-role causal chain. C-52 passes only if B2 is explicitly named as the narrative close of the STATUS QUO COST FRAME — creating an auditable open/close pair. Pairs with C-51: frame opened pre-parse, frame closed at B2. |
| **C-53** | ENTRY REFERENCE structural incompleteness verdict | C-48 passes if the ENTRY REFERENCE includes an inline rationale note. C-53 passes only if the prompt escalates the absence of that note to a named structural incompleteness verdict — the same enforcement register as a missing BOUNDARY PROTOCOL block, not a missing-element warning. |

**Scoring:** 300 → **315 pts** · 50 → **53 criteria** · 45 → **48 aspirational** · Golden 206 → 206 (**65%**).

The STATUS QUO COST FRAME now has a complete two-level placement chain (C-36 pre-Q1 → C-51 pre-parse) and a named closure pair (C-51 open → C-52 B2 close). The ENTRY REFERENCE completeness chain is now three levels: C-46 (annotation present) → C-48 (rationale at point of use) → C-53 (absence is a named structural failure).
