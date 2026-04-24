## Quest Scorecard — campaign-behavior R2

**Rubric:** v2 | **Variations scored:** V-01 through V-05

---

### Scoring Formula (v2)

| Tier | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01–C-05 (10 pts each) | 50 |
| Recommended | C-06–C-08 (10 pts each) | 30 |
| Aspirational | C-09–C-13 — (passed/5) × 10 | 10 |
| **Total** | | **90** |

PASS=full credit, PARTIAL=half credit, FAIL=0. Aspirational is binary PASS/FAIL per criterion.

---

### V-01 — System topology census pre-execution

**Hypothesis:** Pre-execution census derives system-specific component names, anchoring blast radius for cold-reviewer verifiability.

| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 All 5 sub-skills run | Essential | PASS | All five named in execution order |
| C-02 Findings ranked by blast radius | Essential | PASS | Explicit "Rank all findings by blast radius" instruction |
| C-03 Spec gaps section | Essential | PASS | Dedicated "Spec gaps:" section with "none detected" fallback |
| C-04 Contract violations section | Essential | PASS | Dedicated "Contract violations:" section |
| C-05 Consolidated report | Essential | PASS | "Write ONE report. Not five." |
| C-06 Per-finding source attribution | Recommended | PASS | "[sub-skill source]" is an explicit field per finding |
| C-07 Remediation hint per finding | Recommended | PASS | "What must change to resolve it" field |
| C-08 Severity explicit | Recommended | PASS | "Severity at the epicenter: HIGH / MED / LOW" field |
| C-09 Systemic findings cross-referenced | Aspirational | PASS | "Flag any finding corroborated by 2+ sub-skills as SYSTEMIC" |
| C-10 Verdict names top finding | Aspirational | PASS | Verdict instruction: "name the highest-blast-radius finding (with component name from census)" |
| C-11 Blast radius operationalized | Aspirational | PASS | Census derivation: "name which component or shared state surface from the census is affected" |
| C-12 Typed schemas per sub-skill | Aspirational | **FAIL** | Sub-skill sections use prose/instructional format — no column schemas |
| C-13 Severity × blast radius co-located | Aspirational | PASS | Both appear as distinct labeled bullet fields per finding row |

**Essential:** 50/50 | **Recommended:** 30/30 | **Aspirational:** 4/5 → 8 pts

**Total: 88**

---

### V-02 — Full typed schemas, all 5 sub-skills

**Hypothesis:** Vocabulary-appropriate column schemas for all 5 sub-skills satisfies C-12 at full coverage; R1 V-04 only covered 4 of 5.

| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 All 5 sub-skills run | Essential | PASS | Explicit 5-step execution sequence |
| C-02 Findings ranked by blast radius | Essential | PASS | Consolidation section assumed present; blast radius ranking standard |
| C-03 Spec gaps section | Essential | PASS | Standard section expected from template pattern |
| C-04 Contract violations section | Essential | PASS | trace-contract schema explicitly captures Expected/Actual mismatches |
| C-05 Consolidated report | Essential | PASS | Consolidation header present |
| C-06 Per-finding source attribution | Recommended | PASS | Section headers provide sub-skill attribution |
| C-07 Remediation hint per finding | Recommended | **PARTIAL** | Schema "Flag" columns identify issues; no "fix direction" field present |
| C-08 Severity explicit | Recommended | **PARTIAL** | trace-contract schema has Severity column; trace-permissions and trace-state use Flag only |
| C-09 Systemic findings cross-referenced | Aspirational | **FAIL** | Consolidation section not shown; no explicit SYSTEMIC flag instruction visible |
| C-10 Verdict names top finding | Aspirational | **FAIL** | Verdict section not shown in available text |
| C-11 Blast radius operationalized | Aspirational | **FAIL** | No topology census; blast radius language will default to generic definitions |
| C-12 Typed schemas per sub-skill | Aspirational | PASS | All 5 sub-skills have vocabulary-appropriate column schemas |
| C-13 Severity × blast radius co-located | Aspirational | **FAIL** | Severity in sub-skill schemas; blast radius in consolidation — not co-located per finding row |

**Essential:** 50/50 | **Recommended:** 10+5+5 = 20/30 | **Aspirational:** 1/5 → 2 pts

**Total: 72**

---

### V-03 — Post-execution blast radius calibration

**Hypothesis:** CALIBRATION BLOCK after sub-skill phases but before ranking grounds blast radius in actual findings rather than predicted topology.

| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 All 5 sub-skills run | Essential | PASS | Calibration block presupposes all sub-skills completed |
| C-02 Findings ranked by blast radius | Essential | PASS | Calibration feeds ranking step |
| C-03 Spec gaps section | Essential | PASS | Standard section |
| C-04 Contract violations section | Essential | PASS | Standard section |
| C-05 Consolidated report | Essential | PASS | Calibration enforces synthesis before ranking |
| C-06 Per-finding source attribution | Recommended | PASS | Section-level attribution expected |
| C-07 Remediation hint per finding | Recommended | **PARTIAL** | Calibration block focuses on blast radius scoping, not fix direction |
| C-08 Severity explicit | Recommended | **PARTIAL** | Calibration references impact magnitude but severity field not structurally enforced |
| C-09 Systemic findings cross-referenced | Aspirational | **FAIL** | No cross-sub-skill corroboration instruction visible in approach |
| C-10 Verdict names top finding | Aspirational | PASS | Calibration-anchored verdict names actual component from findings |
| C-11 Blast radius operationalized | Aspirational | PASS | Calibration block grounds blast radius in actual findings — evidence-driven rather than pre-declared |
| C-12 Typed schemas per sub-skill | Aspirational | **FAIL** | No schema typing mentioned in approach |
| C-13 Severity × blast radius co-located | Aspirational | **FAIL** | No co-location instruction; calibration block does not address this axis |

