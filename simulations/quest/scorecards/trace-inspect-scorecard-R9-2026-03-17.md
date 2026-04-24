Now I have all five variations fully read. Let me score them.

---

# trace-inspect — Round 9 Scorecard (Rubric v5)

**Skill**: `trace-inspect`
**Rubric**: v5 (C-01–C-21; grand total 99.5 pts)
**Entry state**: R8 champion ~98/99.5. All essential + recommended PASS. C-19, C-20, C-21 each FAIL (0.5 pts each gap = 1.5 pts missing).

---

## Scoring Reference

| Block | Criteria | Weight |
|---|---|---|
| Essential | C-01–C-05 | Pass/fail prerequisite; single FAIL = non-golden |
| Recommended | C-06–C-08 | Degrade quality if failed |
| Aspirational | C-09, C-10 | 2 pts each |
| Aspirational | C-11–C-21 | 0.5 pts each (11 × 0.5 = 5.5 pts) |
| **Total aspirational** | C-09–C-21 | **9.5 pts** |

All variants inherit the R8 champion architecture. Base score for any R9 variant that adds nothing new = 98/99.5 (C-09–C-18 all PASS; C-19, C-20, C-21 all FAIL).

---

## V-01 — Single axis: C-19 (EG-first structural role ordering)

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 Phase completeness | PASS | All four phases present. Phase 1 Setup, Phase 2a (EG roles) + Phase 2b (SA/SG roles), Phase 3 all sub-steps, Phase 4 Amend, Phase 5 Verdict. Structurally closed. |
| C-02 Artifact produced | PASS | Artifact write declared in Phase 2b: `simulations/trace/skill/{topic}-skill-trace-{date}.md`. |
| C-03 Schema 1+2 compliance | PASS | Schema 1 {P1,P2,P3} and Schema 2 {SA,SG,EG,QO} declared in Coverage Matrix; label lock invariant stated. |
| C-04 Enforcement gates checked | PASS | G-1, G-2, G-3 with explicit PASS/FAIL at Step 3c; GATE CLEARANCE SUMMARY block present. |
| C-05 Verdict present and classified | PASS | Verdict section includes all three classification rules (NEEDS-SPEC-REVISION / NEEDS-REDESIGN / USEFUL) with rationale field. |

**All essential: PASS**

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 SA-TO-SG promotion evaluated | PASS | SA-TO-SG PROMOTION lifecycle event present with per-gap evaluation format; requires EG-RELAY COMPLETE PASS as structural prerequisite. |
| C-07 Per-role relays complete | PASS | Phase 2a relay template includes all required fields: Received from, Received values, Schema 2 compliance, SA/SG gaps, Produced, EG gaps. |
| C-08 Findings table depth | PASS | FLOOR CHECK requires >=3 rows, >=2 Source types, action-uniqueness check with named Finding IDs. |

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-09 (2 pts) | PASS | VC-1–VC-5 compliance ledger present with specific Observed behavior cell instructions; "as expected" invalidated. |
| C-10 (2 pts) | PASS | Schema 5 transition sentences at each sub-step boundary (e.g., "Schema 5 transition: Step 3a complete. Step 3b is valid to begin."). |
| C-11 (0.5) | PASS | GATE CLEARANCE SUMMARY structural block before Step 3d; PHASE 4 GATE CLEARANCE SUMMARY at Phase 4 entry. |
| C-12 (0.5) | PASS | REMEDIATION LOG required if any gate FAILs; C-12 EXEMPTION clause if all pass on first evaluation. |
| C-13 (0.5) | PASS | Schema 5 prerequisite verification lines at each step entry (e.g., "Schema 5 prerequisite: Step 3a complete."). |
| C-14 (0.5) | PASS | STEP 3b FLOOR CHECK positioned at end of Step 3b, before Step 3c can begin. |
| C-15 (0.5) | PASS | Layer diversity PASS/FAIL declared at end of Stage 1. |
| C-16 (0.5) | PASS | SA-TO-SG PROMOTION section: "Promotion decisions may cite observed execution evidence from Phase 2a relays." Architectural EG-evidence grounding present. |
| C-17 (0.5) | PASS | VC-4 G-1 cross-role row includes "list Source types present and which roles contributed each" in Observed behavior. |
| C-18 (0.5) | PASS | Verdict section lists all three classification rules with trigger condition before verdict field. |
| **C-19 (0.5)** | **PASS** | EG-FIRST EXECUTION CONSTRAINT block after Role-Schema Binding Summary. Phase 2a (EG roles only) → EG-RELAY COMPLETE checkpoint → SA-TO-SG PROMOTION → Phase 2b. Structural invariant: "SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes." Violation is architecturally impossible, not instructionally discouraged. |
| **C-20 (0.5)** | **FAIL** | No CRITERION INHERITANCE REGISTRY block. No per-criterion enumeration of inherited criteria. Silence about prior versions. |
| **C-21 (0.5)** | **FAIL** | VC-4 G-1 row uses standard text: "list Source types present and which roles contributed each." No pre-printed sub-table embedded in the row cell. |

