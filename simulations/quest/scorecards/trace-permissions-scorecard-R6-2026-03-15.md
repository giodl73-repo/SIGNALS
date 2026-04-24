## Scorecard: trace-permissions v6 — Round 6

### Rubric: Essential (N=4, 60 pts) | Recommended (N=3, 30 pts) | Aspirational (N=17, 10 pts)

---

### V-01 — Lifecycle Emphasis: Pre-Declaration Commitment (C-20 single-axis)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | E | **PASS** | 2a table maps roles to Create/Read/Write/Delete/Assign with Record Scope column |
| C-02 | E | **PASS** | Record Scope column explicit in every 2a row |
| C-03 | E | **PASS** | 2b FLS table with Read/Write/Denied per role; MISSING-FLS triggers G-## |
| C-04 | E | **PASS** | Security Gap Log with G-## identifiers assigned at discovery |
| C-05 | R | **PASS** | Phase 3 five-vector table traces escalation end-to-end per role |
| C-06 | R | **PASS** | 2c sharing rule audit with Conflict-G-## verdict column |
| C-07 | R | **PASS** | 2d team membership dependency check with self-addition assessment |
| C-08 | A | **PASS** | Phase 4a: every G-## gets `Change [element] from [state] to [state]` |
| C-09 | A | **PASS** | 4b defense-in-depth table assesses each layer's independence |
| C-10 | A | **PASS** | Gap log open throughout; "assign G-## now / do not defer" at each step |
| C-11 | A | **PASS** | 2e: "Checked [Role]: audited [operations]. No escalation via [mechanisms] because [reason]" |
| C-12 | A | **PASS** | PHASE 1 GATE and PHASE 2 GATE name coverage before advancing |
| C-13 | A | **PASS** | ENTITY CLOSURE block with Operations/Fields/Gaps/Sharing/Escalation fields |
| C-14 | A | **PASS** | Per-role sharing rule statement required for every role in 2a regardless of outcome |
| C-15 | A | **PASS** | G-## identifiers in gap log; 4a cites same identifiers |
| C-16 | A | **PASS** | ENTITY CLOSURE rules: gaps found → name G-##; gap-free → state NONE explicitly |
| C-17 | A | **PASS** | Five-vector table with POSSIBLE/NOT POSSIBLE verdict per vector per Write-capable role |
| C-18 | A | **PASS** | "Closing Mechanism (NOT POSSIBLE only)" column requires naming the specific privilege confirmed absent |
| C-19 | A | **PASS** | ESCALATION ROLL-UP: Vectors assessed, POSSIBLE count, NOT POSSIBLE count, Mechanisms cited, Declaration honored, Composite verdict |
| C-20 | A | **PASS** | COMMITMENT DECLARATION block before each role's vector table; Phase 3 Gate checks every NOT POSSIBLE traces to a named declaration; roll-up "Declaration honored" field enforces contract |
| C-21 | A | **PARTIAL** | Fourth column ("Closing Mechanism (NOT POSSIBLE only)") is structurally isolated from verdict cell — satisfies the separation requirement. But column content instruction mixes mechanism citation with declaration tracing ("state which declared assumption this confirms") rather than enforcing a single structural fact only; the "one structural fact / no verdict language" exclusivity rule absent |
| C-22 | A | **FAIL** | No per-vector Design Assumption block above each vector. COMMITMENT DECLARATION is role-level only; the vector table is monolithic — no inertia anchor stated at each vector's own block |
| C-23 | A | **PARTIAL** | No-path escalation check: "Checked [Role]: audited [operations]. No escalation because [reason]" — structured but not in formal Checked/Confirmed/Conclusion three-field format. Sharing rule clean: "confirmed do not expand -- basis: [evidence]" — has a basis field but no "Conclusion" label. Partial evidential structure throughout, not full symmetric standard |
| C-24 | A | **PARTIAL** | Roll-up "Mechanisms cited: [list the closing mechanism per NOT POSSIBLE verdict by vector name]" — restates per vector by name. But no explicit prohibition on back-references; "list" instruction does not prevent "see table above" responses |