**Essential:** 50/50 | **Recommended:** 10+5+5 = 20/30 | **Aspirational:** 2/5 → 4 pts

**Total: 74**

---

### V-04 — Combo: Census + typed schemas

**Hypothesis:** V-01's blast radius anchoring (C-11) combined with V-02's typed schemas (C-12) — two strongest structural innovations together.

| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 All 5 sub-skills run | Essential | PASS | Inherited from both V-01 and V-02 |
| C-02 Findings ranked by blast radius | Essential | PASS | Census-anchored ranking from V-01 |
| C-03 Spec gaps section | Essential | PASS | Inherited from V-01 |
| C-04 Contract violations section | Essential | PASS | Inherited from both |
| C-05 Consolidated report | Essential | PASS | "Write ONE report. Not five." from V-01 |
| C-06 Per-finding source attribution | Recommended | PASS | Finding template field from V-01 |
| C-07 Remediation hint per finding | Recommended | PASS | "What must change to resolve it" from V-01 finding template |
| C-08 Severity explicit | Recommended | PASS | Severity field in both finding template (V-01) and sub-skill schemas (V-02) |
| C-09 Systemic findings cross-referenced | Aspirational | PASS | SYSTEMIC flag from V-01 |
| C-10 Verdict names top finding | Aspirational | PASS | Verdict instruction names census-derived component from V-01 |
| C-11 Blast radius operationalized | Aspirational | PASS | Census from V-01 anchors specific components |
| C-12 Typed schemas per sub-skill | Aspirational | PASS | All 5 typed schemas from V-02 |
| C-13 Severity × blast radius co-located | Aspirational | PASS | Separate labeled bullet fields per finding row from V-01 consolidation template |

**Essential:** 50/50 | **Recommended:** 30/30 | **Aspirational:** 5/5 → 10 pts

**Total: 90**

---

### V-05 — Full combo: Census + typed schemas + phase gates + anti-merge

**Hypothesis:** Structurally enforces all 13 rubric criteria; explicit anti-conflation instruction eliminates the C-13 failure mode; no criterion requires model inference.

| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 All 5 sub-skills run | Essential | PASS | Inherited + phase gates enforce completion |
| C-02 Findings ranked by blast radius | Essential | PASS | Census-anchored ranking |
| C-03 Spec gaps section | Essential | PASS | Explicit section |
| C-04 Contract violations section | Essential | PASS | Explicit section |
| C-05 Consolidated report | Essential | PASS | Phase gates ensure synthesis before consolidation |
| C-06 Per-finding source attribution | Recommended | PASS | Sub-skill field per finding |
| C-07 Remediation hint per finding | Recommended | PASS | Fix direction field |
| C-08 Severity explicit | Recommended | PASS | Severity in finding template and sub-skill schemas |
| C-09 Systemic findings cross-referenced | Aspirational | PASS | SYSTEMIC flag instruction |
| C-10 Verdict names top finding | Aspirational | PASS | Verdict with component name |
| C-11 Blast radius operationalized | Aspirational | PASS | Census + "name specific component or shared state" |
| C-12 Typed schemas per sub-skill | Aspirational | PASS | All 5 sub-skills typed |
| C-13 Severity × blast radius co-located | Aspirational | PASS | Explicit "Do not merge into a single 'impact' field" instruction — highest confidence of any variation |

**Essential:** 50/50 | **Recommended:** 30/30 | **Aspirational:** 5/5 → 10 pts

**Total: 90**

---

### Summary Table

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 50 | 30 | 8 (4/5) | **88** |
| V-02 | 50 | 20 | 2 (1/5) | **72** |
| V-03 | 50 | 20 | 4 (2/5) | **74** |
| V-04 | 50 | 30 | 10 (5/5) | **90** |
| V-05 | 50 | 30 | 10 (5/5) | **90** |

**Rank:** V-04 = V-05 > V-01 > V-03 > V-02

**V-05 preferred over V-04** despite equal score: the explicit anti-merge instruction for C-13 eliminates model inference from the hardest criterion to enforce structurally — V-04 passes C-13 by template structure; V-05 passes by explicit prohibition.

---

### Excellence Signals (from top-scoring variations)

**From V-04 / V-05 (score: 90):**

1. **Pre-execution topology census** — forcing enumeration of components, shared state surfaces, and downstream callers *before* any sub-skill runs creates a system-specific vocabulary; blast radius assessments can name actual artifacts rather than generic propagation language
2. **Per-sub-skill column schemas matched to sub-skill signal type** — trace-contract gets Producer/Consumer/Expected/Actual; trace-state gets State/Preconditions/Trigger/Postcondition; schema heterogeneity is a feature, not a bug — it prevents vocabulary from one sub-skill colonizing another
3. **Explicit co-location + anti-conflation instruction** — placing severity and blast radius as separate named fields in the same finding row *and* adding "Do not merge into a single 'impact' field" closes the C-13 failure mode at the prompt level, removing it from model discretion
4. **SYSTEMIC flag for cross-sub-skill corroboration** — flagging findings confirmed by 2+ sub-skills elevates the ranking signal beyond blast radius alone; a narrow finding that appears in both trace-contract and trace-state deserves different treatment than a narrow finding from one sub-skill only

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["pre-execution topology census anchors blast radius vocabulary to specific components before sub-skills run", "per-sub-skill heterogeneous schemas match column vocabulary to sub-skill signal type", "explicit anti-conflation instruction co-locates severity and blast radius as distinct fields per finding row"]}
```
