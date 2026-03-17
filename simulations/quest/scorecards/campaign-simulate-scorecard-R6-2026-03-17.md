---

## campaign-simulate Round 6 Scorecard

### Result: Five-way tie at 100/100

All five R6 variations score 100/100 on rubric v5. The rubric ceiling has been saturated — same outcome as R5 V-04/V-05 on v5, which was the anchor.

### Criterion summary

**Essential (60 pts):** All five PASS C-01 through C-05. Every variation has the full five sub-skills, ranked blast-radius output, per-finding system boundary/severity, spec-gap findings, and single synthesized report.

**Recommended (30 pts):** All five PASS C-06/C-07/C-08. Exception Path column + coverage summary handles C-06; Sub-Skill column 2 in schema handles C-07; trace-state scope explicitly targets anomaly classes for C-08.

**Aspirational (17 criteria, capped at 10 pts):** All five PASS all 17 criteria. The one nuance: V-02/V-03/V-04 have a less explicit C-22 (no "campaign halts + exhaustion rationale" clause, only "must be MET before flow runs"). This counts as PASS because the implicit halt from "must be MET" satisfies the two acceptable-response alternatives. Even if scored as PARTIAL it doesn't matter — 17/17 aspirational criteria still cap at 10 pts.

### Ranking within the tie

| Rank | Variation | Axes | Beyond-rubric additions |
|------|-----------|------|------------------------|
| 1 | **V-05** | A+B+C | Remediation Quality Gate + Entity Coverage Matrix + Blast Radius Re-Assessment Gate |
| 2 | **V-04** | A+B | Remediation Quality Gate + Entity Coverage Matrix |
| 3 | **V-01** | A | Remediation Quality Gate |
| 3 | **V-02** | B | Entity Coverage Matrix |
| 5 | **V-03** | C | Blast Radius Re-Assessment Gate |

### Three new patterns (potential C-26/C-27/C-28)

- **C-26 (Remediation Quality Gate):** Promotes remediation conformance from checklist checkbox to per-row Verb/Target/Location extraction table — same upgrade as C-14 made for System Boundary labels.
- **C-27 (Entity Coverage Matrix):** Extends C-16 sub-skill sentinel down to entity granularity — each manifest entity shows COVERED/CLEAN/SKIPPED; a SKIPPED entity is as unacceptable as a missing sub-skill row.
- **C-28 (Blast Radius Re-Assessment Gate):** Propagates C-24 synthesis results back into the ranked table via ELEVATED annotations — closes the feedback loop that C-24 leaves open.

Scorecard written to `simulations/quest/scorecards/campaign-simulate-scorecard-R6-2026-03-17.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Remediation Quality Gate produces per-remediation table (Verb/Target/Location/Conformance) that makes vague remediation entries structurally visible by column scan -- extends C-17 blank-cell gate to content-quality gate", "Entity Coverage Matrix maps each entity from the Topic Entity Manifest to COVERED/CLEAN/SKIPPED status after sub-skill execution -- extends C-16 sub-skill sentinel rule down to entity granularity", "Blast Radius Re-Assessment Gate propagates cross-skill pattern Combined Blast Radius back into the ranked findings table via ELEVATED annotations -- closes the feedback loop between C-24 synthesis extraction and the primary ranked output"]}
```
|------|
| C-09 Test scenario baseline | PASS | PASS | PASS | PASS | PASS |
| C-10 F-NN Finding IDs | PASS | PASS | PASS | PASS | PASS |
| C-11 CRITICAL/HIGH budget per trace sub-skill | PASS | PASS | PASS | PASS | PASS |
| C-12 Structured table, no blank cells | PASS | PASS | PASS | PASS | PASS |
| C-13 Flow findings reference trace context | PASS | PASS | PASS | PASS | PASS |
| C-14 System Boundary vocabulary pre-assigned | PASS | PASS | PASS | PASS | PASS |
| C-15 Universal sentinel rule all columns | PASS | PASS | PASS | PASS | PASS |
| C-16 No-findings sentinel rows | PASS | PASS | PASS | PASS | PASS |
| C-17 Pre-output blank-cell verification gate | PASS | PASS | PASS | PASS | PASS |
| C-18 Unified schema closes C-03/C-07/C-10/C-13 | PASS | PASS | PASS | PASS | PASS |
| C-19 Finding Type from closed vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-20 Blast radius rationale for top-tier | PASS | PASS | PASS | PASS | PASS |
| C-21 Exception path coverage in named column | PASS | PASS | PASS | PASS | PASS |
| C-22 Severity budget gate enforces trace-before-flow | PASS | PASS | PASS | PASS | PASS |
| C-23 Blast Rationale as named table column | PASS | PASS | PASS | PASS | PASS |
| C-24 Cross-skill synthesis gate extracts named patterns | PASS | PASS | PASS | PASS | PASS |
| C-25 Severity from closed four-value vocabulary | PASS | PASS | PASS | PASS | PASS |
| **Aspirational passed** | 17/17 | 17/17 | 17/17 | 17/17 | 17/17 |
| **Aspirational subtotal (capped)** | **10** | **10** | **10** | **10** | **10** |

