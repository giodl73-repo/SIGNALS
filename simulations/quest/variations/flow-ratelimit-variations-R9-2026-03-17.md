Here are the 5 complete variations for **flow-ratelimit Round 9**, written to `simulations/quest/golden/flow-ratelimit-variate-R9-2026-03-17.md`.

---

## Summary

**Core R9 problem:** V-01 in R8 passed C-21 (full gate chain) and C-24 (terminal reconciler) but failed C-19 — the UX role was implied in a multi-purpose role and the four-field constraint was never a named gate deliverable. C-26 closes this: the UX section must be an explicitly numbered role whose gate condition names all four fields individually, so C-24's check (b) can audit UX completeness automatically.

### Variation axes

| V | Axis | C-26 mechanism | Novel structural element |
|---|------|----------------|--------------------------|
| V-01 | Single: Role sequence | Role 6 is explicitly numbered; Gate 6→7 lists FIELD-A/B/C/D as four separate blocking checklist items | Field-level blocking gate checklist on an explicitly numbered UX role |
| V-02 | Single: Format Contract schema | Schema B in the Format Contract declares the four fields as canonical; Schema B STRUCTURAL REJECTION CLAUSE is scan-time detectable | UX-specific scan-time structural clause parallel to Schema A column enforcement |
| V-03 | Single: Phase lifecycle | Phase 4 gate is a six-item blocking checklist; each of the four fields is a separately evaluated gate condition that cannot be satisfied by completing other tiers | Per-field phase-transition blocking; Verdict currency checks embedded at each phase boundary (C-22) |
| V-04 | Combined V-01+V-02 | Role gate enumerates fields + Format Contract provides canonical Schema B authority | Dual-authority: gate conditions reference Schema B by name; two-tier rejection clause taxonomy (C-25) from the combination |
| V-05 | Combined V-01+V-02+V-03 | All three mechanisms active simultaneously; any single failure triggers Schema B STRUCTURAL VIOLATION + gate blocking + Claim (d) revision | Triple-enforcement: a missing field is simultaneously a scan-time schema violation, a gate violation, and a Verdict claim revision — no single mechanism can be bypassed without the others catching it |

All five variations target **120/120** (all 5 essential + 3 recommended + 18 aspirational, including C-26).
