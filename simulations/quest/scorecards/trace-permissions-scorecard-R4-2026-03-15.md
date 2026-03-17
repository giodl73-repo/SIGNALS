## Quest Score: trace-permissions — Round 4 (Rubric v4)

**Rubric:** C-01 through C-17 | Essential N=4 | Recommended N=3 | Aspirational N=10

---

## Criterion-by-Criterion Evaluation

### V-01 — Gap-State-Neutral Entity Closure Block

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 | Essential | PASS | 2a matrix maps every role to every operation per entity; no operation left unmapped |
| C-02 | Essential | PASS | Record Scope column in 2a with explicit Org/BU/Team/User/Sharing values |
| C-03 | Essential | PASS | 2b FLS table: per-field with Read: Allowed, Write: Allowed, Denied Roles columns; FLS=NONE immediately logged |
| C-04 | Essential | PASS | Gap log with entity, field/operation, role, gap type, risk; concrete mandatory fields |
| C-05 | Recommended | PASS | 2e traces escalation chain format: `[Role] -> [action on Entity] -> [elevated access reached]` |
| C-06 | Recommended | PASS | 2c sharing rule audit with per-rule verdict; conflict triggers G-## at discovery |
| C-07 | Recommended | PASS | 2d team membership dependency check per entity with explicit self-addition verdict |
| C-08 | Aspirational | PASS | 4a: `[G-##]: Change [element] from [state] to [state] in [location]. After fix: [behavioral change]` — generic advice excluded |
| C-09 | Aspirational | PASS | 4b defense-in-depth table with YES/NO per layer independence; single POF identified |
| C-10 | Aspirational | PASS | Gap log at top, G-## assigned at discovery; Phase 2 inline logging before entity close |
| C-11 | Aspirational | PASS | 2e rule-out format: "No escalation via [mechanism] because [specific reason per mechanism]" — each mechanism named |
| C-12 | Aspirational | PASS | Phase 1 GATE with explicit YES/NO inventory checks; "PHASE 1 COMPLETE: YES/NO — resolve before continuing" |
| C-13 | Aspirational | PASS | ENTITY CLOSURE block mandatory, lists operations reviewed, sensitive fields confirmed, gaps tallied |
| C-14 | Aspirational | PASS | 2c per-role sharing rule statement required for every role including those with no rule |
| C-15 | Aspirational | PASS | G-## at discovery; 4a remediation cites identifier, not re-description |
| C-16 | Aspirational | **PASS** | Primary axis; ENTITY CLOSURE template identical for all entities; `Gaps logged` = G-## list or NONE; blank prohibited by rule |
| C-17 | Aspirational | PASS | 2e names 3 vectors (Assign, sharing, field modification) with explicit verdicts including negatives — meets minimum; weaker than V-02/V-04 but passes the 3-mechanism threshold |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 10/10 → 10

**V-01 Composite: 100**

---

