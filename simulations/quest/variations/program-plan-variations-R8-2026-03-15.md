The R8 variate file is written to `simulations/quest/golden/program-plan-variate-R8-2026-03-16.md`.

---

## R8 Variate Summary — `program-plan` (Round 8)

**Rubric v8 context:** 23 aspirational criteria (C-08 through C-30). Three new criteria this round:

| New Criterion | Requirement | First seen in |
|---|---|---|
| **C-28** | `gate:` production field as sibling alongside `gate_fail:`/`gate_pass:` | R7 V-02/V-03 |
| **C-29** | Correction table includes C-05/C-06/C-07 wrong-to-correct pairs | R7 V-02 |
| **C-30** | Dep reminder AND correction bridge present independently at each dep-bearing `skills:` line | R7 V-03 |

**Five variations generated:**

| Variation | Single axis | Key change | Target gain |
|---|---|---|---|
| **V-01** | Gate structure | `gate_fail:` / `gate_pass:` / `gate:` as YAML sibling keys + `# WRONG C-04` + `# Why:` | C-24, C-25, C-26, C-28 |
| **V-02** | Correction table | 13-row table with C-05/C-06/C-07 rows + scaffold bridges | C-18, C-19, C-21, C-22, C-29 |
| **V-03** | Dep reminders | Zone headers + skills lines get dual annotation; BAD YAML gets criterion tags | C-16, C-20, C-23, C-27, C-30 |
| **V-04** | Combo C-28+C-29 | Three-field gates + full correction table; no skills-line dep reminders | ~18-19/23 |
| **V-05** | Golden synthesis | All five clusters simultaneously | 23/23 |

The V-05 template uses 5 explicitly labeled zone headers (`Zone 1` through `Zone 5`), three-field gate structure at every non-echo zone with `# WRONG C-04` + `# Why:` annotations, a 13-row correction table covering all three recommended criteria, uniform `# requires: <artifact> from Zone: <name> (C-05)` syntax at both header and skills positions, and independent correction bridges at every dep-bearing skills line.
