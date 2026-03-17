## trace-permissions — Round 3 Scoring (Rubric v3)

**Rubric:** v3 (C-01–C-15) | **Tier weights:** Essential 60 pts (4 criteria × 15) · Recommended 30 pts (3 × 10) · Aspirational 10 pts (8 × 1.25)
**Trace artifact:** placeholder — scoring evaluates prompt structural design (how reliably each variation forces criterion compliance)

---

## Per-Variation Evaluation

### V-01 — Output Format: Numbered Gap IDs at Discovery

**Axis:** C-15 single-axis

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration with scope | PASS | Phase 1.2 role catalog + Phase 2a operation-role matrix per entity |
| C-02 | Per-role record scope | PASS | Matrix has explicit Record Scope column (Org/BU/Parent-Child BU/Team/User/Sharing-[name]) |
| C-03 | FLS per-role mapping | PASS | Phase 2b table: Read Allowed Roles / Write Allowed Roles / Denied Roles per field |
| C-04 | Consolidated gap structure | PASS | Security Gap Register with ID/Entity/Field/Role/Gap Type/Risk; Phase 3 gate |
| C-05 | Escalation path tracing | PASS | Phase 2e format: `[Role] -> [mechanism] -> [resource reached]`; confirmed and ruled-out paths both required |
| C-06 | Sharing rule conflict analysis | PASS | Phase 2c CONFLICT verdict requires rule name + role + over-exposed record set |
| C-07 | Team membership gap analysis | PASS | Phase 2d checks team dependency per entity; self-addition scenario explicit |
| C-08 | Remediation guidance | PASS | Phase 5a: `[G-##]: Apply [specific change]... Current state / Target state / After fix` per gap |
| C-09 | Defense-in-depth assessment | PASS | Phase 5b table with "Gaps Referenced" column per entity |
| C-10 | Real-time gap accumulation | PASS | "Assign the next sequential ID the moment a gap is identified during entity or field traversal. Do not batch-assign." |
| C-11 | Explicit non-escalation | PASS | Phase 2e ruled-out format names access level + mechanism for every Write role |
| C-12 | Phase-gate completeness | PASS | Phase 3 gate table names entities covered, sensitive fields by name, scope decisions |
| C-13 | Entity-level closure marker | **PARTIAL** | "ENTITY CLEAR" format covers clean entities only; no analogous closure block when gaps are found — gap-containing entities advance without an operations+fields+gaps-tallied assertion |
| C-14 | Per-role sharing rule verdict | PASS | Phase 2c: "For every role in 1.2: state sharing rule verdict explicitly — whether rules were found or not. Silence is not acceptable." |
| C-15 | Numbered gap identifiers | PASS | [G-##] sequential IDs at discovery; "Re-describing a gap in lieu of citing its ID is a format failure" in both gap identifier rules AND output requirements |

**Worksheet:**
```
Essential:    4/4  →  4/4  × 60  = 60.00
Recommended:  3/3  →  3/3  × 30  = 30.00
Aspirational: 7.5/8 → 7.5/8 × 10 =  9.38

Composite: 99.38
Golden (all essential + composite >= 80): YES
```

---

### V-02 — Lifecycle Emphasis: Entity Closure Protocol

**Axis:** C-13 single-axis

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration with scope | PASS | Phase 1.2 + Phase 2a per entity |
| C-02 | Per-role record scope | PASS | Operation-role matrix with Record Scope column |
| C-03 | FLS per-role mapping | PASS | Phase 2b: Read Allowed / Write Allowed / Denied per field |
| C-04 | Consolidated gap structure | PASS | Security Gap Register + Phase 3 gate |
| C-05 | Escalation path tracing | PASS | Phase 2e with both confirmed and ruled-out formats |
| C-06 | Sharing rule conflict analysis | PASS | Phase 2c audit table; conflicts require rule name + role + record set |
| C-07 | Team membership gap analysis | PASS | Phase 2d checks per entity |
| C-08 | Remediation guidance | PASS | Phase 5a `[Gap #]: Apply... Current / Target / After fix` |
| C-09 | Defense-in-depth assessment | PASS | Phase 5b table; stock role summary Phase 5c |
| C-10 | Real-time gap accumulation | PASS | "Add to Security Gap Register now" at field and sharing rule analysis time |
| C-11 | Explicit non-escalation | PASS | Phase 2e ruled-out format: "Checked [Role]: write on [specific ops]. No escalation because [mechanism]." |
| C-12 | Phase-gate completeness | PASS | Phase 3 gate table: Closure Block Written / Operations Count / Fields by Name / Gaps (N) |
| C-13 | Entity-level closure marker | **PASS** | Mandatory ENTITY CLOSURE block with (a) operations reviewed per CRUD op + roles, (b) sensitive fields by name + FLS status, (c) gaps tallied by count; "covered above" is an explicit format failure |
| C-14 | Per-role sharing rule verdict | PASS | Phase 2c verdict per role; ENTITY CLOSURE element (d) lists every role in 1.2 with its verdict before advancing |
| C-15 | Numbered gap identifiers | **PARTIAL** | Gap register has "#" column; remediation cites `[Gap #]:`; but output requirements don't flag re-description as a format failure — weaker downstream citation enforcement than V-01/V-04/V-05 |

**Worksheet:**
```
Essential:    4/4  →  4/4  × 60  = 60.00
Recommended:  3/3  →  3/3  × 30  = 30.00
Aspirational: 7.5/8 → 7.5/8 × 10 =  9.38

Composite: 99.38
Golden (all essential + composite >= 80): YES
```

---

### V-03 — Role Sequence: Per-Role Sharing Verdict Spine

**Axis:** C-14 single-axis

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration with scope | PASS | Phase 1.2 includes Entities Touched; Phase 2a per-role operation matrix across entities |
| C-02 | Per-role record scope | PASS | Per-role operation table with Record Scope per entity |
| C-03 | FLS per-role mapping | PASS | Phase 2b: role × entity × field read/write per FLS profile |
| C-04 | Consolidated gap structure | PASS | Security Gap Register with role-primary organization |
| C-05 | Escalation path tracing | PASS | Phase 2d escalation table: four vectors, POSSIBLE/NOT POSSIBLE + evidence |
| C-06 | Sharing rule conflict analysis | PASS | SHARING RULE VERDICT: "CONFLICT FOUND: [Rule] expands [Role] access to [record set]" |
| C-07 | Team membership gap analysis | PASS | Phase 2c team membership check per role |
| C-08 | Remediation guidance | PASS | Phase 5a `[Gap #]: Apply... Current / Target / After fix` |
| C-09 | Defense-in-depth assessment | PASS | Phase 5b entity-level table |
| C-10 | Real-time gap accumulation | PASS | Gap register populated inline during role traversal |
| C-11 | Explicit non-escalation | PASS | Phase 2d requires NOT POSSIBLE verdict with evidence for every vector for every Write role |
| C-12 | Phase-gate completeness | PASS | Phase 3 gate confirms sharing rule verdicts and escalation verdicts per role before advancing |
| C-13 | Entity-level closure marker | **FAIL** | Role-first organization: there are no entity sections to close. The structural event that C-13 requires (entity advance gated by closure assertion) is absent by design. |
| C-14 | Per-role sharing rule verdict | PASS | Primary axis: SHARING RULE VERDICT mandatory for every role before advancing; covers every "Entities Touched"; explicit negative confirmation required |
| C-15 | Numbered gap identifiers | PASS | Gap register has "#" column; Phase 5a cites `[Gap #]:`; Phase 3 gate lists "Gaps Found (N)" by ID |

**Worksheet:**
```
Essential:    4/4  →  4/4  × 60  = 60.00
Recommended:  3/3  →  3/3  × 30  = 30.00
Aspirational: 7/8  →  7/8  × 10  =  8.75

Composite: 98.75
Golden (all essential + composite >= 80): YES
```

---

### V-04 — Combined: Numbered Gap IDs (C-15) + Entity Closure Protocol (C-13)

**Axis:** Causal coupling — entity closure is the ID-assignment point

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration with scope | PASS | Phase 1.2 + per-entity operation-role matrix |
| C-02 | Per-role record scope | PASS | Matrix with Record Scope column per entity |
| C-03 | FLS per-role mapping | PASS | Phase 2b with Read Allowed / Write Allowed / Denied |
| C-04 | Consolidated gap structure | PASS | Security Gap Register with PROVISIONAL/Promoted lifecycle |
| C-05 | Escalation path tracing | PASS | Phase 2e: escalation confirmed or ruled-out format for every Write role |
| C-06 | Sharing rule conflict analysis | PASS | Phase 2c: `[PROVISIONAL: [Rule] expands [Role] access... SHARING-CONFLICT]` → promoted at closure |
| C-07 | Team membership gap analysis | PASS | Phase 2d: self-addition scenario; provisional if gap found |
| C-08 | Remediation guidance | PASS | Phase 5a: `[G-##]: Apply...` with current/target/after-fix; re-description explicitly a format failure |
| C-09 | Defense-in-depth assessment | PASS | Phase 5b table with "Open Gaps (IDs)" column linking enforcement layer to gap IDs |
| C-10 | Real-time gap accumulation | PASS | [PROVISIONAL] signals appear inline during traversal (not deferred to summary); promoted at closure |
| C-11 | Explicit non-escalation | PASS | Phase 2e ruled-out format requires named mechanism per Write role |
| C-12 | Phase-gate completeness | PASS | Phase 3 "Promotion Audit" gate confirms closure blocks written, provisional signals promoted, sequential IDs assigned |
| C-13 | Entity-level closure marker | **PASS** | Entity closure = ID-assignment block: (a) ops reviewed per CRUD op + roles, (b) sensitive fields by name + FLS status, (c) provisional signals → promoted IDs table; structurally mandatory before next entity |
| C-14 | Per-role sharing rule verdict | **PASS** | Phase 2c requires explicit per-role sharing verdict inline; ENTITY CLOSURE (d) requires listing every role from 1.2 with its sharing verdict before advancing |
| C-15 | Numbered gap identifiers | **PASS** | Primary axis: provisional→[G-##] at closure; "re-description in lieu of ID citation is a format failure" in output requirements; Phase 5b "Open Gaps (IDs)" cites IDs in defense-in-depth table |

**Worksheet:**
```
Essential:    4/4 →  4/4  × 60  = 60.00
Recommended:  3/3 →  3/3  × 30  = 30.00
Aspirational: 8/8 →  8/8  × 10  = 10.00

Composite: 100.00
Golden (all essential + composite >= 80): YES
```

---

### V-05 — Combined: Verdict Vocabulary + Inertia Framing

**Axis:** Baseline-as-null-hypothesis; BASELINE MATCH / DEVIATION [G-##] verdict binary

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role enumeration with scope | PASS | Phase 1.2 includes Dataverse Stock Baseline column; baseline vs actual matrix in Phase 2a |
| C-02 | Per-role record scope | PASS | Phase 2a: "Actual Record Scope" column per role per entity |
| C-03 | FLS per-role mapping | PASS | Phase 2b: FLS baseline expectation vs actual; Read Allowed / Write Allowed per field |
| C-04 | Consolidated gap structure | PASS | Security Deviation Register with Baseline / Actual / Deviation Type columns |
| C-05 | Escalation path tracing | PASS | Phase 2e: baseline risk stated before checking actual; escalation confirmed → DEVIATION [G-##] |
| C-06 | Sharing rule conflict analysis | PASS | Phase 2c: "DEVIATION [G-##]: [Rule name] expands [Role] access to [record set]. Baseline expected: no sharing rules." |
| C-07 | Team membership gap analysis | PASS | Phase 2d: baseline team dependency declared, actual checked, BASELINE MATCH / DEVIATION verdict |
| C-08 | Remediation guidance | PASS | Phase 5a: `[G-##]: Deviation from baseline: [expected]. Actual: [found]. Fix: Apply [specific change]... After fix: returns to baseline` |
| C-09 | Defense-in-depth assessment | PASS | Phase 5b: "Deviations That Threaten This Layer (IDs)" column per entity enforcement layer |
| C-10 | Real-time gap accumulation | PASS | Deviations assigned [G-##] at point of discovery during Phase 2 steps; no batch assignment |
| C-11 | Explicit non-escalation | PASS | Phase 2e: "No escalation path. Mechanism: [specific reason]. Baseline risk assessment: CONFIRMED / REVISED." |
| C-12 | Phase-gate completeness | PASS | Phase 3 gate: "Baseline Declared? / Sharing Verdicts: All Roles Covered? / Deviations Found (IDs) / Baseline Matches Confirmed (N)" |
| C-13 | Entity-level closure marker | **PASS** | ENTITY CLOSURE block: (a) operations reviewed by CRUD op + roles, (b) sensitive fields by name with FLS verdict, (c) deviations logged with IDs |
| C-14 | Per-role sharing rule verdict | **PASS** | Primary axis: Phase 2c per-role sharing verdict table with BASELINE MATCH / DEVIATION binary; "Silence on a clean role fails this section" |
| C-15 | Numbered gap identifiers | **PASS** | DEVIATION [G-##] assigned at discovery; Phase 5a cites by [G-##]; "re-description instead of ID citation is a format failure" in output requirements |

**Worksheet:**
```
Essential:    4/4 →  4/4  × 60  = 60.00
Recommended:  3/3 →  3/3  × 30  = 30.00
Aspirational: 8/8 →  8/8  × 10  = 10.00

Composite: 100.00
Golden (all essential + composite >= 80): YES
```

---

## Rankings

| Rank | Variation | Composite | Golden | Key differentiator |
|------|-----------|-----------|--------|--------------------|
| 1 | V-04 | **100.00** | YES | Provisional→promotion coupling causally links C-13 and C-15; most structurally robust |
| 1 | V-05 | **100.00** | YES | Baseline-first null hypothesis eliminates sharing rule silence by design |
| 3 | V-01 | 99.38 | YES | C-13 partial: ENTITY CLEAR only for clean entities; gap-containing entities lack closure |
| 3 | V-02 | 99.38 | YES | C-15 partial: weaker downstream citation enforcement; no "re-description = format failure" warning |
| 5 | V-03 | 98.75 | YES | C-13 fail: role-first organization structurally prevents entity-level closure |

---

## Excellence Signals

**V-04 — Causal coupling of C-13 and C-15:**
The provisional→promotion mechanism makes entity closure the ID-assignment point. This means (a) you cannot close an entity without reviewing its provisional signals, and (b) you cannot assign IDs without closing entities. The two criteria become a single structural event. Neither can be satisfied without the other, and neither can be skipped without the omission being visible in the promotion table. This is a higher-order design pattern: pairing two structural requirements so that satisfying one is the mechanism for satisfying the other.

**V-05 — Null hypothesis as inertia framing:**
Declaring the baseline state before checking actual configuration forces every check to produce an explicit verdict — the model cannot simply skip clean roles because it must confirm BASELINE MATCH before moving on. The binary verdict vocabulary (BASELINE MATCH / DEVIATION [G-##]) is equally important: with only two outcomes possible, silence is detectable as a missing row rather than a quietly omitted case. This pattern generalizes: any criterion that fails by silence can be enforced by a binary verdict vocabulary anchored to a declared baseline.

**V-04 + V-05 — Entity closure as sharing rule verdict aggregator:**
Both top-scoring variations absorb per-role sharing rule coverage into the entity closure block (V-04 element (d), V-05 elements (b)+(c)). This means C-14 is enforced by the same structural event as C-13 — entity closure becomes a multi-criterion gate rather than a single-criterion format element. The pattern: entity closure blocks can be extended to subsume adjacent criteria that operate at entity granularity, reducing the number of distinct structural events the model must track.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["provisional-to-promotion coupling: making entity closure the ID-assignment point causally links C-13 and C-15 so that satisfying one requires satisfying the other — neither can be omitted without a visible gap in the promotion table", "null hypothesis inertia framing: declaring the expected baseline state before checking actual forces every role-entity pair to produce an explicit BASELINE MATCH or DEVIATION verdict, making sharing rule silence structurally impossible", "binary verdict vocabulary anchored to baseline: two-outcome verdict options (BASELINE MATCH / DEVIATION [G-##]) eliminate ambiguity and make omission detectable as a missing row rather than a quietly skipped case"]}
```
