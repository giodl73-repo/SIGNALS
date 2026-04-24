Now I have everything needed. Let me score all 5 variations against the full 19-criterion rubric.

---

# corps-scan Quest Score — Round 4

**Rubric**: v4 (19 criteria, 190 pts max)
**Target criteria**: C-17 (visible completion tests), C-18 (IVR triples), C-19 (dual independent gates)
**Golden threshold**: all 5 essentials pass AND composite >= 80 pts

---

## Criterion Reference

| ID | Tier | Description |
|----|------|-------------|
| C-01 | Essential | Valid org.yaml code fence (groups:/teams:/exec-office:) |
| C-02 | Essential | Team areas derived from repo signals |
| C-03 | Essential | Group structure organizes teams |
| C-04 | Essential | Standard roles present per team |
| C-05 | Essential | Does not write .roles/ |
| C-06 | Recommended | Pivot mode declared with rationale |
| C-07 | Recommended | Exec office placeholder present |
| C-08 | Recommended | Amend options listed (>=2 named actionable) |
| C-09 | Aspirational | Pre-YAML scan inventory listed |
| C-10 | Aspirational | Draft boundary stated before first structural content |
| C-11 | Aspirational | Inventory formatted as typed table |
| C-12 | Aspirational | Pivot rationale cites specific named signal |
| C-13 | Aspirational | Hard ordering gate between inventory and YAML |
| C-14 | Aspirational | Gate row embedded as terminal row of inventory table |
| C-15 | Aspirational | Phase incompleteness predicate stated per phase |
| C-16 | Aspirational | Traceability failure triggers explicit repair instruction |
| C-17 | Aspirational | Phase completion tests produced as visible model output |
| C-18 | Aspirational | Constraints expressed as INVARIANT/VIOLATION/REPAIR triples |
| C-19 | Aspirational | Dual gate architecture: inventory gate + traceability gate structurally independent |

---

## V-01 — Output Format: Named Dual-Gate Completion Tests + IVR Triples

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 3 template directs complete yaml block with `groups:`, `teams:`, `exec-office:`; header comments included |
| C-02 | PASS | `# source: Signal [ID]` required on every team area; IVR enforces traceability with "Platform Services" violation example |
| C-03 | PASS | IVR VIOLATION: "`org: teams: [...]` with no `groups:` key — flat list"; REPAIR: introduce group, nest teams |
| C-04 | PASS | IVR VIOLATION: "`roles: [TBD, TBD]`"; separate Inertia Advocate IVR with explicit exclusion |
| C-05 | PASS | First-line directive: "No role files are created by this skill"; YAML template comment: "Inertia Advocate added automatically by corps-build" |
| C-06 | PASS | Phase 2 directs pivot declaration block: mode + Primary signal field + Reasoning sentence + Alternatives |
| C-07 | PASS | `exec-office: name:` with placeholder comment in Phase 3 template |
| C-08 | PASS | Phase 4 AMEND-A/B/C all with named commands; "'Let me know if you want changes' does not satisfy this phase" explicit |
| C-09 | PASS | Phase 1 directs typed Signal Inventory Table; Phase 2 opens only after GATE 1 STATUS: OPEN |
| C-10 | PASS | "**Output this line before any structural content:**" — explicit output directive with quoted statement |
| C-11 | PASS | 4-column table (Signal ID / Path or Identifier / Type / Pivot Mode Fit); GATE row as terminal row |
| C-12 | PASS | Phase 2 requires "Primary signal: Signal [ID] — [exact Path]"; IVR VIOLATION: "this repo uses a microservice architecture" without Signal ID |
| C-13 | PASS | GATE 1 STATUS: OPEN required before Phase 2; "Phase 2 does not open until GATE 1 STATUS: OPEN appears" — hard gate |
| C-14 | PASS | `**GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized**` as terminal table row |
| C-15 | PASS | All 4 phases have "Phase N is NOT COMPLETE until..." header predicates: table+GATE row / Signal ID in pivot / groups+GATE2 clear / amend commands |
| C-16 | PASS | Phase 3 IVR REPAIR: "Return to Phase 1. Insert a new signal row..."; GATE 2: "return to Phase 1, add missing signals" if failures > 0 |
| C-17 | PASS | Three directed output blocks with YES/NO fields: "GATE 1 — write this Completion Test block before Phase 2 opens"; Phase 2 "Write this Completion Test block before Phase 3 opens"; "GATE 2 — write this Completion Test block before Phase 4 opens" |
| C-18 | PASS | All constraints use full IVR: Phase 1 VIOLATION shows `groups:` before GATE row; Phase 2 VIOLATION names "this repo uses a microservice architecture"; Phase 3 VIOLATION names "Platform Services" with no `# source:` comment; four separate IVR triples in Phase 3 |
| C-19 | PASS | GATE 1 (Structural Ordering) + GATE 2 (Semantic Traceability) explicitly labeled as independent; "Two separate failure modes; two separate enforcement points"; separate YES/NO blocks with own failure actions; C-13 and C-16 both pass |

