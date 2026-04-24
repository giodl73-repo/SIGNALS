## Round 7 Scorecard — `trace-permissions` (Rubric v7)

---

### Per-Variation Criterion Evaluation

#### V-01 — Output Format: Structural Basis Column Content Exclusivity (C-25 single-axis)

**Foundation:** R6 V-04 (five-vector table, Structural Basis column) + explicit exclusivity rule naming prohibited content forms.

| ID | Criterion | Result | Evidence Note |
|----|-----------|--------|---------------|
| C-01 | Operation-role matrix | **PASS** | 2a table with Create/Read/Write/Delete/Assign and Record Scope |
| C-02 | Record access scope | **PASS** | Record Scope column in 2a; Org/BU/Team/User/Sharing explicitly named |
| C-03 | FLS coverage | **PASS** | 2b table with per-role read/write/denied per sensitive field |
| C-04 | Security gap identification | **PASS** | Gap Log with G-## identifiers at discovery; gap types and risk mandatory |
| C-05 | Escalation path tracing | **PASS** | 2e entity-level escalation check + Phase 3 five-vector table |
| C-06 | Sharing rule conflict analysis | **PASS** | 2c sharing rule audit with Conflict-[G-##] verdict |
| C-07 | Team membership gap analysis | **PASS** | 2d team membership dependency section |
| C-08 | Remediation guidance | **PASS** | 4a cites every G-## with element/entity/role, current→target state |
| C-09 | Defense-in-depth assessment | **PASS** | 4b independence table per entity |
| C-10 | Real-time gap accumulation | **PASS** | "Assign the next sequential identifier the moment a gap is identified. Do not defer." |
| C-11 | Explicit non-escalation documentation | **PASS** | 2e: "Checked [Role]: [ops]. No escalation via [mechanisms] because [reason per mechanism]" |
| C-12 | Phase-gate completeness checkpoint | **PASS** | PHASE 1 GATE and PHASE 2 GATE tables with named checks |
| C-13 | Entity-level closure marker | **PASS** | ENTITY CLOSURE block with Operations reviewed, fields, gaps, sharing, escalation |
| C-14 | Per-role sharing rule explicit verdict | **PASS** | "required for every role in 2a, regardless of outcome" |
| C-15 | Numbered gap identifiers | **PASS** | G-## scheme; 4a remediation cites by identifier |
| C-16 | Entity closure parity across gap states | **PASS** | "An entity where gaps were found must name those gaps by G-## in this block" |
| C-17 | Multi-vector escalation enumeration | **PASS** | Five named vectors with explicit POSSIBLE/NOT POSSIBLE verdicts per row |
| C-18 | NOT POSSIBLE verdict closure mechanism citation | **PASS** | Structural Basis column required per NOT POSSIBLE row |
| C-19 | Per-role escalation roll-up | **PASS** | ESCALATION ROLL-UP block with Vectors assessed / POSSIBLE / NOT POSSIBLE / Mechanisms cited |
| C-20 | Pre-declaration commitment | **FAIL** | No COMMITMENT DECLARATION block before vectors |
| C-21 | Structural isolation of closing mechanism | **PASS** | Dedicated Structural Basis column, separate from Verdict cell |
| C-22 | Inertia framing per vector | **FAIL** | No per-vector Inertia Frame restating design assumption |
| C-23 | No-finding as positive declaration | **FAIL** | Sharing rule: inline "confirmed do not expand -- basis: [evidence]" -- not labeled three-field; team no-dep: two-field (Confirmed + Checked); vector verdicts: bare POSSIBLE/NOT POSSIBLE |
| C-24 | Roll-up mechanisms cited restates inline | **PASS** | Template: "restate the structural fact from the Structural Basis cell" per vector; "not by reference to the table above" in label |
| C-25 | Closing mechanism column content exclusivity | **PASS** | Explicit rule names: no verdict language, no declaration tracing ("do not write 'confirms declared assumption'"), no evidence prose, no conditionals, no placeholder text |
| C-26 | Universal three-field no-finding format | **FAIL** | Five site types not enumerated; no three-field format at vector verdicts, sharing rule, team, entity closure |
| C-27 | Explicit anti-back-reference prohibition | **FAIL** | "not by reference to the table above" is a parenthetical in the field label, not a formal instruction-level prohibition naming multiple disallowed forms |
| C-28 | Composite verdict names mechanism type per vector | **FAIL** | Composite verdict: "[no escalation path identified for this role / ESCALATION PATHS: G-##]" -- count/conclusion only |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 15/21 → 7.14
**V-01 Total: 97.14**

---

#### V-02 — Lifecycle Emphasis: Universal Three-Field No-Finding Format at All Enumerated Sites (C-26 single-axis)

**Foundation:** Introduces No-Finding Declaration (Checked/Confirmed/Conclusion) required at all five explicitly enumerated site types; two-of-three-field formats named violations.

| ID | Criterion | Result | Evidence Note |
|----|-----------|--------|---------------|
| C-01–C-07 | Essential + Recommended | **PASS (all)** | Same structural foundation as V-01 |
| C-08–C-19 | Aspirational base | **PASS (all)** | Gap log, phase gates, entity closure, per-role sharing, G-## cross-reference, five-vector table, NOT POSSIBLE mechanism in Closing Mechanism column, roll-up |
| C-20 | Pre-declaration commitment | **FAIL** | No COMMITMENT DECLARATION |
| C-21 | Structural isolation | **PASS** | "Closing Mechanism" column, separate from Verdict cell; "The Closing Mechanism column holds the single structural fact extracted from that declaration -- a separate column for structural isolation" |
| C-22 | Inertia framing | **FAIL** | No per-vector assumption blocks |
| C-23 | No-finding as positive declaration | **PASS** | Three-field format (Checked/Confirmed/Conclusion) required at escalation vector verdicts (Verdict cell), sharing rule clean, team no-dep, escalation no-path, gap-free entity closure |
| C-24 | Roll-up mechanisms cited restates inline | **PASS** | Template shows vector-by-vector inline listing; "restated inline" instruction present |
| C-25 | Closing mechanism column content exclusivity | **FAIL** | Column instruction: "holds the single structural fact extracted from that declaration" -- describes intent but does NOT name prohibited content forms; no "no declaration tracing," no "no verdict language" in the instruction |
| C-26 | Universal three-field no-finding format | **PASS** | Five site types enumerated; two-of-three-field formats explicitly prohibited by name at all sites |
| C-27 | Explicit anti-back-reference prohibition | **FAIL** | Roll-up instruction says "list closing mechanism... restated inline" -- "list" framing without naming disallowed forms |
| C-28 | Composite verdict names mechanism type per vector | **FAIL** | "[no escalation path identified for this role / ESCALATION PATHS: G-##]" -- no mechanism types inline |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 16/21 → 7.62
**V-02 Total: 97.62**

---

#### V-03 — Phrasing Register: Explicit Anti-Back-Reference Prohibition in Roll-Up (C-27 single-axis)

**Foundation:** R6 V-04 five-vector table with Structural Basis column + explicit prohibition in Mechanisms cited instruction naming disallowed forms.

| ID | Criterion | Result | Evidence Note |
|----|-----------|--------|---------------|
| C-01–C-07 | Essential + Recommended | **PASS (all)** | Standard foundation |
| C-08–C-19 | Aspirational base | **PASS (all)** | Same as V-01 baseline |
| C-20 | Pre-declaration commitment | **FAIL** | No COMMITMENT DECLARATION |
| C-21 | Structural isolation | **PASS** | Dedicated Structural Basis column |
| C-22 | Inertia framing | **FAIL** | No per-vector assumption blocks |
| C-23 | No-finding as positive declaration | **FAIL** | Sharing rule: inline prose; team no-dep: Confirmed + Checked (two-field, no Conclusion); vector verdicts: bare POSSIBLE/NOT POSSIBLE in table cell |
| C-24 | Roll-up mechanisms cited restates inline | **PASS** | Explicit prohibition and per-vector inline template lines |
| C-25 | Closing mechanism column content exclusivity | **FAIL** | Column instruction says "No verdict language. No evidence prose. No conditionals." -- does NOT name "no declaration tracing"; declaration tracing remains unprohibited in the column instruction |
| C-26 | Universal three-field no-finding format | **FAIL** | Five site types not enumerated; no three-field format at sharing rule, team, or entity closure sites |
| C-27 | Explicit anti-back-reference prohibition | **PASS** | "Do not write 'see table above', 'mechanisms cited in Phase 3', 'see vectors above', 'as documented above', or any equivalent back-reference. Back-references to the vector table are not permitted in this field." |
| C-28 | Composite verdict names mechanism type per vector | **FAIL** | Count/conclusion format only |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 15/21 → 7.14
**V-03 Total: 97.14**

---

#### V-04 — Combined: C-25 + C-26 + C-27 (three single-axis criteria)

**Foundation:** Three independent constraints combined: column exclusivity naming prohibited forms, universal three-field format at all five site types, explicit back-reference prohibition naming disallowed forms. Built on a five-vector table (not mini-blocks), so no COMMITMENT DECLARATION or inertia frames.

| ID | Criterion | Result | Evidence Note |
|----|-----------|--------|---------------|
| C-01–C-07 | Essential + Recommended | **PASS (all)** | Standard foundation |
| C-08–C-19 | Aspirational base | **PASS (all)** | Phase gates, entity closure (gap-containing and clean), per-role sharing, G-## cross-reference, five-vector table, mechanism in Structural Basis column, ESCALATION ROLL-UP |
| C-20 | Pre-declaration commitment | **FAIL** | No COMMITMENT DECLARATION -- five-vector table format, not mini-blocks |
| C-21 | Structural isolation | **PASS** | Dedicated Structural Basis column |
| C-22 | Inertia framing | **FAIL** | No per-vector inertia frame blocks |
| C-23 | No-finding as positive declaration | **PASS** | Verdict cell format: "NOT POSSIBLE -- Checked: [...]; Confirmed: [...]; Conclusion: [...]" -- three-field format in Verdict cell; all five site types carry three-field declarations |
| C-24 | Roll-up mechanisms cited restates inline | **PASS** | Explicit prohibition naming back-reference forms; per-vector template shows inline restatement |
| C-25 | Closing mechanism column content exclusivity | **PASS** | Prohibited content list names: "Verdict language ('NOT POSSIBLE', 'Assumption Confirmed', 'path closed'). Declaration tracing ('confirms the declared assumption', 'per commitment above'). Evidence prose. Conditional language. Placeholder text." -- explicitly names declaration tracing |
| C-26 | Universal three-field no-finding format | **PASS** | Five site types enumerated; "Two-of-three-field formats are explicitly prohibited at all five site types." |
| C-27 | Explicit anti-back-reference prohibition | **PASS** | "Do not write 'see table above', 'mechanisms cited in Phase 3 table', 'see vectors above', 'as documented above', or any equivalent back-reference. Back-references to the vector table are not permitted in this field." |
| C-28 | Composite verdict names mechanism type per vector | **FAIL** | "[no escalation path identified for this role / ESCALATION PATHS: G-##, G-##]" -- no mechanism types inline in the composite verdict sentence |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 18/21 → 8.57
**V-04 Total: 98.57**

---

#### V-05 — Full Stack: R6 V-05 Foundation + All Four New v7 Criteria

**Foundation:** R6 V-05 (COMMITMENT DECLARATION, per-vector mini-blocks with inertia frames, three-field NO FINDING at all sites, Structural Basis column, self-contained roll-up) + C-25 + C-26 + C-27 + C-28.

| ID | Criterion | Result | Evidence Note |
|----|-----------|--------|---------------|
| C-01–C-07 | Essential + Recommended | **PASS (all)** | Standard foundation |
| C-08–C-19 | Aspirational base | **PASS (all)** | Full base: gap log with G-## at discovery; phase gates naming entities covered; ENTITY CLOSURE blocks required for all entities including gap-containing; per-role sharing rule verdicts at all sites; five-vector enumeration via mini-blocks; NOT POSSIBLE mechanism in Structural Basis cell; ESCALATION ROLL-UP with Declaration honored counter |
| C-20 | Pre-declaration commitment | **PASS** | COMMITMENT DECLARATION table before vectors; per-vector structural assumptions declared; "Commitment: each vector mini-block confirms or refutes the stated assumption. A NOT POSSIBLE verdict without a corresponding prior assumption is a contract violation." |
| C-21 | Structural isolation | **PASS** | Dedicated Structural Basis cell in each vector mini-block |
| C-22 | Inertia framing | **PASS** | Each vector mini-block opens with "> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption...]" |
| C-23 | No-finding as positive declaration | **PASS** | Three-field NO FINDING format required at all five site types; "Two-of-three-field formats are explicitly prohibited. Bare negatives do not satisfy the standard at any site." |
| C-24 | Roll-up mechanisms cited restates inline | **PASS** | "Do not write 'see table above'... Back-references to the vector mini-blocks are not permitted in this field." Per-vector inline template lines. |
| C-25 | Closing mechanism column content exclusivity | **PASS** | Prohibited: "Verdict language ('NOT POSSIBLE', 'Assumption Confirmed'). Declaration tracing ('confirms assumption', 'per commitment'). Evidence prose. Conditional language. Placeholder text." -- explicitly names declaration tracing |
| C-26 | Universal three-field no-finding format | **PASS** | Five site types enumerated; two-of-three-field explicitly prohibited; all Phase 2 gate checks include site-specific format verification |
| C-27 | Explicit anti-back-reference prohibition | **PASS** | "Do not write 'see table above', 'mechanisms cited in Phase 3', 'see vectors above', 'as documented above', or any equivalent back-reference. Back-references to the vector mini-blocks are not permitted in this field." |
| C-28 | Composite verdict names mechanism type per vector | **PASS** | FIELD INSTRUCTION: "Name each NOT POSSIBLE vector's closing mechanism type inline in this sentence. Do not write only a count... Format: 'no escalation path from [Role Name]: sharing rule creation -- [mechanism type]; team self-injection -- [mechanism type]; field-value escalation -- [mechanism type]; role hierarchy traversal -- [mechanism type]; record ownership transfer -- [mechanism type].' A count-only sentence does not pass." |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 21/21 → 10.00
**V-05 Total: 100.00**

---

### Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total | Golden? |
|-----------|----------------|------------------|-------------------|-------|---------|
| V-05 | 60 | 30 | 10.00 (21/21) | **100.00** | YES |
| V-04 | 60 | 30 | 8.57 (18/21) | **98.57** | YES |
| V-02 | 60 | 30 | 7.62 (16/21) | **97.62** | YES |
| V-01 | 60 | 30 | 7.14 (15/21) | **97.14** | YES |
| V-03 | 60 | 30 | 7.14 (15/21) | **97.14** | YES |

**Ranking:** V-05 > V-04 > V-02 > V-01 = V-03

---

### Discriminating Criterion Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-20 Pre-declaration | FAIL | FAIL | FAIL | FAIL | **PASS** |
| C-22 Inertia framing | FAIL | FAIL | FAIL | FAIL | **PASS** |
| C-23 No-finding as positive declaration | FAIL | PASS | FAIL | PASS | **PASS** |
| C-25 Column content exclusivity | **PASS** | FAIL | FAIL | **PASS** | **PASS** |
| C-26 Universal three-field format | FAIL | **PASS** | FAIL | **PASS** | **PASS** |
| C-27 Anti-back-reference prohibition | FAIL | FAIL | **PASS** | **PASS** | **PASS** |
| C-28 Composite verdict mechanism types | FAIL | FAIL | FAIL | FAIL | **PASS** |

V-04 vs. V-05 separation: three criteria -- C-20, C-22, C-28. V-04 achieves all three new v7 structural constraints but lacks the COMMITMENT DECLARATION lifecycle and the inertia frame discipline. C-28 is the sole separator within the roll-up: V-04's composite verdict sentence remains count-only; V-05's names each mechanism type inline.

V-01 vs. V-03 tie: both score 15/21. V-01 adds C-25 (column exclusivity), V-03 adds C-27 (anti-back-reference prohibition). Neither has the other's criterion, and neither has C-23, C-26.

V-02 vs. V-01/V-03: V-02 adds C-23 + C-26 (full three-field coverage) but drops C-25 (no exclusivity rule naming prohibited forms in the Closing Mechanism column instruction).

---

### Excellence Signals from V-05

**Signal 1 — Dual-position evidence in the roll-up block.** V-05 is the first variation where both the `Mechanisms cited` field AND the `Composite verdict` sentence independently carry mechanism evidence for each vector. The Mechanisms cited field carries the full structural fact (copied from the Structural Basis cell). The Composite verdict sentence carries the mechanism type per vector (e.g., "sharing rule creation -- no Share privilege"). These are two independent evidence positions within a single roll-up block: the verdict sentence is auditable for mechanism coverage at a glance; the Mechanisms cited field provides full structural detail without table lookup. No prior variation enforced evidence at both positions simultaneously.

**Signal 2 — Declaration honored counter as arithmetic cross-audit.** V-05 introduces `Declaration honored: [count / 5]` in the ESCALATION ROLL-UP with the rule: "Declaration honored must equal NOT POSSIBLE count. Mismatch means a NOT POSSIBLE verdict lacks a prior declared assumption -- identify which vector and add the declaration." This is the first variation where a cross-section consistency check is enforced by arithmetic rather than by reading. A mismatch between the NOT POSSIBLE count and the Declaration honored count is detectable without re-reading the COMMITMENT DECLARATION or the vector mini-blocks.

**Signal 3 — C-28 as the discriminating tier-breaker within the combined stack.** V-04 satisfies C-25, C-26, and C-27 -- three independent structural constraints at three different positions. V-05 adds C-28, which acts on the composite verdict sentence itself. The verdict sentence is the highest-level summary in the roll-up; C-28 requires it to carry mechanism content rather than delegate to the Mechanisms cited field. This means a reader auditing only the verdict sentence (the natural audit entry point) has sufficient evidence without consulting any other field. V-04's verdict sentence is silent on mechanism content; V-05's is self-auditing.

---

### Suggested v8 Criterion (Carried Forward)

**Verdict-level mechanism cross-audit:** The mechanism type named in the Composite verdict sentence and the structural fact restated in the Mechanisms cited field for the same vector explicitly confirm they name the same structural basis -- an explicit cross-check assertion is present rather than accidental alignment. This separates V-05-level outputs (where both positions carry mechanism evidence but alignment is not verified) from outputs where the alignment is stated and confirmed. Failure mode: a composite verdict names mechanism types from memory rather than from the Mechanisms cited or Structural Basis content, creating two independent evidence positions that do not actually agree.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual-position evidence in roll-up block: Composite verdict sentence names mechanism type per NOT POSSIBLE vector independently of Mechanisms cited field -- two positions within the roll-up carry overlapping but non-identical evidence, enabling verdict-sentence-level auditing without consulting any other field or section", "Declaration honored counter enforces arithmetic cross-audit between COMMITMENT DECLARATION and NOT POSSIBLE count -- mismatches are detectable without re-reading prior sections; mechanism type alignment between declared assumption and verdict sentence is not yet verified and is the v8 candidate"]}
```
