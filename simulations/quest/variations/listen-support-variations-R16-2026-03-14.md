Written to `simulations/quest/golden/listen-support-variate-R16-2026-03-15.md`.

---

## Round 16 — Variation Map

| Variation | Axis | C-47 probe | C-48 probe | C-49 probe | Notes |
|-----------|------|------------|------------|------------|-------|
| V-01 | Role sequence (SRE-first) | YES | — | — | Phase 2 no-exception confirmation triple-clause |
| V-02 | Output format (phase-organized) | — | YES | — | Post-generation PHASE DISTRIBUTION re-verify in Part C |
| V-03 | Lifecycle emphasis (pre-declared allocation) | — | — | YES | Switching-friction count floor raised from 2 → 3 |
| V-04 | V-01 + V-02 combined | YES | YES | — | SRE-first + phase-organized + both probes |
| V-05 | Full synthesis | YES | YES | YES | All axes, all three probes, targets above 280 |

---

## Signal logic for the three probes

**C-47 (Phase-2 No-Exception Triple-Clause):** C-44 requires triple-clause verbatim on the Phase 1 and Phase 3 no-exception paths in Pass 2C. The Phase 2 scan — which checks for above-range P0 escalations — has no equivalent no-exception confirmation statement in V-05 R15. V-01 adds a third no-exception path for Phase 2 with the same triple-clause form, closing the asymmetry that C-44 leaves open: all three phase scans are now held to the same verbatim standard. SRE-first role ordering is expected to surface more non-trivial Phase 2 escalations, making the Phase 2 scan meaningful rather than trivially empty.

**C-48 (Post-Generation Phase Distribution Re-Verify):** C-45 pre-commits the phase distribution before body generation and verifies the count at Step 5B constraint 0. But no gate re-verifies after generation is complete. V-02 adds Part C sub-check 3: count the actual Phase 1/2/3 card bodies in Step 6 and compare to the committed block. A mismatch detectable at sub-check 3 (but not at 5B) indicates generation-drift — the pre-generation constraint was satisfied but the model quietly added or dropped a phase assignment during body writing. Phase-organized output format makes the count visually self-confirming (section header count instead of Ticket ID parsing).

**C-49 (Switching-Friction Count Floor ≥ 3):** C-46 raises the minimum from 1 to 2. A floor of 2 covers primary and secondary barriers, but permits a sub-section that misses Phase 2 switching-friction — barriers that only surface after partial commitment. V-03 raises the floor to 3 and adds a structural constraint on the third entry: it must cover a Phase 2 migration barrier, not a day-one friction point. This closes the surface-coverage path that a two-entry floor leaves open.