**V-01 Score: 190 / 190 — All 5 essentials PASS — GOLDEN (perfect)**

---

## V-02 — Lifecycle Emphasis: Phase Protocol Blocks

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | PHASE 3 PROTOCOL BODY directs complete yaml template with groups:/teams:/exec-office: |
| C-02 | PASS | `# anchor: Signal [ID]` required per team; IVR VIOLATION: "Identity Services" with `# anchor: general auth concern` |
| C-03 | PASS | IVR VIOLATION: "`org: teams: [...]` with no `groups:` key — all teams at the top level with no group hierarchy" |
| C-04 | PASS | IVR VIOLATION: "`roles: [TBD]` — one placeholder"; Inertia Advocate IVR; substantive roles required |
| C-05 | PASS | "**Output this statement as your first line, before any structural content:** 'Draft org.yaml for human review only. No role files are created.'" |
| C-06 | PASS | PHASE 2 PROTOCOL directs mode + Basis (Signal ID + path) + Reasoning (names Signal ID) + Alternatives |
| C-07 | PASS | exec-office: with name field and placeholder comment in Phase 3 template |
| C-08 | PASS | PHASE 4 PROTOCOL BODY: all three AMEND-A/B/C with named commands; "Let me know if you want changes does not satisfy this phase" |
| C-09 | PASS | PHASE 1 PROTOCOL BODY: typed Signal Inventory Table before YAML (Phase 3) |
| C-10 | PASS | "**Output this statement as your first line, before any structural content:**" — explicit model output directive |
| C-11 | PASS | 4-column typed table; IVR VIOLATION: "bulleted list with no Signal IDs and no GATE row"; GATE row terminal |
| C-12 | PASS | "Basis: Signal [ID] — [exact Path or Identifier from Phase 1 table]"; IVR VIOLATION: "this codebase shows strong domain modeling patterns with bounded contexts" no Signal ID |
| C-13 | PASS | GATE 1: "Phase 2 opens only when the Phase 1 Completion Test shows STATUS: COMPLETE" — explicit hard gate in POSTCONDITION |
| C-14 | PASS | `**GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized**` terminal table row |
| C-15 | PASS | Per-PROTOCOL POSTCONDITION blocks serve as incompleteness predicates: "Phase 2 does not begin until STATUS: COMPLETE"; "Phase 4 does not begin until STATUS: COMPLETE and Traceability failures = 0" — all 4 phases covered |
| C-16 | PASS | Phase 3 IVR REPAIR: "Return to Phase 1. Add a new signal row before the GATE row"; GATE 2: "return to Phase 1, add missing signals before the GATE row, assign Signal IDs, annotate, re-run" |
| C-17 | PASS | Per-PROTOCOL "COMPLETION TEST — write this block before Phase N begins" directive with YES/NO fields in all 4 phases; V-02 is the R3 variation credited for inventing this criterion |
| C-18 | PASS | All SPECs use full IVR: Phase 1 VIOLATION: "writes 'Selected mode: directory' after last signal row before any GATE row appears"; Phase 2 VIOLATION: "domain — this codebase shows strong domain modeling patterns...no Signal ID"; Phase 3 VIOLATION: "Identity Services" with `# anchor: general auth concern` |
| C-19 | PASS | GATE 1 (Structural Ordering) in Phase 1 POSTCONDITION; GATE 2 (Semantic Traceability) in Phase 3 POSTCONDITION; "GATE 2 (Semantic Traceability): independent of GATE 1"; separate failure actions per gate |

