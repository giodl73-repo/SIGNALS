## trace-contract — Round 3 Scoring (Rubric v3)

---

### Variation Scorecards

---

#### V-01 — Per-Finding `connector-impact:` Slot

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | Step 2 explicit "Do not run"; `[CONTRACT COMMITTED]` gate enforced |
| C-02 | Explicit diff | PASS | `deviation: expected {X}; actual {Y}` in every finding block |
| C-03 | Severity per finding | PASS | `severity: [breaking | degraded | cosmetic]` labeled field in template |
| C-04 | Root cause hypothesis | PASS | `hypothesis:` required field in finding block |
| C-05 | Spec reference | PASS | `spec:` required field in finding block |
| C-06 | Automate/Connectors lens | PASS | `connector-impact:` mandatory on every finding; "No finding may omit this field" |
| C-07 | Summary verdict | PASS | Step 5 table with per-severity counts + Verdict line |
| C-08 | Clean zero-finding confirmation | PASS | "Contract satisfied — all fields matched expected output. No findings." |
| C-09 | Amendment suggestion | PASS | `recommendation: [amend-spec | fix-impl | needs-discussion]` required on breaking/degraded |
| C-10 | Pattern recognition | FAIL | No Patterns section or inline grouping |
| C-11 | Structural field enforcement | PASS | 7-field labeled block; missing field is visible gap |
| C-12 | Phase-gate confirmation | PASS | `[CONTRACT COMMITTED]` with "Do not continue past this line" |
| C-13 | Machine-readable gate token | FAIL | Token is `[CONTRACT COMMITTED]` — not `[EXPECTED SEALED]`; not defined as machine-parseable |
| C-14 | Per-finding integration coverage | PASS | `connector-impact:` in unified template on all findings |
| C-15 | Amendment enforcement by template | FAIL | No separate breaking template; field name is `recommendation:` not `recommended-action:`; single unified template with conditional requirement |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 4/7 × 10 = 5.71
**Composite: 95.7** ✓ Golden

---

#### V-02 — Breaking-Finding Template with `recommended-action:` Slot

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | `[CONTRACT COMMITTED]` gate; "Do not proceed past this line" |
| C-02 | Explicit diff | PASS | `deviation: expected {X}; actual {Y}` in both templates |
| C-03 | Severity per finding | PASS | Template A labeled "Breaking Finding"; Template B has `severity: [degraded | cosmetic]` field |
| C-04 | Root cause hypothesis | PASS | `hypothesis:` required in both Template A and B |
| C-05 | Spec reference | PASS | `spec:` required in both templates |
| C-06 | Automate/Connectors lens | PASS | Prose at-least-one callout: "At least one finding must explicitly note integration-level impact" |
| C-07 | Summary verdict | PASS | Step 5 table with counts + Verdict |
| C-08 | Clean zero-finding confirmation | PASS | Explicit no-finding statement present |
| C-09 | Amendment suggestion | PASS | `recommended-action:` required slot in Template A with `amend-spec | fix-impl | needs-discussion` vocabulary |
| C-10 | Pattern recognition | FAIL | No patterns section |
| C-11 | Structural field enforcement | PASS | Two separate templates; missing field produces visible gap |
| C-12 | Phase-gate confirmation | PASS | `[CONTRACT COMMITTED]` explicit gate |
| C-13 | Machine-readable gate token | FAIL | `[CONTRACT COMMITTED]` — not `[EXPECTED SEALED]`; not defined as machine-parseable |
| C-14 | Per-finding integration coverage | FAIL | No `connector-impact:` slot in any finding template; only prose at-least-one callout (satisfies C-06, not C-14) |
| C-15 | Amendment enforcement by template | PASS | Template A (breaking) has `recommended-action:` as 5th required labeled slot with constrained vocabulary |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 4/7 × 10 = 5.71
**Composite: 95.7** ✓ Golden

---