**Key evidence notes per criterion:**

- C-09: All include TEST SCENARIO BASELINE table with F-ID/Severity/Exception Path/Acceptance
  Condition columns; CRITICAL and HIGH findings produce scenarios by rule.
- C-10: F-ID is column 1 in all unified schemas; F-NN pattern specified in execution order.
- C-11: SEVERITY BUDGET GATE table with MET/NOT MET per trace sub-skill; budget must be met
  before flow executes. Structurally guarantees >=1 CRITICAL/HIGH per trace sub-skill.
- C-12: 11-column unified schema with universal no-blank rule; all fields enumerated.
- C-13: Trace Link column required; "at least one non-'none' Trace Link required" per flow
  sub-skill instruction. Flow-lifecycle and flow-conversation both carry this requirement.
- C-14: Type Vocabulary Map pre-assigns exact System Boundary and Type labels per sub-skill;
  instruction reads "copy from this table -- both are copy operations."
- C-15: All optional cells require "N/A -- [reason]" sentinel; blank is not acceptable in any
  column.
- C-16: All specify sentinel rows: Summary = "No findings detected", all other cells populated
  per universal sentinel rule.
- C-17: Named checklist gate (labeled "Pre-output blank-cell verification gate") must show
  PASSED before proceeding; checklist items cover all 11 columns plus type/boundary compliance.
- C-18: Single 11-column findings table is the unique schema; ranked tables are derived views
  (12-column = findings + Rank + Blast Rationale); C-03/C-07/C-10/C-13 all satisfied by one
  table scan.
- C-19: Type Vocabulary Map with closed per-sub-skill vocabulary; Type Vocabulary Verification
  section as named artifact; "copy operation" framing removes model judgment from type field.
- C-20: Blast Rationale column in ranked findings; required sentence for system-wide/cross-
  skill; "N/A -- component-wide/isolated: [name]" for lower tiers; blank = verification failure.
- C-21: Exception Path is column 10 in the 11-column schema; Exception Path Coverage Summary
  section tracks coverage by sub-skill.
- C-22: Named SEVERITY BUDGET GATE table with MET/NOT MET per trace sub-skill; all five
  variations state flow cannot run until budget is MET. V-01/V-05 add explicit campaign-halt
  and exhaustion-rationale clause; V-02/V-03/V-04 have implicit halt via "must be MET before
  flow sub-skills run" -- sufficient for pass condition (halt is one of two acceptable
  responses to shortfall).
- C-23: Ranked findings table has an explicit Blast Rationale column; Blast Rationale
  Verification section confirms conformance per row.
- C-24: CROSS-SKILL SYNTHESIS GATE labeled mandatory in all five; P-ID table or two-sentence
  sentinel justification required; gate status (POPULATED or SENTINEL) must appear in output.