**V-02 Score: 190 / 190 — All 5 essentials PASS — GOLDEN (perfect)**

---

## V-03 — Phrasing Register: Formal Contract Specification Language

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | ARTIFACT 3 template directs complete yaml with org:/exec-office:/groups:/teams: structure |
| C-02 | PASS | `# ref: Signal [ID]` required; SPEC (Team Area Traceability) IVR VIOLATION: "Core Platform" with `# ref: platform infrastructure` |
| C-03 | PASS | SPEC (Group Structure) VIOLATION: "`org: teams: [...]` — a flat team list with no `groups:` key" |
| C-04 | PASS | SPEC (Role Completeness) VIOLATION: "`roles: [TBD, TBD]`"; SPEC (Inertia Advocate Exclusion) with full IVR |
| C-05 | PASS | "SCOPE: draft org.yaml only. No `.roles/` files. No role file content of any kind." + REQUIRED FIRST OUTPUT directive |
| C-06 | PASS | ARTIFACT 2 directs mode + Basis (Signal ID + path) + Reasoning + Alternatives |
| C-07 | PASS | exec-office: with name field and placeholder comment in ARTIFACT 3 template |
| C-08 | PASS | ARTIFACT 4 with AMEND-A/B/C named commands; SPEC (Amend Completeness) IVR VIOLATION: generic "I can adjust the structure...no commands named" |
| C-09 | PASS | ARTIFACT 1 typed Signal Inventory Table; ENFORCEMENT POINT 1 prevents Artifact 2 until CLEAR |
| C-10 | PASS | "REQUIRED FIRST OUTPUT: before any structural content, output this statement" — explicit directive |
| C-11 | PASS | 4-column typed table required; SPEC (Inventory Completeness) IVR VIOLATION: "bulleted list with no Signal IDs and no GATE row" |
| C-12 | PASS | "Basis: Signal [ID] — [exact Path or Identifier from Artifact 1]"; IVR VIOLATION: "service — the repo structure implies a service-oriented layout, with multiple independent modules" no Signal ID |
| C-13 | PASS | ENFORCEMENT POINT 1: "Artifact 2 does not proceed until ENFORCEMENT POINT 1 STATUS: CLEAR" — hard gate |
| C-14 | PASS | `**GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized**` terminal row |
| C-15 | PASS | ENFORCEMENT POINT language serves as incompleteness predicates per artifact: "Artifact 2 does not proceed..."; "Artifact 3 does not proceed..."; "Artifact 4 does not proceed..." |
| C-16 | PASS | SPEC (Team Area Traceability) REPAIR: "Return to Artifact 1. Add a new signal row before the GATE row."; ENFORCEMENT POINT 2: "return to Artifact 1, add missing signal rows, assign Signal IDs, annotate, re-run" |
| C-17 | PASS | Three EVIDENCE BLOCK directives: "EVIDENCE BLOCK N — write this before proceeding to Artifact N+1" with YES/NO fields; framed as required output not just prompts |
| C-18 | PASS | Strongest multi-IVR coverage: 7 SPECs across 4 Artifacts, all with full IVR including concrete named VIOLATION examples; SPEC (Amend Completeness) adds IVR for amend phase not present in V-01/V-04 |
| C-19 | PASS | ENFORCEMENT POINT 1 (Structural Ordering) inside Evidence Block 1; ENFORCEMENT POINT 2 (Semantic Traceability) inside Evidence Block 3; "independent of Enforcement Point 1"; separate failure actions per enforcement point |

