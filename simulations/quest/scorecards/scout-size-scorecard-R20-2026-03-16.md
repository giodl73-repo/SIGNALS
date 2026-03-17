# Scout-Size R20 — Scoring Scorecard

**Skill**: scout-size | **Rubric**: v20 | **Date**: 2026-03-17

---

## Scorecard — V-01 (Gap Section Ordering)

**Structure**: ENTRY GATE → Phase 1 (Sizing Analyst) → CONFIDENCE GAP CHECKPOINT → Phase 2 (Risk Assessor) → Compilation Table

### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "List each integration point individually as named bullets. End with: 'These are {N} integration points.'" |
| C-02 | PASS | "Assign exactly one tier: LOW / MEDIUM / HIGH / XL — this vocabulary only. 'MODERATE', '3/5', and 'complex' all fail." |
| C-03 | PASS | Field 1 — required format with directional label (cheaper/comparable/more expensive) |
| C-04 | PASS | Field 4 — Confidence Basis explicitly required, specific evidence + risk driver |
| C-05 | PASS | "This is not a project plan — do not include task breakdowns, sprint assignments, or owner names." |

**Essential: 60/60**

### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | CONFIDENCE GAP CHECKPOINT standalone section present |
| C-07 | PASS | Phase 2 Tier-Up Condition required |
| C-08 | PASS | Phase 2 Tier-Down Condition required |

**Recommended: 30/30**

### Aspirational (35 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | "Justify the tier by reference to the named integration point count from Field 2." |
| C-10 | PASS | cheaper/comparable/more expensive label required in format |
| C-11 | PASS | "name which integration point carries the highest implementation uncertainty — that is the risk driver, not the average" (Fields 3 & 4) |
| C-12 | PASS | "Reference a **different integration point** than the tier-up condition." in tier-down format |
| C-13 | PASS | Column headers: "[must be HIGHER than current: LOW / MEDIUM / HIGH / XL]" and "[must be LOWER than current]" |
| C-14 | PASS | "(a) the specific open question, and (b) the action that would resolve it" |
| C-15 | PASS | "[must address a dimension NOT confirmed in Phase 1 Confidence Basis]" in section header |
| C-16 | PASS | Destination tier constraints encoded in column headers and format strings |
| C-17 | PASS | C-11 scope: Field 3/4 WRONG names "no named risk driver". C-15 scope: DIAGNOSTIC PATTERN WRONG. C-16 scope: Phase 2 WRONG "(null sensitivity)" with named instance "remains HIGH" [current = HIGH] |
| C-18 | PASS | Compilation table: "[must be HIGHER than current: LOW / MEDIUM / HIGH / XL]" and "[must be LOWER than current — different integration point from Tier-Up]" |
| C-19 | PASS | All WRONG/CORRECT blocks appear before their governed field's format instruction |
| C-20 | PASS | Phase 1 Sizing Analyst produces Basis; Risk Assessor produces Gap; non-access clause present |
| C-21 | PASS | Fields 3, 4, Phase 2 sensitivity, and DIAGNOSTIC PATTERN all have both named WRONG and CORRECT instances |
| C-22 | PASS | "Confidence Gap [must address dimension not confirmed in Basis]" in compilation table column |
| C-23 | PASS | Phase 1 production list + exclusion list; Phase 2 production + exclusion; Gap assigned to Risk Assessor |
| C-24 | PASS | "Do not cite the integration point list, count, tier, or rationale from Phase 1 as your Confidence Gap. Those are confirmed facts, not open questions." — categories named explicitly |
| C-25 | PASS | "Is this gap derivable from my Phase 1 Confidence Basis by negating or paraphrasing something the Sizing Analyst confirmed?" — concrete executable |
| C-26 | PASS | "[Sizing Analyst]" and "[Risk Assessor]" in every column header of compilation table |
| C-27 | PASS | "Confidence Gap [must address dimension not confirmed in Basis]" encoded at column level in compilation table |
| C-28 | PASS | Self-test in checkpoint section (C-25 satisfies the two-phase analog) |
| C-29 | PASS | "Exclusion list — you do NOT produce: Confidence Gap, Tier-Up Condition, Tier-Down Condition." — mirrors Phase 2 charter |
| C-30 | PASS | All three mechanisms inside CONFIDENCE GAP CHECKPOINT: (1) "[must address a dimension NOT confirmed in Phase 1 Confidence Basis]" label; (2) self-test query; (3) WRONG/CORRECT in DIAGNOSTIC PATTERN |
| C-31 | PASS | C-32 removes gap from table; C-31 precondition never triggered |
| C-32 | PASS | `── CONFIDENCE GAP CHECKPOINT ──` with visual delimiter; standalone section; positioned after Phase 1 (Basis) and before Phase 2 (Sensitivity) |
| C-33 | PASS | "If YES: **you have written a basis-negation** — a Phase 2 charter violation." — failure class named in self-test affirmative branch |
| C-34 | PASS | "FAILURE CLASS: basis-negation" co-encoded in WRONG block of DIAGNOSTIC PATTERN |
| C-35 | PASS | ENTRY GATE produces CLEAR/BLOCKED per precondition; OPEN/CLOSED halts analysis |
| C-36 | PASS | Precondition B named separately: "Signal boundary intact: the input requests sizing signals, not a task plan, sprint assignments, or owner names." CLOSED-LABEL identifies which precondition |
| C-37 | PASS | DIAGNOSTIC PATTERN has FAILURE CLASS, DETECTION PATTERN, WHY IT FAILS as three separate labeled entries |
| C-38 | PASS | Formal table with STATUS (CLEAR/BLOCKED) and CLOSED-LABEL columns; each precondition is one row |
| C-39 | PASS | `── DIAGNOSTIC PATTERN ──` visual delimiter wraps the three-field block |
| C-40 | PASS | "→ see CONFIDENCE GAP CHECKPOINT above" in compilation table gap row; no gap content in table |
| C-41 | PASS | "CLOSED-LABEL [fill only if BLOCKED; leave blank if CLEAR — format: …]" in column header |
| C-42 | PASS | R20 fix applied: all three defense mechanisms (relational label, self-test, WRONG/CORRECT) are entirely within the CONFIDENCE GAP CHECKPOINT; compilation table gap column is a pointer only |
| C-43 | PASS | CONFIDENCE GAP CHECKPOINT appears before "Output Compilation Table" in prompt order; pointer follows already-written content |

