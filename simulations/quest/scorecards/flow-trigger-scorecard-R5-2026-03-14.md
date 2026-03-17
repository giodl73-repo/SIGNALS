# flow-trigger — Round 5 Scorecard

## Summary

**Top score: 100** (V-04 and V-05 tied) | **All essential pass: true**

| Rank | ID | Score | Band | C-14 | C-15 | C-16 | C-17 |
|------|----|-------|------|------|------|------|------|
| 1 | **V-04** | 100 | Gold | PASS | PASS | PASS | PASS |
| 1 | **V-05** | 100 | Gold | PASS | PASS | PASS | PASS |
| 3 | **V-03** | 99 | Gold | FAIL | PASS | PASS | PASS |
| 4 | **V-02** | 98 | Gold | FAIL | PASS | FAIL | PASS |
| 5 | **V-01** | 96* | Gold* | FAIL | FAIL | PASS | FAIL |

*V-01 estimated — Section 1 (trigger table) not present in variation file; essential criteria inferred.*

---

## Key Findings

**C-16 specific failure mode confirmed.** V-02 uses `"Verdict: DETECTED / NOT DETECTED / INDETERMINATE"` — the `"Verdict:"` label prefix makes the keyword NOT the first content element. Exact anti-pattern documented. V-01 and V-03 both explicitly prohibit it with `"DO NOT prefix with 'Verdict:'"`.

**4-role minimum is sufficient.** V-04 (no Narrator) and V-05 (with Narrator) both score 100. The Narrator adds terminal coherence checking but zero rubric score. The minimum viable role architecture for full v5 compliance is 4 roles.

**Imperative phrasing achieves 99/100 without roles.** V-03 is the strongest single-analyst result across all rounds — `MUST/DO NOT` numbered rules satisfy C-15, C-16, and C-17 without role structure. C-14 (specialist role accountability) is the only gap.

**No new patterns.** All structural mechanisms in R5 are covered by existing criteria. `new_patterns: []`

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
e unified table — no separate registered/firing lists" |

---

### C-02 — Trigger Inputs/Outputs *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS* | Axis targets C-16 only; no explicit Inputs/Outputs rules visible in Sections 2–4; assumed adequate in implied Section 1; *inferred |
| V-02 | PASS | Column rules: "`Inputs`: at least one concrete field name or event property — 'N/A' is not acceptable"; "`Outputs`: at least one concrete record write, notification, or call — 'N/A' is not acceptable" |
| V-03 | PASS | Rule B-5: "WRITE at least one concrete field name or event property. DO NOT write 'N/A'." Rule B-6: "WRITE at least one concrete record write, notification, or call. DO NOT write 'N/A'." |
| V-04 | PASS | Role 2 Rule 5: "`Inputs`: at least one concrete field name or event property — 'N/A' is not acceptable"; Rule 6: "`Outputs`: at least one concrete record write, notification, or downstream call — 'N/A' is not acceptable" |
| V-05 | PASS | Role 2 Rules 6 and 7: same enforcement as V-04 with identical N/A prohibition |

---

### C-03 — Firing Sequence *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS* | Section 2 M/N/NF block implies firing sequence rows were computed; *inferred from upstream reference |
| V-02 | PASS | "`#`: integer (1, 2, 3...) for YES rows in firing sequence; `--` for NO rows" |
| V-03 | PASS | Rule B-3: "`#` column: WRITE integers for YES rows in firing sequence order. WRITE '--' for NO rows." |
| V-04 | PASS | Role 2 Rule 3: "`#`: integer for YES rows in firing sequence order; `--` for NO rows" |
| V-05 | PASS | Role 2 Rule 4: "`#`: integer for YES rows in firing sequence order; `--` for NO rows" |

---

### C-04 — Pathology Detection *(essential)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 4 covers Trigger Storm (4a), Missing Triggers (4b), Circular Triggers (4c) with verdict keywords, evidence instructions, and remediation requirements; all three pathology types explicitly addressed |
| V-02 | PASS | Section 3 covers all three types with verdict keywords, TC-2 citation evidence instructions, and named-construct remediation per subsection |
| V-03 | PASS | Rule Set D: Rule D-1 "EVALUATE all three pathology types"; Rule D-3 gives verdict keyword set for each type; Rule D-5 requires remediation for every DETECTED/IDENTIFIED verdict |
| V-04 | PASS | Role 4 covers all three subsections with verdict-first format rules, TC-2 citation evidence requirements, and named-construct remediation |
| V-05 | PASS | Role 4 covers all three subsections with same structure as V-04; Role 5 Narrator synthesizes all three verdicts in terminal summary |

