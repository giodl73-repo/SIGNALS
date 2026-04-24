Written to `simulations/quest/golden/topic-open-variate-R3-2026-03-17.md`.

---

## Round 3 Variations — Summary

**Root cause from R2**: All 5 variations scored 88 but failed C-01. The TOPICS.md row template dropped `{YYYY-MM-DD}` in every variation. C-16 and C-17 are the two new aspirational criteria targeting this and the sequencing rationale gap.

---

| Var | Axis | C-16 Strategy | C-17 Strategy | Base |
|-----|------|---------------|---------------|------|
| **V-01** | Template lock | Named `TOPICS.md ROW TEMPLATE` block, physically separated, referenced twice | Inherits R2 V-04 sequencing; rationale-before-table stated positionally | R2 V-04 structure |
| **V-02** | Causal sequencing | Template provided at write time with "do not reconstruct" | Every ordering instruction has a "because" clause: vocab first / rationale first / check after | R2 V-05 structure |
| **V-03** | Conversational register | Three-field template with explicit `{YYYY-MM-DD}` in Step 5 | Step 2 explains *why* rationale precedes table in "you" voice | R2 V-03 style + C-01/C-06 fixes |
| **V-04** | C-16 + C-17 + full scaffolding | First-class `TOPICS.md ROW TEMPLATE` block + write-time reference | Three causal points: vocab placement, rationale ordering, post-gen timing | R2 V-04 phases |
| **V-05** | C-16 + C-17 + compact | ROW TEMPLATE as second named block after VOCABULARY CONSTRAINT | DEFAULTS TABLE row + inline "because" in Phase 2 sequencing instruction | R2 V-05 compact |

**V-04/V-05 predicted**: 9/9 aspirational, 5/5 essential → composite 100 if essential criteria hold. **V-01/V-02**: 8–9/9 aspirational depending on whether single-axis is sufficient. **V-03**: 9/9 aspirational, but C-06 is now explicit (≥ 2 namespaces stated in Step 3 minimums).