**Aspirational: 35/35**

**V-01 Total: 125/125 → Composite: 100.0**

---

## Scorecard — V-02 (Inertia-First Framing)

**Structure**: Identical to V-01 with inertia as anchor frame for all subsequent judgments.

### Essential / Recommended: Same as V-01 — 60/60 + 30/30

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-16 | PASS | Same machinery as V-01; inertia framing doesn't affect count/tier/gap constraints |
| C-17 | PASS | C-11: Fields 3/4 have "no risk driver" failure labels. C-15: DIAGNOSTIC PATTERN WRONG "Gap: The cost direction of the workaround may be different from what was estimated." — concrete named instance. C-16: WRONG "'Tier-Up: If the feature proves harder than expected, complexity increases to HIGH.' [current = HIGH → destination = HIGH — null sensitivity]" with named CORRECT instance |
| C-18–C-19 | PASS | Same structural encoding; examples all precede governed fields |
| C-20 | PASS | Sizing Analyst / Risk Assessor role separation with non-access clause |
| C-21 | PASS | All WRONG/CORRECT blocks have named concrete instances including Phase 2 tier-up |
| C-22–C-29 | PASS | Same charter coverage, column encoding, self-test machinery as V-01 |
| C-30 | PASS | All three mechanisms within CONFIDENCE GAP CHECKPOINT |
| C-31–C-34 | PASS | C-32 used; self-test names failure class; WRONG block encodes FAILURE CLASS |
| C-35–C-41 | PASS | Entry gate, three-field diagnostic, formal table, CLOSED-LABEL conditional header all present |
| C-42 | PASS | Defense cluster entirely inside standalone section; table pointer only |
| C-43 | PASS | CONFIDENCE GAP CHECKPOINT before Output Compilation Table |