#### V-03 — Machine-Readable Seal Token `[EXPECTED SEALED]`

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | "Do not continue past `[EXPECTED SEALED]` until Automate has completed Step 3" |
| C-02 | Explicit diff | PASS | `deviation: expected {X}; actual {Y}` in finding block |
| C-03 | Severity per finding | PASS | `severity: [breaking | degraded | cosmetic]` labeled field |
| C-04 | Root cause hypothesis | PASS | `hypothesis:` required in finding block |
| C-05 | Spec reference | PASS | `spec:` required in finding block |
| C-06 | Automate/Connectors lens | PASS | "At least one finding must explicitly state the integration-level impact" |
| C-07 | Summary verdict | PASS | Summary table with counts + Verdict |
| C-08 | Clean zero-finding confirmation | PASS | Explicit affirmative no-findings statement |
| C-09 | Amendment suggestion | PASS | `recommendation: [amend-spec | fix-impl | needs-discussion]` required on breaking/degraded |
| C-10 | Pattern recognition | FAIL | No patterns section |
| C-11 | Structural field enforcement | PASS | Labeled finding block; missing field is visible |
| C-12 | Phase-gate confirmation | PASS | `[EXPECTED SEALED]` satisfies this as explicit gate confirmation |
| C-13 | Machine-readable gate token | PASS | `[EXPECTED SEALED]` defined explicitly as "a machine-parseable boundary marker"; placement specified (own line, immediately after last Expected Output entry); anti-paraphrase rule stated; automated verification mechanism explained |
| C-14 | Per-finding integration coverage | FAIL | No `connector-impact:` slot in finding block; at-least-one prose callout only (C-06 not C-14) |
| C-15 | Amendment enforcement by template | FAIL | Single unified template; `recommendation:` is conditionally required (N/A for cosmetic); no separate breaking-finding template with `recommended-action:` as required slot |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 4/7 × 10 = 5.71
**Composite: 95.7** ✓ Golden

---

#### V-04 — Combination: `connector-impact:` + `recommended-action:` (No Token Upgrade)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | `[CONTRACT COMMITTED]` gate enforced |
| C-02 | Explicit diff | PASS | `deviation: expected {X}; actual {Y}` in all three templates |
| C-03 | Severity per finding | PASS | Template A: "Breaking Finding" in block title; Template B: "Degraded Finding"; Template C: "Cosmetic Finding" — exact taxonomy labels |
| C-04 | Root cause hypothesis | PASS | `hypothesis:` in Templates A and B; Template C also has it |
| C-05 | Spec reference | PASS | `spec:` required in all three templates |
| C-06 | Automate/Connectors lens | PASS | `connector-impact:` required on all templates satisfies the at-least-one callout |
| C-07 | Summary verdict | PASS | Step 5 table with counts + Verdict |
| C-08 | Clean zero-finding confirmation | PASS | Explicit no-deviation statement present |
| C-09 | Amendment suggestion | PASS | Template A `recommended-action:` with vocabulary and "one sentence rationale: which side of the contract is wrong and why" |
| C-10 | Pattern recognition | FAIL | No patterns section |
| C-11 | Structural field enforcement | PASS | Three-tier template system; missing field per severity template is self-announcing |
| C-12 | Phase-gate confirmation | PASS | `[CONTRACT COMMITTED]` gate confirmed |
| C-13 | Machine-readable gate token | FAIL | Uses `[CONTRACT COMMITTED]` — not `[EXPECTED SEALED]`; not defined as machine-parseable boundary marker |
| C-14 | Per-finding integration coverage | PASS | `connector-impact:` in Templates A, B, and C; "All six fields are required on every breaking finding" + required on degraded + cosmetic |
| C-15 | Amendment enforcement by template | PASS | Template A (breaking) has `recommended-action:` as 6th required labeled slot; vocabulary `amend-spec | fix-impl | needs-discussion` enforced |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 5/7 × 10 = 7.14
**Composite: 97.1** ✓ Golden

---

