| **C-37** Dual Illustrative Baseline Examples | PASS | **FAIL** | PASS | PASS | PASS |

---

#### Evidence Notes for Differentiating Criteria

**C-30** (Run-Level Preamble Schema + Named Post-Stage Reference):
- V-01: No RUN-LEVEL RULE GLOSSARY. TRIAGE NOTE AUDIT SCHEMA co-located in audit section. **FAIL**
- V-02: RUN-LEVEL RULE GLOSSARY contains RULE SYNTHESIS with 5 subsections. Synthesis section header: `[RULE SYNTHESIS applies -- see glossary]`. **PASS**
- V-03: No glossary. Standalone RULE SYNTHESIS block is pre-stage, but TRIAGE NOTE AUDIT SCHEMA remains co-located. **FAIL**
- V-04: RUN-LEVEL RULE GLOSSARY + Synthesis cites `[RULE SYNTHESIS applies -- see glossary]`. **PASS**
- V-05: Glossary + standalone affirmative block + Synthesis cites both. **PASS**

**C-32** (Carry-Forward Structural Artifact):
- V-01: Stage format includes `### Carry Forward` block with Inertia ID column + `CARRY: NONE` zero-state. **PASS**
- V-02: RULE CARRY-FORWARD in glossary, but **stage format omits the `### Carry Forward` block** — only Phase Gate/Calibration/Findings/Verdict. **FAIL**
- V-03: Stage format: Phase Gate → Calibration → Findings → Verdict. No Carry Forward block. **FAIL**
- V-04: Stage format includes `### Carry Forward [RULE CARRY-FORWARD applies]` with Inertia ID column. **PASS**
- V-05: Same as V-04. **PASS**

**C-34** (Conditional-Item vs Condition-Enum Disambiguation):
- V-01: RULE CONDITIONAL-ITEM appears inline in Verdict template only — no explicit `[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]` annotation. **FAIL**
- V-02: Glossary has `RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]` plus Anti-pattern-2 calling out 1/2/3 vs (a)/(b)/(c) distinction explicitly. **PASS**
- V-03: No glossary; Verdict template only. **FAIL**
- V-04: Glossary has `RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]`. **PASS**
- V-05: Same as V-04. **PASS**

**C-35** (Audit Table Additive-Not-Replacement Constraint):
No variation declares `RULE AUDIT-TABLE` with an explicit "inserted above AUDIT RESULT block, not replacing it" constraint. The table and AUDIT RESULT block coexist in all variations, but the named additive rule is absent in every one. **FAIL across all five.**

**C-36** (Synthesis Positive-Artifact Subsection Schema):
- V-01: `"Its five required subsections are listed below"` followed by all 5 named. **PASS**
- V-02: Glossary RULE SYNTHESIS: `Required subsections (5 -- absence of any is VIOLATION-13): 1. BLOCKERS 2. CROSS-CUTTING THEMES SUMMARY 3. RESIDUAL OPEN ITEMS 4. DUAL-DIRECTION CHECK 5. INERTIA PRESSURE SUMMARY`. **PASS**
- V-03: Standalone RULE SYNTHESIS affirmative block enumerates all 5 with bold labels. **PASS**
- V-04: Glossary RULE SYNTHESIS with 5 subsections; INERTIA PRESSURE SUMMARY names both IB-01 and IB-02. **PASS**
- V-05: Both glossary entry + standalone affirmative block enumerate all 5. **PASS**

**C-37** (Dual Illustrative Baseline Examples):
- V-01: IB-01 (Technical Displacement) + IB-02 (Organizational Adoption) — distinct structural axes. **PASS**
- V-02: Single IB-01 only. **FAIL**
- V-03: IB-01 (Current Snapshot) + IB-02 (12-Month Projection) — temporal dimension split. **PASS**
- V-04: IB-01 (Technical) + IB-02 (Organizational). **PASS**
- V-05: IB-01 (Current) + IB-02 (Projected 12-month). **PASS**

---

## Composite Scores

