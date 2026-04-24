## Scoring: trace-permissions — Round 1 (V-01 through V-05)

**Rubric:** v1 (C-01 to C-09) | **Ground truth:** no live artifact — scoring against prompt design reliability

---

### Scoring Method

Since the trace artifact is a placeholder, each criterion is scored by evaluating whether the variation's structural design **reliably elicits** the required output: does the prompt make it structurally difficult for the model to skip the criterion? PASS = the prompt scaffolds this directly and enforces it. PARTIAL = the prompt implies coverage but lacks a hard gate or structural enforcement. FAIL = the prompt has no mechanism for this criterion.

---

## V-01 — Entity-Centric, Risk-Surface-First

**Axis:** Analysis anchored on data objects (not roles); highest-sensitivity entity traced first.

| Criterion | Score | Evidence Note |
|-----------|-------|---------------|
| C-01 | PASS | Per-entity 2a table required for "every role with any privilege"; table format prevents role omission |
| C-02 | PASS | Record Scope column in 2a with enumerated values (Org/BU/Parent-Child BU/Team/User/Sharing); explicit, not implied |
| C-03 | PASS | 2b per-field FLS table per entity; rule: "A sensitive field with no FLS profile applied: add a row to the Security Gap Log now" — missing FLS is structurally trapped |
| C-04 | PASS | Progressive gap log with "add a row the moment you identify a gap" — real-time population prevents deferred collapse; 5 named gap types |
| C-05 | PASS | 2f escalation check per entity per role with chain format + explicit rule-out format ("Checked [Role]: write access to [fields]. No escalation because [specific reason]") |
| C-06 | PASS | 2c sharing rule table per entity; "Unexpected" flag = mandatory gap log entry with SHARING-CONFLICT type |
| C-07 | PASS | 2d team membership: explicit format for blocked scenario + self-addition check; confirms absence explicitly if none |
| C-08 | PASS | Step 4.1: current state → target state → after-fix statement; "generic advice does not qualify" stated in prompt |
| C-09 | PASS | Step 4.2 defense-in-depth table: "Enforces Independently?" per layer per entity; single-point-of-failure column required |

**Composite:**
```
Essential:    4/4 * 60 = 60
Recommended:  3/3 * 30 = 30
Aspirational: 2/2 * 10 = 10
Total: 100  (practical ceiling: ~97 — slight execution risk that model abbreviates Phase 2 for lower-sensitivity entities)
```

**Score: 97**

---

## V-02 — Prose Investigation Log (No Tables)

**Axis:** No tables; structured tokens (ENTITY:, ROLE:, FIELD:, GAP:, FIX:, VERDICT:) as a substitute scaffold.

| Criterion | Score | Evidence Note |
|-----------|-------|---------------|
| C-01 | PARTIAL | ROLE: token required per role, but prose format lacks table enforcement — model may combine roles or omit low-privilege roles without a matrix to force completeness |
| C-02 | PASS | ROLE: format explicitly requires record scope in every entry ("Read on Case at BU scope"); format is specific |
| C-03 | PARTIAL | FIELD: token required per sensitive field; but prose format raises miss rate — no hard gate confirming all sensitive fields are covered before advancing |
| C-04 | PASS | GAP: token is mandatory with named components (role/field/record, type, risk); "every GAP token must be followed by a FIX token before moving to the next section" — strong pairing |
| C-05 | PARTIAL | VERDICT: escalation section exists with format, but chain format is looser in prose; no explicit per-role rule-out requirement |
| C-06 | PASS | Sharing rule audit section with explicit GAP: SHARING-CONFLICT format and rule name required |
| C-07 | PASS | Team membership section with GAP: TEAM-INJECTION format; self-addition check required |
| C-08 | PASS | FIX: token must immediately follow every GAP: token; "no generic advice" stated; format is specific |
| C-09 | PASS | Defense-in-depth VERDICT: section with per-layer (role/FLS/record scope) independence assessment |

**Composite:**
```
Essential:    (0.5+1+0.5+1)/4 * 60 = 45
Recommended:  (0.5+1+1)/3  * 30 = 25
Aspirational: 2/2 * 10 = 10
Total: 80
```

**Score: 80**

