Written to `simulations/quest/variations/discover-literature-variations-R19-2026-03-20.md`.

---

## discover-literature Variations R19

**Criterion probed: C-37** (Chain-Completion Statement Extended to C-36 as Current Terminal)
**Rubric**: v19 (ceiling 235)

| V | Axis | Predicted |
|---|------|-----------|
| V-01 | Wrong-terminal: chain ends at `C-33 complete` (C-35 canonical form, not extended) | C-37 FAIL = 230/235 |
| V-02 | Interior-gap: C-34 skipped (`... -> C-33 -> C-35 -> C-36 complete`) | C-37 FAIL = 230/235 |
| V-03 | Interior-gap: C-35 skipped (`... -> C-33 -> C-34 -> C-36 complete`) | C-37 FAIL = 230/235 |
| V-04 | Double interior-gap: both C-34 and C-35 skipped (`... -> C-33 -> C-36 complete`) | C-37 FAIL = 230/235 |
| V-05 | Full synthesis: chain correctly extended (`... -> C-33 -> C-34 -> C-35 -> C-36 complete`) | C-37 PASS = 235/235 |

**Axis structure**: All five variations pass C-36 (analogy "C-34 is to C-33 what C-25 is to C-23" correctly placed inside the sub-section in all five). C-37 is the sole differentiator. V-01 through V-03 probe single failure modes independently; V-04 combines both interior-gap failures simultaneously; V-05 is the full ceiling form.

The parallel to C-35/R17 is exact: C-35 caught the wrong-terminal failure where the chain stopped at `C-32 complete` instead of `C-33 complete`. C-37 catches the R18 equivalent -- a chain that was not extended from `C-33 complete` to include C-34, C-35, and C-36 as the new terminal links.
