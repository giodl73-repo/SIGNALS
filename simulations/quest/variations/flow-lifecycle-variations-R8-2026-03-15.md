Here are the 5 complete variations for `flow-lifecycle` Round 8 / Rubric v8, written to `flow-lifecycle-variate-R8-v8-2026-03-15.md`.

---

## Summary

**Invariants across all 5**: C-27 (scan table with "Defect Type if OPEN" column; gate sentence references "the Defect Type column" by name and enumerates ≥4 defect categories) and C-28 (Handler column header carries both the backward-trace rule and `Mandatory; blank or uncertified role is a fail`).

### V-01 — Role Sequence: Lifecycle-Type-Driven Derivation
Adds a `LIFECYCLE CONTEXT DECLARATION` block before Step 1, with a reference vocabulary per class (L2O, P2P, Period Close, Case). Gate 0 fires before the Role Registry opens. Hypothesis: constraining role-title vocabulary to a named lifecycle class eliminates generic labels at the earliest possible point, before any table is opened.

### V-02 — Output Format: Maximum Schema Density
Eliminates the Field Content Rules preamble block entirely. Every constraint moves inline into column headers using fail-language at point of use (`does not count`, `is a fail`, `Mandatory`). Three sequential gates guard registry → phase → exception → terminal. Hypothesis: column headers are inescapable; preamble blocks are skippable — maximum header density eliminates the bypass path.

### V-03 — Lifecycle Emphasis: Phase-First Framing
Phase Map becomes Step 1 (with a pre-committed Phase Owner column); Role Registry becomes Step 2 (with a Phase Authority column requiring owners to resolve). An explicit SLA Risk Declaration block sits between Phase Map and Role Registry, locking at-risk SLA vocabulary before any state is written. Hypothesis: roles derived from pre-named phases are grounded in functional authority rather than declared speculatively.

### V-04 — Combined: Role Sequence + Lifecycle Emphasis
Lifecycle Context Declaration → Phase Map with SLA envelope → SLA Risk Declaration → Role Registry with both lifecycle-class constraint and phase-authority mapping. Roles must satisfy two convergent constraints before any state is written. Scan table gains a SC-01 row for "unanchored roles" and SC-02 for "unresolvable phase boundary." Hypothesis: narrowest acceptable-role space of any variation — lifecycle class + phase ownership together.

### V-05 — Combined: Output Format + Inertia Framing
Every section opens with an `AS-IS ANCHOR` block naming a concrete failing example at that exact section (not in a preamble). Column headers carry all constraint language. The combination presents positive constraint (header: what qualifies) and negative example (anchor: what fails) at every structural element. Hypothesis: bidirectional point-of-use constraint produces the lowest overall defect rate.
