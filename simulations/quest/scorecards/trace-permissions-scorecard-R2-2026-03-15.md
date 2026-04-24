## trace-permissions — Round 2 Scoring (Rubric v2)

**Rubric:** C-01 through C-12 | **Essential:** 60 pts | **Recommended:** 30 pts | **Aspirational:** 10 pts

---

## Per-Variation Scoring

### V-01 — Per-Entity Inline Gap Tally (C-10 single-axis)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration | PASS | Phase 1.2 role catalog with type, persona; stock roles (CS Rep, Basic User, Customizer, Admin) explicitly flagged |
| C-02 | Record scope | PASS | Phase 2a operation-role matrix includes Record Scope column; every role from 1.2 required to appear |
| C-03 | FLS per role | PASS | Phase 2b FLS table requires Read/Write/Denied per field; "FLS Profile = NONE: state this explicitly per field" rule enforced |
| C-04 | Security gap identification | PASS | Running Gap Register requires entity, field/operation, role, gap type, risk, fix per row; inline accumulation ensures gaps are named with full context |
| C-05 | Escalation path tracing | PASS | Phase 2e per-role escalation check; confirmed format `[Role] -> [Write action] -> [elevated access]` required |
| C-06 | Sharing rule conflict | PASS | Phase 2c sharing rule audit table with "Exceeds OWD+Role Intent?" column per entity |
| C-07 | Team membership gap | PASS | Phase 2d team membership dependency check — names team, blocked scenario, membership control, self-addition possibility |
| C-08 | Remediation guidance | PASS | Phase 4a format: "Apply [specific change] to [role/FLS/rule] in [solution location]. Current state / Target state / After fix." Generic advice explicitly disqualified |
| C-09 | Defense-in-depth | PASS | Phase 4b defense-in-depth table per entity with "Independent?" column for each layer |
| C-10 | Real-time gap accumulation | **PASS** | ENTITY GAP TALLY block mandatory at close of every entity section before advancing; "do not write all entity traces and then tally all at once" enforced structurally; ENTITY CLEAR entries must name specific fields and operations reviewed |
| C-11 | Explicit non-escalation | **PASS** | Phase 2e ruled-out format required for every Write-access role: "Checked [Role]: write on [specific fields/operations]. No escalation because [specific mechanism]." Every role with Write must have one of the two formats |
| C-12 | Phase-gate completeness | **FAIL** | ENTITY GAP TALLY provides per-entity completeness checkpoints but not a phase-level gate. No structured assertion naming all entities covered, all sensitive fields confirmed, and scope decisions at a phase boundary. Tallies are at entity boundaries, not phase transitions |

**Scoring:**
```
Essential: 4/4 * 60 = 60
Recommended: 3/3 * 30 = 30
Aspirational: 4/5 * 10 = 8
Composite: 98
Golden: YES (all essential pass, 98 >= 80)
```

---

### V-02 — Full-Verdict Per-Role Escalation Spine (C-11 single-axis)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration | PASS | Phase 1.2 role catalog with type, persona, "Has Write Access?" flag; stock roles enumerated |
| C-02 | Record scope | PASS | Phase 2a operation matrix per entity with Record Scope column; "No access entities" confirmed explicitly |
| C-03 | FLS per role | PASS | Phase 2b per-role FLS table; "sensitive field with no FLS profile is readable by any role with entity-level Read" triggers immediate gap register entry |
| C-04 | Security gap identification | PASS | Security Gap Register with role, entity/field, gap type, risk, fix; MISSING-FLS added "now" in Phase 2b |
| C-05 | Escalation path tracing | PASS | ROLE ESCALATION VERDICT 4-vector table with explicit ESCALATION POSSIBLE / NOT POSSIBLE per vector |
| C-06 | Sharing rule conflict | PASS | Phase 2c per-role sharing rule expansion check; "Confirmed: no sharing rules expand [Role] access" required when none |
| C-07 | Team membership gap | PASS | Phase 2d team membership dependency — names team, access granted, control mechanism, self-addition possibility |
| C-08 | Remediation guidance | PASS | Phase 4a format with current state / target state / after fix; "current/cannot" framing required |
| C-09 | Defense-in-depth | PASS | Phase 4b defense-in-depth table per entity with independence assessment |
| C-10 | Real-time gap accumulation | **PASS** | "Add to Security Gap Register now" language in Phase 2b for MISSING-FLS; "Add to Security Gap Register if expansion is beyond design intent" in Phase 2c; ESCALATION-PATH additions in ROLE ESCALATION VERDICT. Gaps accumulate during role traversal, not deferred |
| C-11 | Explicit non-escalation | **PASS** | Strongest C-11 implementation: ROLE ESCALATION VERDICT required for every role before advancing to next role; Write-access roles: 4-vector table with per-vector verdict; Read-only roles: "Checked [Role]: Read-only… VERDICT: NO ESCALATION PATH because read-only" required |
| C-12 | Phase-gate completeness | **FAIL** | Phase 1 (inventory) flows directly into Phase 2 (per-role trace) with no structured gate. No named entity/field/scope-decision checkpoint at the phase boundary |