---

### C-05 — Side Effects *(recommended)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS* | Section 3 storm-risk flag condition references "any side effect exists" — implies side effect tracking exists in Section 1; *inferred |
| V-02 | PASS | TC-3 section classifies side effects INTERNAL/EXTERNAL; Condition column notes "none" for clean triggers; TC-3 citation in Side Effects column required |
| V-03 | PASS | Rule A-5: "TC-3 MUST list every trigger with a side effect, classified INTERNAL or EXTERNAL"; Rule B-7: cite TC-3 for side-effecting triggers, "none" for clean |
| V-04 | PASS | TC-3 INTERNAL/EXTERNAL classification in Role 1; Role 2 Rule 7: TC-3 citation per side-effecting trigger; "none" for clean triggers |
| V-05 | PASS | Same structure as V-04; TC-3 INTERNAL/EXTERNAL; Role 2 Rule 8 enforces TC-3 citation or "none" |

---

### C-06 — Condition Evaluation *(recommended)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS* | No condition evaluation rules visible in Sections 2–4; implied by Section 1 reference; *inferred |
| V-02 | PASS | "`Condition`: exact gate expression; 'always fires' only with explicit justification" |
| V-03 | PASS | Rule B-4: "DO NOT claim 'always fires' without a one-sentence justification inline" |
| V-04 | PASS | Role 2 Rule 4: "'always fires' requires one inline justification sentence" |
| V-05 | PASS | Role 2 Rule 5: "'always fires' requires a one-sentence justification inline" |

---

### C-07 — Scenario Boundary *(recommended)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS* | EXECUTION ORDER references Section 1 which would contain the INPUT block; *inferred from visible execution structure |
| V-02 | PASS | INPUT block requires "Environment/solution layer" and "Triggering change event" |
| V-03 | PASS | INPUT block requires "Environment/solution layer" and "Triggering change event"; Rule Set A executed on registered trigger inventory |
| V-04 | PASS | INPUT block requires "Environment/solution layer" and "Triggering change event"; TC-1 traces condition-to-event relationship |
| V-05 | PASS | INPUT block requires "Environment/solution layer (Dataverse table, SharePoint list, Teams channel, or similar)" and "Triggering change event (field transition, record creation, lifecycle event)"; Role 5 Narrator explicitly names both |

---

### C-08 — Remediation Recommendations *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 4: "Remediation: [name a specific Power Automate construct -- required only if DETECTED; omit if NOT DETECTED or INDETERMINATE]" per subsection; same for Circular Triggers |
| V-02 | PASS | Section 3: "Remediation (if DETECTED): name a specific Power Automate construct" per pathology subsection; omit instruction for non-DETECTED |
| V-03 | PASS | Rule D-5: "For every DETECTED or IDENTIFIED verdict: WRITE a remediation naming a specific Power Automate or Copilot Studio construct by name" |
| V-04 | PASS | Role 4 Rule 5: "Every DETECTED or IDENTIFIED verdict must include a remediation naming a specific Power Automate or Copilot Studio construct" |
| V-05 | PASS | Role 4 Rule 5: same enforcement as V-04; "specific Power Automate or Copilot Studio construct" required by name |

---

### C-09 — Trigger Storm Quantification *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | Section 3 has per-automation arithmetic and integer run duration; no TC-2 cascade pair count because no pre-phase catalog; storm depth as a standalone number not produced |
| V-02 | PASS | Pre-phase threats summary block requires `TC-2 cascade pairs: <integer>` — storm depth as explicit integer; Budget section has run duration as "integer or integer range — prose estimates not acceptable" and PP budget consumed |
| V-03 | PASS | Rule A-6 threats summary block: `TC-2 cascade pairs: <integer>` — explicit cascade depth count; Rule C-3 requires run duration as "integers or integer ranges only" |
| V-04 | PASS | Threats summary block: `TC-2 cascade pairs: <integer>` and `Storm candidates: <integer>`; Budget Analyst produces run duration as integer or integer range; both depth and budget impact quantified |
| V-05 | PASS | Same structure as V-04; threats summary has TC-2 cascade pairs and storm candidates; run duration "<integer> seconds or <low>-<high> second range — prose estimates not acceptable" |

---