**V-03 Score: 190 / 190 — All 5 essentials PASS — GOLDEN (perfect)**

---

## V-04 — Inertia Framing: Failure-Mode-Led Design

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Phase 3 directs complete yaml template with exec-office:/groups:/teams: and trace comments |
| C-02 | PASS | `# trace: Signal [ID]` required; IVR VIOLATION: "Shared Infrastructure" with `# trace: platform work` — "conventional names replacing discovered structure" |
| C-03 | PASS | IVR VIOLATION: "`org: teams: [...]` — a flat list, the typical wiki org chart form"; REPAIR: named group |
| C-04 | PASS | IVR VIOLATION: "`roles: [TBD, TBD]` — the inertia path taken when role assignment is deferred"; Inertia Advocate IVR |
| C-05 | PASS | "**First line of output — state this before any structural content:** 'This is a draft org.yaml for review only. No role files are created by this skill.'" |
| C-06 | PASS | Phase 2 directs mode + Primary signal + Reasoning + Alternatives; Phase 2 SIGNAL CHECK verifies Signal ID citation |
| C-07 | PASS | exec-office: with name field and placeholder comment in Phase 3 template |
| C-08 | PASS | Phase 4 AMEND-A/B/C with named commands; "Inertia failure prevented: without named amend commands, overriding scan decisions requires reconstructing command syntax from memory" |
| C-09 | PASS | Phase 1 Signal Inventory Table directed before Phase 3 YAML; STRUCTURAL INERTIA BARRIER enforces ordering |
| C-10 | PASS | "**First line of output — state this before any structural content:**" — explicit output directive |
| C-11 | PASS | 4-column typed table with Signal ID / Path / Type / Pivot Mode Fit; GATE row terminal row |
| C-12 | PASS | "Primary signal: Signal [ID] — [exact Path or Identifier from Phase 1]"; IVR VIOLATION: "this repo has a microservice architecture...without naming Signal [ID]" |
| C-13 | PASS | STRUCTURAL INERTIA BARRIER CHECK: "Phase 2 does not open until BARRIER STATUS: CLEAR appears" — named hard gate |
| C-14 | PASS | `**GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized**` terminal table row |
| C-15 | PASS | All 4 phases have explicit "Phase N is NOT COMPLETE until..." header predicates: table+GATE row / named Signal ID / SEMANTIC INERTIA BARRIER zero failures / amend commands |
| C-16 | PASS | Phase 3 IVR REPAIR: "Return to Phase 1. Add a signal row for the uninventoried team area before the GATE row."; SEMANTIC INERTIA BARRIER: "return to Phase 1, add the missing signals before the GATE row...re-run this check" |
| C-17 | PASS | Three directed output blocks: "STRUCTURAL INERTIA BARRIER CHECK — write this before Phase 2"; "Write this before Phase 3" (PHASE 2 SIGNAL CHECK); "SEMANTIC INERTIA BARRIER CHECK — write this before Phase 4"; all with YES/NO fields |
| C-18 | PASS | Inertia framing makes VIOLATION blocks the primary teaching mechanism: Phase 1 VIOLATION names the transition before GATE row; Phase 2 VIOLATION names "this repo has a microservice architecture" pattern; Phase 3 VIOLATION names "Shared Infrastructure" as the "inertia path: conventional names replacing discovered structure" |
| C-19 | PASS | STRUCTURAL INERTIA BARRIER (Gate 1: Phase 1 → ordering) and SEMANTIC INERTIA BARRIER (Gate 2: Phase 3 → traceability) explicitly independent; "Two separate inertia failure modes; two separate enforcement points with separate repair paths"; C-13 and C-16 both pass |

**V-04 Score: 190 / 190 — All 5 essentials PASS — GOLDEN (perfect)**

---

