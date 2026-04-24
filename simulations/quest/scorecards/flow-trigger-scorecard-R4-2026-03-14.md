# flow-trigger — Round 4 Scorecard

## Rubric Version: v4 | Variations: V-01 through V-05

---

## Criterion-by-Criterion Evaluation

### C-01 — Unified Trigger Table *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Registry Analyst role: "one table... The `Fires?` column accepts `YES` or `NO` only — no row may omit this column" |
| V-02 | PASS | Section 1 column rules pre-declared: "`Fires?`: YES or NO only — no row may omit this column — no 'maybe', 'pending', or blank" |
| V-03 | PASS | Phase 2 trigger table with "`Fires?`: YES or NO only — no row may omit this column" |
| V-04 | PASS | Registry Analyst role: same enforcement; single unified table |
| V-05 | PASS | Role 2 Rule 3: "`Fires?`: YES or NO only — no row may omit this column — no blanks, no 'TBD', no 'maybe'" |

---

### C-02 — Trigger Inputs/Outputs *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Registry Analyst rules explicitly state: "`Inputs`: Concrete field/record/event values consumed" and "`Outputs`: Concrete record writes, notifications, or downstream calls produced" |
| V-02 | PASS | Column rules: "`Inputs`: at least one concrete value or field reference; 'N/A' is not acceptable" and "`Outputs`: at least one concrete record write, notification, or downstream call; 'N/A' is not acceptable" |
| V-03 | **FAIL** | Phase 2 rules specify Fires?, #, Condition, and Side Effects enforcement but no explicit concrete-value requirement for Inputs or Outputs columns; "N/A is not acceptable" absent |
| V-04 | **FAIL** | Registry Analyst rules cover Fires?, #, Condition, and Side Effects — Inputs and Outputs columns are present in the table header but have no concrete-value enforcement; "N/A is not acceptable" absent |
| V-05 | PASS | Role 2 Rule 6: "`Inputs`: at least one concrete field name or event property — 'N/A' is not acceptable"; Rule 7: "`Outputs`: at least one concrete record write, notification, or downstream call — 'N/A' is not acceptable" |

---

### C-03 — Firing Sequence *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | "`#`: Integer for YES rows in firing sequence order; `--` for NO rows" |
| V-02 | PASS | "`#`: Integer (1, 2, 3...) for YES rows in firing sequence; `--` for NO rows" |
| V-03 | PASS | Phase 2 rules: "`#`: integer for YES rows in firing sequence; `--` for NO rows" |
| V-04 | PASS | Registry Analyst rules: "`#`: integer for YES rows in firing sequence; `--` for NO rows" |
| V-05 | PASS | Role 2 Rule 4: "`#`: integer for YES rows in firing sequence order; `--` for NO rows" |

---

### C-04 — Pathology Detection *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Pathology Analyst role covers Trigger Storms, Missing Triggers, Circular Triggers each with DETECTED/NOT DETECTED/INDETERMINATE verdicts and named-construct remediation requirement |
| V-02 | PASS | Section 3 covers all three pathology types with verdict keywords and named-construct remediation |
| V-03 | PASS | Phase 3 covers all three types; remediation requires "specific Power Automate construct by name" |
| V-04 | PASS | Pathology Analyst role works from TC-2 and TC-3 evidence; TC-referenced cascade pairs strengthen circular trigger detection |
| V-05 | PASS+ | Role 4 format rules: numbered subsections, verdict-first structure, TC-2 cascade pair citations, every DETECTED verdict requires a specific Power Automate or Copilot Studio construct |

---

### C-05 — Side Effects *(recommended)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | "`Side Effects`: Secondary state changes, additional triggers enqueued, external calls; write 'none' if the trigger is clean" |
| V-02 | PASS | "`Side Effects`: secondary state changes or additional triggers enqueued; write 'none' for clean triggers" |
| V-03 | PASS | Phase 2: "`Side Effects`: name secondary state changes; write 'none' for clean triggers" |
| V-04 | PASS | Registry Analyst: TC-3 INTERNAL/EXTERNAL classification required per side-effecting trigger — strongest enforcement via pre-cataloging |
| V-05 | PASS | Role 2 Rule 8: "reference TC-3 for any trigger with a side effect; write 'none' for clean triggers" |

---

