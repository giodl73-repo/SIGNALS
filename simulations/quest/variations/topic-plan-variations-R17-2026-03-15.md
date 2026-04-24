Written to `simulations/quest/golden/topic-plan-variate-R17-2026-03-15.md`.

---

## Round 17 — topic-plan Variations (v17 rubric, C-52+C-53 new)

**Gap analysis** from R16 V-05:
- R16 V-01–V-04: threshold states bare N ("passes when all 11 confirmed") with arithmetic in a SEPARATE labeled field — fails C-52's letter requirement (arithmetic not inside the threshold annotation)
- R16 V-01–V-04: §5b treated as inline Phase 5 instruction, no Gate-0 check item — fails C-53

**Variation map:**

| Variation | Axis | C-52 | C-53 | Key gate-0 form |
|-----------|------|------|------|-----------------|
| V-01 | Output format | YES | NO | `GATE-0 PASS THRESHOLD: 8 declared schemas + 3 structural checks = 11 items total; passes when all 11 items confirmed; blocked by any single STOP result.` |
| V-02 | Lifecycle emphasis | NO | YES | §5b promoted to Check [A6]; threshold bare-count: "passes when all 12 items confirmed" — arithmetic separate (C-52 absent) |
| V-03 | Phrasing register | YES | NO | Arithmetic in threshold, hypothesis-test opening, **C-49 absent** (no attestation clause) |
| V-04 | Combined output+lifecycle | YES | YES | `GATE-0 PASS THRESHOLD: 9 declared schemas + 3 structural checks = 12 items total; passes when all 12 items confirmed; blocked by any single STOP result.` + §5b as [A6] |
| V-05 | Full ceiling (C-43–C-53) | YES | YES | V-04 structure + **role sequence** change: §5b runs FIRST in Phase 5 (before scope filtering), Phase 5 auth = `§5b §5 §6 §7`, §5b evaluates against ALL new evidence pre-scope |

**C-52 mechanical difference (V-01/V-04/V-05 vs R16):** R16 had two separate fields — `Arithmetic decomposition: 8 declared schemas... = 11 items total` then `GATE-0 PASS THRESHOLD: passes when all 11 confirmed`. C-52 requires the derivation inside the threshold field itself: reading the THRESHOLD line alone must reveal the formula. Adding a schema block must update M and N in one place.

**C-53 mechanical difference (V-02/V-04/V-05 vs R16 V-01–V-04):** Without a schema block, §5b has no Gate-0 check item and cannot be detected as absent. As a named schema block it gets Check [A6], participates in the item count arithmetic (+1 to M, +1 to N), and appears in the condition-line conjunction — making its omission detectable by Gate-0.

**V-05 role sequence addition:** §5b runs before §5 scope to ensure NO CHANGE is evaluated against the full new-evidence set — not the scope-filtered subset. This surfaces a structural question C-53 doesn't address: whether the phase-relative position of §5b (before vs. after scope) should be declared in the schema block's phase-authorization note.