**V-01 composite**: 98 (base) + 0.5 (C-19) = **98.5 / 99.5**

---

## V-02 — Single axis: C-20 (Criterion inheritance registry)

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four phases structurally present. |
| C-02 | PASS | Artifact write at `simulations/trace/skill/{topic}-skill-trace-{date}.md` in Phase 2 Execute. |
| C-03 | PASS | Schema 1+2 declared; label lock invariant stated. |
| C-04 | PASS | G-1/G-2/G-3 with GATE CLEARANCE SUMMARY block. |
| C-05 | PASS | Three-way verdict with classification rules and rationale. |

**All essential: PASS**

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | SA-TO-SG PROMOTION section present with per-gap format. |
| C-07 | PASS | Phase 2 Execute relay template has all required fields. |
| C-08 | PASS | FLOOR CHECK with >=3 rows, >=2 Source types, named IDs. |

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-09 (2 pts) | PASS | Full VC ledger with specific Observed behavior instructions. |
| C-10 (2 pts) | PASS | Schema 5 transition sentences at all sub-step boundaries. |
| C-11 (0.5) | PASS | GATE CLEARANCE SUMMARY + PHASE 4 GATE CLEARANCE SUMMARY present. |
| C-12 (0.5) | PASS | REMEDIATION LOG + C-12 EXEMPTION clause present. |
| C-13 (0.5) | PASS | Schema 5 prerequisite verification at each sub-step. |
| C-14 (0.5) | PASS | FLOOR CHECK at Step 3b before Step 3c entry. |
| C-15 (0.5) | PASS | Layer diversity PASS/FAIL in Stage 1 audit block; inertia note: "without a structured Stage 1, a developer reads the spec once and guesses." |
| C-16 (0.5) | PASS | SA-TO-SG PROMOTION section present with reason field; base R8 evidence-grounding intact. |
| C-17 (0.5) | PASS | VC-4 G-1 cross-role row requests Source types + contributing roles. |
| C-18 (0.5) | PASS | Three-way classification rules stated before verdict field. |
| **C-19 (0.5)** | **FAIL** | Standard Phase 2 Execute — no EG-FIRST EXECUTION CONSTRAINT block, no Phase 2a/2b split, no EG-RELAY COMPLETE gate. SA-TO-SG PROMOTION at Stage 2 open, before Execute begins. |
| **C-20 (0.5)** | **PASS** | CRITERION INHERITANCE REGISTRY block at prompt top. Enumerates C-01–C-18 by ID with version of origin and INHERITED status. C-19/C-20/C-21 labeled NEW with mechanism description. INERTIA COMPETITOR block (5 items) grounds the skill purpose. |
| **C-21 (0.5)** | **FAIL** | Standard VC-4 G-1 row. Attribution requires "Source types and contributing roles" but as plain text; no pre-printed sub-table embedded in the cell. |

**V-02 composite**: 98 (base) + 0.5 (C-20) = **98.5 / 99.5**

---