### C-10 — Proactive Budget Gate *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | EXECUTION ORDER: Section 1 → Section 2 → **Section 3 (Budget Gate)** → Section 4 (Pathology); budget explicitly before pathology; "Produce this section before pathology detection" stated |
| V-02 | PASS | EXECUTION ORDER: Pre-Phase → Section 1 → **Section 2 (Budget Analysis)** → Section 3 (Pathology Detection); budget before pathology confirmed |
| V-03 | PASS | EXECUTION ORDER: Rule Set A → B → **C (Budget Gate)** → D (Pathology Detection); Rule C-1 threshold check and budget section structurally precede Rule Set D |
| V-04 | PASS | Role sequence: Threat Analyst (1) → Registry Analyst (2) → **Budget Analyst (3)** → Pathology Analyst (4); explicit statement: "Role 3 (Budget Analyst) runs before Role 4 (Pathology Analyst) -- budget gate precedes pathology detection regardless of storm verdict" |
| V-05 | PASS | Role sequence: Threat Analyst (1) → Registry Analyst (2) → **Budget Analyst (3)** → Pathology Analyst (4) → Narrator (5); Role 3 format rule: "This section appears before pathology detection regardless of whether a storm is confirmed" |

---

### C-11 — Dual-Population Table *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS* | EXECUTION ORDER references Section 1; Section 2 M/N/NF block implies dual-population table exists upstream; *inferred |
| V-02 | PASS | Single Section 1 table; column rules: "`Fires?`: YES or NO only -- no row may omit this column"; explicit per-row enforcement |
| V-03 | PASS | Rule B-1: "PRODUCE exactly one unified trigger table"; Rule B-2: YES/NO only, "DO NOT leave any row blank" |
| V-04 | PASS | Role 2 Rule 1: "One unified table -- no separate registered/firing lists"; Rule 3: YES or NO only with no-blank enforcement |
| V-05 | PASS | Role 2 Rule 1 and Rule 3: identical enforcement; "no separate registered/firing lists" |

---

### C-12 — Registry Summary Code Block *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 2 explicit code-fence: `M  = <integer: YES rows with at least one side effect>`, `N  = <integer: all YES rows>`, `NF = <integer: all NO rows>`; Section 3 reads M and N by name in threshold condition |
| V-02 | PASS | After-table `summary` code-fence with M, N, NF as named integer variables; downstream Section 2 reads "M >= 1 OR N >= 3" by name |
| V-03 | PASS | Rule B-8 requires `summary` code-fence with M, N, NF; Rule C-1 reads "M >= 1 OR N >= 3" by name; Rule C-4 reads "M >= 3" by name |
| V-04 | PASS | Role 2 produces `summary` code-fence with M, N, NF; Role 3 reads M and N by name in threshold condition |
| V-05 | PASS | Role 2: "write the Registry Summary block exactly as shown" with explicit M, N, NF integers; Role 3 threshold reads M and N by name; re-derivation by row-count structurally blocked |

---

### C-13 — Per-Automation Calculation Basis *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 3: "Trigger name: X [action type] + Y [action type] = Z requests per invocation" required per YES trigger; "aggregate totals alone do not satisfy this section" stated explicitly |
| V-02 | PASS | "Per-automation arithmetic (required): For each YES trigger: 'Trigger name: X [action type] + Y [action type] = Z requests per invocation'"; TC-3 EXTERNAL entries cited in connector action count |
| V-03 | PASS | Rule C-2: "WRITE per-automation arithmetic for every YES trigger: 'Trigger name: X [type] + Y [type] = Z requests per invocation'. DO NOT provide aggregate totals only -- per-trigger lines are required." |
| V-04 | PASS | Role 3 Rule 1: "Per-automation arithmetic -- required; aggregate totals alone do not satisfy this section"; explicit per-trigger line format; TC-3 EXTERNAL entries cited when counting connector actions |
| V-05 | PASS | Role 3 Rule 1: same enforcement as V-04 with identical aggregate-only prohibition |

---

### C-14 — Specialist Role Accountability Chain *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | Visible content (Sections 2–4) shows no named specialist roles; single-analyst design per axis description ("C-16 without role separation") |
| V-02 | **FAIL** | Single "Power Automate / Copilot Studio domain expert" performs all sections; no named specialist roles; no section ownership accountability |
| V-03 | **FAIL** | Single "Power Automate / Copilot Studio domain expert" with rule sets; rule sets ≠ named specialist accountability chain; no Owns: declaration per section |
| V-04 | PASS | Four named specialist roles: Threat Analyst (owns TC-1/TC-2/TC-3), Registry Analyst (owns trigger table), Budget Analyst (owns Budget Gate), Pathology Analyst (owns pathology detection); explicit "strict accountability boundaries"; each role has explicit do-not-cross instructions |
| V-05 | PASS | Five named specialist roles: Threat Analyst, Registry Analyst, Budget Analyst, Pathology Analyst, Simulation Narrator — each with explicit "Owns:" declaration and do-not-cross instructions; "Roles 2 through 5 must reference the Threat Catalog by TC type-number" |

