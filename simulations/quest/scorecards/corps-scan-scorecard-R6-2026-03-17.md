## Quest Score — corps-scan Round 6

Rubric: v6 (27 criteria, 270 pts max). Five variations evaluated.

---

## Per-Criterion Scorecard

### V-01 — Inertia Framing

| C | Result | Evidence |
|---|--------|----------|
| C-01 | PASS | Full YAML template with `org:`, `exec-office:`, `groups:`, `teams:` in code fence |
| C-02 | PASS | Teams derived from Phase 2 table; IVR-3B detected-from: annotation ties every team to a signal |
| C-03 | PASS | IVR-3C: `groups:` wrapper required; flat list VIOLATION named |
| C-04 | PASS | IVR-3D: 2+ substantive roles; Inertia Advocate exclusion named explicitly |
| C-05 | PASS | IVR-1B: no `.roles/` content anywhere; IVR-3F traceability statement re-confirms |
| C-06 | PASS | IVR-2B: pivot rationale required; PIVOT MODE ENUMERATION block shown |
| C-07 | PASS | IVR-3E: `exec-office:` with `name:` field required |
| C-08 | PASS | IVR-4A: 3+ named AMEND A/B/C with commands |
| C-09 | PASS | Phase 2 inventory structurally prior to Phase 3; GATE 1 enforces ordering |
| C-10 | PASS | IVR-1A: boundary declaration as absolute first output line; directed output template present |
| C-11 | PASS | IVR-2A: typed table required; bulleted-list VIOLATION named |
| C-12 | PASS | IVR-2B: specific Signal column value citation required; generic-sentence VIOLATION named |
| C-13 | PASS | GATE 1 (Structural Ordering) explicitly blocks Phase 3 until Phase 2 Completion Test all YES |
| C-14 | PASS | IVR-2C: gate row is terminal table row; sentinel-below-table VIOLATION named |
| C-15 | PASS | Phase 2 and Phase 3 completion tests both include YES/NO incompleteness predicates |
| C-16 | PASS | IVR-3A REPAIR: return to Phase 2, add missing signal row; GATE 2 blocks on IVR-3A/3B failure |
| C-17 | PASS | Phase 2 and Phase 3 Completion Test blocks directed as visible model output |
| C-18 | PASS | All IVR triples use INVARIANT/VIOLATION/REPAIR named blocks; traceability and pivot both covered |
| C-19 | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) are structurally independent |
| C-20 | PASS | IVR-4A: `"Let me know if you want changes" does not satisfy this phase` — named in the triple |
| C-21 | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) — parenthesized category labels |
| C-22 | PASS | 14 IVR triples cover all structural constraints across all phases; META-RULE lists all by name |
| C-23 | PASS | IVR-3B: detected-from: required on every team; VIOLATION: team entry without field; REPAIR: add to YAML itself |
| C-24 | PASS | IVR-2D: all 4 candidates + rejection reasons required; YES/POSSIBLE/NO-without-reasons VIOLATION named |
| C-25 | PASS | Labels IVR-1A through IVR-4A; 14 triples enumerated in META-RULE with count instruction |
| C-26 | PASS | META-RULE: "Any directive not expressed as a labeled IVR triple is advisory context only...full constraint set consists exactly of the labeled IVR triples below" |
| C-27 | PASS | Phase 2: "Proceed to GATE 1: only if all YES. If any item is NO: resolve before continuing." Phase 3 same pattern |

**V-01 Score: 270/270** — All 27 PASS. All 5 essentials pass.

---

### V-02 — Lifecycle Emphasis (ENTRY/EXIT Contracts)