**Aspirational: 35/35**

**V-02 Total: 125/125 → Composite: 100.0**

---

## Scorecard — V-03 (Phrasing Register / Single-Phase)

**Structure**: Single-phase conversational — ENTRY GATE → Steps 0–4 → CONFIDENCE GAP CHECKPOINT → Step 5 → Output Summary Table. No role separation.

### Essential / Recommended: 60/60 + 30/30

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Step 3: "Explain how the count from Step 2 maps to this tier." |
| C-10 | PASS | Step 1 directional label required |
| C-11 | PASS | "Name the one integration point that carries the most implementation uncertainty — your risk driver." (Steps 3 and 4) |
| C-12 | PASS | "Name a **different integration point** than Tier-Up." in Step 5 |
| C-13 | PASS | Format placeholders "{higher tier [LOW / MEDIUM / HIGH / XL]}" and "{lower tier [LOW / MEDIUM / HIGH / XL]}" |
| C-14 | PASS | "Name the question AND the action that resolves it." |
| C-15 | PASS | "[must address a dimension NOT confirmed in Step 4 Confidence Basis]" in section header |
| C-16 | PASS | Step 5 "destination tier must be **higher** than your Step 3 tier" and structured in format |
| C-17 | **PARTIAL** | C-11 and C-15 scopes have concrete named instances. C-16 scope in Step 5 uses only rule-description form: "WRONG: destination tier = current tier (null sensitivity). CORRECT: destination tier is strictly higher." — no concrete named output example, reader cannot see what a failing Tier-Up sentence looks like |
| C-18 | PASS | Summary table: "{higher tier}", "{lower tier — different integration point}", "[must address dimension not confirmed in Step 4]" |
| C-19 | PASS | All examples appear before the output instructions they govern |
| C-20 | **FAIL** | Single-phase design — no role-separated production; no basis/gap role split |
| C-21 | **PARTIAL** | C-11 and C-15 scoped examples have both concrete WRONG and CORRECT instances. Step 5 Tier-Up uses only abstract pattern labels ("destination tier = current tier"), not concrete named instances — fails C-21's "concrete named" requirement |
| C-22 | PASS | "[must address dimension not confirmed in Step 4]" in Summary Table gap column |
| C-23 | **FAIL** | No role charters; field ownership by role is not assigned (C-20 not used) |
| C-24 | **FAIL** | No Phase 2 charter; prohibited-content naming mechanism absent |
| C-25 | **FAIL** | No Phase 2 role charter for self-test embedding; C-28 used instead |
| C-26 | **FAIL** | No role tags in table column headers |
| C-27 | PASS | Relational constraint encoded in Summary Table gap column, even in single-phase design |
| C-28 | PASS | "Self-test — ask yourself: 'Could a reader derive this gap from my Step 4 Confidence Basis by negating something I confirmed?'" — concrete executable in gap section |
| C-29 | **FAIL** | No Phase 1 charter; no explicit exclusion list mirroring Phase 2 (Phase 2 does not exist) |
| C-30 | PASS | CONFIDENCE GAP CHECKPOINT contains: relational label, self-test query, WRONG/CORRECT in DIAGNOSTIC PATTERN — all three mechanisms co-located |
| C-31 | PASS | C-32 used; gap removed from table; C-31 precondition not triggered |
| C-32 | PASS | `── CONFIDENCE GAP CHECKPOINT ──` standalone section positioned after Step 4 (Basis), before Step 5 (Sensitivity) |
| C-33 | PASS | "you have written a basis-negation — a gap field production violation." — failure class named |
| C-34 | PASS | "FAILURE CLASS: basis-negation" in WRONG block |
| C-35 | PASS | Entry gate with CLEAR/BLOCKED per precondition, OPEN/CLOSED gate result |
| C-36 | PASS | Precondition B: "Is the input free of task breakdowns, sprint assignments, and owner names?" — named separately; CLOSED-LABEL format identifies precondition |
| C-37 | PASS | DIAGNOSTIC PATTERN has FAILURE CLASS, DETECTION PATTERN, WHY IT FAILS as three labeled entries |
| C-38 | PASS | Formal precondition table with STATUS and CLOSED-LABEL columns |
| C-39 | PASS | `── DIAGNOSTIC PATTERN ──` visual delimiter wraps three-field block |
| C-40 | PASS | "→ see CONFIDENCE GAP CHECKPOINT above" in Summary Table gap row |
| C-41 | PASS | "[fill only if BLOCKED; leave blank if CLEAR]" in CLOSED-LABEL column header |
| C-42 | PASS | All three mechanisms inside standalone section; table carries pointer only |
| C-43 | PASS | CONFIDENCE GAP CHECKPOINT precedes Output Summary Table |