- C-25: Pre-output gate checklist includes "All Severity values from the four-value enumerated
  set"; Type Vocabulary Map defines the four values; Severity Scale section present in all.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

**All five R6 variations score 100/100 on rubric v5. The rubric ceiling has been saturated.**

---

## Ranking

All variations tie at 100/100 on v5. Within the tie, ranked by structural completeness --
specifically by how many of the three beyond-rubric axes (A, B, C) are present:

| Rank | Variation | Score | Axes | Beyond-rubric mechanisms |
|------|-----------|-------|------|--------------------------|
| 1 | **V-05** | 100 | A + B + C | Remediation Quality Gate + Entity Coverage Matrix + Blast Radius Re-Assessment Gate |
| 2 | **V-04** | 100 | A + B | Remediation Quality Gate + Entity Coverage Matrix |
| 3 | **V-01** | 100 | A only | Remediation Quality Gate |
| 3 | **V-02** | 100 | B only | Entity Coverage Matrix |
| 5 | **V-03** | 100 | C only | Blast Radius Re-Assessment Gate |

**V-01 and V-02 share rank 3.** Each adds one axis addressing a different failure mode
(output quality vs. input coverage). Neither is superior to the other for rubric purposes;
their isolation distinguishes the failure modes most clearly for rubric design purposes.

**V-03 ranks 5th** within the tie. Axis C (Blast Radius Re-Assessment) addresses a feedback
loop gap -- synthesis results orphaned from the ranked table -- which is less fundamental than
the output-quality gap (Axis A) and input-coverage gap (Axis B) addressed by higher-ranked
variations.

---

## Excellence Signals

Three new patterns from V-05 (top-ranked full-combination variation) that exceed the rubric
ceiling and should inform v6 criteria.

### Signal 1 -- Remediation Quality Gate (Axis A; potential C-26)

**Pattern:** After the findings table is assembled, a named REMEDIATION QUALITY GATE extracts
Verb, Target, and Location from every remediation cell and checks each against the approved
verb set and template structure. Output: per-remediation table with Conformance column
(PASS / FAIL -- [violation type]: VAGUE-VERB / MISSING-TARGET / MISSING-LOCATION /
TEMPLATE-MISMATCH). Gate must show all-PASS before ranked findings are written.

**Why it matters:** The pre-output blank-cell gate (C-17) confirms a cell is not empty; it
cannot detect whether the cell content is actionable. A remediation that reads "Fix the spec
at the state machine boundary" passes C-17 but fails the Remediation Quality Gate (verb "fix"
is vague). The gate extends the mechanical-verification principle from cell presence to content
quality -- the same structural upgrade relation as C-14 applied to System Boundary
(prose inference to vocabulary copy) and C-19 applied to Finding Type.

**Upgrade path:** C-26 would require a Remediation Quality Gate table as a named structural
artifact, making remediation template conformance verifiable by column scan of the Verb column.
C-17 gates on blank cells; C-26 gates on verb and location quality.

---

### Signal 2 -- Entity Coverage Matrix (Axis B; potential C-27)