---

### C-15 — Threat-First Phase Pre-Cataloging *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | No pre-phase catalog visible in Sections 2–4; Section 3 references side effects but without TC-typed pre-cataloging; trigger table (Section 1) is written without a named threat surface catalog |
| V-02 | PASS | Pre-Phase section produces TC-1 (Candidate Conditions), TC-2 (Cascade Paths), TC-3 (Side-Effect Scope) before trigger table; trigger table Condition column and Side Effects column reference TC entries; pathology evidence references TC-2 cascade pairs |
| V-03 | PASS | Rule Set A produces TC-1, TC-2, TC-3 before Rule Set B (trigger table); rule sets enforce downstream citations; execution order: Rule Set A → B → C → D |
| V-04 | PASS | Role 1 (Threat Analyst) owns TC-1, TC-2, TC-3 with explicit format rules; trigger table written in Role 2 after catalog is complete; "Do not write trigger table rows" restriction on Role 1 enforces pre-catalog discipline |
| V-05 | PASS | Role 1 (Threat Analyst) owns TC-1, TC-2, TC-3 before any trigger table; "Roles 2 through 5 must not introduce trigger assessments absent from the Role 1 Threat Catalog without explicitly noting the addition as an inline discovery" — catalog integrity enforced across all downstream roles |

---

### C-16 — Verdict-First Pathology Structure *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Section 4 template: bare keyword on its own line immediately after subsection heading — "DETECTED (replace with NOT DETECTED or INDETERMINATE as applicable)"; three explicit DO NOT rules: "DO NOT prefix the verdict with 'Verdict:', 'State:', 'Finding:', or any other label"; "DO NOT embed the verdict in a sentence"; "DO NOT build toward the verdict — state it first, then provide evidence" |
| V-02 | **FAIL** | Pathology format: "Verdict: DETECTED / NOT DETECTED / INDETERMINATE" — label prefix "Verdict:" appears before the keyword; the verdict keyword is NOT the first content element; this is exactly the label-prefix pattern C-16 prohibits |
| V-03 | PASS | Rule D-2: "WRITE the verdict keyword as the FIRST content element on its own line after the subsection heading"; "DO NOT prefix the keyword with 'Verdict:', 'State:', 'Finding:', or any label"; "DO NOT embed the verdict in a sentence"; "DO NOT build toward the verdict" — all three prohibition categories covered |
| V-04 | PASS | Role 4 Rule 2: "VERDICT-FIRST FORMAT (required for every subsection): the verdict keyword is the first content element after the subsection heading -- on its own line, before any evidence or supporting text. Do not prefix with 'Verdict:', 'State:', or any label. Do not embed in a sentence. Do not build toward the verdict -- state it first."; template bracket notation `[DETECTED | NOT DETECTED | INDETERMINATE]` is a fill-in placeholder, not a label |
| V-05 | PASS | Role 4 Rule 2: same enforcement as V-04; template `[DETECTED | NOT DETECTED | INDETERMINATE]` on its own line after subsection heading; same three prohibition categories |

---

### C-17 — Typed Threat Catalog Cross-Reference *(aspirational)*

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | No typed TC catalog sections; no downstream type-number citations; single-analyst design with no pre-phase catalog |
| V-02 | PASS | Pre-phase has TC-1, TC-2, TC-3 (three typed sections); downstream: Condition column uses "-> TC-1:[TriggerName]", Side Effects column uses "-> TC-3:[TriggerName]", pathology 3a cites "TC-2:[TriggerA -> TriggerB]", pathology 3b cites "TC-1:[TriggerName] -- not found in registry" — four downstream typed citations across three section types |
| V-03 | PASS | Rule Set A has TC-1, TC-2, TC-3 typed sections; Rule B-4 cites TC-1 in Condition column; Rule B-7 cites TC-3 in Side Effects column; Rule D-4 cites TC-2 in pathology storm/circular evidence; three downstream section types with typed citations |
| V-04 | PASS | Role 1 pre-phase has TC-1, TC-2, TC-3 typed sections; Role 2 Condition column: "-> TC-1:[TriggerName]"; Side Effects column: "-> TC-3:[TriggerName]"; Role 4 4a/4c evidence: "TC-2:[TriggerA -> TriggerB]"; Role 4 4b evidence: "TC-1:[TriggerName] -- absent from registry"; four downstream typed citations; execution instruction: "Roles 2 through 4 must reference the Threat Catalog by TC type-number" |
| V-05 | PASS | Same structure as V-04 with Role 5 Narrator also required to reference prior sections; execution instruction: "Roles 2 through 5 must reference the Threat Catalog by TC type-number (TC-1, TC-2, TC-3). Prose references to the catalog without type-numbers do not satisfy this requirement." |