## V-03 — Single axis: C-21 (Attribution table co-located in VC-4 G-1 row)

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All four phases present and structurally closed. |
| C-02 | PASS | Artifact write declared. |
| C-03 | PASS | Schema 1+2 declared; label lock stated. |
| C-04 | PASS | G-1/G-2/G-3 explicit; GATE CLEARANCE SUMMARY present. |
| C-05 | PASS | Three-way verdict with classification rules. |

**All essential: PASS**

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | SA-TO-SG PROMOTION with per-gap evaluation. |
| C-07 | PASS | Full relay template with Schema 2 compliance field. |
| C-08 | PASS | FLOOR CHECK with >=3 rows, >=2 Source types, named IDs. |

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-09 (2 pts) | PASS | VC compliance ledger present; "as expected" explicitly invalidated. |
| C-10 (2 pts) | PASS | Schema 5 transition sentences at all sub-step boundaries. |
| C-11 (0.5) | PASS | GATE CLEARANCE SUMMARY + PHASE 4 GATE CLEARANCE SUMMARY. |
| C-12 (0.5) | PASS | REMEDIATION LOG + C-12 EXEMPTION. |
| C-13 (0.5) | PASS | Schema 5 prerequisite verification lines. |
| C-14 (0.5) | PASS | FLOOR CHECK at Step 3b, gating Step 3c. |
| C-15 (0.5) | PASS | Layer diversity declared. |
| C-16 (0.5) | PASS | Base R8 evidence-grounding present in SA-TO-SG PROMOTION. |
| C-17 (0.5) | PASS | C-17 attribution satisfied by the co-located sub-table itself; C-21 subsumes and satisfies C-17. |
| C-18 (0.5) | PASS | Three-way classification rules before verdict field. |
| **C-19 (0.5)** | **FAIL** | Standard Phase 2 Execute; no EG-first structural split. |
| **C-20 (0.5)** | **FAIL** | No inheritance registry; no per-criterion enumeration. |
| **C-21 (0.5)** | **PASS** | VC-4 G-1 row labeled "C-21 CO-LOCATED ATTRIBUTION." Observed behavior cell contains pre-printed G-1 SOURCE ATTRIBUTION TABLE (3 columns: Source type / Role(s) that contributed / Finding IDs) with explicit constraint: "this cell is not complete until the sub-table below is filled." Filling ledger row and attribution are a single write operation; they cannot drift. |

**V-03 composite**: 98 (base) + 0.5 (C-21) = **98.5 / 99.5**

---

## V-04 — Combined: C-19 + C-20 (EG-first ordering + inheritance registry)

### Essential Criteria

All five PASS. Combines V-01 (Phase 2a/2b split with EG-RELAY COMPLETE gate) and V-02 (CRITERION INHERITANCE REGISTRY at top). Independent mechanisms — no structural conflict.

### Recommended Criteria

All three PASS. Both mechanisms preserve base relay template, promotion evaluation, and FLOOR CHECK structure.

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-09 (2 pts) | PASS | Full VC ledger; "as expected" invalidated. |
| C-10 (2 pts) | PASS | Schema 5 transitions at all sub-step boundaries. |
| C-11 (0.5) | PASS | GATE CLEARANCE SUMMARY + PHASE 4 GATE CLEARANCE SUMMARY. |
| C-12 (0.5) | PASS | REMEDIATION LOG + C-12 EXEMPTION. |
| C-13 (0.5) | PASS | Schema 5 prerequisite verification. |
| C-14 (0.5) | PASS | FLOOR CHECK placement. |
| C-15 (0.5) | PASS | Layer diversity declared. |
| C-16 (0.5) | PASS | VC-2 SA-TO-SG row requires "EG-RELAY COMPLETE PASS cited as prerequisite" — architectural evidence grounding stronger than base R8. |
| C-17 (0.5) | PASS | VC-4 G-1 row requests Source types and contributing roles per phase. |
| C-18 (0.5) | PASS | Three-way classification rules before verdict. |
| **C-19 (0.5)** | **PASS** | EG-FIRST EXECUTION CONSTRAINT block + Phase 2a/2b + EG-RELAY COMPLETE gate. SA-TO-SG PROMOTION structurally BLOCKED until PASS. Registry explicitly notes: "enforced via EG-FIRST EXECUTION CONSTRAINT." |
| **C-20 (0.5)** | **PASS** | CRITERION INHERITANCE REGISTRY enumerates C-01–C-18 as INHERITED with version of origin; C-19/C-20/C-21 as NEW with mechanism notes. C-21 explicitly noted as "deferred to V-05." INERTIA COMPETITOR (5 items) present. |
| **C-21 (0.5)** | **FAIL** | V-04 explicitly defers C-21 to V-05. VC-4 G-1 row is standard — no embedded attribution sub-table. |