| C | Result | Evidence |
|---|--------|----------|
| C-01 | PASS | Full YAML template; `org:`, `exec-office:`, `groups:`, `teams:` present |
| C-02 | PASS | IVR-P3-A + IVR-P3-B: traceability + detected-from: |
| C-03 | PASS | IVR-P3-C: groups: wrapper required |
| C-04 | PASS | IVR-P3-D: 2+ named roles, Inertia Advocate excluded |
| C-05 | PASS | IVR-P1-B: role file exclusion |
| C-06 | PASS | IVR-P2-B: pivot rationale with named signal |
| C-07 | PASS | IVR-P3-E: exec-office: with name: |
| C-08 | PASS | IVR-P4-A: 3+ named amend options |
| C-09 | PASS | Phase 2 inventory; ENTRY-P3 requires Phase 2 EXIT all YES |
| C-10 | PASS | IVR-P1-A: boundary declaration line 1 |
| C-11 | PASS | IVR-P2-A: typed table 4 columns |
| C-12 | PASS | IVR-P2-B: Signal column value citation |
| C-13 | PASS | GATE 1 (Structural Ordering): EXIT-P2 required |
| C-14 | PASS | IVR-P2-C: terminal gate row in table |
| C-15 | PASS | All phases have EXIT contracts with YES/NO incompleteness predicates |
| C-16 | PASS | IVR-P3-A REPAIR: return to Phase 2; GATE 2 blocks on failure |
| C-17 | PASS | Completion test blocks directed for all phases (P1 through P4) |
| C-18 | PASS | All IVR-Px-y triples use INVARIANT/VIOLATION/REPAIR named blocks |
| C-19 | PASS | GATE 1 and GATE 2 structurally independent |
| C-20 | PASS | IVR-P4-A: anti-pattern named inline |
| C-21 | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) labeled |
| C-22 | PASS | 14 labeled IVR-Px-y triples listed in META-RULE |
| C-23 | PASS | IVR-P3-B: detected-from: per team; REPAIR states "traceability must be in YAML itself" |
| C-24 | PASS | IVR-P2-D: all 4 modes + rejection reasons; two VIOLATION examples |
| C-25 | PASS | Labels IVR-P1-A through IVR-P4-A; 14 triples with count in META-RULE |
| C-26 | PASS | META-RULE: "Any directive in this prompt not expressed as a labeled IVR triple is advisory context only" |
| C-27 | PASS | EXIT CONTRACT blocks: "Advance to Phase N: only if all YES. If any item is NO: resolve before exiting." All 4 phases |

**V-02 Score: 270/270** — All 27 PASS. All 5 essentials pass.

---

### V-03 — Conversational Imperative (Direct-Command Register)

| C | Result | Evidence |
|---|--------|----------|
| C-01 | PASS | YAML template with all required keys |
| C-02 | PASS | [P3-A]: all team names from Phase 2 table; [P3-B]: detected-from: required |
| C-03 | PASS | [P3-C]: groups: with nested teams required |
| C-04 | PASS | [P3-D]: real role names, no Inertia Advocate |
| C-05 | PASS | [P1-B]: no role file content anywhere |
| C-06 | PASS | [P2-B]: name a specific table row for pivot rationale |
| C-07 | PASS | [P3-E]: exec-office: with name: required |
| C-08 | PASS | [P4-A]: 3+ specific named options with commands |
| C-09 | PASS | Phase 2 inventory precedes YAML; GATE 1 enforces |
| C-10 | PASS | [P1-A]: boundary line as very first output |
| C-11 | PASS | [P2-A]: typed table required; "bulleted list doesn't count" named |
| C-12 | PASS | [P2-B]: specific row citation; "'The repo appears service-oriented' doesn't count" |
| C-13 | PASS | GATE 1 (Structural Ordering): "only move to Phase 3 if every check is YES" |
| C-14 | PASS | [P2-C]: last row of inventory table is the gate row |
| C-15 | PASS | "Only move to Phase 2 if both YES" / "only move to Phase 3 if every check is YES" / etc. |
| C-16 | PASS | [P3-A]: "go back to Phase 2, add the missing signal row"; GATE 2 directs repair |
| C-17 | PASS | Directed check blocks at end of all four phases |
| **C-18** | **PARTIAL** | Violation examples present throughout ("`YES/POSSIBLE/NO` without reasons doesn't count"; "invented name"), but not in formally **named** INVARIANT/VIOLATION/REPAIR blocks — blocks are direct commands, not labeled structural units. Two required constraints (traceability, pivot) have all three components inline but unnamed as blocks |
| C-19 | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) are independent |
| C-20 | PASS | [P4-A]: "Let me know if you want changes" named as non-compliant form in the rule itself |
| C-21 | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) parenthesized category labels present |
| **C-22** | **FAIL** | Requires C-18 to pass. [Px-Y] tag blocks contain constraint content but not the IVR triple discipline required by C-22. |
| C-23 | PASS | [P3-B]: detected-from: on every team; "A team entry without detected-from: fails even if the inventory is complete" |
| C-24 | PASS | [P2-D]: all four modes required with per-mode rejection reasons; YES/POSSIBLE/NO VIOLATION named |
| **C-25** | **FAIL** | Requires C-22 to pass. Phase-scoped [Px-Y] labels are present but C-25 dependency on C-22 is not satisfied. |
| **C-26** | **FAIL** | Requires C-22 and C-25 to pass. Meta-rule content present ("Every binding rule has a tag... Prose without a tag is context") but dependency chain broken by C-22/C-25 failure. |
| C-27 | PASS | "Only move to Phase 3 if every check is YES. If any check is NO: fix it and re-check." Pattern in all gates. |