**Worksheet:**
- Essential: 4/4 → 4/4 × 60 = **60.00**
- Recommended: 3/3 → 3/3 × 30 = **30.00**
- Aspirational: 13 PASS + 3 PARTIAL (0.5 each) = 14.5 / 17 × 10 = **8.53**

**V-01 Composite: 98.53** | Golden: YES (all essential pass, composite ≥ 80)

---

### V-02 — Inertia Framing: Design Assumption Mini-Block Per Vector (C-22 single-axis)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | E | **PASS** | 2a operation-role matrix present |
| C-02 | E | **PASS** | Record Scope column in 2a |
| C-03 | E | **PASS** | 2b FLS table with per-role read/write/denied |
| C-04 | E | **PASS** | Security Gap Log with G-## at discovery |
| C-05 | R | **PASS** | Phase 3 escalation per vector per role |
| C-06 | R | **PASS** | 2c sharing rule conflict analysis |
| C-07 | R | **PASS** | 2d team membership dependency check |
| C-08–C-19 | A | **PASS** (×12) | All retained from prior rounds: gap accumulation, phase gates, entity closure, sharing verdicts, G-## cross-reference, gap parity, five-vector enumeration, NOT POSSIBLE mechanism citation, per-role roll-up |
| C-20 | A | **FAIL** | No role-level COMMITMENT DECLARATION block. Design Assumption is per-vector (inside each mini-block) not a pre-analysis role-level commitment. C-20 requires the structural assumption declared before any vector analysis begins for that role; V-02 declares it at each vector block, not at role entry. No "Declaration honored" field in roll-up |
| C-21 | A | **FAIL** | Mini-block format has no dedicated structural column. Each vector is a prose block (Design Assumption / Evidence / Verdict) — the closing mechanism is embedded in the Verdict field ("Assumption Confirmed: [structural fact]"), not in an isolated column detectable by structural inspection |
| C-22 | A | **PASS** | Each vector mini-block opens with "> **Design Assumption:** [Role] is expected to... If this assumption holds, the verdict is NOT POSSIBLE." Verdict says "NOT POSSIBLE -- Assumption Confirmed: [structural fact]" OR "POSSIBLE -- Assumption Refuted: G-##". ESCALATION ROLL-UP adds "Assumptions honored: [count/vectors assessed]" |
| C-23 | A | **PARTIAL** | "Assumption Confirmed: [structural fact]" for NOT POSSIBLE verdicts is structured but not in three-field format. Sharing rule clean: "confirmed do not expand -- basis: [evidence]" — partial. Team no-dependency: "Confirmed: [Entity] access requires no team membership. Checked: [what was reviewed]" — has two of three fields |
| C-24 | A | **PARTIAL** | Roll-up "Mechanisms cited: [list the structural fact cited per NOT POSSIBLE verdict by vector name]" — per-vector listing but no explicit "no back-references" prohibition |

**Worksheet:**
- Essential: 4/4 → 60.00
- Recommended: 3/3 → 30.00
- Aspirational: 13 PASS + 2 PARTIAL = 14.0 / 17 × 10 = **8.24**

**V-02 Composite: 98.24** | Golden: YES

---

### V-03 — Phrasing Register: No-Finding as Formal Declaration (C-23 single-axis)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01–C-04 | E | **PASS** (×4) | Full operation-role matrix, explicit scope, FLS per-role, G-## gap log |
| C-05–C-07 | R | **PASS** (×3) | Escalation tracing, sharing conflict, team gap analysis |
| C-08–C-19 | A | **PASS** (×12) | All retained |
| C-20 | A | **FAIL** | No COMMITMENT DECLARATION block. Five-vector uses monolithic table (no role-level pre-analysis commitment) |
| C-21 | A | **PARTIAL** | Has a "Closing Mechanism" fourth column — structurally isolated from verdict. But column content rule does not enforce exclusivity: allows "[structural mechanism if NOT POSSIBLE; N/A if POSSIBLE]" without the strict "one structural fact only / no verdict language" prohibition. The Verdict cell itself uses No-Finding Declaration format inline (mixing declaration into the verdict cell rather than isolating pure structural fact in a dedicated column) |
| C-22 | A | **FAIL** | No per-vector Design Assumption block. Monolithic five-vector table, no inertia anchor per vector |
| C-23 | A | **PASS** | No-Finding Declaration format (Checked / Confirmed / Conclusion) required at every level: NOT POSSIBLE vector verdicts, sharing rule clean per role (explicit three-field template provided), team no-dependency, escalation no-path per role, gap-free ENTITY CLOSURE with "confirmed by reviewing [what was checked]" rule. Bare negatives explicitly prohibited: "A bare negative... without the three-field declaration does not satisfy the evidential standard" |
| C-24 | A | **PARTIAL** | Roll-up "Mechanisms cited: [list closing mechanism per NOT POSSIBLE verdict by vector name]" — per-vector listing but no explicit back-reference prohibition |

