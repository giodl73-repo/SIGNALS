Now I have all the evidence needed. Let me score all five variations.

---

## Scout-Risk — Round 15 Scorecard (Rubric v14)

### Scoring Methodology

Baseline confirmed: R14 V-05 passes C-01 through C-41 cleanly. R15 variations are targeted single-sentence edits at three sites only. Each variation is the R15 baseline with exactly the described changes applied.

Three discriminating criteria this round: **C-42** (Phase 2 violation typing), **C-43** (Phase 2b two-part exclusion), **C-44** (Phase 0b exhaustivity closure).

---

### Criterion-by-Criterion Evidence

#### Essential (12 pts each — all variations)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-01 | PASS | PASS | PASS | PASS | PASS | Phase 1 requires single-row Table 1 "in all output regardless of any AMEND directive" — mandatory and first |
| C-02 | PASS | PASS | PASS | PASS | PASS | Phase 1b seeds one HIGH row per all five dimensions; Phase 2 "All active dimensions must be represented" |
| C-03 | PASS | PASS | PASS | PASS | PASS | Phase 0b schema enforces Risk-ID, Dimension, Severity, Likelihood, Mitigation, Type-Class on every row; Table 1 Extension adds Status-quo Description, Inertia Condition, Decision Window |
| C-04 | PASS | PASS | PASS | PASS | PASS | "Severity: Exactly one of: HIGH \| MEDIUM \| LOW. No other values." — column-level vocabulary constraint |
| C-05 | PASS | PASS | PASS | PASS | PASS | Phase 0 requires `[Type-Class: sub-field=value]` format; Phase 2a enumerates 7 forbidden hedge-phrases with Repair Loop B |

**Essential subtotal: 60/60 all variations**

---

#### Recommended (10 pts each — all variations)

| ID | All | Evidence |
|----|-----|----------|
| C-06 | PASS | Dimension column vocabulary-constrained to exactly 5 named values |
| C-07 | PASS | "IF-THEN form: IF [named condition], THEN this risk activates. Bare labels are violations." — enforced on all rows |
| C-08 | PASS | Phase 2 final ordering: "HIGH rows first, MEDIUM second, LOW third" |

**Recommended subtotal: 30/30 all variations**

---

#### Aspirational C-09 through C-41 (2 pts PASS — all variations)

All 33 criteria confirmed PASS for all five variations. Key evidence by criterion group:

| Range | Evidence Summary |
|-------|-----------------|
| C-09, C-13, C-16, C-17 | Phase 3 produces dedicated Table 3 with From-Risk-ID, To-Risk-ID, Trigger Condition, From-Severity, To-Severity; Phase 4 enforces 3-row minimum with Repair Loop D |
| C-10, C-34, C-35 | Phase 0a produces structured AMEND Scope Declaration (Active/Suppressed Dimensions table) as closed precondition before any role activates |
| C-11, C-12, C-14, C-19 | Phase 2a enumerates 7 forbidden phrases; IF-THEN form required; Repair Loop B |
| C-15, C-18, C-24, C-26 | Phase 0 defines all 6 type classes with required sub-fields before Phase 0b; `[Type-Class: sub-field=value, sub-field=value]` format enforced inline |
| C-20, C-21, C-23 | Four named repair loops (A/B/C/D) matching four count gates; each uniquely labeled |
| C-22, C-33 | From-Severity and To-Severity: "Exactly one of: HIGH \| MEDIUM \| LOW"; Dimension: "Exactly one of: Technical \| Market \| Compliance \| Dependency \| Timeline. No other values." — cell-level vocabulary constraints |
| C-25 | Phase 2b labeled "Standalone Phase — Do Not Merge with Any Other Step" |
| C-27 | Phase 0 (taxonomy) precedes Phase 0b (schema) which precedes Phase 1 — taxonomy block is pre-generation |
| C-28, C-29, C-30 | Table 1 Schema Extension defines Status-quo Description, Inertia Condition, Decision Window as named distinct fields; Table 1 isolated from Table 2 |
| C-31 | Phase 2 minimum 7 rows with Repair Loop A |
| C-32 | Phase 3 specifies Trigger Condition as "a dedicated column, not embedded in severity cells" |
| C-36, C-38 | Phase 1b seeds one HIGH per dimension before Phase 2; "Count active dimensions. Count HIGH rows. They must match." — equality gate |
| C-37 | Phase 0b declares Table 2 Row Schema + Table 1 Schema Extension as explicit field list before any row population; INERTIA-01 required to fill same base schema with named substitutions |
| C-39 | Phase 2 header: "Add MEDIUM and LOW rows to the seeded HIGH rows from Phase 1b" + explicit prohibition on HIGH rows (varies by variation — but prohibition form passes C-39 in all) |
| C-40 | V-01/V-03: "a deficit here means type monoculture, not a per-dimension HIGH coverage gap" — diagnosis redirection names the upstream-guaranteed property and partitions diagnostic scope; PASS. V-02/V-04/V-05: explicit declarative scope claim + action prohibition — PASS (stronger form) |
| C-41 | Phase 0b "Forward-Reference Coverage Declaration" names Phase 1, Phase 1b, Phase 2 as consumers; each phase references "Phase 0b" by name (backward pointers present) |

