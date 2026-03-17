Written to `simulations/quest/golden/program-plan-variate-R14-2026-03-16.md`.

---

## program-plan -- R14 Variate Prompt Bodies (V-01 through V-05)

**R13 state under v14 rubric:**
| Variant | C-44 | C-45 | C-46 | Score |
|---------|------|------|------|-------|
| V-01 | FAIL | FAIL | FAIL | 255/285 |
| V-02 | FAIL | FAIL | FAIL | 255/285 |
| V-03 | PASS | FAIL | FAIL | 260/285 |
| V-04 | FAIL | PASS | FAIL | 260/285 |
| V-05 | FAIL | PASS | PASS | 265/285 |

**R14 design constraint:** All 5 variations satisfy C-44 + C-45 + C-46, targeting 285/285.

---

### Variation axes

| Variant | Axis | C-44 form | C-45 form | C-46 form |
|---------|------|-----------|-----------|-----------|
| **V-01** | Phrasing Register (compact table-first) | 3-column table `\| field \| criterion \| tag \|` in header | Single-line cross-refs in each direction | `# Co-location family verified (C-41 index above)` |
| **V-02** | Structural Foreground (bounded teaching unit) | Inline: `# C-26: gate_fail: field carries # WRONG C-04` | "Bounded unit" language; C-42 references the bounded BAD PLAN header | `# Exit marker (C-46): all annotation types from header index confirmed present` |
| **V-03** | Enumeration Format (numbered list C-42 + C-41) | Enumeration entries: `(1) gate_fail: → C-04 → tag: # WRONG C-04` | C-42 footer references `BAD PLAN header below`; C-41 header references `enumeration above` | `# All three co-location annotations from the enumeration above confirmed present` |
| **V-04** | C-44 + C-45 Combined (per-entry rule pointers) | Each entry embeds its own back-reference: `carries # WRONG C-04 (rule in FIELD CO-LOCATION PRINCIPLE above)` | C-42 table has a `BAD PLAN header entry` column with per-row forward pointers | `# Co-location family verified (C-41 index above)` |
| **V-05** | Full Integration (BLOCK SPECIFICATION PROTOCOL) | `# C-26 → gate_fail: carries # WRONG C-04: Why: ...` in "Component 1" header | Protocol section names `Component 1 below / Component 2 / Component 3`; C-41 header names `Component 1 of BLOCK SPECIFICATION PROTOCOL above` | `# BLOCK SPECIFICATION PROTOCOL -- Component 3: Exit Verification (C-46) -- all types confirmed` |

**Key C-44 principle:** Every C-41 index entry must state the exact `# WRONG C-XX` tag string — not just field type + criterion number. V-03's R13 form achieves this; V-01/V-02/V-04/V-05 of R13 left tag-string verification as a block-scanning task.
