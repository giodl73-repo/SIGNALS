Written to `simulations/quest/rubrics/trace-migration-rubric-v19-2026-03-15.md`.

**v18 → v19 summary:**

| New | Chain position | What it tests |
|-----|---------------|---------------|
| **C-54** | FRAME CLOSURE STATEMENT enforcement (parallel to C-53) | C-52 passes if closure statement is present at B2. C-54 passes only if the prompt also names the absent-statement verdict — "An absent or placeholder FRAME CLOSURE STATEMENT row means B2 is not explicitly positioned as the STATUS QUO COST FRAME close." Same escalation pattern as C-48 → C-53 for ENTRY REFERENCE, now applied to B2. |
| **C-55** | STATUS QUO COST FRAME placement as DIRECTIVE infraction | C-51 passes if the frame precedes the parse phase. C-55 passes only if late placement is named as a DIRECTIVE violation — "A STATUS QUO COST FRAME that first appears after constraint type enumeration has begun violates this directive." Enforcement register distinction: aspirational miss → DIRECTIVE infraction. |
| **C-56** | STATUS QUO COST FRAME universal scope claim | C-51 passes if the frame precedes parsing. C-56 passes only if the prompt explicitly declares that ALL subsequent content operates within the frame — "Everything that follows operates within this frame." Scope declaration vs. placement: C-51 tests position, C-56 tests whether the frame's coverage domain is stated rather than inferred. |

**Scoring:** 315 → **330 pts** · 53 → **56 criteria** · 48 → **51 aspirational** · Golden 206 → 206 (**62%**).

The FRAME CLOSURE STATEMENT now has a named absent-verdict (C-54), closing the STATUS QUO COST FRAME enforcement chain to parallel the ENTRY REFERENCE chain: `C-52 (present) → C-54 (absence = named failure)` mirrors `C-48 (present) → C-53 (absence = named failure)`. The STATUS QUO COST FRAME is now fully specified at three dimensions: placement (C-51), enforcement register (C-55), and scope declaration (C-56).