---

## Score Summary

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
```

| ID | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | E | R | A | Composite | Band |
|----|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|---|---|---|-----------|------|
| V-01 | P* | P* | P* | P | P* | P* | P* | P | **F** | P | P* | P | P | **F** | **F** | P | **F** | 4/4* | 3/3* | 6/10 | **96*** | Gold* |
| V-02 | P | P | P | P | P | P | P | P | P | P | P | P | P | **F** | P | **F** | P | 4/4 | 3/3 | 8/10 | **98** | Gold |
| V-03 | P | P | P | P | P | P | P | P | P | P | P | P | P | **F** | P | P | P | 4/4 | 3/3 | 9/10 | **99** | Gold |
| V-04 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 4/4 | 3/3 | 10/10 | **100** | Gold |
| V-05 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 4/4 | 3/3 | 10/10 | **100** | Gold |

*V-01 essential and recommended criteria are inferred from visible Sections 2–4 and axis description; Section 1 not present in variation file.

---

## Ranking

| Rank | ID | Score | Band | C-14 | C-15 | C-16 | C-17 | Notes |
|------|----|-------|------|------|------|------|------|-------|
| 1 | **V-04** | 100 | Gold | PASS | PASS | PASS | PASS | 4-role minimum achieves perfect score; no Narrator layer; proves Narrator is not required for any v5 criterion |
| 1 | **V-05** | 100 | Gold | PASS | PASS | PASS | PASS | 5-role architecture extends R4 V-05 with surgical C-16/C-17 additions; Narrator adds coherence checking beyond rubric requirement |
| 3 | **V-03** | 99 | Gold | **FAIL** | PASS | PASS | PASS | Strongest single-analyst result across all rounds; MUST/DO NOT phrasing achieves C-15, C-16, C-17 without roles; C-14 is the sole gap |
| 4 | **V-02** | 98 | Gold | **FAIL** | PASS | **FAIL** | PASS | Typed catalog cross-reference (C-17) passes; C-16 fails via "Verdict:" label-prefix pattern — confirms exact failure mode |
| 5 | **V-01** | 96* | Gold* | **FAIL** | **FAIL** | PASS | **FAIL** | C-16 passes via explicit DO NOT rules; Section 1 absent — score estimated |

---

## Excellence Signals from Top Variations

### Signal 1 — 4-Role Minimum Is Sufficient for Full v5 Compliance

V-04 (4 roles: Threat Analyst, Registry Analyst, Budget Analyst, Pathology Analyst) achieves
100/100 under v5, equal to V-05 (5 roles). The Narrator role adds terminal cross-validation
and deployment readiness verdict, but no v5 criterion requires it. The minimum viable role
architecture for full compliance under the current rubric is four roles. Architects who want
simplicity without sacrificing score can omit the Narrator layer.

### Signal 2 — Imperative Phrasing Register Reaches 99/100 Without Role Structure

V-03 is a single-analyst prompt with no named roles. It achieves 99/100 (only C-14 fails)
by using MUST/DO NOT imperative numbered rules that enforce verdict-first format, typed TC
citations, pre-cataloging, budget-before-pathology order, and concrete value requirements.
This is the highest single-analyst score across all five rounds. For lightweight applications
where role overhead is undesirable, V-03’s phrasing register is a near-complete structural
substitute — the one non-negotiable gap is C-14 (specialist role accountability chain).

### Signal 3 — “Verdict:” Label Prefix Is the Specific C-16 Failure Mode

V-02 fails C-16 with the pattern "Verdict: DETECTED / NOT DETECTED / INDETERMINATE". The
"Verdict:" label prefix makes the keyword NOT the first content element. This is the precise
failure mode C-16 was designed to prevent. V-01 and V-03 directly address this with explicit
"DO NOT prefix with 'Verdict:'" rules. V-04 and V-05 address it via bracket-notation fill-in
templates. The failure mode is now documented as a concrete anti-pattern.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