---

## V-03 — Conversational Walking-Investigator

**Axis:** First-person investigator voice; stated assumptions up front; "this surprised me" judgment language.

| Criterion | Score | Evidence Note |
|-----------|-------|---------------|
| C-01 | PASS | Explicit requirement: "every role with any privilege on this entity / every privilege (C/R/W/D/A) with its record scope — do not collapse these into 'standard access'" |
| C-02 | PASS | Record scope required per operation: "record scope -- do not collapse these into 'standard access'" is stated as a rule |
| C-03 | PASS | "You must cover at least three sensitive fields across the entities in scope. Do not collapse this into 'FLS is configured' -- walk each field individually." — hard floor with explicit format |
| C-04 | PARTIAL | No central gap log; security signals are flagged inline as "security signals" but there is no structural accumulation mechanism — risk that signals are mentioned once and not consolidated |
| C-05 | PASS | Dedicated "Privilege escalation" section with "walk through what you checked and what you concluded" per role; escalation path described if found |
| C-06 | PASS | Sharing rules section with format for unexpected rules: "this rule opens [what] to [who] beyond what the role-defined scope permits" |
| C-07 | PASS | "Team access" section with explicit format: blocked scenario, team, who controls it, self-addition possibility |
| C-08 | PASS | "WHAT I WOULD FIX" section with "Problem / Why it matters / Fix" format; "named precisely enough that a Dataverse admin can implement it" stated |
| C-09 | FAIL | No defense-in-depth layer independence analysis; the conversational format has no section or prompt for whether role/FLS/record scope each independently enforce — C-09 is structurally absent |

**Composite:**
```
Essential:    (1+1+1+0.5)/4 * 60 = 52.5
Recommended:  3/3 * 30 = 30
Aspirational: (1+0)/2 * 10 = 5
Total: 87.5
```

**Score: 87**

---

## V-04 — Extended Inventory Gate + Phase-End Checkpoint Summaries

**Axis:** Inventory as a fully gated phase; explicit self-audit checkpoint summaries the model must complete before advancing.

| Criterion | Score | Evidence Note |
|-----------|-------|---------------|
| C-01 | PASS | 1.3 operation-role matrix per entity; every role from 1.2 catalog must appear in every relevant entity matrix; Phase 1 checkpoint confirms coverage |
| C-02 | PASS | Record Scope column in 1.3 with enumerated values; Phase 1 checkpoint: "The 1.3 matrix contains a row for every role-entity pair" |
| C-03 | PASS | 1.4 FLS inventory per entity per sensitive field; "Every field with Sensitivity Category != Not-Sensitive must have a row"; NONE = [GAP: MISSING-FLS] added to Master Gap Table immediately; Phase 1 checkpoint confirms |
| C-04 | PASS | Master Gap Table progressively filled; FLS gaps in 1.4, escalation in 2.1, cascade in 2.4, sharing conflicts in 1.5 — four structured gap-injection points across phases |
| C-05 | PASS | 2.1 escalation analysis: chain format per role + explicit rule-out with "named privileges" requirement; Phase 2 checkpoint confirms per-role verdict |
| C-06 | PARTIAL | 1.5 sharing rule inventory has "Exceeds OWD+Role Scope?" column, but the analysis of *which specific records become over-exposed* (C-06 pass condition) is captured in the table but not narratively developed — functional but thin |
| C-07 | PASS | 2.3 team membership gap analysis with blocked-scenario format + self-addition check; Phase 2 checkpoint confirms coverage |
| C-08 | PASS | 3.3 remediation: from/to format with solution location; "generic advice does not qualify"; Phase 3 checkpoint: "every row in the Master Gap Table has a complete remediation entry" |
| C-09 | PASS | 3.2 defense-in-depth layer assessment: "Independent?" column per layer per entity; SINGLE-LAYER-FAILURE added to Master Gap Table |

**Composite:**
```
Essential:    4/4 * 60 = 60
Recommended:  (1+0.5+1)/3 * 30 = 25
Aspirational: 2/2 * 10 = 10
Total: 95
```

**Score: 95**

---

## V-05 — Inertia Framing + CS-Last Validation

