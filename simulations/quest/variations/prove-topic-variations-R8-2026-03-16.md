Written to `simulations/quest/golden/prove-topic-variate-R8-2026-03-16-v8.md`.

---

## Round R8 -- 5 Variations

**Three single-axis, two combined.** All built on the R7 full-stack base (C-27+C-28+C-29 present in all variations) with surgical targeting of C-30, C-31, C-32.

| Variation | Axis | C-30 | C-31 | C-32 |
|-----------|------|------|------|------|
| V-01 | Stage 5 entry gate cross-references `displacement_read_contract` by field name | FAIL | **PASS** | FAIL |
| V-02 | `evidence_summary` instruction is mandatory, names websearch/interview/prototype explicitly | **PASS** | FAIL | FAIL |
| V-03 | Stage 5 EXIT SIGNAL names each artifact type individually (not count assertion) | FAIL | FAIL | **PASS** |
| V-04 | C-31 + C-30 combined | **PASS** | **PASS** | FAIL |
| V-05 | Full stack -- all three | **PASS** | **PASS** | **PASS** |

**Key discriminations:**

- **C-31** fires only when Stage 5 ENTRY CONDITIONS says `[per ROLE A displacement_read_contract -- ...]`. Without that field-name cross-reference, C-28 passes but C-31 fails.
- **C-30** fires only when `evidence_summary` instruction uses mandatory language: `Must cite all three... Mandatory -- not conditional. Omission = FAIL.` Conditional phrasing ("where available") or Stage-4-verdict-only citation fails C-30.
- **C-32** fires only when EXIT SIGNAL individually enumerates: `websearch Displacement read, interview Displacement read, prototype Displacement read`. "All three confirmed" (count assertion) passes C-29 but fails C-32.

**R9 open target:** C-10 -- no variation in any round yet anchors a ROLE 2 displacement loop role at Stage 3 to close the three-point displacement loop.