**V-03 Score: 235/270** — C-18 PARTIAL (−5), C-22/C-25/C-26 FAIL (−30). All 5 essentials pass.

---

### V-04 — Inertia Framing + Lifecycle (Combination)

| C | Result | Evidence |
|---|--------|----------|
| C-01 | PASS | YAML template with all required keys |
| C-02 | PASS | IVR-3A + IVR-3B traceability and detected-from: |
| C-03 | PASS | IVR-3C groups: wrapper |
| C-04 | PASS | IVR-3D 2+ named roles, no Inertia Advocate |
| C-05 | PASS | IVR-1B role exclusion |
| C-06 | PASS | IVR-2B pivot rationale with signal citation |
| C-07 | PASS | IVR-3E exec-office: |
| C-08 | PASS | IVR-4A 3+ named amend options |
| C-09 | PASS | Phase 2 inventory; ENTRY-P3 requires EXIT-P2 all YES |
| C-10 | PASS | IVR-1A boundary as line 1 |
| C-11 | PASS | IVR-2A typed table 4 columns |
| C-12 | PASS | IVR-2B named signal citation |
| C-13 | PASS | GATE 1 (Structural Ordering) present |
| C-14 | PASS | IVR-2C terminal gate row |
| C-15 | PASS | Phase 2 and Phase 3 EXIT contracts with YES/NO predicates |
| C-16 | PASS | IVR-3A REPAIR: return to Phase 2; GATE 2 blocks |
| C-17 | PASS | Completion test blocks directed for all 4 phases |
| C-18 | PASS | All IVR triples use INVARIANT/VIOLATION/REPAIR named blocks |
| C-19 | PASS | GATE 1 and GATE 2 structurally independent |
| C-20 | PASS | IVR-4A: "Let me know if you want changes" does not satisfy this phase |
| C-21 | PASS | EXIT-P2/GATE 1 (Structural Ordering); EXIT-P3/GATE 2 (Semantic Traceability) |
| C-22 | PASS | 14 labeled IVR triples; META-RULE lists all by name with count |
| C-23 | PASS | IVR-3B: detected-from: per team; REPAIR: traceability must be in YAML itself |
| C-24 | PASS | IVR-2D: all 4 modes with rejection reasons; two VIOLATION patterns named |
| C-25 | PASS | Labels IVR-1A through IVR-4A; 14 triples listed with count instruction in META-RULE |
| C-26 | PASS | META-RULE: "Binding constraints in this prompt are labeled IVR triples only... A constraint without a label is advisory only." |
| C-27 | PASS | EXIT contracts: "Advance to Phase 2 only if all YES. If any NO: resolve before exiting Phase 1." All 4 phases |

