Saved to `simulations/quest/rubrics/draft-spec-rubric-v9-variate-R9-2026-03-15.md`.

---

## Round 9 — Axis Map

| V | Primary Axis | Hypothesis |
|---|-------------|------------|
| **V-01** | **C-28 single** — PM pre-assignment gates inertia via named [PM-CONTRACT-SEAL]; INERTIA ANALYSIS REQUIRES header names it explicitly. Minimal base (merged table, no C-22/C-23/C-27). | C-28 passes on any base where the gate name appears in the inertia phase REQUIRES header — no split registers or imperative phrasing required |
| **V-02** | **C-29 single, inline** — Elimination Path cells carry mandatory "R-ID: R-XX — [reason]" sub-slot. AMPLIFIED rows require risk dimension + R-ID both. On V-01 base. | C-29 passes via inline embedding; the sub-slot makes omission structural rather than invisible; AMPLIFIED dual requirement is satisfied by prepend syntax |
| **V-03** | **C-29 single, column** — Dedicated "Req Closed (from [PM-COVERAGE-TABLE])" column in [INERTIA-TABLE] separate from Elimination Path prose. On V-01 base. | C-29 satisfies via column isolation; blank column cell is more immediately visible than missing inline sub-slot; tests which format is the stronger implementation |
| **V-04** | **C-28+C-29 combined** — R8 V-04 base (split [IG-REGISTER]/[ID-REGISTER], C-22/C-23, C-26 Branch B sub-conditions, C-27 imperative phrasing; no C-24). [IG-REGISTER] Elimination Path gains R-ID slots. | C-28+C-29 compose with split registers; [IG-REGISTER] carries hypothesis + Elimination Path + R-ID while [ID-REGISTER] carries risk + defeat; no axis conflict with C-26/C-27 |
| **V-05** | **Full combination** — All 29 v9 criteria. R8 V-05 base + C-28 gate on INERTIA ANALYSIS + C-29 R-ID slots in [IG-REGISTER] Elimination Paths. CASCADE TO annotations on all unified declarations (C-24). Ordinal markers on both CNS slots (C-19). | 175/175 composite under v9; PM-first ordering makes R-IDs available at inertia-write time; all gate tokens carry invalidity rules; all unified declarations carry CASCADE TO; two CNS locations marked "location 1 of 2 / 2 of 2" |

**Key structural change across all variations**: Phase sequence flips from R8's `Inertia (0B) → PM Pre-Assignment (1)` to R9's `PM Pre-Assignment (1) → Inertia Analysis (2)`, with the inertia phase carrying `REQUIRES: [PM-CONTRACT-SEAL] from Phase 1` as the structural gate (C-28). C-29 is satisfied by requiring named R-IDs from [PM-COVERAGE-TABLE] in each Elimination Path cell before inertia analysis can seal — PM-first ordering is what makes those IDs available.
