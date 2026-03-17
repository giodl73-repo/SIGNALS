## flow-trigger Round 2 Scorecard

**All five R2 variations achieve Gold.** The rubric expansion (C-10 and C-11) differentiates only in the aspirational tier.

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-04 | 4/4 | 3/3 | 4/4 | **100** | GOLD |
| V-05 | 4/4 | 3/3 | 4/4 | **100** | GOLD |
| V-02 | 4/4 | 3/3 | 3/4 | **97.5** | GOLD |
| V-01 | 4/4 | 3/3 | 2/4 | **95** | GOLD |
| V-03 | 4/4 | 3/3 | 1/4 | **92.5** | GOLD |

---

**Key per-variation verdicts on the two new criteria:**

| | C-10 (Proactive Budget Gate) | C-11 (Dual-Population Table) |
|--|--|--|
| V-01 | FAIL — gate after pathology (instruction only, not structural) | PASS — table first, "Fires? YES or NO only" enforced |
| V-02 | PASS — Section 3 before Section 4, labeled mandatory | FAIL — prose enumeration, no unified Fires? table |
| V-03 | FAIL — gate after verdicts in Pass 3 | FAIL — Fires? column present but no YES/NO enforcement rule |
| V-04 | PASS — "runs before pathology -- mandatory" | PASS — "No row may omit this column. No trigger may be omitted." |
| V-05 | PASS — Phase 3 before Phase 4, "does not require a confirmed storm" | PASS — "sole enumeration surface. No supplemental trigger lists." |

**C-09 split**: V-01 and V-03 fail (no anti-hedge instruction); V-02/V-04/V-05 pass ("unknown is not acceptable").

---

**Two new patterns** from the 100-scoring variations:

