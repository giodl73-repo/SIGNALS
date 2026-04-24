`corps-pr-variate-R13-2026-03-17.md` written to `simulations/quest/golden/`.

---

## R13 — corps-pr — 5 Variations

**Baseline gap summary**: R11 V-05 scores 27/27 aspirational against v10. Against v11 it fails three criteria, each requiring decomposition of a previously monolithic element into named, independently auditable sub-components.

---

### Variation Axes

| V | Axis | Criterion | Single change from R11 V-05 |
|---|------|-----------|----------------------------|
| V-01 | Lifecycle emphasis | C-36 | Phase C exit condition item (3) adds: "a C2 RESULT before its role's READ RECEIPT is a Phase C exit-condition failure; Phase D does not begin" |
| V-02 | Output format | C-37 | Replaces separate "C2 Receipt Check" block + standalone terminal line with unified "C2 RESULT" block that contains per-field (a)-(e) PRESENT/ABSENT verdicts and the terminal "C2 RESULT: SATISFIED [all five PRESENT]" in one block |
| V-03 | Phrasing register (schema) | C-38 | F-01 Description template changes from prose `"IA found X; role rates P-N because Y"` to `[IA-VERDICT: ...] | [ROLE-MECHANISM: ...]` as separately-labeled columns/slots visible in output |
| V-04 | Lifecycle + Output format | C-36 + C-37 | V-01 + V-02 combined |
| V-05 | All three | C-36 + C-37 + C-38 | V-01 + V-02 + V-03 combined — 30/30 target |

---

### Key structural distinctions per criterion

**C-36 gap in V-05 (R11)**: Item (3) in Phase C exit condition read `"READ RECEIPT precedes C2 RESULT per role in the output [C-35]"` — listed as a condition but made no statement that violation is a phase-gate failure. C-36 requires the exit condition to explicitly state that violation elevates to a Phase C failure (not a C-35 output format gap alone), blocking Phase D. Exact analog to how C-30 elevated PRE-COMMITMENT absence from a C-27 format issue to a phase-gate violation.

**C-37 gap in V-05 (R11)**: The C2 block was a two-part structure: a "C2 Receipt Check" block with per-field present/absent lines, then a standalone `C2 RESULT: SATISFIED` terminal line. C-37 requires the per-field enumeration to appear *within* the C2 RESULT block — the terminal line must derive visibly from per-field verdicts above it in the same block. A reviewer auditing only the `C2 RESULT: SATISFIED` line finds no per-field evidence without reading the preceding check block.

**C-38 gap in V-05 (R11)**: F-01 Description format was `"IA found [verdict]; [role] rates P-N because [mechanism]"` — both C-34 components present but no named labels. C-38 requires `[IA-VERDICT: ...]` and `[ROLE-MECHANISM: ...]` to appear as literal label strings in the output cell. V-05's findings table had no `[IA-VERDICT]` or `[ROLE-MECHANISM]` column headers or inline labels. Compliance is not verifiable at component granularity without prose parsing.