| Criterion Block | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Essential (5 × 15) | 75 | 75 | 75 | 75 | 75 |
| Recommended (3 × 5) | 15 | 15 | 15 | 15 | 15 |
| C-09 to C-29 (21 × 5) | 105 | 105 | 105 | 105 | 105 |
| C-30 | 0 | 5 | 0 | 5 | 5 |
| C-31 | 5 | 5 | 5 | 5 | 5 |
| C-32 | 5 | 0 | 0 | 5 | 5 |
| C-33 | 5 | 5 | 5 | 5 | 5 |
| C-34 | 0 | 5 | 0 | 5 | 5 |
| C-35 | 0 | 0 | 0 | 0 | 0 |
| C-36 | 5 | 5 | 5 | 5 | 5 |
| C-37 | 5 | 0 | 5 | 5 | 5 |
| **TOTAL** | **220** | **220** | **215** | **230** | **230** |
| All essential pass | YES | YES | YES | YES | YES |

---

## Ranking

| Rank | Variation | Score | Fails |
|---|---|---|---|
| 1 (tie) | **V-04** | **230** | C-35 |
| 1 (tie) | **V-05** | **230** | C-35 |
| 3 (tie) | V-01 | 220 | C-30, C-34, C-35 |
| 3 (tie) | V-02 | 220 | C-32, C-35, C-37 |
| 5 | V-03 | 215 | C-30, C-32, C-34, C-35 |

---

## Excellence Signals — V-04 and V-05

Three structural patterns distinguish the 230-scoring variations from the 215–220 group:

**Signal 1 — RUN-LEVEL RULE GLOSSARY is a multi-criterion enabler, not documentation.**
V-01 and V-03 fail both C-30 and C-34 for the same root cause: no preamble glossary. The glossary is the structural prerequisite that simultaneously delivers C-30 (named schema at preamble scope with post-stage citation) and C-34 (disambiguation annotation at rule-declaration level). Neither can be satisfied inline in stage templates or section bodies. V-04/V-05 gain 10 pts over V-01/V-03 from this single structural decision.

**Signal 2 — Inertia ID column in CARRY FORWARD blocks closes the dual-baseline audit chain.**
V-04/V-05 carry blocks include `Inertia ID` column tagging each carried finding by IB-01/IB-02/both/N/A. This operationalizes dual-baseline traceability through the cross-stage handoff artifact — the TPM can assign risk register entries to the correct baseline without re-reading stage prose. The column is cost-free to implement but makes IB-01/IB-02 attribution structurally verifiable at the carry-block level.

**Signal 3 — Temporal IB-02 Urgency Verdict cascades into mandatory downstream citations (V-05).**
V-05's temporal framing creates a structural enforcement cascade absent in V-04's dimensional framing: when `Urgency Gradient = HIGH`, the Go/No-Go table must cite IB-02, at least one Risk Register entry must name delay-compounding as the inertia driver, and the Inertia Pressure Summary must name the compounding path explicitly. Each downstream section is constrained by the IB-02 Urgency Gradient value — delay-cost analysis is not additive documentation but a verdict-shaping input.

**Persistent gap — C-35 fails universally.**
No R11 variation declares `RULE AUDIT-TABLE` with an explicit additive constraint ("inserted above AUDIT RESULT block, not replacing it"). All five variations have tables coexisting with AUDIT RESULT blocks, but the named constraint is absent in every prompt body. C-35 remains a hard target for R12.

---

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["RUN-LEVEL RULE GLOSSARY is a multi-criterion structural enabler: simultaneously satisfies C-30 (preamble schema with named post-stage reference) and C-34 (CONDITIONAL-ITEM vs CONDITION-ENUM disambiguation annotation) -- variations without a glossary lose both criteria regardless of other compliance", "Temporal IB-02 Urgency Gradient cascades into mandatory downstream citations: when HIGH, Go/No-Go must cite IB-02 and Risk Register must include a delay-compounding entry -- making delay-cost analysis a verdict-shaping constraint rather than additive documentation", "Inertia ID column in CARRY FORWARD blocks closes dual-baseline audit chain structurally: each carried finding is tagged IB-01/IB-02/both/N/A at the carry block level, enabling TPM risk register assignment without re-reading stage prose"]}
```
