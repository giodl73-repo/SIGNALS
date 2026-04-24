`simulations/quest/rubrics/flow-dataflow-rubric-v11-R11-2026-03-15.md` written — 5 complete variations.

**What each variation tests:**

| | Axis | Sequence | C-36 | C-37 | C-38 |
|---|---|---|---|---|---|
| **V-01** | Role sequence | Ops → Commerce → Finance | — | — | SC-11: Finance must cite [A-04] (skip-level) |
| **V-02** | Output format | Finance → Ops → Commerce | — | Parts A/B sole authority header | — |
| **V-03** | Inertia framing | Ops → Finance → Commerce | SC-11: no boundary before [A-01] complete | — | — |
| **V-04** | C-36+C-37 | Ops → Finance → Commerce | SC-11 | Parts A/B | — |
| **V-05** | All three | Commerce → Ops → Finance | SC-11 | Parts A/B | SC-12: Finance cites [A-04] (Commerce boundary, 2 roles prior) |

**Key R11 additions vs R10:**

- **C-36** closes with explicit sequencing prohibition language: "no boundary block and no stage trace may appear before [A-01] is fully produced" — plus the registry row annotates "(First artifact produced — SC-11 applies)" to make the token assignment non-arbitrary.
- **C-37** closes with the REGISTER DECLARATION header asserting "evaluator may determine C-34 and C-35 pass/fail by reading this section alone" and SC-9/SC-10 becoming callbacks that don't restate requirements.
- **C-38** closes with SC-12 naming the specific skip-level token ([A-04]) and Phase Gate 2 including a named checklist item that fails if [A-04] is absent from Finance's Citing line.
