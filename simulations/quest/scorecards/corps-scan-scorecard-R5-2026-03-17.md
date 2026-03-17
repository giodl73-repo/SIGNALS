## corps-scan Round 5 — Scorecard

### V-01 -- Role Sequence: 3-Role with Per-Role IVR Declaration

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 valid org.yaml | PASS | ROLE 3 template: `org:`, `exec-office:`, `groups:`, `teams:`, `roles:` |
| C-02 team areas from signals | PASS | IVR-3A + `detected-from:` field traces every team to ROLE 2 inventory |
| C-03 group structure | PASS | IVR-3B enforces `groups:` wrapper with nested teams |
| C-04 standard roles | PASS | IVR-3C: 2+ substantive roles, Inertia Advocate absent |
| C-05 no .craft/roles/ | PASS | IVR-1B: unconditional, essential failure if violated |
| C-06 pivot mode + rationale | PASS | ROLE 2: pivot mode candidates + selected pivot with Signal citation |
| C-07 exec office placeholder | PASS | IVR-3D enforces exec-office: with name field |
| C-08 amend options | PASS | IVR-3E: 3 named AMEND A/B/C with commands |
| C-09 pre-YAML inventory | PASS | ROLE 2 produces typed inventory before any YAML |
| C-10 draft boundary first | PASS | IVR-1A: hard boundary declaration is line 1 unconditionally |
| C-11 typed table | PASS | IVR-2A: 4-column typed table required |
| C-12 pivot cites named signal | PASS | IVR-2B: names specific Signal column value |
| C-13 hard ordering gate | PASS | GATE 1: "ROLE 3 may not begin until Phase 2 Completion Test all YES" |
| C-14 gate row in table | PASS | IVR-2C: terminal row of typed inventory table |
| C-15 incompleteness predicates | PASS | Completion Tests + IVR-2C: "inventory not complete without gate row" |
| C-16 traceability repair | PASS | IVR-3A REPAIR: "Return to ROLE 2 and add missing signal row" |
| C-17 completion tests as output | PASS | Phase 2 Completion Test + Phase 3 Completion Test directed |
| C-18 IVR triples | PASS | IVR-1A/B/C/D, IVR-2A/B/C/D, IVR-3A/B/C/D/E: all three blocks present |
| C-19 dual gate | PASS | GATE 1 (Structural Ordering) + GATE 2 (Semantic Traceability) independent |
| C-20 amend anti-pattern named | PASS | IVR-3E + AMEND header: `"Let me know if you want changes" does not satisfy this phase` |
| C-21 gate category labels | PASS | `GATE 1 (Structural Ordering)` + `GATE 2 (Semantic Traceability)` in headers |
| C-22 all constraints IVR | PASS | 13 labeled IVR triples across all roles; no prose-only constraints |

**V-01 score: 220/220 — Golden**

---

### V-02 -- Output Format: SPEC-Object Architecture

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS × 5 | SPEC-01/02 cover scope + exclusion; SPEC-07/08/09/10 cover YAML structure |
| C-06 pivot rationale | PASS | SPEC-04 enforces named signal citation |
| C-07 exec office | PASS | SPEC-10 enforces exec-office: present |
| C-08 amend options | PASS | SPEC-12: 3+ named options; VIOLATION names anti-pattern |
| C-09 pre-YAML inventory | PASS | Phase 2 produces SPEC-03 table before YAML |
| C-10 draft boundary first | PASS | SPEC-01: first output line unconditionally |
| C-11 typed table | PASS | SPEC-03: 4-column typed table |
| C-12 pivot cites signal | PASS | SPEC-04: cites specific Signal column value |
| C-13 hard ordering gate | PASS | GATE 1 blocks Phase 3 until SPEC-05 gate row present |
| C-14 gate row in table | PASS | SPEC-05: terminal row of SPEC-03 table |
| C-15 incompleteness predicates | PASS | Phase 2 + Phase 3 Completion Tests |
| C-16 traceability repair | PASS | SPEC-07 REPAIR: "Return to Phase 2, add missing signal row, re-enter Phase 3" |
| C-17 completion tests as output | PASS | Phase 2 + Phase 3 Completion Tests directed as visible output |
| C-18 IVR triples | PASS | All 12 SPEC objects: INVARIANT + VIOLATION + REPAIR |
| C-19 dual gate | PASS | GATE 1 (Structural Ordering) + GATE 2 (Semantic Traceability) independent |
| C-20 amend anti-pattern named | PASS | SPEC-12 VIOLATION: `"Let me know if you want changes" does not satisfy this phase` |
| C-21 gate category labels | PASS | `GATE 1 (Structural Ordering)` + `GATE 2 (Semantic Traceability)` |
| C-22 all constraints IVR | PASS | "A constraint not expressed as a SPEC is not a constraint" — 12 SPECs cover every phase |

**V-02 score: 220/220 — Golden**

---