1. **Pre-positioned budget gate (labeled mandatory, before pathology section)** — structural pre-positioning eliminates no-storm omission reasoning; a behavioral instruction ("do not wait") is insufficient without it
2. **Dual-population Fires? YES/NO table as sole enumeration surface with explicit supplemental-list ban** — the enforcement *rule* ("YES or NO only, no row may omit this column") is what makes the criterion structural; a Fires? column without the rule is not sufficient (V-03 failure case)

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-positioned budget gate as numbered mandatory section before pathology detection eliminates no-storm omission", "dual-population Fires? YES/NO table as sole enumeration surface with explicit supplemental-list ban makes C-11 a structural guarantee"]}
```
s not acceptable" enforcement |
| C-10 | Aspirational | FAIL | Budget gate in STEP 5 comes after STEP 4 pathology; "Do not wait for a storm verdict from Step 4" is a behavioral instruction, not structural -- model has already written storm verdict before reaching gate |
| C-11 | Aspirational | PASS | Dual-population table is FIRST output; "Fires?: YES or NO only -- every registered automation must appear as one row"; supplemental lists explicitly banned; row-number cross-referencing enforces completeness |

**Essential**: 4/4 -> 60
**Recommended**: 3/3 -> 30
**Aspirational**: 2/4 -> 5
**Composite**: **95** -- GOLD

---

### V-02 — Single Axis: Lifecycle Emphasis (Budget Gate Before Pathology)

| Criterion | Band | Result | Evidence |
|-----------|------|--------|---------|
| C-01 | Essential | PASS | SECTION 2 enumerates all automations with YES/NO; "Number YES rows in firing sequence. List NO rows after YES rows with '--' sequence number" -- both populations required |
| C-02 | Essential | PASS | YES rows numbered in firing sequence; execution timing (sync/async) required per YES row in the enumeration |
| C-03 | Essential | PASS | "If YES: execution timing (sync/async), inputs, outputs, side effects" -- I/O required per firing trigger |
| C-04 | Essential | PASS | SECTION 4 covers all three pathologies with Verdict + Evidence + Remediation (PRESENT/RISK only) |
| C-05 | Recommended | PASS | Side effects enumerated per YES trigger; "side effects (external state changes or 'none')" -- clean triggers must declare "none" |
| C-06 | Recommended | PASS | Condition required for all rows: "failed expression for NO rows; expression that passed, or 'unconditional -- always fires on [event type]'" |
| C-07 | Recommended | PASS | SECTION 1 scenario declaration with all required fields |
| C-08 | Aspirational | PASS | SECTION 4 remediation required for PRESENT/RISK: "specific construct: run-after condition, depth check, field guard, concurrency control -- name the exact flow/plugin/setting" |
| C-09 | Aspirational | PASS | SECTION 3: "Estimation required -- 'unknown' is not acceptable. State assumptions explicitly." + calculation basis template: "Flow A calls [N] Dataverse actions + [M] connector actions = [X] requests" -- anti-hedge enforced |
| C-10 | Aspirational | PASS | SECTION 3 is structurally before SECTION 4; "This section runs before pathology detection. Do not wait for a storm verdict." Gate fires on M >= 3 AND side effects -- model cannot defer based on storm outcome |
| C-11 | Aspirational | FAIL | SECTION 2 uses prose/numbered list format, not a unified table; no "Fires?" column; YES/NO is embedded in prose items -- C-11 pass condition requires "one unified table with explicit fires/does-not-fire distinction per row" |

**Essential**: 4/4 -> 60
**Recommended**: 3/3 -> 30
**Aspirational**: 3/4 -> 7.5
**Composite**: **97.5** -- GOLD

---

### V-03 — Single Axis: Role Sequence (Threat Model Leads)

| Criterion | Band | Result | Evidence |
|-----------|------|--------|---------|
| C-01 | Essential | PASS | PASS 2 STEP 2: "Include both firing and non-firing. Use a single table -- no supplemental lists." Table includes all registered automations; YES rows numbered, NO rows with "--" |
| C-02 | Essential | PASS | "# = firing sequence number for YES rows"; Sync/Async column in table; execution order is a structural property of the table |
| C-03 | Essential | PASS | "For YES rows: fill all columns with concrete values" -- I/O columns mandatory; NO rows get "--" |
| C-04 | Essential | PASS | PASS 3 pathology verdicts table covers all three; PASS 1 threat declaration primes completeness; PASS 2d cross-check catches discrepancies |
| C-05 | Recommended | PASS | Side Effects column in PASS 2 table; YES rows required to name external state changes; clean triggers must declare absence |
| C-06 | Recommended | PASS | Condition column required for all rows; NO rows must "state the condition that filtered it out" |
| C-07 | Recommended | PASS | PASS 2 STEP 1 scenario declaration with entity, solution layer, environment, license tier |
| C-08 | Aspirational | PASS | PASS 3 pathology table has Remediation column: "specific construct only -- name the flow, the step, the condition expression, or the plugin registration setting" |
| C-09 | Aspirational | FAIL | PASS 3 budget table present but no anti-hedge instruction; "estimate and declare confidence level" pattern absent; model may hedge API request counts |
| C-10 | Aspirational | FAIL | Budget gate in PASS 3 comes after pathology verdicts table in PASS 3; structural ordering: verdicts table -> budget gate -> confidence note; model has written pathology section before evaluating the gate |
| C-11 | Aspirational | FAIL | Fires? column present in table header but no explicit "YES or NO only" enforcement per-row rule; design notes confirm "RISK -- table present but no Fires?/YES/NO enforcement"; column may be populated inconsistently |

**Essential**: 4/4 -> 60
**Recommended**: 3/3 -> 30
**Aspirational**: 1/4 -> 2.5
**Composite**: **92.5** -- GOLD

Note: V-03's threat-first role sequence is the strongest C-04 depth mechanism of any R2 variation. The 92.5 score entirely reflects aspirational failures (C-09, C-10, C-11), not any structural gap in essential or recommended coverage.

---

### V-04 — Combined: Output Format + Lifecycle Emphasis

| Criterion | Band | Result | Evidence |
|-----------|------|--------|---------|
| C-01 | Essential | PASS | "UNIFIED TRIGGER REGISTRY" as "single source of truth"; "No supplemental lists permitted"; "Fires?: YES or NO. No row may omit this column. No trigger may be omitted from the table." |
| C-02 | Essential | PASS | "# = Firing sequence number for YES rows (execution order)"; Sync/Async column present; "--" for NO rows makes ordering unambiguous |
| C-03 | Essential | PASS | "for YES rows, concrete values" required for Inputs and Outputs columns; "--" for NO rows |
| C-04 | Essential | PASS | SECTION 4 pathology table covers all three; Evidence and Remediation columns required; architectural reason required for ABSENT verdicts (not "no issues found") |
| C-05 | Recommended | PASS | Side Effects column: "name all external state changes or write 'none'" -- clean triggers must declare "none" |
| C-06 | Recommended | PASS | "Condition Expression: non-empty for all rows"; "No filter -- always fires on [event type]" valid for unconditional; NO rows: "State the failed expression" -- cannot write "N/A" |
| C-07 | Recommended | PASS | SECTION 1 scenario as structured table with all required fields; explicitly labeled format |
| C-08 | Aspirational | PASS | SECTION 4: "Remediation: exact construct (flow condition node, plugin depth check, Copilot topic condition, concurrency limit setting, trigger filter expression)" with specific PA/Copilot Studio examples |
| C-09 | Aspirational | PASS | SECTION 3 budget table; "Show calculation basis. 'Unknown' is not acceptable -- estimate with stated assumptions." Strong anti-hedge + per-automation calculation basis required |
| C-10 | Aspirational | PASS | "SECTION 3 -- BUDGET GATE (runs before pathology -- mandatory)"; "This section uses values from Section 2. It does not wait for a storm verdict." Structural ordering: Section 3 before Section 4 -- model cannot reach pathology before completing budget gate |
| C-11 | Aspirational | PASS | "Fires?: YES or NO. No row may omit this column. No trigger may be omitted from the table." Registry summary code block forces explicit M, N, Non-firing counts -- structural verification layer |

**Essential**: 4/4 -> 60
**Recommended**: 3/3 -> 30
**Aspirational**: 4/4 -> 10
**Composite**: **100** -- GOLD

---

### V-05 — Combined: All Four Axes (R2 Golden Candidate)

| Criterion | Band | Result | Evidence |
|-----------|------|--------|---------|
| C-01 | Essential | PASS | PHASE 2 "2b. Dual-population trigger table: List every automation... firing AND non-firing... This table is the sole enumeration surface. No supplemental trigger lists." Registry summary code block requires M, N, Non-firing counts |
| C-02 | Essential | PASS | "# = Integer sequence for YES rows (execution order). '--' for NO rows"; Sync/Async column with Pre-commit = Sync, Post-commit = Async clarification |
| C-03 | Essential | PASS | "YES rows: concrete values (field schema name, OData value, token name)" for Inputs; "concrete state changes (field schema name written, entity name created, message type sent, API endpoint called)" for Outputs -- most specific I/O requirements of any variation |
| C-04 | Essential | PASS | PHASE 1 threat declaration primes pathology awareness; PHASE 4 verdicts table covers all three; PHASE 2d hypothesis cross-check surfaces unexpected triggers; ABSENT verdicts require specific guard mechanism named |
| C-05 | Recommended | PASS | "external state changes with specifics (email recipient role, audit table schema name, child entity schema name, API hostname) or 'none'" -- highest specificity requirement; "--" not valid for YES rows |
| C-06 | Recommended | PASS | "Condition Expression: mandatory for all rows. Do not write 'N/A.'" with unconditional YES allowed; PHASE 1 hypothesis cross-check in Phase 2d catches shallow condition evaluation |
| C-07 | Recommended | PASS | PHASE 2 "2a. Scenario block" as a code-fence table with all fields; license tier requires basis stated ("assumed: TIER -- basis: REASON") |
| C-08 | Aspirational | PASS | PHASE 4 remediation with construct-specific examples for PA (trigger condition expression syntax), Dataverse Plugin (Depth check code), Copilot Studio (condition node syntax), and required phrasing for ABSENT verdicts |
| C-09 | Aspirational | PASS | PHASE 3: "Do not write 'unknown' -- estimate and declare confidence level"; "state the minimum plausible count and reason from there"; budget risk level (LOW/MEDIUM/HIGH) adds stratification |
| C-10 | Aspirational | PASS | "PHASE 3 -- BUDGET GATE" structurally before "PHASE 4 -- PATHOLOGY VERDICTS"; "Gate condition does not require a confirmed storm." -- strongest structural pre-positioning of any variation |
| C-11 | Aspirational | PASS | "Fires?: YES or NO. Every registered automation must appear as exactly one row."; "sole enumeration surface. No supplemental trigger lists."; PHASE 2d cross-check confirms completeness against Phase 1 hypothesis |

**Essential**: 4/4 -> 60
**Recommended**: 3/3 -> 30
**Aspirational**: 4/4 -> 10
**Composite**: **100** -- GOLD

---

## Variation Ranking

1. **V-05** (100) — Quality leader on all criteria. Threat-first priming (PHASE 1) produces the deepest C-04 coverage and most specific C-05 side effects of any variation. Hypothesis cross-check (2d) catches gaps that pure enumeration misses. Budget risk stratification (LOW/MEDIUM/HIGH) exceeds rubric minimum for C-09. Phase 1 hypothesis reconciliation in PHASE 4 is a built-in learning loop. V-04 ties on composite; V-05 wins on depth within passing criteria.

2. **V-04** (100) — Strongest minimal mechanism. Cleanest isolation of C-10 + C-11 co-satisfaction without the threat-lead complexity. Confirms the mechanism (pre-positioned budget gate + dual-population table + anti-hedge instruction) is sufficient on its own. "Mandatory" label on the budget gate section is the clearest enforcement signal in any R2 variation.

3. **V-02** (97.5) — Structurally solves C-10 (pre-positioned budget gate with anti-hedge) but fails C-11 (prose enumeration format). Clearest single-axis test for the budget-gate pre-positioning fix.

4. **V-01** (95) — Structurally solves C-11 (dual-population table as first output with "Fires? YES or NO only" enforcement) but fails C-10 (gate after pathology). Clearest single-axis test for the table fix.

5. **V-03** (92.5) — Highest C-04 depth potential via threat-first design, but fails C-09, C-10, and C-11. The threat-lead axis is structurally sound; its combined-axis integration in V-05 fixes the aspirational misses.

---

## R2 Findings

**All five variations achieve Gold.** The R2 rubric expansion (C-10 and C-11) differentiates only in the aspirational tier. Essential and recommended scores are uniformly maxed -- R2 variation design inherited strong coverage from R1 and targeted new aspirational criteria only.

**C-10 requires structural pre-positioning, not just instruction.** V-01 and V-03 have budget gate sections with correct gate conditions but both come after pathology detection. V-01 even says "Do not wait for a storm verdict" -- yet the structural failure mode remains: the model writes storm = ABSENT in the pathology section before reaching the budget gate. V-02, V-04, and V-05 fix this by numbering the budget gate section before the pathology section.

**C-11 requires unified table + explicit YES/NO enforcement, not just a table with a Fires? column.** V-03 has a Fires? column in its table but lacks the "YES or NO only -- every registered automation must appear as one row" enforcement rule. Without it, the column may be populated inconsistently. V-01, V-04, and V-05 pass because they add the explicit per-column enforcement rule. V-02 fails because its enumeration format is prose.

**C-09 is now the secondary aspirational differentiator.** In R1, C-09 separated V-05 from all others (V-05 was the only variation with a budget template). In R2, all variations have a budget template. The differentiator is the anti-hedge instruction ("unknown is not acceptable"). V-01 and V-03 lack it; V-02, V-04, V-05 include it.

**V-04 is the R2 mechanism proof.** It isolates C-10 + C-11 co-satisfaction without the threat-lead complexity. Its 100 score confirms the mechanism is sufficient on its own. V-05's threat declaration adds depth but not rubric points.

---

## Excellence Signals from V-04 and V-05

1. **Pre-positioned budget gate labeled "mandatory"** (V-04 Section 3, V-05 Phase 3): placing the budget gate as a numbered section BEFORE pathology detection, labeled "mandatory" and "does not wait for a storm verdict," structurally prevents no-storm omission. Model cannot write a storm verdict before the gate fires.

2. **Dual-population Fires? YES/NO table as sole enumeration surface with explicit supplemental-list ban** (V-04 Section 2, V-05 Phase 2): "Fires?: YES or NO. No row may omit this column. No trigger may be omitted from the table." + "No supplemental trigger lists." Together these make C-11 omission a structural error rather than a model-dependent choice.

3. **Registry summary code block with explicit M, N, Non-firing counts** (V-04, V-05): forcing explicit M, N, and side-effect presence values in a code-fence immediately after the table creates downstream-referenceable variables that the budget gate section uses -- preventing the M count from being implicit or inconsistent.

4. **Anti-hedge quantification instruction attached to budget template** (V-02, V-04, V-05): "'Unknown' is not acceptable -- estimate with stated assumptions" converts C-09 from a structural presence check to a content quality check. V-04/V-05 add per-automation calculation basis requirements that produce intermediate arithmetic, not just final numbers.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-positioned budget gate as numbered mandatory section before pathology detection eliminates no-storm omission", "dual-population Fires? YES/NO table as sole enumeration surface with explicit supplemental-list ban makes C-11 a structural guarantee"]}
```