**Worksheet:**
- Essential: 4/4 → 60.00
- Recommended: 3/3 → 30.00
- Aspirational: 13 PASS + 2 PARTIAL = 14.0 / 17 × 10 = **8.24**

**V-03 Composite: 98.24** | Golden: YES

---

### V-04 — Combined: Structural Column Isolation (C-21) + Self-Contained Roll-Up (C-24)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01–C-04 | E | **PASS** (×4) | Full matrix, scope, FLS, G-## |
| C-05–C-07 | R | **PASS** (×3) | Escalation, sharing conflict, team gap |
| C-08–C-19 | A | **PASS** (×12) | All retained |
| C-20 | A | **FAIL** | No COMMITMENT DECLARATION block |
| C-21 | A | **PASS** | `Structural Basis` column rules explicitly enforced: "holds exactly one value per row: either a single structural fact sentence (NOT POSSIBLE) or literal `N/A -- G-##` (POSSIBLE). No verdict language. No conditionals. No evidence prose." Column integrity self-check required before ESCALATION ROLL-UP. A blank or generic Structural Basis on NOT POSSIBLE is a named format error |
| C-22 | A | **FAIL** | No per-vector Design Assumption. Monolithic table format |
| C-23 | A | **PARTIAL** | Sharing rule clean: "confirmed do not expand -- basis: [evidence]" — partial structure. Team no-dependency: "Confirmed: [Entity] access requires no team membership. Checked: [what was reviewed]." — two of three fields. Escalation no-path: "Checked [Role]: [operations audited]. No escalation via [mechanisms] because [reason per mechanism]." — structured but not formal three-field format with explicit labels |
| C-24 | A | **PASS** | `Mechanisms cited (restated inline -- not by reference to the table above)` with per-vector sub-lines: "- Sharing rule creation: [restate structural fact]..." Roll-up rule: "Writing 'see table above', 'mechanisms cited in Phase 3', or any back-reference is a format violation." Phase 3 Gate explicitly checks "Every roll-up Mechanisms cited entry restates its structural fact inline -- no back-references" |

**Worksheet:**
- Essential: 4/4 → 60.00
- Recommended: 3/3 → 30.00
- Aspirational: 14 PASS + 1 PARTIAL = 14.5 / 17 × 10 = **8.53**

**V-04 Composite: 98.53** | Golden: YES

---