### C-06 — Condition Evaluation *(recommended)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | "`Condition`: The gate expression that controls firing; 'always fires' must be explicitly justified" |
| V-02 | PASS | "`Condition`: exact gate expression; 'always fires' only with explicit justification" |
| V-03 | PASS | Phase 2: "`Condition`: gate expression; 'always fires' requires explicit justification" |
| V-04 | PASS | Registry Analyst: "gate expression referencing TC-1 candidate analysis where applicable"; TC-1 pre-identifies candidate conditions |
| V-05 | PASS | Role 2 Rule 5: "'always fires' requires a one-sentence justification inline" |

---

### C-07 — Scenario Boundary *(recommended)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Input block explicitly requires "Environment/solution layer" and "Triggering change event (field name, field value transition, or lifecycle event)" |
| V-02 | PASS | Same input block; environment/solution layer and triggering change event named |
| V-03 | PASS | Phase 1 scope block: `Event: <field or lifecycle change>` and `Layer: <Dataverse / SharePoint / Teams / other>` declared before any analysis |
| V-04 | PASS | Input requires "Environment/solution layer" and "Triggering change event"; TC-1 traces condition-to-event relationship |
| V-05 | PASS | Input requires "Environment/solution layer" and "Triggering change event (field transition, record creation, lifecycle event)"; Role 5 Narrator names both explicitly |

---

### C-08 — Remediation Recommendations *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Pathology Analyst: "recommend a specific Power Automate pattern (e.g., child-flow consolidation, compose-action deduplication) referencing the construct by name" for both storms and circular triggers |
| V-02 | PASS | Pathology section: "Remediation (if DETECTED): name a specific Power Automate construct" per subsection |
| V-03 | PASS | Phase 3: "Remediation (if DETECTED): specific Power Automate construct by name" for storms; "guard condition or run-once pattern" for circular |
| V-04 | PASS | Pathology Analyst: "Remediation (if DETECTED): specific Power Automate construct by name" with TC-3 EXTERNAL classification enabling connector-specific framing |
| V-05 | PASS | Role 4 Rule 5: "Every DETECTED or IDENTIFIED verdict includes a remediation naming a specific Power Automate or Copilot Studio construct" — structural enforcement at role level |

---

### C-09 — Trigger Storm Quantification *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | Per-automation arithmetic present; run duration requires "seconds or range" (hedging blocked); but storm depth as a standalone number is not required — no explicit "state storm chain depth as N" instruction in the storm or budget sections |
| V-02 | **FAIL** | Per-automation arithmetic and run duration integer required ("prose estimates not acceptable"); same gap: storm depth as a number not required — budget arithmetic gives request totals but not chain depth |
| V-03 | **FAIL** | Phase 4 has total requests, run duration, risk rating; same gap as V-01/V-02: storm depth not quantified as a number |
| V-04 | PASS | TC-2 threat summary requires `Cascade pairs: <count>` as an integer — storm depth is quantified pre-table; budget section adds request arithmetic and run duration; cascade pair count from TC-2 satisfies "storm depth as a number" |
| V-05 | PASS | TC-2 `Cascade pairs: <integer>` required; Budget Gate has run duration as "<integer> seconds or <low>–<high> second range — prose estimates not acceptable"; storm chain depth declared before table construction |

---

### C-10 — Proactive Budget Gate *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | Role sequence: Registry Analyst → Pathology Analyst → Budget Analyst — budget runs AFTER pathology; C-10 requires budget section before pathology detection |
| V-02 | **FAIL** | Section order: Trigger Table → Registry Summary → Pathology Detection → Budget Analysis — budget (Section 4) after pathology (Section 3) |
| V-03 | **FAIL** | Phase order: Scope → Trigger Table → Pathology Detection → Budget Assessment — budget (Phase 4) after pathology (Phase 3) |
| V-04 | **FAIL** | Role sequence: Threat Analyst → Registry Analyst → Pathology Analyst → Budget Analyst — budget (Role 4) after pathology (Role 3); proactive gate inverted |
| V-05 | PASS | Role sequence: Threat Analyst → Registry Analyst → **Budget Analyst (Role 3)** → Pathology Analyst (Role 4) → Narrator — budget gate explicitly before pathology; "This section appears before pathology detection regardless of whether a storm is confirmed" |

---

### C-11 — Dual-Population Table *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | "Produce one table with the following columns. Every row must have a value in every column. The `Fires?` column accepts `YES` or `NO` only — no row may omit this column" |
| V-02 | PASS | Column rules with YES/NO enforcement stated before table; single Section 1 table only |
| V-03 | PASS | Phase 2 produces one unified trigger table with YES/NO enforcement |
| V-04 | PASS | "one table" with YES/NO only enforcement; no separate lists permitted |
| V-05 | PASS | Role 2 Rule 1: "One unified table — no separate registered/firing lists"; Rule 3: YES or NO only |