### V-03 -- Phrasing Register: Formal Numbered Requirements

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS × 5 | REQ-1.1/1.2 cover scope + exclusion; REQ-3.1–3.4 cover YAML structure |
| C-06 pivot rationale | PASS | REQ-2.2: names specific Signal column value in pivot rationale |
| C-07 exec office | PASS | REQ-3.4 enforces exec-office: present |
| C-08 amend options | PASS | REQ-4.1: 3+ named options with commands |
| C-09 pre-YAML inventory | PASS | Phase 2 inventory table required before any YAML |
| C-10 draft boundary first | PASS | REQ-1.1: first output line unconditionally |
| C-11 typed table | PASS | REQ-2.1: 4-column typed table |
| C-12 pivot cites signal | PASS | REQ-2.2: specific Signal column value |
| C-13 hard ordering gate | PASS | GATE 1 (Structural Ordering) between Phase 2 and Phase 3 |
| C-14 gate row in table | PASS | REQ-2.3: terminal row of inventory table |
| C-15 incompleteness predicates | PASS | REQ-2.5 + REQ-3.6 output directives; "Proceed to GATE 1: only if all YES" |
| C-16 traceability repair | PASS | REQ-3.1 REPAIR: "Return to Phase 2, add the missing row, re-enter Phase 3" |
| C-17 completion tests as output | PASS | REQ-2.5 + REQ-3.6 explicitly direct visible Completion Test output |
| C-18 IVR triples | PASS | 11 REQ blocks each with INVARIANT/VIOLATION/REPAIR |
| C-19 dual gate | PASS | GATE 1 (Structural Ordering) + GATE 2 (Semantic Traceability) independent |
| C-20 amend anti-pattern named | PASS | REQ-4.1 VIOLATION + Phase 4 output: `"Let me know if you want changes" does not satisfy this phase` |
| C-21 gate category labels | PASS | `GATE 1 (Structural Ordering)` + `GATE 2 (Semantic Traceability)` with category headers |
| C-22 all constraints IVR | PASS | All REQs are INVARIANT/VIOLATION/REPAIR — no non-normative constraints |

**V-03 score: 220/220 — Golden**

---

### V-04 -- Role Sequence + Output Format: 4-Role Cast with SPEC Auditor

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS × 5 | IVR-1A/B in ROLE 1; SPEC table covers scope, YAML structure, roles |
| C-06 pivot rationale | PASS | ROLE 2: "Pivot: [mode] -- citing Signal: [specific table value]" |
| C-07 exec office | PASS | SPEC-05 enforces exec-office: with name |
| C-08 amend options | PASS | SPEC-07: 3+ named options with commands |
| C-09 pre-YAML inventory | PASS | ROLE 2 produces typed inventory before ROLE 4 YAML |
| C-10 draft boundary first | PASS | IVR-1A: first line of entire response |
| C-11 typed table | PASS | IVR-2A: typed table with 4 columns |
| C-12 pivot cites signal | PASS | IVR-2B: names specific Signal column value |
| C-13 hard ordering gate | PASS | GATE 1 (Structural Ordering): ROLE 4 blocked until SPEC table complete |
| C-14 gate row in table | PASS | IVR-2C: terminal row of inventory table |
| C-15 incompleteness predicates | PASS | ROLE 2, 3, 4 completion tests; "only if all YES" mechanism |
| C-16 traceability repair | PASS | SPEC-02 REPAIR: "Return to ROLE 2, add missing row, re-enter ROLE 4" |
| C-17 completion tests as output | PASS | Phase 2, Phase 3, Phase 4 Completion Tests directed |
| C-18 IVR triples | PASS | ROLE 1 IVRs + ROLE 2 IVRs + SPEC table all have INVARIANT/VIOLATION/REPAIR |
| C-19 dual gate | PASS | GATE 1 (Structural Ordering) + GATE 2 (Semantic Traceability) in ROLE 3 |
| C-20 amend anti-pattern named | PASS | SPEC-07 VIOLATION + ROLE 4 header: `"Let me know if you want changes" does not satisfy this phase` |
| C-21 gate category labels | PASS | `GATE 1 (Structural Ordering)` + `GATE 2 (Semantic Traceability)` in ROLE 3 |
| C-22 all constraints IVR | **PARTIAL** | Inertia Advocate notice in ROLE 2 expressed as prose bullet — no IVR triple governing it. All other structural constraints are IVR; this one omission means "every constraint" is not met. |

**V-04 score: 215/220 — Golden**

---