**V-04 composite**: 98 (base) + 0.5 (C-19) + 0.5 (C-20) = **99.0 / 99.5**

---

## V-05 — Combined: C-19 + C-20 + C-21 (full integration)

### Essential Criteria

All five PASS. All R8 essential mechanisms intact. Three new mechanisms are structurally independent and do not interfere.

### Recommended Criteria

All three PASS. Per-role relay templates, FLOOR CHECK, SA-TO-SG promotion all fully specified.

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-09 (2 pts) | PASS | VC compliance ledger present; "as expected" structurally invalid; all five VC overall results declared. |
| C-10 (2 pts) | PASS | Schema 5 transition sentences at every sub-step boundary; Step 3a/3b/3c/3d transitions explicit (e.g., "Schema 5 transition: Step 3a complete. Step 3b is valid to begin."). |
| C-11 (0.5) | PASS | GATE CLEARANCE SUMMARY structural block before Step 3d; PHASE 4 GATE CLEARANCE SUMMARY at Phase 4 entry. |
| C-12 (0.5) | PASS | REMEDIATION LOG required on gate failure; C-12 EXEMPTION clause for first-evaluation pass. |
| C-13 (0.5) | PASS | Schema 5 prerequisite and output lines at each sub-step entry (e.g., "Schema 5 prerequisite: Step 3a complete. Schema 5 output: merged findings table + FLOOR CHECK PASS"). |
| C-14 (0.5) | PASS | STEP 3b FLOOR CHECK positioned as required structural output of Step 3b, gating Step 3c entry. |
| C-15 (0.5) | PASS | Layer diversity PASS/FAIL at Stage 1 close; instruction to examine all three layers before declaring done. |
| C-16 (0.5) | PASS | SA-TO-SG PROMOTION: "Promotion decisions cite Phase 2a execution evidence where available." VC-2 compliance row requires "EG-RELAY COMPLETE PASS confirmed as prerequisite." Evidence-grounded promotion architecturally enforced. |
| C-17 (0.5) | PASS | Attribution satisfied by co-located sub-table in VC-4 G-1 row (C-21 mechanism). Registry entry documents: "co-located with VC-4 G-1 row per C-21." |
| C-18 (0.5) | PASS | Three-way verdict classification rules with trigger condition stated before verdict field. |
| **C-19 (0.5)** | **PASS** | EG-FIRST EXECUTION CONSTRAINT block; Phase 2a (EG roles only) → EG-RELAY COMPLETE → SA-TO-SG PROMOTION → Phase 2b. EG-RELAY COMPLETE checkpoint inside Phase 2a states "SA-TO-SG PROMOTION now valid" only on PASS. Constraint ends: "Evidence-grounded promotion is architecturally enforced, not merely recommended." |
| **C-20 (0.5)** | **PASS** | CRITERION INHERITANCE REGISTRY enumerates all 21 criteria by ID with version of origin. C-19/C-20/C-21 entries annotated with inline mechanism description (e.g., C-19: "enforced via EG-FIRST EXECUTION CONSTRAINT and EG-RELAY COMPLETE gate; SA-TO-SG PROMOTION structurally blocked until PASS"). INERTIA COMPETITOR block (6 items, strongest version). |
| **C-21 (0.5)** | **PASS** | VC-4 G-1 row labeled "C-21 CO-LOCATED ATTRIBUTION." Observed behavior cell pre-prints G-1 SOURCE ATTRIBUTION TABLE (4 columns: Source type / Phase / Role(s) / Finding IDs). Cell declares: "This cell is not complete until the G-1 SOURCE ATTRIBUTION TABLE below is filled." Filling ledger and attribution are one operation; structural drift impossible. Phase column (absent in V-03) ties attribution evidence back to Phase 2a/2b execution split. |