---

### C-12 — Registry Summary Code Block *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Registry Analyst produces code-fence with M, N, NF as named variables; "This block is the downstream reference for Roles 2 and 3" — Role 3 Budget Analyst explicitly reads "M and N values" from the block |
| V-02 | PASS | Section 2 code-fence with M, N, NF; "This block is referenced by name in Sections 3 and 4" — explicit downstream reference stated |
| V-03 | PASS | Phase 2 produces `summary` code-fence with M, N, NF; Phase 4 references "M >= 1 OR N >= 3" — downstream reference present; Phase 3 told to "Reference the Phase 2 table and summary" |
| V-04 | PASS | Registry Analyst produces `summary` code-fence with M, N, NF; "Reference Registry Summary M and N" stated in Role 4 — named variable reference enforced |
| V-05 | PASS | Role 2: "write the Registry Summary block exactly as shown" with M, N, NF as explicit integers; Role 3 reads M and N by name; Role 4 "Reference: Registry Summary N"; downstream re-derivation structurally blocked |

---

### C-13 — Per-Automation Calculation Basis *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Budget Analyst: "List additive action count components: 'Trigger name: X Dataverse actions + Y connector actions = Z requests per invocation'" — one line per YES trigger required |
| V-02 | PASS | "Per-automation arithmetic (required; aggregate totals alone do not satisfy this section): For each YES trigger, write one line: 'Trigger name: X [action type] + Y [action type] = Z requests per invocation'" |
| V-03 | PASS | Phase 4: "For each YES trigger, one line: 'Trigger name: X [action type] + Y [action type] = Z requests per invocation'" |
| V-04 | PASS | Budget Analyst: "Per-automation arithmetic (required)" with explicit one-line format per YES trigger; "Reference TC-3 EXTERNAL classifications when assessing connector action counts" adds cross-reference depth |
| V-05 | PASS | Role 3 Rule 1: "Per-automation arithmetic — required; aggregate totals alone do not satisfy this section" with explicit per-trigger line format |

---

### C-14 — Specialist Role Accountability Chain *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Three named roles: Registry Analyst, Pathology Analyst, Budget Analyst — each owns specific output sections; explicit non-revision rule: "Each role owns specific output sections and does NOT revise the prior role's output"; role handoff forces fresh-eyes derivation |
| V-02 | **FAIL** | Single domain expert ("You are a Power Automate / Copilot Studio domain expert") performs all sections; no named specialist roles; no accountability chain |
| V-03 | **FAIL** | Phase-based structure with single anonymous expert; lifecycle phases ≠ specialist role accountability; no named analysts with section ownership |
| V-04 | PASS | Four named roles: Threat Analyst, Registry Analyst, Pathology Analyst, Budget Analyst — explicit section ownership with "strict accountability boundaries"; Roles 2–4 reference TC section identifiers from Role 1 |
| V-05 | PASS | Five named roles: Threat Analyst, Registry Analyst, Budget Analyst, Pathology Analyst, Simulation Narrator — each with explicit "Owns:" declaration and format rules; "Roles may not merge or share sections" |

---

### C-15 — Threat-First Phase Pre-Cataloging *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | Analysis begins with trigger table construction (Registry Analyst, Role 1); no pre-cataloging phase; threats discovered inline during table construction |
| V-02 | **FAIL** | Section 1 immediately writes trigger table; no threat-surface catalog before table is written |
| V-03 | **FAIL** | Phase 1 is Scope Definition (one paragraph + `scope` parameter block); no TC-1/TC-2/TC-3 threat catalog; trigger table written in Phase 2 without pre-identified threat references |
| V-04 | PASS | Role 1 (Threat Analyst) produces TC-1 (Automation Candidates), TC-2 (Cascade Paths), TC-3 (Side-Effect Scope) with threat summary block before trigger table; Roles 2–4 must "reference the Threat Catalog by section identifier (TC-1, TC-2, TC-3)" |
| V-05 | PASS | Role 1 (Threat Analyst) owns TC-1, TC-2, TC-3 with numbered format rules before trigger table; "Roles 2 through 5 must not introduce trigger assessments absent from the Role 1 Threat Catalog without explicitly noting the addition as an inline discovery" — catalog integrity enforced |