**Aspirational breakdown:**
- PASS (×27): C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-18, C-19, C-22, C-27, C-28, C-30, C-31, C-32, C-33, C-34, C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-42, C-43 = 27.0 pts
- PARTIAL (×2): C-17, C-21 = 1.0 pts
- FAIL (×6): C-20, C-23, C-24, C-25, C-26, C-29 = 0 pts

**Aspirational: 28.0/35**

**V-03 Total: 118.0/125 → Composite: 94.4**

---

## Scorecard — V-04 (Three-Role Sequence + Table-Dominant)

**Structure**: ENTRY GATE → Phase 1 Inertia Auditor → Phase 2 Sizing Analyst (table-dominant) → CONFIDENCE GAP CHECKPOINT → Phase 3 Risk Assessor → Three-column Compilation Table

### Essential / Recommended: 60/60 + 30/30

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Field B: "Justify by the count from Field A." plus count-based justification column in table |
| C-10 | PASS | Phase 1 inertia table has "Cost direction [cheaper / comparable / more expensive]" as a named column |
| C-11 | PASS | Field B Complexity Tier table: "Risk Driver [name the highest-uncertainty integration point]" column. Field C Confidence Basis table: "Risk Driver (highest-uncertainty component and why)" column |
| C-12 | PASS | Field E: "Reference a **different integration point** than Field D." encoded in column: "[must differ from Field D]" |
| C-13 | PASS | Tier-Up column "[must be HIGHER than current: LOW / MEDIUM / HIGH / XL]" and Tier-Down "[must be LOWER than current: LOW / MEDIUM / HIGH / XL]" |
| C-14 | PASS | Gap section: "Name the question AND the resolution action." |
| C-15 | PASS | "[must address a dimension NOT confirmed in Phase 2 Confidence Basis]" in section header |
| C-16 | PASS | Tier-Up WRONG "Current = HIGH, Destination = HIGH → null-sensitivity: no range"; destination columns encode constraint |
| C-17 | PASS | C-11: Field B WRONG "fails: no count cited; no risk driver" and CORRECT. Field C WRONG "no specific facts; no risk driver." C-15: DIAGNOSTIC PATTERN WRONG with named instance. C-16: Field D WRONG "Current = HIGH, Destination = HIGH" and CORRECT "Current = HIGH, Destination = XL" |
| C-18 | PASS | Tier table columns structurally encode tier constraints; "[must be HIGHER]" / "[must be LOWER]" / "[must differ from Field D]" all in column headers |
| C-19 | PASS | All examples precede their governed output fields |
| C-20 | PASS | Inertia Auditor / Sizing Analyst / Risk Assessor role separation; basis/gap separated across Sizing Analyst and Risk Assessor charters with non-access clause |
| C-21 | PASS | All WRONG/CORRECT examples have concrete named instances — Field B, C use table WRONG/CORRECT; Field D has "Current = HIGH → HIGH" vs "Current = HIGH → XL"; DIAGNOSTIC PATTERN has named gap examples |
| C-22 | PASS | Gap column in compilation table: "[must address dimension not confirmed in Phase 2 Basis]" |
| C-23 | PASS | Phase 1, 2, 3 each have explicit production charter + exclusion list covering all fields; gap assigned to Risk Assessor in checkpoint |
| C-24 | PASS | "Do not cite the integration point list, count, tier, or basis from Phase 2 as your Confidence Gap. Those are confirmed facts." — specific content categories named |
| C-25 | PASS | "Is this gap derivable from Phase 2 Confidence Basis by negating something the Sizing Analyst confirmed?" — concrete executable self-test |
| C-26 | PASS | Three-column compilation table: "[Inertia Auditor]", "[Sizing Analyst]", "[Risk Assessor]" in every column header |
| C-27 | PASS | "[must address dimension not confirmed in Phase 2 Basis]" in compilation table gap column |
| C-28 | PASS | Self-test present in checkpoint (C-25 satisfies the multi-phase analog) |
| C-29 | PASS | Phase 2 exclusion: "Inertia Check, Confidence Gap, Tier-Up Condition, Tier-Down Condition." Mirrors Phase 3 charter exactly |
| C-30 | PASS | All three mechanisms inside CONFIDENCE GAP CHECKPOINT: relational label, self-test query, WRONG/CORRECT in DIAGNOSTIC PATTERN |
| C-31 | PASS | C-32 used; gap outside table; C-31 not triggered |
| C-32 | PASS | `── CONFIDENCE GAP CHECKPOINT ──` standalone section; positioned between Phase 2 (Basis) and Phase 3 (Sensitivity) |
| C-33 | PASS | "you have written a basis-negation — a Phase 2 Risk Assessor charter violation." |
| C-34 | PASS | "FAILURE CLASS: basis-negation" inside WRONG block |
| C-35 | PASS | Phase 0 entry gate with binary CLEAR/BLOCKED, OPEN/CLOSED halt |
| C-36 | PASS | Precondition B: "Signal boundary intact: input contains no task plan, sprint assignments, or owner names." Named separately; CLOSED-LABEL identifies which precondition failed |
| C-37 | PASS | DIAGNOSTIC PATTERN: FAILURE CLASS, DETECTION PATTERN, WHY IT FAILS as labeled entries |
| C-38 | PASS | Formal table with STATUS and CLOSED-LABEL per precondition row |
| C-39 | PASS | `── DIAGNOSTIC PATTERN ──` visual delimiter |
| C-40 | PASS | "→ see CONFIDENCE GAP CHECKPOINT above" in three-column compilation table gap row |
| C-41 | PASS | "[fill only if BLOCKED; leave blank if CLEAR]" in CLOSED-LABEL column header |
| C-42 | PASS | All three defense mechanisms entirely within standalone section |
| C-43 | PASS | CONFIDENCE GAP CHECKPOINT precedes Output Compilation Table |

