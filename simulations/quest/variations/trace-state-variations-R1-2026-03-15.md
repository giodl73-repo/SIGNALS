Written to `simulations/quest/golden/trace-state-variate-R1-2026-03-15.md` (updated for rubric v17).

---

## trace-state — Round 1 Variations (rubric v17)

### Variation Map

| Var | Axis | C-09 | C-10 | Hypothesis |
|-----|------|------|------|------------|
| V-01 | Output format — reachability-first layout | ? | **exp** | Opening with the coverage grid makes C-10 structural; grid-to-table mismatch makes omissions visible |
| V-02 | Lifecycle emphasis — negative path promoted to first-class peer section | **exp** | ? | Dedicated 4-element template per blocked op means the writer fills the form, not retrofits findings |
| V-03 | Phrasing register — per-criterion call-outs embedded inline | **exp** | **exp** | Naming each rubric criterion at the exact point of satisfaction gives the writer a continuous checklist |
| V-04 | Combined: role sequence — Domain Expert + Trace Developer + Concurrency Analyst | **exp** | **exp** | Dedicated Concurrency Analyst owns C-08/C-09 exclusively; can't defer to findings |
| V-05 | Combined: output format + inertia framing + reachability audit | **exp** | **exp** | Inertia challenge seeds C-09 rows; transition table enforces C-01–C-06; reachability audit closes C-10 |

---

### Key design decisions

**Why these axes vs R1's axes (role-seq, table-format, conversational, GATE-phases, inertia)?**

R1 was written against v1 of the rubric (9 criteria). v17 adds C-10 (reachability) and tightens C-09 to require all four elements explicitly. None of R1's variations structurally guaranteed both. These five variations specifically target the new failure modes:

- **V-01** introduces the reachability grid as an *opening deliverable* rather than a closing annotation — the grid must be filled before a single trace row is written
- **V-02** restructures the prompt so the negative path has its own scenario setup and per-blocked-op format template (not just a table under Adversarial Review)
- **V-03** embeds `(C-01a)`, `(C-02b)`, `(C-09 — all four elements required)` etc. as inline labels so criteria coverage is checkable during writing
- **V-04** splits the single Developer role into Developer (forward path) + Concurrency Analyst (negative path + race conditions) — structural role pressure rather than attention
- **V-05** chains inertia → state machine → transition table → reachability audit as a self-checking loop where each stage feeds the next

**Single-axis first:** V-01, V-02, V-03 are single-axis. V-04 and V-05 combine two or three axes. Run V-01–V-03 first to isolate which axis moves the needle on C-09/C-10 before evaluating the combined variants.