**Aspirational C-09–C-41 subtotal: 66/66 all variations**

---

#### Aspirational C-42, C-43, C-44 — Discriminating Criteria (2 pts each)

##### C-42 — Expansion step prohibition typed as named violation category

| | Evidence | Result |
|--|---------|--------|
| **V-01** | Phase 2: "Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b. **Adding a HIGH-severity row here is a format violation.**" — explicit "format violation" category naming | **PASS** |
| **V-02** | Phase 2: "Do not add HIGH-severity rows in Phase 2 — all HIGH coverage is provided exclusively by Phase 1b." — behavioral instruction only; no violation category named | **FAIL** |
| **V-03** | Phase 2: same as V-02 — prohibition without violation typing | **FAIL** |
| **V-04** | Phase 2: "...Adding a HIGH-severity row here is a **format violation**." — same as V-01 | **PASS** |
| **V-05** | Phase 2: "...Adding a HIGH-severity row here is a **format violation**." — same as V-01 | **PASS** |

##### C-43 — Scope exclusion carries both declarative scope claim and specific action prohibition

| | Evidence | Result |
|--|---------|--------|
| **V-01** | Phase 2b: "Note: Phase 1b seeded HIGH-severity rows across all active dimensions. This audit confirms the type distribution of the complete register — a deficit here means type monoculture, not a per-dimension HIGH coverage gap." — diagnosis redirection only; neither declarative scope claim nor action prohibition | **FAIL** |
| **V-02** | Phase 2b: "**This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only.** A deficit here means the register has type monoculture, not a HIGH coverage gap. **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**" — declarative scope claim (part 1) + specific action prohibition naming two forbidden operations (part 2) | **PASS** |
| **V-03** | Phase 2b: "Note: Phase 1b seeded... a deficit here means type monoculture, not a per-dimension HIGH coverage gap." — diagnosis redirection only, same as V-01 | **FAIL** |
| **V-04** | Phase 2b: "**This audit does not repair...** **Do not revise Phase 1b entries or add HIGH rows to address a type-diversity deficit.**" — both parts present, same as V-02 | **PASS** |
| **V-05** | Phase 2b: same two-part form as V-02/V-04 | **PASS** |

##### C-44 — Consumer list closed by exhaustivity statement

| | Evidence | Result |
|--|---------|--------|
| **V-01** | Phase 0b: "...Each of these phases references this schema by name." + "This schema is complete. Advance to Phase 1." — no exhaustivity statement; open enumeration | **FAIL** |
| **V-02** | Phase 0b: same as V-01 — "This schema is complete. Advance to Phase 1." | **FAIL** |
| **V-03** | Phase 0b: "...Each of these phases references this schema by name. **No generation phase outside this list adds columns or defines its own row anatomy.**" + "This schema is complete **and closed**." — exhaustivity statement present; consumer list converted to closed contract | **PASS** |
| **V-04** | Phase 0b: same as V-01/V-02 — no exhaustivity statement | **FAIL** |
| **V-05** | Phase 0b: "...Each of these phases references this schema by name. **No generation phase outside this list adds columns or defines its own row anatomy.**" + "This schema is complete and closed." — same as V-03 | **PASS** |

---

### Composite Score Summary