---

## Score Summary

```
composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 8 * 10)
```

| ID | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | E | R | A | Composite | Band |
|----|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|---|---|---|-----------|------|
| V-01 | P | P | P | P | P | P | P | P | **F** | **F** | P | P | P | **P** | **F** | 4/4 | 3/3 | 5/8 | **96.3** | Gold |
| V-02 | P | P | P | P | P | P | P | P | **F** | **F** | P | P | P | **F** | **F** | 4/4 | 3/3 | 4/8 | **95.0** | Gold |
| V-03 | P | **F** | P | P | P | P | P | P | **F** | **F** | P | P | P | **F** | **F** | 3/4 | 3/3 | 4/8 | **80.0** | Silver |
| V-04 | P | **F** | P | P | P | P | P | P | **P** | **F** | P | P | P | **P** | **P** | 3/4 | 3/3 | 7/8 | **83.75** | Silver |
| V-05 | P | P | P | P | P | P | P | P | **P** | **P** | P | P | P | **P** | **P** | 4/4 | 3/3 | 8/8 | **100** | Gold |

---

## Ranking

| Rank | ID | Score | Band | C-14 | C-15 | C-09 | C-10 | C-02 | Notes |
|------|----|-------|------|------|------|------|------|------|-------|
| 1 | **V-05** | 100 | Gold | PASS | PASS | PASS | PASS | PASS | First variation to achieve perfect score under v4; Budget Analyst placed before Pathology Analyst — the only structural fix that solves C-10 |
| 2 | **V-01** | 96.3 | Gold | PASS | FAIL | FAIL | FAIL | PASS | C-14 solved by three-role structure; C-15 absent; C-10 inverted by role sequence order (Budget last) |
| 3 | **V-02** | 95.0 | Gold | FAIL | FAIL | FAIL | FAIL | PASS | Strong format enforcement solves C-01/C-11/C-12/C-13; single-analyst design blocks C-14 and C-15 |
| 4 | **V-04** | 83.75 | Silver | PASS | PASS | PASS | FAIL | FAIL | Best aspirational profile outside V-05 (7/8); C-10 inverted (Pathology before Budget); C-02 structural gap |
| 5 | **V-03** | 80.0 | Silver | FAIL | FAIL | FAIL | FAIL | FAIL | Phase boundary structure improves completion discipline; no role accountability, no threat catalog, C-02 structural gap |

---

## Excellence Signals from V-05

### Signal 1 — Budget Role Position as Compliance Mechanism

V-05 is the only variation in Rounds 1–4 where the Budget Analyst (Role 3) is placed sequentially before the Pathology Analyst (Role 4). All prior designs that included a budget section placed it last, violating C-10. V-05 treats role sequence order itself as a structural compliance mechanism: the model physically cannot write pathology findings before budget arithmetic is complete because the role index enforces it. This is not a gate condition — it is a position constraint.

### Signal 2 — Numbered Format Rules as Role-Local Enforcement Checklist

V-05 declares format rules as numbered lists within each role definition, not as prose descriptions. Role 2 has 8 numbered rules that must be satisfied in sequence before the first table row is written. Numbered rules create an implicit checklist: a model following the prompt must check "1. One unified table ✓, 2. Columns in order ✓, 3. Fires? YES or NO only ✓..." This is structurally stronger than bullet lists because numbered items have a natural sequence-completion interpretation that bullets lack.

### Signal 3 — Simulation Narrator as Terminal Cross-Validation Layer

Role 5 (Simulation Narrator) introduces a synthesis pattern not present in any prior variation: a terminal role that can only reference findings from prior sections, never introduce new data, and must issue a deployment readiness verdict (READY FOR PRODUCTION / REQUIRES REMEDIATION / DO NOT DEPLOY) that synthesizes all findings. This creates a built-in coherence check — any inconsistency between pathology verdicts, budget risk rating, and the final deployment assessment is immediately visible. The Narrator's output signals whether the five sections tell a single coherent story.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Budget Analyst role positioned before Pathology Analyst makes C-10 impossible to violate — role sequence index is a compliance mechanism, not a gate condition", "Numbered format rules as role-local sequential checklist enforce column compliance before first row is written; stronger than bullet lists because numbered items imply a check-off sequence", "Terminal synthesis narrator role cross-validates all prior sections and issues deployment readiness verdict without introducing new findings — structural coherence check across five independent role outputs"]}
```
