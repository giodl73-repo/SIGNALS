## Scorecard — trace-permissions R1

### Rubric Reference

| Criterion | Tier | Max |
|-----------|------|-----|
| C-01 Role-Operation Matrix | Essential | 15 |
| C-02 Field-Level Security Per Role | Essential | 15 |
| C-03 Record Access Scope | Essential | 15 |
| C-04 At Least One Gap Identified | Essential | 15 |
| C-05 Privilege Escalation Path | Recommended | 10 |
| C-06 Sharing Rule Conflict | Recommended | 10 |
| C-07 Team Membership Gap | Recommended | 10 |
| C-08 Risk-Ranked Gap Summary | Aspirational | 5 |
| C-09 Remediation Per Gap | Aspirational | 5 |

---

### V-01 — Security Expert Leads

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | ROLE-OPERATION MATRIX section with full table; "Do not skip any operation" instruction; Y/Y\*/N format with restrictions block |
| C-02 | PASS | FIELD-LEVEL SECURITY table: field \| role \| read \| write; "Writing 'FLS should be configured' without naming fields and roles fails"; FLS gaps subsection |
| C-03 | PASS | RECORD ACCESS SCOPE table uses Own/BU/Parent BU/Org vocabulary; explicit anti-conflation instruction; per-record-type rows permitted |
| C-04 | PASS | GAP SUMMARY section: "At least one row is required — a trace with zero gaps fails." Additionally, mandatory PRIVILEGE ESCALATION and SHARING RULE CONFLICTS sections structurally guarantee gap content flows into summary |
| C-05 | PASS | Dedicated PRIVILEGE ESCALATION PATHS section; From role → Mechanism → Unintended access → Evidence template; four-vector checklist (reassignment, team promotion, sharing bypass, impersonation); "None identified" requires explicit justification |
| C-06 | PASS | Dedicated SHARING RULE CONFLICTS section; Rule \| Baseline scope \| Sharing grants \| Conflict narrative; "None identified" requires listing rules examined |
| C-07 | PASS | CUSTOMER SERVICE: TEAM MEMBERSHIP GAPS section; Gap 1 template; both missing-membership and over-combined types covered; "None identified" requires justification |
| C-08 | PASS | GAP SUMMARY table has Risk column (H/M/L); "one-line justification" row is implied by table structure |
| C-09 | PASS | REMEDIATION table maps by gap name; specificity example provided; "Tighten security" explicitly excluded |

**Weakness:** CS section runs second; model may rush through team membership after completing SE analysis. C-04 is guaranteed by GAP SUMMARY but the path to it runs through expert-first framing, creating mild description-before-gap risk.

**Score: 98/100** (C-04 execution reliability: strong; C-07 execution reliability: moderate — CS placed second)

---

### V-02 — Full Table-Matrix

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | TABLE 1: ROLE-OPERATION MATRIX; "Do not leave any cell blank"; R = restricted with mandatory restrictions row |
| C-02 | PASS | TABLE 2: FIELD-LEVEL SECURITY; per-role read/write columns; FLS gaps subsection requires naming field and role |
| C-03 | PASS | TABLE 3: RECORD ACCESS SCOPE; "Correct for Role?" column surfaces misconfigurations; anti-conflation instruction |
| C-04 | PASS | TABLE 4: SECURITY GAPS; "This table must contain at least one row. A permissions trace with zero gaps identified is not a valid output." Strongest single-criterion structural guarantee in R1 |
| C-05 | PARTIAL | TABLE 4 includes "Escalation" as gap type and "Named Path / Conflict / Missing Control" column forces mechanism naming — but no dedicated escalation section, no four-vector checklist, no systematic checking across reassignment/team promotion/sharing/impersonation. Model names one path if it thinks of one; does not systematically hunt |
| C-06 | PARTIAL | TABLE 4 includes "Sharing" as gap type — but no dedicated sharing rule examination section. No prompt to check criteria-based, owner-based, or manual sharing rules independently. Model includes a sharing row only if it happens to identify one |
| C-07 | PARTIAL | TABLE 4 includes "Team" as gap type; SETUP has "Teams found" field — but no dedicated CS team membership section. No "minimum one row" for team gaps specifically. CS perspective absent |
| C-08 | PASS | TABLE 4 has Risk column (H/M/L); "Risk justification (one line per row)" block beneath table; defensible rating required |
| C-09 | PASS | TABLE 5: REMEDIATION maps by gap number; specificity example present; "Tighten security or review permissions does not pass" |

**Strength:** TABLE 4 with "minimum one row" is the most structurally unambiguous C-04 guarantee in R1. Blank cell is visually obvious; table cannot be omitted.

**Weakness:** C-05/C-06/C-07 are merged into TABLE 4 type columns rather than dedicated sections. No CS reviewer role. Systematic examination of each gap type is not prompted — model captures what it thinks of, not what it checked.