**Scoring:**
```
Essential: 4/4 * 60 = 60
Recommended: 3/3 * 30 = 30
Aspirational: 4/5 * 10 = 8
Composite: 98
Golden: YES (all essential pass, 98 >= 80)
```

---

### V-03 — Named Inventory Gate with Per-Entity FLS Confirmation (C-12 single-axis)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration | PASS | Phase 1.2 role catalog; stock roles explicitly checked |
| C-02 | Record scope | PASS | Phase 1.3 operation-role matrix per entity with Record Scope column; every role from 1.2 required per entity |
| C-03 | FLS per role | PASS | Phase 1.4 FLS inventory with "Read: Roles / Write: Roles / Denied: Roles" columns; MISSING-FLS entries added to Master Gap Table "immediately" |
| C-04 | Security gap identification | PASS | Master Gap Table with phase, entity, detail, gap type, severity, fix; MISSING-FLS added inline in Phase 1.4 |
| C-05 | Escalation path tracing | PASS | Phase 2.1 rule-out format required for every role: "Checked [Role]: holds Write on [operations]. No escalation because [specific mechanism]. VERDICT: NO ESCALATION PATH" |
| C-06 | Sharing rule conflict | PASS | Phase 1.5 sharing rule inventory with "Exceeds Intent?" column; "Zero rules found" confirmation required |
| C-07 | Team membership gap | PASS | Phase 2.3 team gap: "Users in [Role] not in [Team] cannot access [record type] because [OWD + scope]. Self-addition: [possible/not possible]" |
| C-08 | Remediation guidance | PASS | Phase 3.3 remediation with current/target/after format for every Master Gap Table row |
| C-09 | Defense-in-depth | PASS | Phase 3.2 defense-in-depth table with Single Point of Failure flag adding to Master Gap Table |
| C-10 | Real-time gap accumulation | **PASS** | Phase 1.4 "add to Master Gap Table immediately" for MISSING-FLS; Phase 2.1 escalation paths added during analysis phase. Multiple inline additions during body of trace — not deferred to end |
| C-11 | Explicit non-escalation | **PASS** | Phase 2.1 "Rule-out format (required for every role)": names Write operations and entities, states specific mechanism closing escalation, gives explicit VERDICT for every role |
| C-12 | Phase-gate completeness | **PASS** | PHASE GATE: INVENTORY COMPLETE? structured table checks: all entities named, all roles named, all role-entity pairs, all sensitive fields by entity and field name, all MISSING-FLS gap numbers, all sharing rule confirmations, all stock roles — plus mandatory Scope Decisions section. Gate verdict: YES or return to Phase 1. Second gate at Phase 2 → Phase 3 boundary. Both are mandatory structured tables |

**Scoring:**
```
Essential: 4/4 * 60 = 60
Recommended: 3/3 * 30 = 30
Aspirational: 5/5 * 10 = 10
Composite: 100
Golden: YES (all essential pass, 100 >= 80)
```

---