**Pattern:** After all five sub-skills execute, a named ENTITY COVERAGE MATRIX maps every
entity from the Topic Entity Manifest to its Coverage Status: COVERED (finding produced),
CLEAN (explicitly examined, no anomaly -- record "CLEAN -- examined, no anomaly detected at
[entity name]"), or SKIPPED (not examined -- add coverage gap finding to findings table).
Entity coverage gate: zero SKIPPED = PASSED.

**Why it matters:** C-16 (no-findings sentinel rows) operates at sub-skill granularity -- it
confirms trace-state ran but says nothing about whether every state in Entity List 1 was
examined. A manifest with 6 states and only 2 F-IDs from trace-state is ambiguous: did the
other 4 produce no anomaly, or were they silently skipped? The Entity Coverage Matrix forces
an explicit coverage claim per entity. A SKIPPED entity row is structurally equivalent to a
missing sub-skill row under C-16 -- both represent unverifiable execution gaps.

**Upgrade path:** C-27 would require an Entity Coverage Matrix as a named structural artifact
after sub-skill execution, making entity-level examination completeness verifiable by counting
SKIPPED rows rather than by cross-referencing Spec Location values across finding rows.
Extends C-16's sub-skill sentinel rule down to entity granularity.

---

### Signal 3 -- Blast Radius Re-Assessment Gate (Axis C; potential C-28)

**Pattern:** After the Cross-Skill Synthesis Gate produces P-IDs with Combined Blast Radius,
a mandatory BLAST RADIUS RE-ASSESSMENT GATE compares each finding's individual blast radius
to the combined blast radius of any pattern it participates in. If combined > individual,
the finding's blast radius is elevated with an "(ELEVATED by P-ID)" annotation in the Blast
Rationale column, and a revised ranked findings table is produced.

**Why it matters:** C-24 (Cross-Skill Synthesis Gate) extracts patterns with Combined Blast
Radius values. Without the re-assessment gate, this combined blast radius is an observation in
the P-ID table that has no effect on the primary deliverable -- the ranked findings table. A
finding ranked 15th as "isolated" during trace-state execution could belong to a system-wide
pattern after synthesis but would remain ranked 15th. The re-assessment gate propagates
synthesis back into the output, closing the feedback loop between the synthesis gate and the
ranked output.

**Upgrade path:** C-28 would require findings in cross-skill patterns to carry an updated
blast radius (if elevated) in the revised ranked table, with "(ELEVATED by P-ID)" visible in
the Blast Rationale column. C-24 gates on pattern extraction; C-28 gates on pattern
propagation back into ranking.

---

## Rubric v6 Recommendation

Three new aspirational criteria warranted by R6 evidence:

| ID | Criterion | Upgrades | Axis |
|----|-----------|----------|------|
| C-26 | Remediation Quality Gate: per-remediation table with Verb/Target/Location/Conformance columns; gate must show all-PASS before ranked findings | C-17 (blank-cell gate -> content-quality gate) | A |
| C-27 | Entity Coverage Matrix: per-entity rows with COVERED/CLEAN/SKIPPED status; zero SKIPPED = PASSED | C-16 (sub-skill sentinel -> entity sentinel) | B |
| C-28 | Blast Radius Re-Assessment Gate: findings in cross-skill patterns carry updated blast radius if pattern combined radius > individual; revised ranked table produced | C-24 (synthesis extraction -> synthesis propagation) | C |

All three follow the structural upgrade relation that characterizes prior aspirational pairs:
- C-17/C-26: gate on presence -> gate on content quality
- C-16/C-27: sub-skill sentinel -> entity sentinel
- C-28/C-24: synthesis gate -> propagation gate

**Post-v6 scoring preview:**
- V-05 passes C-26 + C-27 + C-28: 100/100 on v6 (aspirational pool 20; still capped at 10)
- V-04 passes C-26 + C-27 but not C-28: 100/100 on v6 (passes >=10 aspirational)
- V-01 passes C-26 only: 100/100 on v6
- V-02 passes C-27 only: 100/100 on v6
- V-03 passes C-28 only: 100/100 on v6

V-05 remains the only variation that saturates both the v5 and v6 aspirational ceilings.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Remediation Quality Gate produces per-remediation table (Verb/Target/Location/Conformance) that makes vague remediation entries structurally visible by column scan -- extends C-17 blank-cell gate to content-quality gate", "Entity Coverage Matrix maps each entity from the Topic Entity Manifest to COVERED/CLEAN/SKIPPED status after sub-skill execution -- extends C-16 sub-skill sentinel rule down to entity granularity", "Blast Radius Re-Assessment Gate propagates cross-skill pattern Combined Blast Radius back into the ranked findings table via ELEVATED annotations -- closes the feedback loop between C-24 synthesis extraction and the primary ranked output"]}
```