**V-05 composite**: 98 (base) + 0.5 (C-19) + 0.5 (C-20) + 0.5 (C-21) = **99.5 / 99.5**

---

## Rankings

| Rank | Variation | Score | C-19 | C-20 | C-21 | All Essential |
|------|-----------|-------|------|------|------|---------------|
| 1 | V-05 | 99.5 / 99.5 | PASS | PASS | PASS | YES |
| 2 | V-04 | 99.0 / 99.5 | PASS | PASS | FAIL | YES |
| 3 (tie) | V-01 | 98.5 / 99.5 | PASS | FAIL | FAIL | YES |
| 3 (tie) | V-02 | 98.5 / 99.5 | FAIL | PASS | FAIL | YES |
| 3 (tie) | V-03 | 98.5 / 99.5 | FAIL | FAIL | PASS | YES |

---

## Excellence Signals from V-05

V-05 achieves 99.5/99.5 — the first perfect score. Three signals explain why it outperforms V-04 (the nearest competitor) and represents something beyond closing the three 0.5-pt gaps:

**Signal 1: Phase column in attribution sub-table creates architectural cross-reference between C-19 and C-21.**
V-05's G-1 SOURCE ATTRIBUTION TABLE includes a Phase column (2a/2b) absent in V-03's version. This means the attribution evidence explicitly records which execution phase produced each source type — directly linking the attribution completeness check back to the Phase 2a/2b split mandated by C-19. The two new mechanisms reinforce each other: EG-first ordering gives the Phase structure; the Phase column in the attribution table audits that the EG relay structure actually produced the claimed source coverage. No single-axis variant captures this: V-01 has the Phase split without the attribution column; V-03 has attribution without the Phase column.

**Signal 2: Registry entries annotated with mechanical satisfaction — the registry becomes executable documentation.**
V-05's inheritance registry entries for new criteria include inline mechanism descriptions, not just "NEW." C-19 entry: "enforced via EG-FIRST EXECUTION CONSTRAINT and EG-RELAY COMPLETE gate; SA-TO-SG PROMOTION structurally blocked until PASS." C-21 entry: "C-17 table embedded directly in VC-4 G-1 cross-role row; filling ledger and attribution are one operation." This transforms the registry from a checklist into a compact specification of how each criterion is implemented. A future version auditing the registry can verify not just that a criterion exists but how it's satisfied — and whether a change to the prompt has broken the mechanism. V-02 and V-04 list criteria by ID and status; V-05 adds the mechanism, creating what amounts to a self-documenting implementation map.

**Signal 3: Structural vs instructional distinction statement in EG-FIRST block.**
V-05 ends its EG-FIRST EXECUTION CONSTRAINT block with: "Evidence-grounded promotion is architecturally enforced, not merely recommended." This explicit structural-vs-instructional distinction marker does not appear in V-01 or V-04. The statement surfaces the design intent behind C-19 directly in the prompt body — a model executing the prompt reads the constraint and the reason why the constraint exists in the same block. This is a tighter form of C-16 (evidence-grounded promotion citation) than merely requiring evidence to be cited: it declares the mechanism's categorical property.

---

```json
{"top_score": 99.5, "all_essential_pass": true, "new_patterns": ["Phase column in G-1 SOURCE ATTRIBUTION TABLE ties attribution evidence to Phase 2a/2b execution split, creating architectural cross-reference between EG-first ordering (C-19) and co-located attribution (C-21) that neither single-axis variant captures", "Inheritance registry entries annotated with inline mechanism descriptions transform the registry from a criterion checklist into executable documentation — each entry names not just the criterion ID but how it is mechanically satisfied in this version", "Structural-vs-instructional distinction statement at end of EG-FIRST EXECUTION CONSTRAINT block explicitly marks architectural enforcement as categorically different from instructional guidance, surfacing design intent in the prompt body"]}
```
