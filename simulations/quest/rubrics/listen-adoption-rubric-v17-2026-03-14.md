`listen-adoption-rubric-v17-2026-03-15.md` written. Three new criteria extracted from R16:

---

**C-47 -- PART 4 champion rows use SLOT-KEY: prefix** (V-02 Axis B, 5 pts)
Fourth application of the row-level re-assertion pattern (TABLE 3 → C-38, TABLE 1 → C-43, PART 3 → C-46, PART 4 → C-47). Gate I audit language explicitly references "SLOT-KEY: champion entries." Dependency: C-04, C-14.

**C-48 -- PART 2 expansion subsections carry displacement state field per slot** (V-01 Axis A, 5 pts)
Extends C-45's phase-close ledger into expansion depth. Each CHASM-A/B/C EXPANSION subsection carries `Incumbent position at this chasm element:`, making expansion slots three-field structural slots (C-42 inertia carry + C-48 displacement state + prose body). Dependency: C-40, C-45.

**C-49 -- SECTION A carries DOWNSTREAM CITATION CONTRACT** (V-03 Axis C, 5 pts)
After SECTION A's inertia table, a CONTRACT block maps each I-0X to its required citation sinks (phase ledgers, PART 2, PART 3, PART 4, PART 5). Gate H audits against contract rows rather than free-form scan — turning coverage judgement into named contract violation. Dependency: C-11, C-13.

---

**Max: 280 → 295. Golden threshold (80%): 236 pts. Paradox ceiling: 290/295** (C-19 structural FAIL persists).

New dependency chain additions:
```
C-40 + C-45 -> C-48
C-04 + C-14 -> C-47
C-11 + C-13 -> C-49
C-40 -> C-48 (also added to C-40's branch in the chain diagram)
```