**Aspirational: 35/35**

**V-04 Total: 125/125 → Composite: 100.0**

---

## Scorecard — V-05 (Maximum Lifecycle Explicitness / Champion Candidate)

**Structure**: ENTRY GATE → Phase 1 Sizing Analyst (Steps 1.1–1.4, each with DIAGNOSTIC PATTERN) → CONFIDENCE GAP CHECKPOINT (as phase gate) → Phase 2 Risk Assessor (Steps 2.1–2.2) → PHASE 2 COMPLETE marker → Compilation Table

### Essential / Recommended: 60/60 + 30/30

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Step 1.3: "Justify by reference to the integration point count from Step 1.2." |
| C-10 | PASS | "Assign exactly one directional label: **cheaper** / **comparable** / **more expensive**" |
| C-11 | PASS | Step 1.3: "Name the risk driver — the integration point with the highest implementation uncertainty." Step 1.4: "identify which integration point is the risk driver and explain why it carries the highest uncertainty (not average uncertainty)." |
| C-12 | PASS | "Reference a **different integration point** than the tier-up condition." in Step 2.2 |
| C-13 | PASS | "[must be HIGHER than current: LOW / MEDIUM / HIGH / XL]" and "[must be LOWER than current — different integration point from Step 2.1: LOW / MEDIUM / HIGH / XL]" |
| C-14 | PASS | "(a) the specific open question, and (b) the action that would resolve it" |
| C-15 | PASS | "[must address a dimension NOT confirmed in Phase 1 Confidence Basis]" in section header |
| C-16 | PASS | Step 2.1 WRONG "[current = HIGH → destination = HIGH]"; destination format encodes constraint |
| C-17 | PASS | C-11: Step 1.3 DIAGNOSTIC PATTERN WRONG "no citation of integration point count; no named risk driver". Step 1.4 "no specific named facts; no risk driver distinguished". C-15: gap DIAGNOSTIC PATTERN WRONG. C-16: Step 2.1 WRONG "[current = HIGH → destination = HIGH]" with CORRECT "[current = HIGH → XL > HIGH]" |
| C-18 | PASS | Compilation table column headers encode all relational constraints; format strings encode tier vocabulary |
| C-19 | PASS | Every WRONG/CORRECT block appears within "Read before writing your X" — before the output instruction for that field |
| C-20 | PASS | Phase 1 Sizing Analyst / Phase 2 Risk Assessor; basis/gap role-separated with non-access clause |
| C-21 | PASS | All DIAGNOSTIC PATTERN instances have concrete named WRONG (e.g., "Tier-Up: If things get more complex, tier goes to HIGH.") and CORRECT instances |
| C-22 | PASS | Compilation table: "Confidence Gap [must address dimension not confirmed in Basis — integration points, count, tier, and rationale are all confirmed]" |
| C-23 | PASS | Phase 1 charter and exclusion list; Phase 2 charter and exclusion list; all fields owned exactly once |
| C-24 | PASS | "Specifically: the integration point list, the count, the complexity tier, and the confidence basis rationale are ALL confirmed in Phase 1 and are prohibited as gap content." — most explicit version of any variation |
| C-25 | PASS | "Is this gap derivable from my Phase 1 Confidence Basis by negating or paraphrasing something the Sizing Analyst confirmed?" — concrete executable |
| C-26 | PASS | "[Sizing Analyst]" and "[Risk Assessor]" in compilation table column headers |
| C-27 | PASS | Cross-phase constraint in compilation table gap column label |
| C-28 | PASS | Self-test present in checkpoint (C-25 satisfies multi-phase analog) |
| C-29 | PASS | Phase 1 exclusion: "Confidence Gap, Tier-Up Condition, Tier-Down Condition." — mirrors Phase 2 charter |
| C-30 | PASS | All three mechanisms inside CONFIDENCE GAP CHECKPOINT |
| C-31 | PASS | C-32 used; gap outside table; C-31 not triggered |
| C-32 | PASS | `── CONFIDENCE GAP CHECKPOINT ──` as explicit phase gate; standalone section; between Phase 1 and Phase 2; explicit note "Phase 1 begins only when gate result = OPEN" |
| C-33 | PASS | "you have written a basis-negation — a Phase 2 charter violation." |
| C-34 | PASS | "FAILURE CLASS: basis-negation" in WRONG block |
| C-35 | PASS | "Gate result [produce exactly one]: OPEN — both preconditions CLEAR or CLOSED — {CLOSED-LABEL value}"; binary signal required explicitly |
| C-36 | PASS | Precondition B: "Signal boundary intact: the input requests sizing signals only — no task breakdowns, sprint assignments, owner names, or milestone dates." Named separately; CLOSED-LABEL identifies precondition |
| C-37 | PASS | Every DIAGNOSTIC PATTERN has FAILURE CLASS, DETECTION PATTERN, WHY IT FAILS as labeled entries. Gap section also adds REMEDIATION as 4th field (exceeds minimum, doesn't violate) |
| C-38 | PASS | Formal precondition table; STATUS (CLEAR/BLOCKED); CLOSED-LABEL per row |
| C-39 | PASS | `── DIAGNOSTIC PATTERN ──` visual delimiter used consistently across Steps 1.3, 1.4, gap section, and Step 2.1 |
| C-40 | PASS | "→ see CONFIDENCE GAP CHECKPOINT above" in compilation table; no gap content in table |
| C-41 | PASS | "[fill only if BLOCKED; leave blank if CLEAR]" in CLOSED-LABEL column header |
| C-42 | PASS | All three defense mechanisms entirely inside CONFIDENCE GAP CHECKPOINT |
| C-43 | PASS | CONFIDENCE GAP CHECKPOINT precedes Output Compilation Table; "── PHASE 2 COMPLETE ──" marker further separates analysis from compilation |

**Aspirational: 35/35**

**V-05 Total: 125/125 → Composite: 100.0**

---

## Rankings

| Rank | Variation | Composite | pts/125 | All Essential |
|------|-----------|-----------|---------|---------------|
| 1 (tie) | **V-01** Gap Section Ordering | **100.0** | 125.0 | YES |
| 1 (tie) | **V-02** Inertia-First Framing | **100.0** | 125.0 | YES |
| 1 (tie) | **V-04** Three-Role + Table-Dominant | **100.0** | 125.0 | YES |
| 1 (tie) | **V-05** Maximum Lifecycle Explicitness | **100.0** | 125.0 | YES |
| 5 | **V-03** Single-Phase Conversational | **94.4** | 118.0 | YES |

**All five variations exceed the golden threshold (≥ 90 composite, all essential PASS).**

**V-03 gap analysis** (6 pts lost):
- C-20, C-23, C-24, C-25, C-26, C-29 — all role-charter criteria structurally inaccessible to single-phase designs
- C-17, C-21 — Step 5 Tier-Up example uses abstract pattern labels rather than concrete named instances; -1.0 pt combined

The v20 rubric structurally scores single-phase designs ~5.6 pts below two-phase designs when they achieve everything else. This is an inherent design floor for the register.

---

## Excellence Signals (R21 Candidates)

These patterns appear in R20 top-scorers but are not yet captured by any criterion:

**Signal 1 — REMEDIATION as 4th field in DIAGNOSTIC PATTERN** (V-05)

V-05 adds a REMEDIATION field after WHY IT FAILS:
```
REMEDIATION: identify a dimension Phase 1 did not address — e.g., the operational details of 
the risk driver (signing scheme implementation class, not just the fact that it is unconfirmed)
```
C-37 requires recognition of the failure class; REMEDIATION gives the repair path at diagnosis time. The model encounters not just "you did X wrong" but "here is the exit." This is a stronger generation-time guard than the three-field form: after naming the class and pattern, the model is handed a concrete alternative direction before returning to produce the field. Potential C-44.

**Signal 2 — Explicit phase completion marker as ordered boundary** (V-05)

V-05 adds `── PHASE 2 COMPLETE ──` between the sensitivity analysis and the compilation table:
```
### ── PHASE 2 COMPLETE ──
Both sensitivity conditions are written. Proceed to the output compilation table.
```
This creates an explicit structural gate between analysis phases and the output compilation pass. Without it, a model that reaches the compilation table could loop back into analysis — especially under regeneration. The marker makes the analysis-before-compilation ordering enforced at the section level, not just implied by proximity. Potential C-45.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["REMEDIATION field as 4th entry in DIAGNOSTIC PATTERN gives repair path at failure-class exposure time, converting diagnosis into directed correction before the model returns to produce the field", "Explicit phase completion marker (-- PHASE 2 COMPLETE --) as a named section boundary between analysis phases and output compilation enforces analysis-first ordering at document-structure level"]}
```