## V-05 — Role Sequence + Phrasing: Specialist Roles with IVR Exit Contracts

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | DRAFTER BODY directs complete yaml template with exec-office:/groups:/teams:; all required keys present |
| C-02 | PASS | `# anchor: Signal [ID]` required; DRAFTER EXIT INVARIANT VIOLATION: "Data Platform" with `# anchor: data infrastructure` |
| C-03 | PASS | DRAFTER EXIT INVARIANT includes "At least one `groups:` container above teams" — enforced at exit |
| C-04 | PASS | DRAFTER EXIT INVARIANT: "Every team has >= 2 named roles. Inertia Advocate absent from all role lists." DRAFTER EXIT DECLARATION checks both |
| C-05 | PASS | "SKILL-WIDE CONSTRAINT: No role writes `.roles/` files. No role produces role file content." + "Before SCANNER begins, output this statement: 'Draft org.yaml for review only. No role files are created.'" |
| C-06 | PASS | ANALYST BODY directs mode + Decision signal (Signal ID + path) + Reasoning (names Signal ID) + Alternatives |
| C-07 | PASS | DRAFTER template includes exec-office: with name field and placeholder comment |
| C-08 | PASS | FINAL OUTPUT section: AMEND-A/B/C all with named commands including Signal ID references |
| C-09 | PASS | SCANNER produces Signal Inventory Table; SCANNER EXIT DECLARATION must precede ANALYST and DRAFTER |
| C-10 | PASS | "**Before SCANNER begins, output this statement:**" — explicit output directive as first output action |
| C-11 | PASS | SCANNER produces 4-column typed table; SCANNER EXIT INVARIANT VIOLATION: "SCANNER EXIT: Signals found: 2" with no GATE row shows table-unclosed failure |
| C-12 | PASS | "Decision signal: Signal [ID] — [exact Path or Identifier from SCANNER table]"; ANALYST EXIT INVARIANT VIOLATION: "directory — the repository has a clear top-level directory structure with well-separated concerns" without Signal ID |
| C-13 | PASS | GATE 1 STATUS in SCANNER EXIT DECLARATION: "ANALYST does not activate until GATE 1 STATUS: OPEN appears" — hard gate |
| C-14 | PASS | `**GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized**` as terminal row of SCANNER table |
| C-15 | PASS | All three roles have explicit "ROLE N IS NOT COMPLETE until the EXIT INVARIANT is satisfied" predicates; DRAFTER ENTRY CONDITION adds pre-YAML incompleteness check |
| C-16 | PASS | DRAFTER EXIT INVARIANT REPAIR: "Return to SCANNER table. Add a signal row for 'Data Platform' before the GATE row. Re-issue SCANNER EXIT DECLARATION."; DRAFTER EXIT DECLARATION: "return to SCANNER, resolve, re-run ANALYST and DRAFTER in sequence" |
| C-17 | PASS | Three directed exit declaration blocks: "SCANNER EXIT DECLARATION — write this block to activate ANALYST"; "ANALYST EXIT DECLARATION — write this block to activate DRAFTER"; "DRAFTER EXIT DECLARATION — write this block" — all with YES/NO fields activating subsequent roles |
| C-18 | PASS | All three role EXIT INVARIANTS have full IVR with concrete VIOLATION examples: SCANNER (table unclosed example), ANALYST (unanchored pivot reasoning example), DRAFTER (Data Platform without anchor). Note: DRAFTER's IVR bundles 4 constraints with one VIOLATION example — meets minimum threshold (traceability + pivot rationale both covered) |
| C-19 | PASS | GATE 1 (Structural Ordering): SCANNER EXIT DECLARATION `GATE 1 STATUS`; GATE 2 (Semantic Traceability): DRAFTER ENTRY CONDITION before YAML authoring begins; "GATE 2 is structurally independent of GATE 1...independent gates with independent failure modes"; DRAFTER EXIT DECLARATION also checks GATE 2 STATUS: CLEAR |

