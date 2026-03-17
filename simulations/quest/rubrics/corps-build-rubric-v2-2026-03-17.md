Looking at the scorecard, the two patterns that separated the 100-scoring variates (V-02, V-04) from the 92/89 variates (V-01, V-03) are:

1. **Named invariant block at entry point** — INVARIANTs declared before steps, referenced by name in body and AMEND. V-01/V-03 stated requirements inline; V-02/V-04 pre-declared them structurally.
2. **Auditable check-output (MATCH/MISMATCH)** — V-02/V-04 required the model to emit a literal verification statement. V-01/V-03 stated the requirement without forcing verifiable output (both C-01 and C-10 PASSed in V-02/V-04 but were PARTIAL in the others for exactly this reason).
3. **Named failure mode** — V-02 named the concrete violation ("An IA whose lens reads 'resistance to change in general' violates INVARIANT-5"). V-01/V-03 relied on the model to infer the boundary.

Three new aspirational criteria → C-11, C-12, C-13. Max rises from 100 → 115; golden threshold updated accordingly.

---

```markdown
# corps-build Rubric — v2
**Updated**: 2026-03-17  
**Based on**: Round 3 scorecard (V-01 through V-04)  
**Changes from v1**: Added C-11, C-12, C-13 from R3 excellence signals; weights rebalanced; golden threshold updated.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 5 | 5 | 25 |
| **Max** | | | **115** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 95  
**PARTIAL pass**: composite >= 70 with all 5 essential passing — earn full pass with 2/3 recommended

---

## Criteria

### Essential (12 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-01 | **Role file completeness** — total file count in summary equals count of files written in Step 2; gap identified and resolved before proceeding | correctness | PASS requires verification mechanism, not just count statement |
| C-02 | **org-chart.md with ASCII hierarchy** — uses `+--` / `\|` notation; all org.yaml names verbatim; nesting reflects group → team depth | format | Concrete example or INVARIANT declaration required for PASS |
| C-03 | **Inertia Advocate in every team** — one IA per team, no exceptions; enforced as a closure gate before moving to next team | correctness | "Mandatory" imperative + enforcement hook required |
| C-04 | **org.yaml structural fidelity** — files written only to subdirectories derived from org.yaml; path pattern `.craft/roles/{area-slug}/{role-slug}.md` | correctness | Pre-write path validation required for PASS |
| C-05 | **Role file typed fields present** — all five fields (`title`, `role-type`, `area`, `lens`, `expertise`) present with substantive bodies | coverage | Example files or field descriptions with quality bar required |

---

### Recommended (10 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-06 | **Headcount by group table + levels** — table includes group, standard count, specialized count, IA count, total, and Levels column | depth | Column structure must be explicit |
| C-07 | **Standard vs specialized distinction** — `role-type` in frontmatter; write sequence orders standard → specialized → IA | correctness | Sequence must be stated; specialized distinctness must be enforced (not copyable from standard) |
| C-08 | **AMEND section with three options** — close with named repair options: specific area regeneration, level-term update, group-node addition | behavior | Area regeneration option should reference invariant re-checks |

---

### Aspirational (5 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-09 | **Inertia Advocate team-contextualized** — IA lens and expertise drawn from this team's declared domain vocabulary; generic resistance language fails | depth | Named failure mode earns full PASS (see C-13) |
| C-10 | **Cross-reference integrity chart/roles** — explicit check statement: `Table Total = [n], files written = [n] — [MATCH \| MISMATCH]`; format is literal and auditable | correctness | Silent compliance is PARTIAL; emitted check string is PASS |
| C-11 | **Named invariant block at entry point** — all enforcement mechanisms declared as `INVARIANT-N` (or `INV-N`) before any steps; each invariant referenced by name in step body and AMEND section | structure | Entry-point declaration + downstream reference required; inline-only restatement is PARTIAL |
| C-12 | **Auditable check-output statements** — at least one criterion requires the model to emit a literal verification string (`[MATCH \| MISMATCH]`, `[PASS \| FAIL]`, or equivalent) as part of its output, not silent compliance | verifiability | One emitted check string anywhere earns PASS; pure compliance-reliance is FAIL |
| C-13 | **Named failure mode per aspirational criterion** — each aspirational criterion (C-09, C-10, C-11, C-12) names at least one concrete violation example (what the wrong output looks like) | precision | All four named earns PASS; one or more named earns PARTIAL; none is FAIL |

---

## Scoring Table

| Criterion | Weight | PASS | PARTIAL | FAIL |
|-----------|--------|------|---------|------|
| C-01 | 12 | 12 | 6 | 0 |
| C-02 | 12 | 12 | 6 | 0 |
| C-03 | 12 | 12 | 6 | 0 |
| C-04 | 12 | 12 | 6 | 0 |
| C-05 | 12 | 12 | 6 | 0 |
| C-06 | 10 | 10 | 5 | 0 |
| C-07 | 10 | 10 | 5 | 0 |
| C-08 | 10 | 10 | 5 | 0 |
| C-09 | 5 | 5 | 2.5 | 0 |
| C-10 | 5 | 5 | 2.5 | 0 |
| C-11 | 5 | 5 | 2.5 | 0 |
| C-12 | 5 | 5 | 2.5 | 0 |
| C-13 | 5 | 5 | 2.5 | 0 |
| **Total** | **115** | | | |

---

## Pass Levels

| Level | Condition |
|-------|-----------|
| **GOLDEN** | All 5 essential PASS + composite >= 95 |
| **PARTIAL PASS** | All 5 essential PASS + composite >= 70 + 2/3 recommended PASS |
| **FAIL** | Any essential FAIL, or composite < 70 |

---

## R3 Retrospective Scores (v2 re-scored)

| Variate | C-11 | C-12 | C-13 | New pts | v1 score | v2 score |
|---------|------|------|------|---------|---------|---------|
| V-01 Example-Driven | FAIL | PASS | PARTIAL | 7.5 | 92 | 99.5 |
| V-02 Constraint-First | PASS | PASS | PASS | 15 | 100 | 115 |
| V-03 Minimal Imperative | FAIL | PARTIAL | FAIL | 2.5 | 89 | 91.5 |
| V-04 Constraint-First + Example-Driven | PASS | PASS | PASS | 15 | 100 | 115 |

**Observation**: V-02 and V-04 both reach max (115) under v2. V-01 improves significantly
(+7.5) due to C-12 PASS. V-03 gains minimally (+2.5) — Minimal Imperative variant
structurally cannot satisfy named-invariant or named-failure-mode criteria.

---

## Diagnostic Rubric — What Each Criterion Catches

| Criterion | What fails without it |
|-----------|----------------------|
| C-01 | File count drift — model writes 11 files, reports 9, no one notices |
| C-02 | Hierarchy uses indentation or bullets instead of ASCII box-drawing |
| C-03 | IA omitted from one team; model closes team file set silently |
| C-04 | File written to wrong path (e.g., flat `.craft/roles/` instead of area subdirectory) |
| C-05 | Role files with placeholder or single-word field values |
| C-06 | Headcount table missing Levels column or totals |
| C-07 | Specialized role files indistinguishable from standard |
| C-08 | No repair path; consumer cannot extend output without re-running |
| C-09 | IA uses generic "resistance to change" lens regardless of team domain |
| C-10 | Cross-reference inconsistency undetected (chart and roles diverge silently) |
| C-11 | Enforcement requirements scattered inline; model loses track across long outputs |
| C-12 | Compliance cannot be audited from transcript alone |
| C-13 | Aspirational criteria enforced by positive example only; boundary cases drift |
```

---

**Three new criteria extracted from R3 excellence signals:**

- **C-11** (named invariant block): Structural pattern — V-02/V-04 pre-declared all constraints before Step 1. V-01/V-03 restated them inline per-step. The pre-declaration is what enabled cross-step and AMEND references.
- **C-12** (auditable check-output): The MATCH/MISMATCH pattern is what turned C-01 and C-10 from PARTIAL to PASS in V-02/V-04. Silent compliance can't be audited from transcript.
- **C-13** (named failure mode): V-02's C-09 PASS hinged on naming the violation ("An IA whose lens reads 'resistance to change in general' violates..."). A criterion without a named failure mode relies on the model to infer the boundary.

The re-scored R3 table at the bottom shows the v2 rubric correctly widens the gap between V-02/V-04 (115) and V-03 (91.5), while V-01 scores higher than V-03 despite being below the 100-scoring pair — which matches the observed quality ordering.
