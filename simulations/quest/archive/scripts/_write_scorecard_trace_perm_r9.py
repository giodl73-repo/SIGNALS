content = r"""
# trace-permissions Scorecard — Round 9
**Date:** 2026-03-16
**Rubric:** v7 (C-01 through C-25, max 132.5)
**Variations scored:** V-01 through V-05

---

## Base Criterion Scores (shared by all variations unless noted)

All 5 variations share the same 4-phase CA→CS→SE→CA-1 structure with Schema Registry, Criterion Enforcement Matrix, ENFORCEMENT LANGUAGE INDEX (EL-01 through EL-12 or EL-13), Phase 0 Gate State Log, Gap? per-row boolean, TABLE_1-5 + CS-2 + CS-3 schemas, three-field Remediation, and CA-1 double-anchor verification. Criterion evaluations are stated once; variation-specific deviations are noted.

### Essential (12.0 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | TABLE_1 declared with Role column; Record Scope column carries Own/BU/Parent-Child BU/Org-wide/Team-scoped values — BU scope level structurally enforced. SHALL-A requires all cells Granted/Denied/Conditional/N/A. |
| C-02 | **PASS** | TABLE_2 FLS Coverage with Roles: Read and Roles: Write columns covers field visibility per role. SHALL-B requires every sensitive field listed. |
| C-03 | **PASS** | TABLE_3 Record Scope by Role evaluates scope appropriateness per role. SHALL-C requires Effective Scope filled for every TABLE_1 role; ambiguous scope routes to TABLE_5. |
| C-04 | **PASS** | TABLE_4 requires all four vectors (team inheritance / sharing rules / impersonation / admin or environment role override), Checked? = YES for all. Per-role escalation roll-up requires Pre-Declaration Commitment + Composite Verdict + Mechanisms Cited + Cross-Audit. |
| C-05 | **PASS** | TABLE_5 Security Gap Inventory with enumerated gap types (MISSING-FLS, ESCALATION-PATH, SHARING-CONFLICT, TEAM-GAP, OVER-PERMISSIONED, CS-EXPECTATION-VIOLATED). Three-field Remediation structurally required. |

Essential subtotal: **60.0**

### Recommended (10.0 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | All variations use: business units, column security profiles/FLS, security roles, owner-access teams, TABLE_3 references OWD (organization-wide default), sharing rules, environment role override. 4+ Dataverse-specific terms accurate. |
| C-07 | **PASS** | CS-2 "Sharing Rule Expectations" schema includes Potential Overreach? column; SE-4 checks sharing rules as one of the four escalation vectors; SE-3 CONTEXT-CLOSES: OWD-sharing-rule override. |
| C-08 | **PASS** | TABLE_5 Remediation three-field format: (1) Config change with exact object + location + change; (2) Expected state as specific UI view; (3) Verification step as named action. Structurally specific rather than generic. |

Recommended subtotal: **30.0**

### Aspirational (2.5 pts each; PARTIAL = 1.25)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PARTIAL** | All four Dataverse layers addressed across SE sections (SE-1: role+BU, SE-2: FLS/column profiles, SE-3: OWD+sharing, SE-4: escalation/teams); CONTEXT-CLOSES labels name which failure mode each SE section resolves. MISS: no single defense-in-depth table identifying the effective enforcement layer per operation with why-upper-layers-do-not-override explanation. |
| C-10 | **PASS** | CS-3 schema "CS Expected Access \| Privileged-Role Expected Access \| Gap Expected?" requires explicit cross-role comparison. SE fills CS-3 Confirmation column after TABLE_1. |
| C-11 | **PASS** | Phase 0 gate hands named artifacts (Schema Registry, SHALL obligations, INDEX) to Phase 1. CS-0 (or V-03 equivalent) declares Phase 0 input dependency. SE references CS-2/CS-3 by Schema ID. CA-1 verdict cites "Schema Registry (Step 0.1), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate state log" — named artifacts matching prior phase output labels. |
| C-12 | **PARTIAL** | Sentinel type 1: Gap? = YES in TABLE_2 (placed at each row discovery; triggers TABLE_5 entry per-row — aggregates to gap inventory ✓). Sentinel type 2: SCOPE-DRIFT tokens ([SCOPE-DRIFT-CS-COUNT], [SCOPE-DRIFT-SE-EXPAND]) placed at scope-drift discovery points but block TABLE_1 population rather than aggregating to TABLE_5. Gap inventory aggregates Gap? sentinels but not SCOPE-DRIFT sentinels. Two sentinel types present but aggregation pattern incomplete for second type. |
| C-13 | **FAIL** | No CLEARED/NOT CLEARED verdict carry-forward language across consecutive phases. V-05 "inertia framing" describes why manual audits fail (dysfunction inertia), not security verdict persistence across analytical phases. |
| C-14 | **PASS** | CONTEXT-CLOSES labels at each SE section name the failure mode closed: "cumulative privilege accumulation" (SE-1), "post-incident FLS discovery" (SE-2), "OWD-sharing-rule override" (SE-3). At least 3 structural elements carry associated named failure modes. |
| C-15 | **PASS** | CONTEXT section before Phase 1 lists 3 named failure modes (Blind spot 1/2/3 or Failure mode 1/2/3 or COMPLIANCE GAP CATEGORY 1/2/3 depending on variation). Each maps to an SE section via CONTEXT-CLOSES label. |
| C-16 | **PARTIAL (base)** | SHALL obligations present; SHALL-D requires TABLE_4 all vectors and per-role rule-out. CS-3 schema requires cross-role comparison. MISS for V-01/V-02/V-03/V-05: update instruction ("Update CS-3 SE Confirmation") is advisory, not SHALL-level. V-04 exception noted below. |
| C-17 | **PASS** | CONTEXT section names 3 failure modes for permissions tracing as a category of analysis (FLS post-incident discovery, cumulative privilege accumulation, OWD-sharing-rule override) — skill-level threat model, not per-phase failure modes. |
| C-18 | **PASS** | Phase 0 Step 0.1 Schema Registry declares all TABLE schemas with labeled column headers (Schema ID: TABLE_1 through TABLE_5, CS-2, CS-3). Artifact names match downstream references: TABLE_1 schema → CA-1.1 "Registry anchor -- TABLE_1 schema (Step 0.1)"; CS-2 → Phase 1 CS-0 "Schema ID: CS-2" acknowledgment; CS-3 → Phase 2 SE-3 update instruction. At least two phases (0 and 1) satisfy the named-artifact-with-schema requirement with matching reference tokens. |
| C-19 | **PASS** | "Gap? = YES rows forward to TABLE_5 immediately (per-row, before next row begins)" — explicit routing rule naming (a) discovery mechanism (Gap? = YES in TABLE_2) and (b) aggregation destination (TABLE_5 by name). |
| C-20 | **FAIL** | No dedicated "Why Not Overridden" or equivalent column in any defense-in-depth table. TABLE_3 has OWD Baseline + Scope Modifier + Effective Scope but no layer-override explanation field. CONTEXT-CLOSES labels name the failure mode but do not provide per-operation layer-override reasoning as a structurally required table cell. |
| C-21 | **PASS (base)** | Phase 0: outputs Schema Registry, SHALL obligations, INDEX, gate log (declared with labeled schemas). Phase 1: input declared (CS-0 acknowledges Phase 0 Schema Registry by label + count); output declared (CS-1, CS-2, CS-3 by Schema ID). Phase 2: input declared (CS-2/CS-3 referenced by Schema ID in SE update instructions); output declared (TABLE_1-5 by Schema ID). Phase 3: input declared (cites Schema Registry, preamble, INDEX, gate log by label). All phase boundaries closed with matching artifact labels. V-03 exception noted below. |
| C-22 | **PARTIAL** | ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION in CA-1 performs N/12 (or N/13) count-comparison with "N < 12: C-28 FAIL unconditionally" — a named pass/fail gate before trace close. MISS: counts enforcement points, not findings-discovered vs gap-identifiers-assigned. Gap inventory is populated incrementally via Gap? boolean during analysis (not aggregated at a post-analysis gate). No formal "before aggregation" gate comparing TABLE_5 row count against a pre-declared scope. |
| C-23 | **FAIL** | CA-1 verdict cites Phase 0 artifacts by label ("Schema Registry (Step 0.1), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate state log") but does not produce a linear chain trace statement listing every phase boundary: "Phase 0 EXIT GATE → Phase 1 INPUT → Phase 1 EXIT GATE → Phase 2 INPUT → Phase 2 EXIT GATE → Phase 3 INPUT → Phase 3 EXIT GATE." The full boundary chain is not auditable at a single point without traversing all phase headers. |
| C-24 | **PASS** | CA-1.1 through CA-1.5 name criterion IDs explicitly ("C-01: TABLE_1/SE-1/SHALL-A/CA-1.1"). ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION names C-28. PLACEMENT-CRITERION CONFIRMED annotations throughout Phase 0 cite criterion IDs (C-18/C-22, C-29/C-31, etc.). At least 2 exit gate items name criterion IDs matching the criteria they enforce. |
| C-25 | **FAIL** | ENFORCEMENT LANGUAGE INDEX count (12/12 or 13/13) propagates from Phase 0 to CA-1, but there is no role entity count M declared in Phase 0 EXIT GATE and echoed with cross-phase constraint at each intermediate phase. No intermediate phase echoes a count variable with "must equal M from Phase 0." The v9 prompt structure dropped the ROLE ENTITY COUNT DECLARED mechanism from the rubric v7/v8 design. |

---

## Variation-Specific Deviations

### V-01 — C-31 isolation (verbatim cross-audit; C-32 absent)
- C-16: **PARTIAL** — SE instructions are advisory ("Update CS-3 SE Confirmation"), not SHALL/MUST-level.
- C-21: **PASS** — CS-0 explicitly acknowledges Phase 0 Schema Registry by Schema ID; all phase boundaries closed.

**Aspirational sum: 27.5**
**Total: 60.0 + 30.0 + 27.5 = 117.5**

---

### V-02 — C-32 isolation (intent-anchored equivalence; C-31 absent)
- C-16: **PARTIAL** — same advisory pattern as V-01.
- C-21: **PASS** — CS-0 acknowledgment present.
- Note: Cross-audit in this variation uses characterization format, not verbatim quotation; this is a v9-criterion distinction not captured in v7 rubric.

**Aspirational sum: 27.5**
**Total: 60.0 + 30.0 + 27.5 = 117.5**

---

### V-03 — SE-first sequence + C-31 isolation
- C-21: **PARTIAL** — Phase 1 (SE) lacks an explicit CS-0-equivalent opening section acknowledging Phase 0 Schema Registry by label before beginning analysis. Phase 0 gate state log declares "SE-first sequence active" but Phase 1 does not carry an input dependency declaration matching the Phase 0 exit gate labels. Phase 2 (CS) and Phase 3 (CA-1) recover the chain, but Phase 1 as the first analytical phase is an orphan at its input boundary.
- All other criteria: same as base.

**Aspirational sum: 27.5 − 1.25 (C-21 PARTIAL) = 26.25**
**Total: 60.0 + 30.0 + 26.25 = 116.25**

---

### V-04 — Combined C-31 + C-32 + formal/technical register
- C-16: **PASS** — formal register throughout. "SE MUST update CS-3 SE Confirmation column after filling TABLE_1" is a MUST-level instruction. CS-3 schema requires "CS Expected Access \| Privileged-Role Expected Access \| Gap Expected?" — comparison across named roles (a) ✓; "Gap Expected?" column requires an explicit conclusion per pair (b) ✓. Combined with the MUST instruction, this satisfies both conditions of C-16 pass criterion.
- C-21: **PASS** — CS-first sequence with CS-0 acknowledgment.
- Note: 13/13 enforcement points (EL-01 through EL-13, both C-31 and C-32 present). ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION in CA-1 checks EL-12 (C-31) and EL-13 (C-32) by ID.

**Aspirational sum: 27.5 + 1.25 (C-16 PASS) = 28.75**
**Total: 60.0 + 30.0 + 28.75 = 118.75**

---

### V-05 — C-31 + C-32 + quantified inertia framing, CS-first
- C-16: **PARTIAL** — SE update instruction is advisory ("Update CS-3 SE Confirmation"), not SHALL/MUST-level as in V-04. Inertia framing in CONTEXT describes manual audit dysfunction, not verdict persistence or structural enforcement obligation.
- C-21: **PASS** — CS-first with explicit CS-0 acknowledgment block.
- Note: 13/13 enforcement points. V-05 CONTEXT is the most mechanistically detailed: each failure mode names both the structural detection gap AND the specific mechanism that closes it (e.g., "Gap? = YES / NO per field row, not with a narrative summary" for Failure mode 1). This is the strongest CONTEXT framing across all variations.

**Aspirational sum: 27.5**
**Total: 60.0 + 30.0 + 27.5 = 117.5**

---

## Composite Scores and Ranking

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| 1 | **V-04** | **118.75 / 132.5** | YES | C-16 PASS from formal/technical register + MUST-level cross-role differential instruction |
| 2 | V-01 | 117.5 / 132.5 | YES | C-31 verbatim cross-audit; C-32 absent; CS-first |
| 2 | V-02 | 117.5 / 132.5 | YES | C-32 intent-anchored equivalence; C-31 absent; CS-first |
| 2 | V-05 | 117.5 / 132.5 | YES | C-31 + C-32; quantified inertia framing; advisory register |
| 5 | V-03 | 116.25 / 132.5 | YES | C-21 PARTIAL from SE-first Phase 1 input declaration gap |

---

## Excellence Signals from V-04

**Signal 1 — Formal/technical register unlocks C-16 (SHALL-level cross-role differential enforcement).**
Converting SE update instructions from advisory ("Update CS-3") to SHALL/MUST-level ("SE MUST update CS-3 SE Confirmation column after filling TABLE_1") is the minimal change needed to satisfy C-16. The CS-3 schema already provides the comparison structure and "Gap Expected?" conclusion column; the register shift is what closes the enforcement gap. Pattern: C-16 is satisfiable without structural redesign — it requires only that existing cross-role comparison instructions be stated with SHALL/MUST obligation language.

**Signal 2 — Combined C-31 + C-32 presence with criterion IDs in INDEX (EL-12 + EL-13).**
V-04 and V-05 carry 13/13 enforcement points (EL-01 through EL-13). The ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION in CA-1 explicitly checks both EL-12 (verbatim cross-audit) and EL-13 (intent-anchored equivalence) by ID. This is the criterion-referenced gate pattern (C-24) at its most comprehensive across all variations: the gate explicitly names the criteria it enforces for the two newest mechanisms.

**Signal 3 — Intent-anchored equivalence clause (EL-13/C-32) is a generalizing prohibition.**
The Mechanisms Cited prohibition in V-04 (and V-05) anchors the equivalence clause to the prohibited mechanism of effect: "a form PRODUCES THE PROHIBITED EFFECT OF DELEGATION if it routes the reader to another section to obtain the mechanism content." This makes the prohibition generalizable to novel back-reference forms that satisfy its form while violating its function. The v7 rubric has no criterion for this; it is a candidate for C-26.

---

## Criteria Failing Across All Variations (Rubric Improvement Candidates)

| Criterion | Failure Reason | Improvement Candidate |
|-----------|---------------|----------------------|
| C-13 | No verdict carry-forward with CLEARED/NOT CLEARED syntax across phases | v9 variations use "inertia" for the manual audit problem, not for analytical verdict persistence |
| C-20 | No dedicated "Why Not Overridden" table column in any defense-in-depth table | SE sections cover the four layers but no structural column enforces per-operation layer-override explanation |
| C-23 | No linear phase boundary chain statement at terminal phase | CA-1 cites Phase 0 artifacts but does not produce the end-to-end chain trace |
| C-25 | No intermediate phase count echo with cross-phase constraint | v9 prompt dropped the role entity count M propagation mechanism present in earlier rubric designs |

---

## JSON Output

```json
{"top_score": 118.75, "all_essential_pass": true, "new_patterns": ["formal/technical register (SHALL/MUST/PROHIBITED throughout) unlocks C-16 by making CS-3 cross-role differential update instruction obligation-level rather than advisory", "intent-anchored equivalence clause anchors back-reference prohibition to mechanism of effect rather than form-resemblance — generalizes to novel delegation forms, candidate for C-26", "SE-first phase sequence creates Phase 1 input declaration orphan (C-21 gap) when opening acknowledgment section is absent — CS-0-equivalent section needed regardless of sequence direction"]}
```
"""

with open(r'C:\src\sim\simulations\quest\scorecards\trace-permissions-scorecard-R9-2026-03-16.md', 'w', encoding='utf-8') as f:
    f.write(content.lstrip('\n'))

print("Written successfully.")