### V-04 — Combined: Inline Gap Stream + Gate Checkpoint (C-10 + C-12)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration | PASS | Phase 1.2 role catalog; stock roles enumerated |
| C-02 | Record scope | PASS | Phase 1.3 per-entity operation-role matrix with Record Scope column |
| C-03 | FLS per role | PASS | Phase 1.4 FLS table with "Read: Who / Write: Who / Denied: Who"; immediate Inline Gap Stream entry required for MISSING-FLS with full format template including fix |
| C-04 | Security gap identification | PASS | Inline Gap Stream format: `[G-##] [Entity].[Field / Operation] -- [Role(s)] -- [Gap Type] -- Risk -- Fix`; concrete entries required at discovery time |
| C-05 | Escalation path tracing | PASS | Phase 2.1 Write-access ruled-out format: "Vectors: Assign [verdict + reason], Share [verdict + reason], Field modification [verdict + reason], Team self-addition [verdict + reason]. VERDICT: NO ESCALATION PATH because [specific mechanism]" |
| C-06 | Sharing rule conflict | PASS | Phase 1.5 sharing rules "beyond intent: add to Inline Gap Stream immediately" with specific format template |
| C-07 | Team membership gap | PASS | Phase 2.3: "Users in [Role] not in [Team] cannot access [record type] because [OWD + scope]. Team controlled by [mechanism]. Self-addition: [possible/not possible -- reason]" |
| C-08 | Remediation guidance | PASS | Phase 3.1 remediation for every G-## entry: current/target/after fix with "Fix field in the stream is your starting point — expand it here" |
| C-09 | Defense-in-depth | PASS | Phase 3.2 defense-in-depth table; Single Point of Failure = YES adds to Inline Gap Stream |
| C-10 | Real-time gap accumulation | **PASS** | Primary axis. Inline Gap Stream open throughout entire trace. Phase 1.4: immediate entry required; Phase 1.5: immediate entry required; Phase 2.1: escalation paths added during role analysis. OUTPUT REQUIREMENTS explicitly state "pre-populating at the end fails C-10." Structural enforcement stronger than any single-axis variation |
| C-11 | Explicit non-escalation | **PASS** | Phase 2.1 Write-access: full vector-by-vector analysis with verdict + reason; Read-only: "Checked [Role]: Read-only on [entities]. No Write, no Assign, no escalation vector. VERDICT: NO ESCALATION PATH." Every role covered |
| C-12 | Phase-gate completeness | **PASS** | PHASE 1 GATE Part A: names entities, roles, sensitive fields per entity, sharing rules per entity, scope decisions. PHASE 1 GATE Part B: gap stream audit — lists every G-## ID added so far with type and section. Arithmetic check: "Gap stream entries at Phase 1 close: [N] entries." PHASE 2 GATE repeats structure. FINAL GATE: "Inline Gap Stream entry count matches remediation count" — count balance verification. Three mandatory gates |

**Scoring:**
```
Essential: 4/4 * 60 = 60
Recommended: 3/3 * 30 = 30
Aspirational: 5/5 * 10 = 10
Composite: 100
Golden: YES (all essential pass, 100 >= 80)
```

---