**V-04 Score: 270/270** — All 27 PASS. All 5 essentials pass.

---

### V-05 — Role Sequence + Inertia Framing (4-Role with Inertia Auditor)

| C | Result | Evidence |
|---|--------|----------|
| C-01 | PASS | YAML template in ROLE 4 with all required keys and detected-from: annotations |
| C-02 | PASS | IVR-4A: all team areas trace to ROLE 3 inventory; IVR-4B: detected-from: per team |
| C-03 | PASS | IVR-4C: groups: wrapper with nested teams |
| C-04 | PASS | IVR-4D: 2+ substantive roles, no Inertia Advocate |
| C-05 | PASS | IVR-1B: no .roles/ content anywhere |
| C-06 | PASS | IVR-2B (ROLE 2): pivot candidates with rationale; IVR-3B (ROLE 3): citation of named signal |
| C-07 | PASS | IVR-4E: exec-office: with name: field |
| C-08 | PASS | IVR-4F: 3+ named amend options; anti-pattern named ("Let me know if you want changes" does not satisfy per IVR-1C) |
| C-09 | PASS | ROLE 3 produces typed inventory table; GATE 1 blocks ROLE 4 until ROLE 3 complete |
| C-10 | PASS | IVR-1A: boundary declaration as line 1 |
| C-11 | PASS | IVR-3A: typed table Signal/Type/Team Area Candidate/Org Relevance |
| C-12 | PASS | IVR-3B: pivot confirmation cites specific Signal column value from ROLE 3 table |
| C-13 | PASS | GATE 1 (Structural Ordering) in ROLE 3: "ROLE 4 may not begin until ROLE 3 Completion Test passes" |
| C-14 | PASS | IVR-3C: terminal gate row in ROLE 3 inventory table |
| C-15 | PASS | ROLE 3 and ROLE 4 both have Completion Tests with YES/NO incompleteness predicates |
| C-16 | PASS | IVR-4A REPAIR: return to ROLE 3; GATE 2: return to ROLE 3, resolve, re-enter ROLE 4 |
| C-17 | PASS | All 4 roles have directed Completion Test blocks |
| C-18 | PASS | All 16 IVR triples use INVARIANT/VIOLATION/REPAIR named blocks |
| C-19 | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) structurally independent |
| C-20 | PASS | IVR-4F + IVR-1C forward commitment: "Let me know if you want changes" named as non-compliant in ROLE 1 pre-check before ROLE 4 exists |
| C-21 | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) with parenthesized category labels |
| C-22 | PASS | 16 labeled triples (role-scoped: IVR-1A/1B/1C, IVR-2A/2B/2C, IVR-3A/3B/3C/3D, IVR-4A/4B/4C/4D/4E/4F); META-RULE lists all |
| C-23 | PASS | IVR-4B: detected-from: on every team; REPAIR: "The YAML must be self-documenting: traceability appears in the YAML itself, not only in the pre-YAML inventory" |
| C-24 | PASS | IVR-2B (ROLE 2): all four candidates required with inertia-comparison rejection reasons; two VIOLATION patterns (missing alternatives; rejection reasons without repo signal observations) |
| C-25 | PASS | Role-scoped labels (IVR-1A/2B/3C/4F etc.); 16 triples enumerated in META-RULE with count instruction |
| C-26 | PASS | META-RULE: "Binding constraints are the labeled IVR triples declared within each role block. Any prose in a role block that is not a labeled IVR triple is advisory context and does not constitute a pass/fail requirement." |
| C-27 | PASS | All roles: "Advance to ROLE N: only if all YES. If any NO: resolve and re-run this test before continuing." |