**Axis:** Security design assumptions stated before tracing; CS role analyzed last as a validator of expert-level design claims.

| Criterion | Score | Evidence Note |
|-----------|-------|---------------|
| C-01 | PASS | 1b operation-role matrix with "Why This Role Has This Access" column; Phase 3a CS workflow independently traces CS operations — dual coverage |
| C-02 | PASS | 1a entity/OWD inventory + record scope in 1b; design rationale column forces explicit OWD justification per entity |
| C-03 | PASS | 1c FLS with "Assumption Protected" column; ASSUMPTION UNPROTECTED flag for sensitive fields without FLS; Phase 3b CS view independently checks field readability — dual coverage |
| C-04 | PASS | Phase 2 assumption testing: every violated assumption is a named gap; Gap Log maps gaps to assumptions; Phase 3 surfaces any CS-perspective gaps not caught in design review |
| C-05 | PASS | 1d privilege escalation: DESIGNED/EMERGENT/NOT PREVENTED classification; EMERGENT or NOT PREVENTED = Gap Log entry; stronger than "possible/not possible" binary |
| C-06 | PASS | 1e sharing rule design intent table: "Is the Exposure Scoped?" = NO → Gap Log; "Records Exposed" column names over-exposed records directly |
| C-07 | PASS | 1f team structure design intent: "failure mode if team membership is wrong" required; design assumption mapped to A# |
| C-08 | PASS | 4a remediation: assumption-linked format — "Assumption A-# requires... The gap is... Fix: specific configuration element"; generic advice prohibited |
| C-09 | PASS | 4b defense-in-depth: three-column table ("if X removed, still enforced by Y+Z?"); PARTIAL/WEAK rating triggers single-point-of-failure identification |

**Composite:**
```
Essential:    4/4 * 60 = 60
Recommended:  3/3 * 30 = 30
Aspirational: 2/2 * 10 = 10
Total: 100  (practical ceiling: ~95 — assumption-list risk: if model writes assumptions that are too broad, Phase 2 testing may miss narrow gaps not anticipated in the A-table)
```

**Score: 95**

---

## Rankings

| Rank | Variation | Score | All Essential Pass | Notes |
|------|-----------|-------|-------------------|-------|
| 1 | V-01 | **97** | YES | Entity-centric + risk-surface-first + progressive gap log |
| 2 | V-05 | **95** | YES | Assumption-first + CS validation; slight assumption-list risk |
| 2 | V-04 | **95** | YES | Checkpoint gates strongest completeness mechanism; C-06 thin |
| 4 | V-03 | **87** | YES (C-04 partial) | Conversational voice strong on judgment signals; C-09 structurally absent |
| 5 | V-02 | **80** | NO (C-01/C-03 partial) | Prose format is a real liability for completeness; GAP:/FIX: pairing is best-in-round |

---

## Excellence Signals from V-01

Three patterns made V-01 the top scorer:

**1. Entity-before-role ordering as a completeness forcing function.**
Starting with entities (not roles) guarantees that the highest-sensitivity data surface is fully traced before the model's attention can diffuse into lower-priority areas. In role-first variations, the model can enumerate roles exhaustively while glossing over the actual data at risk. Entity-first makes the data the anchor; roles are secondary.

**2. Immediate gap log population as a structural contract.**
The rule "add a row the moment you identify a gap — do not defer to the end" prevents the most common failure mode: completing all analysis sections and then writing a summary gap list that omits gaps identified early. Real-time population makes the gap log a running audit, not a post-hoc summary.

**3. Explicit rule-out format for negative-space coverage.**
Requiring "Checked [Role]: write access to [specific fields/operations]. No escalation because [specific reason]" — rather than silence — forces the model to confirm absence rather than just failing to mention it. This is structurally different from formats where "no escalation path" might mean "I didn't check" or "I checked and found nothing."

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["entity-before-role ordering: anchoring analysis on data objects (not roles) ensures highest-risk fields are fully covered before model attention diffuses", "immediate gap log population: requiring gap rows the moment a gap is identified prevents deferred-collapse into a post-hoc summary", "explicit rule-out format: requiring named evidence for negative findings (not silence) forces thorough negative-space coverage on escalation paths"]}
```