### V-05 — Verdict-Per-Role Discipline + Dataverse Stock Defaults as Baseline (C-11 + C-10)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration | PASS | Phase 1.2 role catalog with "Stock Baseline Privileges / Configured Privileges / Delta Type / Security Implication" — stock roles get explicit baseline statement |
| C-02 | Record scope | PASS | Phase 1.3 operation-role matrix includes "Record Scope (Default) / Record Scope (Configured)" columns |
| C-03 | FLS per role | PASS | Phase 1.4 FLS comparison with Security State: PROTECTED/UNPROTECTED per field; UNPROTECTED entries add to both Deviation Log and Gap Register |
| C-04 | Security gap identification | PASS | Gap Register with gap type, risk, fix; MISSING-FLS entries added in Phase 1.4 with specific format |
| C-05 | Escalation path tracing | PASS | Phase 2 vector-by-vector analysis per role: "For escalation to occur via this vector: [what would need to be true]. That condition is [MET / NOT MET] because [specific reason]." All 4 vectors covered |
| C-06 | Sharing rule conflict | PASS | Phase 1.5 sharing rules: "If unintentional or over-broad: add to Deviation Log (LOOSENED) and Gap Register" |
| C-07 | Team membership gap | **FAIL** | V-05 traces team self-addition as an *escalation* vector (Phase 2) but has no dedicated team-gap analysis. C-07 requires identifying roles *blocked* from legitimate operations due to missing team assignments. The escalation vector framing addresses one direction (can I add myself to get higher privilege?) but not the other (am I blocked from needed access because I'm not in a team?). No equivalent to V-01 Phase 2d, V-02 Phase 2d, V-03 Phase 2.3, or V-04 Phase 2.3 |
| C-08 | Remediation guidance | PASS | Phase 3.2 remediation format: "Current state: [vs. stock default]. Target state. Change: [specific Dataverse admin action in named solution location]. After fix. Why this matters vs. default" — more detailed than other variations |
| C-09 | Defense-in-depth | PASS | Phase 3.3 defense-in-depth vs. default table: "Default Defense-in-Depth / Configured Defense-in-Depth / Improvement or Regression" |
| C-10 | Real-time gap accumulation | **PASS** | Deviation Log open throughout trace: "add entries when configured access deviates from stock defaults." Phase 1.4 "add to Deviation Log AND add to Gap Register" for unprotected sensitive fields. Phase 1.5 "add to Deviation Log (LOOSENED) and Gap Register" for over-broad sharing rules. Inline additions during body of trace |
| C-11 | Explicit non-escalation | **PASS** | Core axis. CLOSED CASE statement required for every role: Write-access roles: "CLOSED CASE: [ESCALATION CONFIRMED -- see G-## / NO ESCALATION PATH -- all vectors closed because [specific named mechanisms]]"; Read-only roles: "CLOSED CASE: NO ESCALATION PATH -- read-only access on all entities." No role may be left without a verdict — OUTPUT REQUIREMENTS enforce this |
| C-12 | Phase-gate completeness | **FAIL** | Phase 1 flows directly into Phase 2 with no structured completeness gate. Deviation Log review occurs in Phase 3 (retrospective), not at a Phase 1→2 boundary. No table naming entities covered, sensitive fields confirmed, scope decisions before advancing to gap analysis |

**Scoring:**
```
Essential: 4/4 * 60 = 60
Recommended: 2/3 * 30 = 20
Aspirational: 4/5 * 10 = 8
Composite: 88
Golden: YES (all essential pass, 88 >= 80)
```

---

## Ranking

| Rank | Variation | Composite | Golden | Notes |
|------|-----------|-----------|--------|-------|
| 1 | **V-04** | 100 | YES | C-10 + C-12 + C-11 all pass; gap stream ID audit at each gate is the decisive edge |
| 2 | **V-03** | 100 | YES | C-12 + C-10 + C-11 all pass; two-gate architecture with named entities/fields |
| 3 | **V-01** | 98 | YES | C-10 + C-11 pass; per-entity tallies are strong but no phase-level gate |
| 4 | **V-02** | 98 | YES | C-11 strongest of all variations; C-10 pass; no phase gate |
| 5 | **V-05** | 88 | YES | C-11 strong, C-10 pass; fails C-07 (team-gap) and C-12 (no gate) |

V-04 and V-03 tie at 100 on the scoring formula. V-04 ranks first because:

1. Part B gap stream ID audits at each gate make C-10 failure structurally impossible (the model cannot say "all captured" without listing IDs)
2. Final gate arithmetic check: "stream count = remediation count" creates a balance equation that catches uncounted gaps
3. The two axes reinforce each other causally: the gate *requires* the stream to have been maintained, so C-12 cannot pass on a collapsed C-10

---

## Excellence Signals

**From V-04 (top):**

1. **ID-enumerated gap stream audit at gates** — Requiring every G-## entry to be listed by ID in Part B of each phase gate prevents silent gap collapse. A model claiming the stream is complete must provide the enumeration. This is structurally stronger than V-03's gate, which names entities and fields but does not audit the gap stream entries.

2. **Count arithmetic verification at final gate** — "Inline Gap Stream entry count matches remediation count: [N] = [N]: YES / NO" creates a balanced-books check. Any gap that slipped through Phase 1 or 2 without a stream entry will show as a count mismatch. This is novel — no other variation has a numeric balance check.

3. **Multi-gate sequential reinforcement** — Three mandatory gates (Phase 1, Phase 2, Final) create successive checkpoints where each gate cannot pass if the prior phase left open signals. V-03 has two gates; V-04 has three. This prevents cascade propagation: a Phase 1 inventory miss cannot silently enter Phase 2 analysis.

**From V-05 (failure signal):**

4. **Role-organized traces sacrifice team-gap analysis** — V-05's role-first organization with escalation-vector framing is excellent for C-11 but misses C-07. The escalation direction (can I self-add to a higher team?) and the blockage direction (am I missing team membership I need?) require different analytical stances. Variations that organize around escalation vectors need an explicit separate section for access-blockage team gaps, or they will consistently fail C-07.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["ID-enumerated gap stream audit at gates prevents silent gap collapse without relying on prose assertions", "Count arithmetic verification at final gate: stream entry count must equal remediation count creating a numeric balance check", "Multi-gate sequential reinforcement: each gate audits the gap stream forcing prior-phase completeness before advancing", "Role-organized escalation traces miss team-gap coverage: self-addition vectors and access-blockage gaps require separate analytical stances"]}
```