### V-02 — Write-Capable Role Escalation Vector Spine

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 | Essential | PASS | 1c operation-role matrix per entity |
| C-02 | Essential | PASS | Record Scope column in 1c |
| C-03 | Essential | PASS | 1d FLS table per entity; FLS=NONE triggers immediate G-## |
| C-04 | Essential | PASS | Gap log with concrete fields; progressive |
| C-05 | Recommended | PASS | Phase 3 POSSIBLE verdict triggers chain format; G-## logged |
| C-06 | Recommended | PASS | 1e per-entity sharing rule inventory; per-role explicit verdicts |
| C-07 | Recommended | PASS | 2a team membership gap per entity with self-addition verdict |
| C-08 | Aspirational | PASS | 4a G-## citation format; all G-## must have entry |
| C-09 | Aspirational | PASS | 4b defense-in-depth table per entity |
| C-10 | Aspirational | PASS | G-## assigned at discovery; Phase 1 FLS gaps logged during inventory |
| C-11 | Aspirational | PASS | Per-role summary: "five vectors assessed… all vectors ruled out — evidence in table above" |
| C-12 | Aspirational | PASS | Phase 1 GATE with 5 named checks including "all sensitive fields in 1d with FLS status" |
| C-13 | Aspirational | PASS | 2d entity closure: operations reviewed, sensitive fields confirmed, Gaps logged (G-## or NONE), status CLOSED |
| C-14 | Aspirational | PASS | 1e per-role verdict for all entities; per-role verdict required even with no rule |
| C-15 | Aspirational | PASS | G-## scheme; 4a cites identifiers |
| C-16 | Aspirational | PASS | 2d `Gaps logged this entity` field is gap-state-neutral; G-## list or NONE, never blank |
| C-17 | Aspirational | **PASS** | Primary axis; five-vector table per Write-capable role; blank verdict cell = format error; NOT POSSIBLE requires naming the closing mechanism explicitly |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 10/10 → 10

**V-02 Composite: 100**

---

### V-03 — Formal Security Audit Certification Mode

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 | Essential | PASS | 2.1 operation rights matrix with Scope Justification column |
| C-02 | Essential | PASS | Record Scope + Scope Justification columns; excess scope triggers F-## immediately |
| C-03 | Essential | PASS | 2.2 FLS audit with Audit Verdict per field: COMPLIANT / FINDING F-## |
| C-04 | Essential | PASS | Findings Register: F-## at discovery with type and severity |
| C-05 | Recommended | PASS | Section 3 FINDING F-## verdicts with chain format; required basis for finding |
| C-06 | Recommended | PASS | 2.3 sharing rule audit with per-role verdict; "a role with no sharing rule verdict is an omission" |
| C-07 | Recommended | PASS | 2.4 team membership assessment per entity with self-addition verdict |
| C-08 | Aspirational | PASS | Section 5 remediation: current state, required state, corrective action in specific location, post-fix verification |
| C-09 | Aspirational | PASS | Section 6.1 defense-in-depth with STRONG/PARTIAL/WEAK rating; single POF assignment |
| C-10 | Aspirational | PASS | F-## assigned at moment of discovery; progressive across sections |
| C-11 | Aspirational | PASS | Section 3 "No finding" verdicts require explicit basis: "confirmed by reviewing [what] — [basis]"; verdict without basis is non-conforming |
| C-12 | Aspirational | **PARTIAL** | Section 1.3 scope statement names entities and roles, but no explicit YES/NO completeness gate; "sensitive fields confirmed" check absent before Section 2 begins |
| C-13 | Aspirational | PASS | Section 2.5 SECTION VERDICT mandatory: operations audited, sensitive fields audited, Findings (list or NONE explicitly) |
| C-14 | Aspirational | PASS | 2.3 per-role verdict required; "a role with no sharing rule verdict is an omission in the audit record" |
| C-15 | Aspirational | PASS | F-## scheme; Section 5 cites by identifier |
| C-16 | Aspirational | PASS | 2.5 Section Verdict Findings field = list or NONE; "silence is not a valid audit entry" — applies to all entities unconditionally |
| C-17 | Aspirational | PASS | Section 3 five-vector audit per role; "No finding" verdicts require basis statement; verdict without basis is non-conforming |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 9/10 → 9

**V-03 Composite: 99**

---

### V-04 — Combined: Gap-State-Neutral Closure + Vector Spine

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 | Essential | PASS | 2a operation-role matrix per entity; all roles from 1b appear |
| C-02 | Essential | PASS | Record Scope column in 2a |
| C-03 | Essential | PASS | 2b FLS table; FLS=NONE assigns G-## immediately |
| C-04 | Essential | PASS | Gap log; concrete required fields |
| C-05 | Recommended | PASS | Phase 3 POSSIBLE verdicts include chain: `[Role] -> [action] -> [elevated access]` |
| C-06 | Recommended | PASS | 2c per-role sharing rule statements required for all roles including those with no active rule |
| C-07 | Recommended | PASS | 2d team membership dependency with self-addition verdict |
| C-08 | Aspirational | PASS | 5a: G-## cited, state before/after, location specific |
| C-09 | Aspirational | PASS | 5b defense-in-depth per entity |
| C-10 | Aspirational | PASS | Gap log progressive; G-## at discovery |
| C-11 | Aspirational | PASS | Phase 3 NOT POSSIBLE requires named closing mechanism; summary: "5 vectors assessed… all vectors ruled out" |
| C-12 | Aspirational | PASS | Phase 1 GATE + Phase 3 GATE; both with binary YES/NO named checks |
| C-13 | Aspirational | PASS | ENTITY CLOSURE: 6-field template with operations, fields, gaps, sharing verdicts, BU scope, status CLOSED |
| C-14 | Aspirational | PASS | 2c per-role verdict for all entities in scope |
| C-15 | Aspirational | PASS | G-## scheme; 5a cites identifiers |
| C-16 | Aspirational | **PASS** | ENTITY CLOSURE "does not branch on gap state"; `Gaps logged` = G-## list / NONE; blank prohibited; Phase 2 GATE explicitly checks gap-containing row AND gap-free row separately |
| C-17 | Aspirational | **PASS** | Phase 3 five-vector table; "blank verdict cell is a format error"; NOT POSSIBLE must name closing mechanism; Phase 3 GATE audits all rows explicitly |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 10/10 → 10

**V-04 Composite: 100**

---

### V-05 — Lifecycle Emphasis + Inertia Framing (Design Assumptions)

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 | Essential | PASS | E-a operation-role matrix with Assumption Tested column |
| C-02 | Essential | PASS | Record Scope in E-a matrix |
| C-03 | Essential | PASS | E-b FLS table with Assumption Protected column; FLS=NONE = ASSUMPTION UNPROTECTED + G-## |
| C-04 | Essential | PASS | Gap log with Assumption Violated column; concrete gap fields |
| C-05 | Recommended | PASS | E-e POSSIBLE verdicts include chain format and A-## linkage |
| C-06 | Recommended | PASS | E-c per-role sharing rule verdict with assumption linkage |
| C-07 | Recommended | PASS | E-d team membership with assumption-violation framing |
| C-08 | Aspirational | PASS | 5a: G-## + A-## cited; fix must restore assumption |
| C-09 | Aspirational | PASS | 5b defense-in-depth with Assumption at Risk column |
| C-10 | Aspirational | PASS | Gap log progressive with A-## linkage at discovery |
| C-11 | Aspirational | PASS | E-e NOT POSSIBLE verdicts with closing mechanism per vector |
| C-12 | Aspirational | PASS | Pre-analysis assumption table + Phase 1 GATE + Phase 2 GATE + Phase 5 GATE; assumption coverage confirms each entity's analysis completeness |
| C-13 | Aspirational | PASS | ENTITY CLEARANCE GATE: operations reviewed, sensitive fields, Gaps logged, sharing verdicts, escalation vectors checked, assumption coverage per A-## |
| C-14 | Aspirational | PASS | E-c per-role sharing rule verdict with "assumption A-## upheld/violated" determination |
| C-15 | Aspirational | PASS | G-## scheme; 5a cites identifiers with assumption context |
| C-16 | Aspirational | **PASS** | ENTITY CLEARANCE GATE fires on every entity; gap-containing entities cannot receive CLEARED status — they receive CLEARED: PENDING [G-##], encoding gap-state directly into the clearance status field |
| C-17 | Aspirational | **PASS** | E-e five-vector table per Write-capable role per entity; every row requires verdict + assumption linkage; Phase 2 GATE checks "All Write-capable roles have five-vector table for each entity" |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 10/10 → 10

**V-05 Composite: 100**

---

## Composite Scores Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | All Essential |
|-----------|---------------|-----------------|------------------|-----------|--------------|
| V-01 | 60 | 30 | 10 | **100** | YES |
| V-02 | 60 | 30 | 10 | **100** | YES |
| V-03 | 60 | 30 | 9 | **99** | YES |
| V-04 | 60 | 30 | 10 | **100** | YES |
| V-05 | 60 | 30 | 10 | **100** | YES |

---

## Ranking

**1. V-04 (100)** — Best structural coverage of both new criteria simultaneously. Phase 2 GATE has two separate rows checking gap-containing entities and gap-free entities independently. Phase 3 GATE checks all vector table rows and NOT POSSIBLE closing mechanisms. Neither enforcement structure can produce a gap via omission — blank fields and blank cells are structurally visible violations.

**2. V-05 (100)** — Richest semantic structure. CLEARED: PENDING [G-##] is the strongest C-16 enforcement of all five: gap-state is encoded into the clearance status itself, not just a field. Assumption-violation framing makes every unchecked escalation vector produce an irreconcilable assumption in Phase 3. Complex but maximally informative.

**3. V-02 (100)** — Cleanest C-17 single-axis enforcement. Front-loading FLS/sharing into Phase 1 is a structural innovation that separates field-level concerns from entity-level walk. Five-vector table is the same quality as V-04's Phase 3.

**4. V-01 (100)** — Cleanest C-16 single-axis enforcement. The ENTITY CLOSURE block with gap-state-neutral template and explicit invalid-state prohibition is elegant. C-17 is met at minimum (3 vectors with verdicts) rather than the exhaustive 5-vector structure.

**5. V-03 (99)** — Audit register produces C-16 and C-17 via format convention rather than structural enforcement. Solid throughout but PARTIAL on C-12: scope declaration does not confirm sensitive field inventory before Section 2 begins.

---

## Excellence Signals from Top Variation (V-04)

**1. Dual-gate criterion mirroring.** V-04's Phase 2 GATE contains two separate YES/NO rows for the new criterion: one row for gap-containing entities ("Every gap-containing entity has a CLOSURE block with G-## in the `Gaps logged` field") and one row for gap-free entities ("Every gap-free entity has a CLOSURE block with NONE in the `Gaps logged` field"). Each state is auditable independently. Prior rounds had single-row gates that could pass on clean entities and fail on gap-containing ones without the gate catching it.

**2. Explicit invalid-state prohibition in field rules.** The `Gaps logged` field rules name all three invalid forms: blank, "see above," and omission of the field. Naming what invalid looks like is what prevents the model from defaulting to it. Criteria that only state the valid form leave the model free to produce something that looks like a placeholder.

**3. Structural non-overlap.** The closure block fires at entity boundaries; the vector table fires in the escalation phase by role. The two criteria target different structural positions in the output. Neither mechanism interferes with the other, and both can be enforced simultaneously via their respective phase gates. This is what makes V-04 strictly stronger than V-01 or V-02 alone: the gains stack additively rather than requiring a tradeoff.

**4. NOT POSSIBLE requires naming the closing mechanism.** The verdict rule "NOT POSSIBLE: name the specific mechanism that closes this vector (e.g., 'sharing rule creation requires System Customizer privilege — this role does not hold it')" distinguishes a genuine ruling-out from a silence that happens to produce "NOT POSSIBLE." A verdict without a closing mechanism is identically detectable to an omission — the gate checks it.

**New pattern from V-05 worth extracting:** **Two-state clearance status encoding gap inventory into the status field itself.** CLEARED vs CLEARED: PENDING [G-##] means the clearance status is syntactically wrong for a gap-containing entity if the G-## list is absent. This is stronger than a separate `Gaps logged` field because the model cannot write "CLEARED" on a gap-containing entity without violating the semantic definition of CLEARED. The status carries the inventory, not just a field next to it.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual-gate criterion mirroring: Phase 2 GATE has separate YES/NO rows for gap-containing entities and gap-free entities independently, making each state auditable and preventing a single gate row from passing on clean entities while silently failing on gap-containing ones", "Explicit invalid-state prohibition: field rules name all three invalid forms (blank, 'see above', field omission), not just the valid form — the model can only avoid the invalid state if it is named as invalid", "Two-state clearance status encoding gap inventory: CLEARED vs CLEARED: PENDING [G-##] encodes gap-state into the status field itself, making it syntactically incorrect to write CLEARED on a gap-containing entity without naming the open gaps"]}
```