### V-05 -- Lifecycle Emphasis: Phase-Centric with Entry/Exit IVR Specs

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS × 5 | IVR-1A/B enforce scope + exclusion; Phase 3 IVRs enforce YAML structure |
| C-06 pivot rationale | PASS | IVR-2B enforces named signal citation |
| C-07 exec office | PASS | IVR-3D enforces exec-office: with name |
| C-08 amend options | PASS | IVR-4A: 3+ named options with commands |
| C-09 pre-YAML inventory | PASS | Phase 2 produces typed table before Phase 3 YAML |
| C-10 draft boundary first | PASS | IVR-1A: scope declaration as line 1 |
| C-11 typed table | PASS | IVR-2A: 4-column typed table |
| C-12 pivot cites signal | PASS | IVR-2B: specific Signal column value |
| C-13 hard ordering gate | PASS | EXIT SPEC (Phase 2) = GATE 1: blocks Phase 3 until gate row present |
| C-14 gate row in table | PASS | IVR-2C: terminal row of inventory table |
| C-15 incompleteness predicates | PASS | ENTRY SPEC per phase: "Phase N begins only after Phase N-1 Completion Test all YES" — strongest C-15 coverage of all variations |
| C-16 traceability repair | PASS | IVR-3A REPAIR: "Return to Phase 2, add missing signal row, re-enter Phase 3" |
| C-17 completion tests as output | PASS | All 4 phases have directed Completion Tests — extends minimum to Phase 1 + Phase 4 |
| C-18 IVR triples | PASS | ENTRY/EXIT SPECs + intra-phase IVRs all have INVARIANT/VIOLATION/REPAIR |
| C-19 dual gate | PASS | EXIT SPEC (Phase 2) = GATE 1 (Structural Ordering); EXIT SPEC (Phase 3) = GATE 2 (Semantic Traceability) — structurally independent |
| C-20 amend anti-pattern named | PASS | IVR-4A VIOLATION + Phase 4 output: `"Let me know if you want changes" does not satisfy this phase` |
| C-21 gate category labels | PASS | `GATE 1 (Structural Ordering)` in EXIT SPEC Phase 2; `GATE 2 (Semantic Traceability)` in EXIT SPEC Phase 3 |
| C-22 all constraints IVR | PASS | ~21 IVR triples: ENTRY SPEC + intra-phase IVRs + EXIT SPEC per phase; zero prose-only constraints |

**V-05 score: 220/220 — Golden**

---

## Summary Table

| Variation | Score | Essential | Recommended | Aspirational | Golden? |
|-----------|-------|-----------|-------------|--------------|---------|
| V-01 Role Sequence (3-role) | 220/220 | 50/50 | 30/30 | 140/140 | YES |
| V-02 SPEC-Object Architecture | 220/220 | 50/50 | 30/30 | 140/140 | YES |
| V-03 Formal Numbered REQs | 220/220 | 50/50 | 30/30 | 140/140 | YES |
| V-04 4-Role + SPEC Auditor | 215/220 | 50/50 | 30/30 | 135/140 | YES |
| V-05 Entry/Exit IVR Specs | 220/220 | 50/50 | 30/30 | 140/140 | YES |

**Top score: 220/220.** Four variations tie. V-04 misses by one PARTIAL (Inertia Advocate notice — a structural constraint with a named failure mode — expressed as prose bullet rather than IVR triple in ROLE 2).

## Ranking Among Tied 220s

V-05 is the architecturally strongest. Every phase has a bidirectional IVR guard (entry precondition + exit postcondition), producing the highest IVR triple density (~21) and extending C-17's minimum to all 4 phases. V-02 is the most proof-resistant against prose drift ("a constraint not expressed as a SPEC is not a constraint"). V-01 and V-03 are strong but have less structural novelty relative to prior rounds.

**Rank: V-05 > V-02 > V-01 ≈ V-03 > V-04**

## Excellence Signals

From the R5 top-scoring variations, three patterns exceed current rubric coverage:

**ES-1 -- Bidirectional phase gating: ENTRY + EXIT IVR per phase** (V-05)
Every phase has both an ENTRY SPEC (precondition to enter — expressed as IVR triple) and an EXIT SPEC (postcondition to advance — expressed as IVR triple). Current rubric only requires exit gates (C-13: ordering gate; C-19: dual gate). ENTRY SPECs make each phase's start condition as unambiguous as its end condition. The ENTRY SPEC for Phase 3 is the direct enforcement that YAML cannot begin before Phase 2's Completion Test block exists in the response.

**ES-2 -- Completion Tests extended to all phases including Phase 1 and Phase 4** (V-05)
C-17 requires "at least the inventory phase and the YAML authoring phase." V-05 directs completion tests for all 4 phases — Phase 1 (scope + role exclusion confirmed), Phase 2 (inventory), Phase 3 (YAML), Phase 4 (amend: 3+ named options present AND anti-pattern absent). The Phase 4 Completion Test introduces explicit negative verification: `[ ] Anti-pattern ("Let me know if you want changes") absent: YES / NO` — the model must confirm the anti-pattern is NOT present, not just that actionable options exist.

**ES-3 -- Anti-pattern absence as explicit Completion Test item** (V-05)
The amend anti-pattern (C-20) is currently enforced via IVR VIOLATION block. V-05 additionally converts the anti-pattern into a YES/NO checklist item in the Phase 4 Completion Test. This is a new enforcement layer: the model must produce visible proof of absence, not just follow an instruction. Analogous to how C-17 made phase predicates visible rather than only prompt-internal — this makes the anti-pattern check visible in the response.

```json
{"top_score": 220, "all_essential_pass": true, "new_patterns": ["entry-spec per phase: each phase has an IVR entry precondition blocking it until prior phase completion test passes, creating bidirectional gating", "completion tests extended to all 4 phases including scope initialization and amend phases beyond C-17 minimum", "anti-pattern absence as explicit YES/NO completion test item: model must produce visible proof of absence not just follow an instruction"]}
```