**Score: 88/100**

---

### V-03 — Gap-First Framing

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | EVIDENCE: ROLE-OPERATION MATRIX table with H-link column; matrix flags subsection for cells that confirm/refute hypotheses |
| C-02 | PASS | EVIDENCE: FIELD-LEVEL SECURITY table with H-link; FLS flags subsection explicitly ties entries to H2; "should be configured" language explicitly fails the section |
| C-03 | PASS | EVIDENCE: RECORD ACCESS SCOPE table; scope flags subsection; "Own/BU/Parent BU/Org" hierarchy required |
| C-04 | PASS | FINDINGS section is mandatory and precedes REMEDIATION; "Minimum one finding"; each finding must reference an evidence table and address a hypothesis; gap-first preamble frames the entire prompt as problem-finding; "a trace that describes the model without identifying at least one real gap fails" |
| C-05 | PASS | H1 is explicitly defined as escalation hypothesis ("Where a user is likely able to gain access beyond their intended scope, and the mechanism"). FINDINGS must address H1. Hypothesis pre-commitment forces escalation to be a named finding, not an afterthought |
| C-06 | PARTIAL | Opening says "What does a sharing rule grant that the security role should prevent?" — but this is preamble, not structural. No dedicated sharing rule evidence section. H1 could be satisfied by record reassignment (not sharing rules). Model may not examine sharing rules if H1 frames an escalation via a different mechanism |
| C-07 | PASS | H3 is explicitly defined as team membership hypothesis. FINDINGS must address H3 or explicitly refute it with justification. Structural guarantee comparable to dedicated section |
| C-08 | PASS | Dedicated RISK RANKING section; "one-line justification per finding"; "ranking must be defensible — reference the operation type or data sensitivity" |
| C-09 | PASS | REMEDIATION table maps by finding; specificity example present; "Tighten security or improve FLS does not pass — name the exact change: which field, which role, which configuration setting" |

**Strength:** Hypothesis pre-commitment makes C-04 the starting frame. Model commits to expected gaps before evidence gathering, which improves C-05 and C-07 specificity. FINDINGS must resolve each hypothesis — prevents vague gap descriptions.

**Weakness:** C-06 is the single structural gap. No dedicated sharing rule examination section. H1 may resolve through a non-sharing-rule escalation mechanism, leaving sharing rules unexamined.

**Score: 96/100**

---

### V-04 — Customer Service Leads + Full Tables

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | CS-1 ROLE-OPERATION MATRIX with CS Flag column; "Complete every cell"; CS Observations subsection for anomaly description |
| C-02 | PASS | SE-3: FIELD-LEVEL SECURITY AUDIT table with FLS Gap? column; "Complete every cell"; naming requirement explicit |
| C-03 | PASS | SE-4: RECORD ACCESS SCOPE; "Do not conflate role privileges with record ownership"; Correct? column surfaces misconfigurations |
| C-04 | PASS | CONSOLIDATED GAP SUMMARY: "At least one row required — a trace with zero gaps fails." CS Observations (CS-1) flags anomalies early, before SE deepening. Two-stage gap surfacing: CS flags → SE deepens → consolidated table |
| C-05 | PASS | SE-5: PRIVILEGE ESCALATION PATHS as a dedicated table with Path \# \| From Role \| Mechanism \| Unintended Access Gained columns. "Name the path. Do not assert escalation without naming the mechanism." Vectors checklist present |
| C-06 | PASS | SE-6: SHARING RULE CONFLICTS as a dedicated table with Rule \| Role \| Baseline Scope \| Sharing Grants \| Conflict Type. "None identified" requires listing rules examined |
| C-07 | PASS | CS-2: TEAM MEMBERSHIP GAPS as a dedicated table; "Minimum one row"; CS-first ordering means team gaps surface before technical analysis; both missing-membership and over-combined types captured |
| C-08 | PASS | CONSOLIDATED GAP SUMMARY table has Risk + Justification columns; one-line justification required per row |
| C-09 | PASS | REMEDIATION table maps by gap number; specificity example present; "Tighten security does not pass" |

**Strength:** CS-first ordering surfaces practical C-07 gaps early and makes C-04 concrete through operational framing before SE deepens with technical C-05/C-06 analysis. All recommended criteria have dedicated sub-sections with structured tables.

**Weakness:** No hypothesis pre-commitment — model may produce accurate gap descriptions without the depth that comes from committing to expected gaps in advance. C-04 specificity relies on CS flags rather than hypothesis anchoring.

**Score: 100/100**

---

