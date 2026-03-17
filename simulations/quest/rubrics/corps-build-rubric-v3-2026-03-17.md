Reading the scorecard carefully to extract the R4 excellence patterns before writing the rubric.

**R4 excellence signals I'm extracting:**

1. **V-02 — Dedicated FAILURE MODES block (pre-step)**: All 4 aspirational failure modes front-loaded in a single named section before Step 1. Scorecard note: "Strongest C-13 coverage: model encounters all wrong-output anchors before producing any output." This is structurally distinct from C-13 (which requires naming failure modes) — C-14 requires grouping them in a dedicated pre-step section.

2. **V-03 — Named CHECK-OUTPUT PROTOCOL section**: Verifiable output elevated from scattered inline requirement to a first-class named protocol section with explicit rules. Scorecard note: "Strongest C-12 coverage in R4." Distinct from C-12 (which requires one emitted check string) — C-15 requires a named protocol section with rules.

These become **C-14** and **C-15**. Max rises 115 → 125. Golden threshold scales proportionally (82.6% → ~103).

---

```markdown
# corps-build Rubric — v3
**Updated**: 2026-03-17  
**Based on**: Round 4 scorecard (V-01 through V-04)  
**Changes from v2**: Added C-14, C-15 from R4 excellence signals; max updated 115 → 125; thresholds scaled.

---

## What Changed

| Version | Change | Source |
|---------|--------|--------|
| v1 → v2 | Added C-11 (named invariants block), C-12 (auditable check-output), C-13 (named failure modes per criterion) | R3 excellence signals |
| v2 → v3 | Added C-14 (dedicated pre-step FAILURE MODES block), C-15 (named CHECK-OUTPUT PROTOCOL section) | R4 excellence signals |

**R4 pattern summary**: R4 revealed two structural innovations beyond R3. V-02 showed that front-loading all failure modes in a dedicated block (rather than placing them inline per step) is the strongest realization of "constraints active during write" — the model encounters every wrong-output anchor before producing any output. V-03 showed that elevating the verifiability requirement from a scattered inline rule to a named protocol section with explicit rules is the strongest realization of auditable output — it becomes a first-class obligation rather than a compliance note.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 7 | 5 | 35 |
| **Max** | | | **125** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 103  
**PARTIAL pass**: composite >= 76 with all 5 essential passing — earn full pass with 2/3 recommended

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
| C-14 | **Dedicated pre-step FAILURE MODES block** — all aspirational failure modes collected in a single named section (e.g., `FAILURE MODES`, `WRONG OUTPUT ANCHORS`) that appears before Step 1; model encounters all wrong-output anchors before producing any output | structure | Dedicated named block with all aspirational failure modes earns PASS; scattered inline-only placement is PARTIAL; no explicit wrong-output anchors is FAIL |
| C-15 | **Named CHECK-OUTPUT PROTOCOL section** — verifiable output requirements elevated to a first-class named protocol section with explicit rules: what strings to emit, when to emit them, and what silent compliance looks like; not scattered inline | verifiability | Dedicated named protocol section with rules earns PASS; single inline check-output requirement is PARTIAL; no named protocol is FAIL |

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
| C-14 | 5 | 5 | 2.5 | 0 |
| C-15 | 5 | 5 | 2.5 | 0 |
| **Total** | **125** | | | |

---

## Round History

| Round | Best score | Threshold met | Key signal |
|-------|------------|---------------|------------|
| R3 | 100 / 100 | Yes (v1) | Named invariants block, auditable check-output, named failure modes → C-11, C-12, C-13 |
| R4 | 115 / 115 | Yes (v2) | Dedicated FAILURE MODES block, named CHECK-OUTPUT PROTOCOL section → C-14, C-15 |
```

---

**Extraction rationale:**

- **C-14** captures V-02's structural insight: grouping failure modes in a dedicated pre-step block is categorically stronger than inline placement (C-13 requires naming; C-14 requires co-location before any output is generated). The PARTIAL case covers the common intermediate — some failure modes named inline but no dedicated block.

- **C-15** captures V-03's structural insight: a named protocol section is categorically stronger than a scattered inline requirement for check-output (C-12 requires at least one emitted string; C-15 requires the mechanism to be a first-class named section). The PARTIAL case covers C-12-satisfying prompts that don't yet elevate it to a protocol.

- **Threshold scaling**: 95/115 = 82.6% → 103/125 = 82.4%. The bar is unchanged in practice.
