# Quest Score — campaign-evidence (Round 9)

**Only V-01 was provided in the variate.** Scoring proceeds on V-01 only; V-02 through V-06 are absent from the prompt body.

---

## V-01 — Role Sequence Axis

**Axis**: Stage ordering enforced as named role-handoff social contract.
**Hypothesis tested by design**: Naming each stage as a role that explicitly passes control to the next prevents hypothesis pre-commitment because the executor must see the evidence-receiver role named before the hypothesis stage may open.

---

### Criterion-by-Criterion Evaluation

#### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Five named stages (Web Researcher → Intelligence Analyst → Hypothesis Architect → Evidence Analyst → Synthesis Director) declared in strict role-handoff order. "Role passes left-to-right. No role may begin until the preceding role has closed its output." |
| C-02 | **PASS** | SEQUENCING RULE: "Hypotheses may be declared only after Stage 1 and Stage 2 have closed their outputs." Stage 3 entry condition: "Stage 1 AND Stage 2 outputs both present." Hypothesis stage cannot open until evidence stages are closed. |
| C-03 | **PASS** | FALSIFICATION RULE declared in preamble. Stage 3 exit condition: "Each hypothesis carries a falsification condition." Binary invocation at Stage 3: "Does every hypothesis carry an explicit falsification condition? [ Yes / No ]" |
| C-04 | **PASS** | Final output section specifies a single document with 9 named parts: title, findings, hypotheses, analysis, synthesis, gaps, decision readiness, gate record, audit table. Self-contained by design. |

**Essential result: 4/4 — 60/60 pts**

---

#### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | **PASS** | ATTRIBUTION RULE: 70% threshold, invoked with binary form at Stages 1, 2, 4, 5. Stage-source tags (S1)–(S5) mandated per claim. |
| C-06 | **PASS** | Stage 5 explicitly: "Distinguish consensus from conflict between S1 and S2." Final brief section 5: "Synthesis — consensus vs conflict, S1/S2 distinguished explicitly." Not a side-by-side list — named distinction required. |
| C-07 | **PASS** | CALIBRATION RULE: "at least two distinct levels." Anti-pattern guard: "if every finding carries the same confidence level, calibration has failed — revise before closing." Both preamble and Stage 5 carry the guard. |

**Recommended result: 3/3 — 30/30 pts**

---

#### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | **PASS** | Final brief section 6: "Gaps and open questions — what remains unknown." Stage 5: "Surface gaps and open questions." |
| C-09 | **PASS** | Final brief section 7: "Decision readiness — one sentence: posture + blocking gap if not ready." |
| C-10 | **PASS** | Stage 3 entry condition requires S1 AND S2 present. SEQUENCING RULE invoked at Stage 3 with binary "Do all hypothesis rows reference only S1/S2 stage values? [ Yes / No ]" |
| C-11 | **PASS** | CALIBRATION RULE in preamble: "A brief where every finding carries the same confidence rating fails calibration." Anti-pattern guard re-stated at Stage 5 close with an explicit "revise before closing" instruction. |
| C-12 | **PASS** | "one sentence: posture + blocking gap if not ready" — compression is explicit and required. |
| C-13 | **PASS** | All four rules declared as named identifiers in GOVERNANCE PREAMBLE. Each rule is invoked by name at every applicable stage with explicit binary form. |
| C-14 | **PASS** | SEQUENCING RULE encodes: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis." Rationale is part of the rule body, not merely structural. |
| C-15 | **PASS** | SEQUENCING RULE appears in the preamble as a peer rule with inline scope annotation `[invoked at: Stage 3, Stage 4, Stage 5]`. Named and referenceable by identifier. |
| C-16 | **PASS** | Coverage map cross-checked against stage executions: ATTRIBUTION invoked at S1/S2/S4/S5 (4/4), SEQUENCING at S3/S4/S5 (3/3), FALSIFICATION at S3/S5 (2/2), CALIBRATION at S4/S5 (2/2). Zero stages silently apply a rule. Note: Stage 1 includes a "SEQUENCING RULE invoked [Stage 1 of 5]: No — this is an evidence stage" note, which is structurally clean given the coverage map shows `—` for S1/SEQUENCING. |
| C-17 | **PASS** | Section header: "PRE-DECLARED COVERAGE MAP (immutable after this point)" — appears in the preamble, before Stage 1 execution. Commitment precedes execution. |
| C-18 | **PASS** | "Four rules govern this campaign. All four are peers — none is primary." All four rules appear at the same structural tier with the same formatting. |
| C-19 | **PASS** | "This map is finalized before Stage 1 begins and cannot be modified after any stage executes." Explicit immutability clause present. |
| C-20 | **PASS** | Every rule carries an inline scope annotation within the rule body: ATTRIBUTION `[invoked at: Stage 1, Stage 2, Stage 4, Stage 5]`, SEQUENCING `[invoked at: Stage 3, Stage 4, Stage 5]`, FALSIFICATION `[invoked at: Stage 3, Stage 5]`, CALIBRATION `[invoked at: Stage 4, Stage 5]`. Coverage is inseparable from rule identity. |
| C-21 | **PASS** | CALIBRATION at Stage 4: "Do confidence ratings span at least two distinct levels so far? [ Yes / No ]" — binary. FALSIFICATION at Stage 3: "Does every hypothesis carry an explicit falsification condition? [ Yes / No ]" — binary. Multiple critical rules use interrogative binary form, not passive tags. |
| C-22 | **PASS** | All 11 applicable invocations (ATTRIBUTION×4, SEQUENCING×3, FALSIFICATION×2, CALIBRATION×2) use `[ Yes / No ]` binary verification form. No stage applies a rule via passive tag. |
| C-23 | **PASS** | Every invocation carries `[Stage N of 5]` suffix. Count is arithmetic: 11 invocations derivable from the coverage map. Completeness is verifiable without prose interpretation. |
| C-24 | **PASS** | All five stages carry explicit entry and exit conditions. Stage 1: "Entry: User has provided the investigation topic. Exit: Web findings documented with source attribution." All five gates are formally specified. |
| C-25 | **PASS** | Gate record appears as final brief section 8 ("Gate Record — filled table from the pre-template above") and as a standalone pre-templated section in the preamble. Gate trail is inspectable as a named artifact. |
| C-26 | **PASS** | Final brief section 9: "Consolidated Invocation Audit Table" with column headers for rule, stage, stage index, form, pass/fail. Row count = 11, derived explicitly from "ATTRIBUTION=4, SEQUENCING=3, FALSIFICATION=2, CALIBRATION=2" — not an independent hardcoded integer. Count is derivable from the coverage map. |
| C-27 | **PASS** | "PRE-TEMPLATED GATE RECORD (blank — fill as each stage closes)" — blank Pass/Fail cells for all 5 stages appear in the preamble before Stage 1. Filling a cell is mechanical; omitting the section would be structurally visible as an unfilled blank. |
| C-28 | **PASS** | SEQUENCING RULE: "Machine-verifiable enforcement: the evidence table carries a Stage column (S1/S2/S3/S4/S5); any hypothesis row may reference only S1 or S2 source rows." Grounded-in constraint encoded as a column rule, not just prose. Sort-based verification is possible. |
| C-29 | **PARTIAL** | Derivation mechanism is in place: row count is computed from per-rule applicable-stage counts, not pre-declared as an independent static integer — adding a rule and updating the coverage map automatically updates the count. However, the peer-equality declaration uses a hardcoded count: "Four rules govern this campaign. All four are peers — none is primary." Adding a fifth rule would require manually updating "Four" to "Five" — the peer declaration does not use a variable-N form. The criterion's pass path requires a declaration that "updates automatically as rules are added"; V-01 satisfies the derivation half but not the peer-declaration-extensibility half. |

