Written to `simulations/quest/golden/corps-chart-variate-R14-2026-03-17.md`.

---

## R14 Variations — Summary

**Two target criteria:** C-35 (HALT header embeds schema recall) and C-36 (ROLE-NAME LOCK embeds per-cell notes adjacent to role list).

**The R13 V-05 gaps being closed:**
- C-35: R13 V-05 had `BEFORE PRODUCING -- re-read FORMAT CONTRACT schema (N):\nHALT.` — the schema citation was in the label line above the HALT, not in the HALT line. Fix: `HALT. Re-read FORMAT CONTRACT schema (N) -- [name].`
- C-36: R13 V-05 had `[per-cell directive: verify each cell against this list...]` inside the SITES ENUMERATION. Fix: Move full-form notes (`[DRI/Owner -- per-cell: for each cell in this column, verify the value appears in this list before populating the next row -- do not complete the table and verify after]`) to immediately after the role-name list, adjacent to the enumeration.

| ID | Axis | Base | C-35 | C-36 |
|----|------|------|------|------|
| V-01 | C-36 only | R13 V-01 (no FC) | N/A | Full adjacent notes at sites 2+5 |
| V-02 | C-35 only | R13 V-02 (has FC, single-site DRI/Owner) | Schema in HALT header at all 5 FC steps | — |
| V-03 | C-36 only | R13 V-03 (STOP/audit variant, no FC) | N/A | Full adjacent notes + STOP audit checks the notes |
| V-04 | C-35 + C-36 | R13 V-04 (C-33+C-34, has FC) | Schema in HALT header | Full adjacent notes |
| V-05 | Full integration | R13 V-05 (max stack, C-20–C-34) | Schema in HALT header | Full adjacent notes; sites enumeration also cross-references |

V-05 is the golden attempt — all 36 criteria targeted.