#### V-05 — Full Combination: `[EXPECTED SEALED]` + `connector-impact:` + `recommended-action:` (Skeleton-First)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Expected before actual | PASS | Skeleton shows `[EXPECTED SEALED]` placement; "Do not continue past `[EXPECTED SEALED]`. The Contract Expert role suspends here." |
| C-02 | Explicit diff | PASS | `deviation: expected {X}; actual {Y}` in all three templates |
| C-03 | Severity per finding | PASS | "Breaking Finding / Degraded Finding / Cosmetic Finding" labels in all template block headers |
| C-04 | Root cause hypothesis | PASS | `hypothesis:` required in Templates A, B, and C |
| C-05 | Spec reference | PASS | `spec:` required in all three templates |
| C-06 | Automate/Connectors lens | PASS | `connector-impact:` mandatory on all finding blocks; structural per-finding enforcement satisfies at-least-one callout |
| C-07 | Summary verdict | PASS | Summary table with per-severity counts + Verdict + Coverage ratio |
| C-08 | Clean zero-finding confirmation | PASS | "Contract satisfied — all Expected Output entries matched. No findings." |
| C-09 | Amendment suggestion | PASS | Template A `recommended-action:` with three-way vocabulary and rationale requirement |
| C-10 | Pattern recognition | FAIL | No Patterns section; no inline finding grouping by root cause |
| C-11 | Structural field enforcement | PASS | Three separate severity templates; skeleton explicitly enumerates required fields per type — missing field leaves visible gap |
| C-12 | Phase-gate confirmation | PASS | `[EXPECTED SEALED]` constitutes explicit gate acknowledgment |
| C-13 | Machine-readable gate token | PASS | Skeleton shows `[EXPECTED SEALED]` as a named section with Marker/Placement/Format/Purpose sub-keys; instructions define it as machine-parseable; "It is not a prose acknowledgment and must not be paraphrased. Write the exact string." + "This is the token that mechanical verification tools search for to confirm sequencing." |
| C-14 | Per-finding integration coverage | PASS | `connector-impact:` in Templates A, B, C; skeleton explicitly lists: "Breaking: element / deviation / spec / connector-impact / hypothesis / recommended-action"; "This field is required on all findings. Write (a) or (b). No finding may omit this field." |
| C-15 | Amendment enforcement by template | PASS | Template A (breaking) has `recommended-action:` as 6th required labeled slot; skeleton shows it as part of the breaking-finding field list; "required on every breaking finding" |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 6/7 × 10 = 8.57
**Composite: 98.6** ✓ Golden

---

### Ranking

| Rank | Variation | Composite | Golden? | Aspirational Pass |
|------|-----------|-----------|---------|-------------------|
| 1 | **V-05** | **98.6** | yes | C-09, C-11, C-12, C-13, C-14, C-15 |
| 2 | **V-04** | **97.1** | yes | C-09, C-11, C-12, C-14, C-15 |
| 3 (tie) | **V-01** | **95.7** | yes | C-09, C-11, C-12, C-14 |
| 3 (tie) | **V-02** | **95.7** | yes | C-09, C-11, C-12, C-15 |
| 3 (tie) | **V-03** | **95.7** | yes | C-09, C-11, C-12, C-13 |

---

### Excellence Signals — V-05

**1. Skeleton-first presentation absorbs prompt density risk.**
V-05 opens with a complete artifact skeleton (sections → `[EXPECTED SEALED]` → finding block field lists by severity) before any step-by-step instruction. When a prompt introduces three new structural features simultaneously, showing the operator the finished artifact shape upfront means all three new fields (`[EXPECTED SEALED]`, `connector-impact:`, `recommended-action:`) are visible before any rule is read. The cognitive load of "what am I building?" is eliminated before the "how do I build it?" instructions begin. V-04 achieves the same two output-format targets (C-14 + C-15) without the skeleton and scores one criterion lower.

**2. Triple-constraint token definition produces C-13 where single-constraint naming fails.**
V-01, V-02, V-04 all use `[CONTRACT COMMITTED]` — they have a gate but not a machine-parseable one. V-03 introduces `[EXPECTED SEALED]` with definition, but V-05 strengthens it: the skeleton shows `[EXPECTED SEALED]` as a formal structural element with four labeled sub-keys (Marker / Placement / Format / Purpose), then the instructions add the anti-paraphrase rule and the mechanical-verification use case. Three constraints — exact string, placement requirement, prohibition on paraphrase — make the token self-defining at write time. A single constraint ("write this token") invites drift; three constraints close the gap.

**3. Three-tier severity template enforces per-finding structural requirements without conditional logic.**
V-01 and V-03 use a unified finding template where `recommendation:` is conditionally required ("cosmetic: N/A"). V-02 has two templates but no `connector-impact:`. V-04 and V-05 use separate Template A / B / C, which removes the conditionality entirely: each block has exactly its required fields with no optional carve-outs. A blank `connector-impact:` slot in a cosmetic finding is a visible gap, not a field the operator can rationalize skipping.

---

### Cross-Variation Miss: C-10

No variation scored C-10. Pattern recognition requires a "Patterns" section grouping findings by shared root cause. This criterion is fully independent of the Round 3 axes — it would require a dedicated axis variation to pass.

---

```json
{"top_score": 98.6, "all_essential_pass": true, "new_patterns": ["Skeleton-first presentation mitigates prompt-density risk on multi-feature variations: showing the complete artifact anatomy (all sections, marker, field lists per severity template) before step-by-step instructions lets the operator internalize the target shape before encountering any rule", "Triple-constraint token definition produces machine-parseable gate compliance where single-constraint naming fails: exact string + placement requirement + anti-paraphrase prohibition closes the operator-drift gap that allows CONTRACT COMMITTED to substitute for EXPECTED SEALED"]}
```