### V-05 — Combined: All Five New Criteria (C-20 + C-21 + C-22 + C-23 + C-24)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01–C-04 | E | **PASS** (×4) | Full operation-role matrix, explicit scope, FLS per-role, G-## gap log |
| C-05–C-07 | R | **PASS** (×3) | Phase 3 escalation tracing, 2c sharing conflict, 2d team gap |
| C-08–C-19 | A | **PASS** (×12) | All retained structural disciplines |
| C-20 | A | **PASS** | COMMITMENT DECLARATION table before each Write-capable role names assumption per vector; every NOT POSSIBLE verdict in vector mini-blocks must trace to this table. Roll-up "Declaration honored: [count / 5]" must equal NOT POSSIBLE count — mismatch flags uncredited verdicts. Phase 3 Gate: "Declaration honored count equals NOT POSSIBLE count in every roll-up" |
| C-21 | A | **PASS** | Each vector mini-block has a single-row Evidence/Verdict/Structural Basis table. Structural Basis column rule: "one structural fact sentence only -- no verdict language, no evidence prose." Phase 3 Gate: "Every Structural Basis cell holds only one structural fact -- no verdict language or evidence prose." Both the column structure and its exclusivity rule are enforced |
| C-22 | A | **PASS** | Each vector mini-block opens with "> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]" Verdict statement: "NOT POSSIBLE -- Assumption Confirmed: [structural fact]" or "POSSIBLE -- Assumption Refuted: G-##". Phase 3 Gate: "Every vector mini-block restates the inertia frame from the COMMITMENT DECLARATION" |
| C-23 | A | **PASS** | No-Finding Declaration format (Checked / Confirmed / Conclusion) applied universally: FLS correct-configuration, sharing rule clean per role, team no-dependency, escalation no-path per role, gap-free ENTITY CLOSURE with "confirmed by reviewing [what]." Bare negatives explicitly disallowed: "NOT POSSIBLE / none found / NONE / no gaps without this three-field format do not satisfy the evidential standard anywhere in the output" |
| C-24 | A | **PASS** | Roll-up "Mechanisms cited (restated inline -- not by reference to vectors above)" with per-vector sub-lines restating Structural Basis cells. Roll-up rule: "'See vectors above' or any back-reference is a format violation." Phase 3 Gate: "Every Mechanisms cited entry restates its structural fact inline -- no back-references." Roll-up is self-contained and independently auditable |

**Worksheet:**
- Essential: 4/4 → 60.00
- Recommended: 3/3 → 30.00
- Aspirational: 17/17 × 10 = **10.00**

**V-05 Composite: 100.00** | Golden: YES

---

## Rankings

| Rank | Variation | Composite | All Essential |
|------|-----------|-----------|--------------|
| 1 | **V-05** | **100.00** | YES |
| 2 | V-01 | 98.53 | YES |
| 2 | V-04 | 98.53 | YES |
| 4 | V-02 | 98.24 | YES |
| 4 | V-03 | 98.24 | YES |

---

## Excellence Signals from V-05

**1. Four-point audit chain per structural fact.** Each NOT POSSIBLE structural fact appears at four independent structural positions: (a) declared as assumption in COMMITMENT DECLARATION table, (b) restated as Inertia Frame at the vector block, (c) isolated in the Structural Basis column cell, (d) restated inline in ESCALATION ROLL-UP Mechanisms cited. A structural fact that passes through all four points is auditable at each location independently.

**2. Declaration honored as a roll-up integrity counter.** The roll-up includes `Declaration honored: [count / 5]` that must equal the NOT POSSIBLE count. This creates an automatic cross-check: if any NOT POSSIBLE verdict was issued without a prior declared assumption, the counter mismatch flags it before the Phase 3 Gate runs. Self-enforcing without requiring a reader to scan back.

**3. No-Finding Declaration extends to correct configurations, not just absences.** V-03 introduced the three-field format for absences. V-05 extends it explicitly to FLS correct-configuration findings — when a sensitive field has no FLS gap, the trace declares it as a positive No-Finding rather than silently advancing. This eliminates the implicit "correct configuration = invisible" pattern.

**4. Structural Basis column + Inertia Frame dual isolation.** V-04 isolated the structural fact in a column; V-02 anchored each vector to an assumption. V-05 combines both: the Structural Basis column holds the structural fact, and the Inertia Frame above each vector confirms which declared assumption that cell must satisfy. The column provides format-level detectability; the inertia frame provides semantic traceability. They address independent failure modes simultaneously.

**5. Phase 3 Gate is maximally specific.** V-05's Phase 3 Gate has nine checks (vs. four in V-03, six in V-04, seven in V-01), including: "Declaration honored count equals NOT POSSIBLE count in every roll-up" — the only gate that enforces the C-20/C-24 integration at the output level.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["four-point audit chain: structural fact traverses commitment declaration, inertia frame restatement, isolated column cell, and self-contained roll-up inline restatement as four independent structural positions", "declaration-honored counter in roll-up as automatic cross-check: NOT POSSIBLE count must equal declaration count, making uncredited verdicts self-flagging before the phase gate", "no-finding declaration extends to correct configurations (not just absences), making clean FLS a positive assertion equal in evidential weight to a gap finding"]}
```