| Variation | Essential | Recommended | Aspir C-09–C-41 | C-42 | C-43 | C-44 | **Total** | Band |
|-----------|-----------|-------------|-----------------|------|------|------|-----------|------|
| V-01 | 60 | 30 | 66 | 2 | 0 | 0 | **158/162** | Golden |
| V-02 | 60 | 30 | 66 | 0 | 2 | 0 | **158/162** | Golden |
| V-03 | 60 | 30 | 66 | 0 | 0 | 2 | **158/162** | Golden |
| V-04 | 60 | 30 | 66 | 2 | 2 | 0 | **160/162** | Golden |
| **V-05** | 60 | 30 | 66 | 2 | 2 | 2 | **162/162** | **Golden — Perfect** |

---

### Ranking

1. **V-05 — 162/162** — All three new criteria: format violation typing (C-42) + two-part closed exclusion (C-43) + exhaustivity closure (C-44)
2. **V-04 — 160/162** — C-42 + C-43; Phase 1b forward boundary closed, backward boundary closed; only missing C-44 exhaustivity
3. **V-01 — 158/162** — C-42 only; violation typing at Phase 2
4. **V-02 — 158/162** — C-43 only; two-part exclusion at Phase 2b
5. **V-03 — 158/162** — C-44 only; exhaustivity closure at Phase 0b

(V-01, V-02, V-03 tied at 158; all are Golden band)

---

### Excellence Signals from V-05

**1. Rule-classifiable prohibition vs. behavioral instruction**
"Adding a HIGH-severity row here is a format violation" does something different from "Do not add HIGH-severity rows." A behavioral instruction tells the model what not to do; a named violation category makes non-compliance a detectable fact in the prompt's rule system — classifiable without intent interpretation, the same way an out-of-vocabulary cell value is detectable by scan. Violation typing is the extension of the vocabulary-constraint pattern into prose prohibitions.

**2. Two-part closed scope exclusion as a complete mechanism**
The Phase 2b exclusion requires two independent components that serve distinct structural roles: the declarative scope claim ("this audit does not repair...its scope is type-class distribution only") defines the boundary as a positive assertion; the action prohibition ("Do not revise Phase 1b entries or add HIGH rows...") closes it behaviorally by naming the specific forbidden operations. A scope claim without a prohibition defines the boundary but leaves it behaviorally open. A prohibition without a scope claim forecloses operations without explaining the structural reason. Only the conjunction constitutes a complete closed mechanism.

**3. Exhaustivity converts enumeration to contract**
"No generation phase outside this list adds columns or defines its own row anatomy" takes the consumer enumeration from an affirmative list ("these phases consume the schema") to a contractual constraint ("only these phases may consume it"). The structural move is identical to the vocabulary constraint pattern: naming permitted values is an open affirmation; adding "no other values permitted" is a closed contract. Consumer enumeration exhaustivity applies the same closure logic at the schema-scope level.

**4. Minimal-edit principle confirmed at scale**
All three C-42/C-43/C-44 additions are single-sentence changes — one sentence added to Phase 2, one sentence replacing one sentence in Phase 2b (plus a second prohibition sentence), one sentence appended to Phase 0b's footer. None required phase restructuring. The largest scoring leverage (6 pts across three criteria) comes from the smallest linguistic units because the underlying structural machinery (precondition phases, repair loops, named schemas) was already in place from prior rounds. Structural scaffolding pays compounding returns on subsequent micro-additions.

**5. Non-interacting orthogonal additions compose cleanly**
C-42 targets Phase 2 (expansion boundary), C-43 targets Phase 2b (audit boundary), C-44 targets Phase 0b (schema boundary). Different phases, different schema relationships, different structural roles. Composition does not produce side effects — V-04 (C-42 + C-43) scores exactly V-01 + V-02 − 156; V-05 (all three) scores exactly V-04 + V-03 − 156. Orthogonality means the combination score is the sum of the individual additions, confirming independent structural concerns.

---

```json
{"top_score": 162, "all_essential_pass": true, "new_patterns": ["Named violation categories convert behavioral prohibitions to rule-classifiable constraints — same scan-detectability mechanism as vocabulary-constrained column fields", "Complete scope exclusions require two structurally distinct parts: declarative scope claim naming what the audit will not do, plus specific action prohibition naming the forbidden operations — scope claim defines the boundary, prohibition closes it behaviorally", "Consumer list exhaustivity converts affirmative enumeration to closed contract by appending a statement that prohibits unlisted phases from extending the schema — mirrors the vocabulary constraint pattern applied at schema-scope level"]}
```