**V-05 Score: 190 / 190 — All 5 essentials PASS — GOLDEN (perfect)**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Total | Golden |
|-----------|-----------|-------------|--------------|-------|--------|
| V-01 | 50/50 | 30/30 | 110/110 | **190/190** | YES |
| V-02 | 50/50 | 30/30 | 110/110 | **190/190** | YES |
| V-03 | 50/50 | 30/30 | 110/110 | **190/190** | YES |
| V-04 | 50/50 | 30/30 | 110/110 | **190/190** | YES |
| V-05 | 50/50 | 30/30 | 110/110 | **190/190** | YES |

**All 5 variations score 190/190.** R4 was a successful round — every variation correctly implemented C-17, C-18, and C-19, and no variation dropped any criterion from R3.

---

## Ranking

All variations tie at 190/190. Rank ordered by implementation quality and pattern novelty:

| Rank | Variation | Distinguishing Strength |
|------|-----------|------------------------|
| 1 | V-04 (Inertia Framing) | Inertia narrative makes VIOLATION blocks the primary teaching mechanism per phase; barrier names encode failure surfaces; genuinely new axis |
| 2 | V-03 (Contract/Formal) | Strongest C-18 coverage — 7 separate IVR SPECs including amend completeness IVR absent from other variations; ARTIFACT/ENFORCEMENT POINT naming most rigorous |
| 3 | V-01 (Output Format) | Cleanest phase-linear implementation; most literal direct satisfaction of all three new criteria |
| 4 | V-02 (Lifecycle Protocol) | PROTOCOL structure with PRECONDITION/BODY/CONSTRAINTS/COMPLETION TEST/POSTCONDITION is most systematic lifecycle documentation |
| 5 | V-05 (Role Sequence) | Gate 2 as DRAFTER ENTRY CONDITION is innovative; DRAFTER IVR bundles 4 constraints with 1 VIOLATION example — weakest C-18 coverage of the five |

---

## Excellence Signals

Patterns from the top-scoring variation (V-04) and the innovation in V-05 that made them stronger:

**1. Inertia failure narrative as phase header (V-04)**
Each phase opens with "Inertia failure prevented: without Phase N..." — naming the specific failure mode that the phase prevents. This inverts the usual structure: instead of describing what to do and appending a VIOLATION, the VIOLATION becomes the opening framing. The procedural steps are positioned as the solution to the named failure rather than the primary content. Result: VIOLATION examples are load-bearing, not supplementary.

**2. Named barriers encode failure surfaces (V-04)**
"STRUCTURAL INERTIA BARRIER" vs "SEMANTIC INERTIA BARRIER" — each name encodes what kind of failure it prevents (ordering vs traceability) without requiring re-reading the gate definition. The C-19 two-gate distinction becomes self-explanatory from the barrier names alone. Compare to "GATE 1 / GATE 2" (V-01) which requires reading the labels to understand the distinction.

**3. Gate 2 as role ENTRY CONDITION, not only post-YAML check (V-05)**
Placing the semantic traceability gate as DRAFTER's ENTRY CONDITION — before YAML authoring begins — adds a pre-authoring checkpoint distinct from the post-YAML DRAFTER EXIT DECLARATION. The model verifies "every team area to be drafted has a corresponding Signal ID" before writing a single YAML line. This prevents traceability-blind YAML generation rather than catching it after the fact.

---

```json
{"top_score": 190, "all_essential_pass": true, "new_patterns": ["Inertia failure narrative as phase header: each phase opens with its named inertia failure, making VIOLATION examples load-bearing rather than supplementary", "Named barriers encode failure surfaces: STRUCTURAL INERTIA BARRIER vs SEMANTIC INERTIA BARRIER makes the dual-gate distinction self-explanatory from the name alone without re-reading gate definitions", "Gate 2 as role ENTRY CONDITION: placing the semantic traceability gate as a pre-YAML precondition before DRAFTER begins, not only as a post-YAML completion check, catches traceability gaps before YAML generation starts"]}
```