### V-05 — Full Synthesis (All Three Axes)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | CS ROLE-OPERATION MATRIX with CS Flags; restrictions block; same structural quality as V-04 plus H-link for anomalies tied to hypotheses |
| C-02 | PASS | SE FLS AUDIT table with FLS Gap? column and H-link column; H2 hypothesis pre-commits to a specific field/role expectation before evidence is gathered |
| C-03 | PASS | SE RECORD ACCESS SCOPE table with H-link; scope misconfigurations flagged against H1/H3 |
| C-04 | PASS | Three independent structural mechanisms: (1) GAP HYPOTHESIS section before analysis — model commits to expected gap categories; (2) CS Flags in role-op matrix surface anomalies at data layer; (3) CONSOLIDATED FINDINGS: "This section must have at least one row — a trace with no findings fails" + hypothesis resolution summary requires every finding to name a gap and resolve an H |
| C-05 | PASS | SE PRIVILEGE ESCALATION PATHS table H1-linked; H1 is explicitly defined as escalation; table columns force mechanism + unintended access naming; hypothesis pre-commitment means escalation specificity is anchored before evidence |
| C-06 | PASS | SE SHARING RULE CONFLICTS as dedicated table; no H assigned to H1 by default, but SE section prompts dedicated examination; same dedicated structure as V-04 |
| C-07 | PASS | CS TEAM MEMBERSHIP GAPS table H3-linked; "Minimum one row. 'None identified' requires explicit justification of what was checked"; CS-first ensures this surfaces before SE analysis |
| C-08 | PASS | CONSOLIDATED FINDINGS table embeds Risk + Justification per row; HYPOTHESIS RESOLUTION SUMMARY requires H1/H2/H3 resolution — prevents generic risk statements that don't reference the operation or data sensitivity |
| C-09 | PASS | REMEDIATION table maps by finding number; specificity example present; "Tighten security does not pass — name the exact change: which field, which role, which configuration setting, which team" (most complete exclusion list in R1) |

**Strength:** Three independent C-04 mechanisms. H-link columns connect every evidence cell and every finding to a pre-stated hypothesis — this is the deepest traceability structure in R1. Hypothesis resolution summary prevents the model from leaving hypotheses dangling. CS-first + hypothesis pre-commitment produces the highest expected gap specificity.

**Weakness:** Template is the longest and most complex. Model may introduce H-links mechanically rather than substantively. Execution quality is highest but execution risk (model skipping H-resolution steps) is also highest.

**Score: 100/100**

---

### Ranking

| Rank | Variation | Score | All Essential Pass | Differentiator |
|------|-----------|-------|--------------------|----------------|
| 1 | V-05 | 100 | Yes | All three axes; H-link traceability; highest C-04 execution reliability |
| 1 | V-04 | 100 | Yes | CS-first + full tables; dedicated sections for all criteria; no template overhead |
| 3 | V-01 | 98 | Yes | All dedicated sections; slight execution risk on C-07 (CS second) and C-04 (expert-first framing may delay gap naming) |
| 4 | V-03 | 96 | Yes | Hypothesis anchoring; strong C-05/C-07 via H1/H3; C-06 structurally unguaranteed |
| 5 | V-02 | 88 | Yes | Strongest single-criterion C-04 guarantee; C-05/C-06/C-07 PARTIAL — no dedicated sections, no CS role |

---

### Excellence Signals from Top-Scoring Variations

**1. Dual-role convergence into a single consolidated table (V-04, V-05)**
CS and SE each fill dedicated sub-sections with separate structural requirements, then merge into a CONSOLIDATED GAP SUMMARY. This creates natural cross-validation: CS surfaces operational gaps the SE might not notice (record-visibility failures, team membership); SE surfaces technical gaps the CS might not articulate (privilege escalation mechanics, sharing rule widening). The merge step forces both perspectives into a single ranked output rather than two parallel summaries.

**2. H-link column embedded in evidence tables (V-05)**
Rather than cross-referencing findings to hypotheses in prose, V-05 embeds an H-link column directly in each evidence table (role-op matrix, FLS, scope, escalation, sharing rule). This means traceability is enforced at the data layer: every cell that confirms or refutes a hypothesis is marked at collection time, not retroactively at finding time. The hypothesis resolution summary then closes the loop. This pattern has not appeared in any prior R1 skill variation.

**3. CS Flag column in the role-operation matrix (V-04, V-05)**
Adding an anomaly-detection column to the role-operation matrix itself — not a separate observations section — surfaces C-04 evidence at the data layer before findings are written. The flag column prompts the model to mark anomalies as it fills in permissions, creating a structured audit trail. Previous skills have used "observations" sections after tables; this pattern embeds flagging into the table itself.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["dual-role convergence into consolidated table: CS and SE fill separate structured sections then merge into single ranked gap summary, creating cross-validation between operational and technical perspectives", "H-link column embedded in evidence tables: hypothesis references encoded as a column in each data table at collection time, not cross-referenced retroactively in findings prose", "CS Flag column in role-operation matrix: anomaly detection embedded as a column in the permission matrix itself, surfacing C-04 evidence at the data layer before findings are written"]}
```