**V-05 Score: 270/270** — All 27 PASS. All 5 essentials pass.

---

## Composite Summary

| Variation | Score | Essentials | All Pass? |
|-----------|-------|------------|-----------|
| V-01 Inertia Framing | **270/270** | 5/5 | Yes |
| V-02 Lifecycle Emphasis | **270/270** | 5/5 | Yes |
| V-03 Conversational Imperative | **235/270** | 5/5 | No (C-18 PARTIAL; C-22/25/26 FAIL) |
| V-04 Inertia + Lifecycle | **270/270** | 5/5 | Yes |
| V-05 Role Sequence + Inertia Auditor | **270/270** | 5/5 | Yes |

**Top score: 270/270** (V-01, V-02, V-04, V-05 all tie)

---

## Differential Analysis: Why V-03 Falls Short

V-03's single gap is register incompatibility with C-18's "named blocks" requirement. The direct-command format (`[P2-A] Build a table, not a list: ...`) contains all three semantic components (invariant, violation example, repair) but presents them as inline prose commands rather than formally named `INVARIANT:` / `VIOLATION:` / `REPAIR:` blocks. This triggers a dependency cascade:

- **C-18 PARTIAL** (−5 pts): Violation examples present; formal block naming absent
- **C-22 FAIL** (−10 pts): Requires C-18 to pass; [Px-Y] command blocks ≠ IVR triples
- **C-25 FAIL** (−10 pts): Requires C-22; phase-scoped labels [P1-A] etc. present but dependency broken
- **C-26 FAIL** (−10 pts): Requires C-22 + C-25; meta-rule content present ("Prose without a tag is context") but dependency chain broken

Total loss: 35 pts. The hypothesis that conversational register lowers activation energy is partially supported for all criteria *except* those requiring formal IVR structure. Conversational register is compatible with C-23/C-24/C-27 but incompatible with C-18/C-22.

---

## Excellence Signals (from top-scoring variations)

**From V-05 (structural novelty):**

1. **Forward commitment pattern for amend anti-pattern**: IVR-1C declares the `"Let me know if you want changes"` prohibition in ROLE 1 as a forward commitment active throughout. This removes any ambiguity about when C-20 activates and creates cross-role enforcement — ROLE 4 cites IVR-1C explicitly, closing the loop.

2. **Inertia Auditor as dedicated C-24 role**: Elevating pivot candidate enumeration from a Phase 2 sub-task to a full dedicated role (ROLE 2) with its own Completion Test makes rejection reasons structurally non-skippable. C-24 compliance is architecturally guaranteed rather than prompt-instruction-dependent.

3. **Manual-gap reconciliation loop** (IVR-3D): ROLE 3 explicitly reconciles which ROLE 2 gap types were found/absent in the actual repo — closing the inertia-audit → inventory feedback loop and making the two roles causally connected.

4. **16-triple coverage vs 14**: Role-scoped labels (IVR-1A/1B/1C, IVR-2A/2B/2C, IVR-3A/3B/3C/3D, IVR-4A/4B/4C/4D/4E/4F) allow 2 additional IVR triples (IVR-1C forward commitment, IVR-3D gap reconciliation) that phase-based variations omit.

**From V-02/V-04 (lifecycle pattern):**

5. **EXIT contract as natural C-27 carrier**: ENTRY/EXIT lifecycle structure generates conditional advance instructions by architectural construction. C-27 compliance is guaranteed wherever an EXIT contract exists — the pattern collapses C-17 and C-27 into a single structural primitive.

---

```json
{"top_score": 270, "all_essential_pass": true, "new_patterns": ["forward-commitment-in-role-1-locks-amend-anti-pattern-before-phase-4-exists", "dedicated-inertia-auditor-role-makes-C24-pivot-rejection-structurally-non-skippable", "manual-gap-reconciliation-loop-closes-inertia-audit-to-inventory-feedback", "exit-contract-structure-generates-C27-compliance-by-construction"]}
```