**Aspirational result: 21 PASS + 1 PARTIAL / 22**

---

### Composite Score

```
essential:    4/4  × 60  =  60.00
recommended:  3/3  × 30  =  30.00
aspirational: 21.5/22 × 10 =  9.77   (PARTIAL counted as 0.5)
─────────────────────────────────
composite                  = 99.77  ≈  99.8
```

**Band: Silver** (all essential + recommended pass; one aspirational criterion partially fails on the peer-declaration-extensibility half of C-29).

---

### Excellence Signals

**Pattern 1 — Role-handoff as sequencing social contract**
Naming each stage as a role with an explicit "Role passes to: Stage N — Role Name" transition converts sequence enforcement from a structural property into a named social obligation between actors. Before Stage 3 (Hypothesis Architect) can open, the executor must read "Role passes to: Stage 3 — Hypothesis Architect" — which makes hypothesis pre-commitment structurally visible at the handoff boundary, not only at the rule declaration. This is a new enforcement mechanism not captured in C-01 through C-29.

**Pattern 2 — SEQUENCING "does not apply here" at non-applicable stages**
Stage 1 carries: "SEQUENCING RULE invoked [Stage 1 of 5]: No — this is an evidence stage; sequencing rule does not apply here." This is a negative invocation — explicitly noting that the rule was checked and does not apply. Without this, a reader scanning invocations might flag Stage 1 as a gap. Negative invocations make the coverage map machine-checkable without ambiguity.

**Pattern 3 — Gate record pre-instantiation converts compliance to mechanical act**
Placing the blank gate table in the preamble before Stage 1 removes the creative act of "remembering to create a gate record section." An unfilled cell is visible at any point in the brief's lifecycle; post-hoc omission is structurally impossible. C-27 captures the requirement; V-01's execution demonstrates the difference between requirement satisfaction and structural enforcement.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["role-handoff-as-social-contract: naming each stage as a role that explicitly passes control to the next stage converts sequence enforcement from a structural convention into a named social obligation between actors — hypothesis pre-commitment is blocked by seeing the evidence-receiver role named before the hypothesis stage may open", "negative-invocation-at-non-applicable-stages: explicitly noting 'this rule does not apply here' at stages where the coverage map shows no applicable cells makes the coverage map machine-checkable and eliminates gap-detection ambiguity"]}
```
