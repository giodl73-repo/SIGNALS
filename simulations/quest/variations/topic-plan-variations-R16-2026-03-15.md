Written to `simulations/quest/golden/topic-plan-variate-R16-2026-03-15.md`.

---

## Summary

**5 complete variations for `topic-plan` Round 16** targeting C-50 (semantic category grouping) and C-51 (pass/halt co-location in labeled field):

| Variation | Axis | C-50 | C-51 | C-49 | Key Gate-0 structure |
|-----------|------|------|------|------|----------------------|
| **V-01** | Lifecycle emphasis | YES | NO | YES | Grouped condition line + inline halt annotation |
| **V-02** | Output format | NO | YES | YES | Flat AND-conjunction + `GATE-0 PASS THRESHOLD:` field |
| **V-03** | Phrasing register | YES | YES | NO | Grouped + labeled THRESHOLD, no attestation clause |
| **V-04** | Combined LC + OF | YES | YES | YES | Grouped + labeled THRESHOLD + attestation |
| **V-05** | Full ceiling | YES | YES | YES | V-04 + §5b inertia evaluation block (12-item Gate-0) |

**Critical differences at Gate-0:**

- **C-50** discriminator: grouped (`schemas [A1][A2]...[A8] all present + phase index [B] + ...`) vs flat (`[A1] AND [A2] AND ... AND [D]`)
- **C-51** discriminator: `GATE-0 PASS THRESHOLD: passes when all N confirmed; blocked by any single STOP result` as a dedicated labeled field vs pass/halt as clauses in an inline annotation sentence

**V-05 adds one new schema (§5b)**, raising the item count from 11 to 12 and testing whether the grouped condition line scales cleanly when the schema inventory grows — which is precisely the structural guarantee C-50 was designed to provide.
