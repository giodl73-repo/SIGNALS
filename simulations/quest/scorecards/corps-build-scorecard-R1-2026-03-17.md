# Quest Score — corps-build R1

## Scoring

### V-01 — Role Sequence: Categorical Write Order

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-01 | Role file completeness | **PASS** | Parse manifest commits to `total role slots: n`; 2a→2b→2c sub-steps per team before advancing; no team can be skipped |
| C-02 | org-chart.md with ASCII hierarchy | **PASS** | Step 5a specifies `+--`/`|` chars, names verbatim from org.yaml, ≥2 hierarchy levels; example structure provided |
| C-03 | Inertia Advocate in every team | **PASS** | Step 2c is a required sub-step for every team; five fields with domain-grounding explicitly required |
| C-04 | org.yaml structural fidelity | **PASS** | Path uses `{area-slug}` from parse manifest; area names must match org.yaml "character for character" |
| C-05 | Role file typed fields present | **PASS** | "non-empty body text" required per field in 2a and 2b; IA fields each carry explicit domain-grounding requirement |
| C-06 | Headcount by group table + levels | **PASS** | Step 5b: explicit table with per-area rows, Total row, level-distribution column; counts from actual files written |
| C-07 | Standard vs specialized distinction | **PASS** | Categorical write order (2a standard, 2b specialized) with separate frontmatter `role-type` applied at write time — C-07 satisfied by construction |
| C-08 | AMEND section with three options | **PASS** | Step 6 has three concrete options; each references an actual org.yaml name as target |
| C-09 | Inertia Advocate team-contextualized | **PARTIAL** | Per-field domain-grounding required ("No generic 'stability' text"), but no pre-commit profiling phase to enforce distinctness before writing |
| C-10 | Cross-reference integrity chart/roles | **PARTIAL** | "counts must reflect actual files written" stated; no explicit phase exit check verifying chart total equals file count |

**Composite**: 60 + 30 + 2.5 + 2.5 = **95** | All essential pass: **YES** | **GOLDEN**

---

### V-02 — Table-First org-chart.md

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-01 | Role file completeness | **PASS** | Parse summary captures declared counts; role write loop covers all teams in declaration order |
| C-02 | org-chart.md with ASCII hierarchy | **PASS** | Section 3 specifies box chars, verbatim names, ≥2 nesting levels |
| C-03 | Inertia Advocate in every team | **PASS** | "mandatory — one per team, no exceptions" explicit |
| C-04 | org.yaml structural fidelity | **PASS** | "no renaming, no flattening" stated; path pattern uses area slugs from org.yaml |
| C-05 | Role file typed fields present | **PASS** | Five fields with "substantive (non-empty, non-'TBD') body text" required per file |
| C-06 | Headcount by group table + levels | **PASS** | Section 1 is table-first with per-area rows + exec-office + shared; Section 2 adds level distribution; Total = exact file count |
| C-07 | Standard vs specialized distinction | **PASS** | `role-type` in frontmatter required; write order (1. standard, 2. specialized, 3. IA) still present |
| C-08 | AMEND section with three options | **PASS** | AMEND block names three options with actual group/level terms |
| C-09 | Inertia Advocate team-contextualized | **FAIL** | No instruction requiring IA content to be team-specific; only generic five-field requirement applies — boilerplate IA across teams is not prohibited |
| C-10 | Cross-reference integrity chart/roles | **PASS** | "Count the role files just written. Do not estimate — count from the file set." Total must equal exact file count; table-first structure commits to count before ASCII draw |

**Composite**: 60 + 30 + 0 + 5 = **95** | All essential pass: **YES** | **GOLDEN**

---

### V-03 — Phrasing Register: Descriptive/Narrative

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-01 | Role file completeness | **PARTIAL** | "generate one file per role" stated but no parse count commitment (no `total role slots: n`); narrative framing increases omission risk on larger orgs |
| C-02 | org-chart.md with ASCII hierarchy | **PASS** | "ASCII diagram of the org hierarchy, using box-drawing characters… All names verbatim" — clearly stated |
| C-03 | Inertia Advocate in every team | **PASS** | "Every team must have at least one Inertia Advocate" explicit |
| C-04 | org.yaml structural fidelity | **PASS** | "Area names in the directory tree must match the area names in org.yaml exactly — no renaming, no flattening" |
| C-05 | Role file typed fields present | **PASS** | All five fields described with explicit non-generic requirements ("'Technical perspective' is not a lens. 'Distributed cache invalidation latency' is.") — best field descriptions of any variation |
| C-06 | Headcount by group table + levels | **PASS** | "headcount section with a table… Include a Total row. Totals must reflect actual files written — not estimates." |
| C-07 | Standard vs specialized distinction | **PASS** | `role-type` values enumerated (standard/specialized/inertia-advocate/shared-group/exec-office) with meaning defined |
| C-08 | AMEND section with three options | **PASS** | Three specific amendments with org.yaml names described narratively with concrete targets |
| C-09 | Inertia Advocate team-contextualized | **PARTIAL** | "must be drawn from the team's specific domain… same-sounding IA is not acceptable" — strong language, but no pre-commit profiling mechanism to enforce before write |
| C-10 | Cross-reference integrity chart/roles | **PARTIAL** | "totals must reflect actual files written" stated; no explicit verification step or count equality check |

**Composite**: 6 + 12 + 12 + 12 + 12 + 10 + 10 + 10 + 2.5 + 2.5 = **89** | All essential pass: **NO** (C-01 PARTIAL) | **PARTIAL PASS** (composite 89 > 60; all 3 recommended pass — qualifies for full pass via PARTIAL track if C-01 is remediated)

---

### V-04 — Inertia Framing + Role Sequence

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-01 | Role file completeness | **PASS** | Parse manifest with `total role slots: n`; categorical write order per team; Step 3 and 4 handle shared/exec |
| C-02 | org-chart.md with ASCII hierarchy | **PASS** | Step 4 ASCII with `+--`/`|`, verbatim names, min 2 nesting levels |
| C-03 | Inertia Advocate in every team | **PASS** | "Inertia Advocate files must use the resistance profile from Step 2" — every IA anchored to its team's profile |
| C-04 | org.yaml structural fidelity | **PASS** | `{area-slug}` paths from parse manifest; all teams mapped with parent path |
| C-05 | Role file typed fields present | **PASS** | "No empty bodies. No 'TBD'." across all five fields in every category |
| C-06 | Headcount by group table + levels | **PASS** | Step 4 headcount table with per-area rows, Total row, level distribution column |
| C-07 | Standard vs specialized distinction | **PASS** | Frontmatter `role-type` values listed; categorical write order maintained |
| C-08 | AMEND section with three options | **PASS** | Step 5 AMEND with three concrete options; option 1 includes "re-derive resistance profile" — strongest AMEND of single-axis variations |
| C-09 | Inertia Advocate team-contextualized | **PASS** | Step 2 produces resistance profiles with vocabulary distinctness check before any file writing; IA fields must trace to profile (`lens` ← vocabulary, `expertise` ← status-quo investment, `orientation` ← rational objection); "no two IA files may share identical lens or expertise text" |
| C-10 | Cross-reference integrity chart/roles | **PARTIAL** | Headcount table present with "actual files written" implied; no explicit Phase exit check comparing chart total to file count (present in V-05 but absent here) |

**Composite**: 60 + 30 + 5 + 2.5 = **97.5** | All essential pass: **YES** | **GOLDEN**

---

### V-05 — Combination: Phase Gates + Table-First + Resistance Profile

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-01 | Role file completeness | **PASS** | Phase 2 exit check: "count files written. Must equal total declared role slots from PHASE 0. If count does not match, identify the gap before proceeding." |
| C-02 | org-chart.md with ASCII hierarchy | **PASS** | Phase 3 Section 3: box chars, verbatim names, ≥2 nesting levels, all org.yaml teams visible |
| C-03 | Inertia Advocate in every team | **PASS** | "Category C — Inertia Advocate (mandatory — one per team, no exceptions)" + Phase 1 resistance profile anchors each |
| C-04 | org.yaml structural fidelity | **PASS** | Phase 0 captures exact area names with parent paths; Phase 2 paths mirror org.yaml nesting |
| C-05 | Role file typed fields present | **PASS** | "(non-empty, non-'TBD')" in all three categories A/B/C; Phase 2 exit check verifies file count |
| C-06 | Headcount by group table + levels | **PASS** | Phase 3 Section 1 table-first with full column breakdown (Standard/Specialized/IA/Shared/Exec/Total/Levels); Section 2 level distribution; exit check requires Total = Phase 2 file count |
| C-07 | Standard vs specialized distinction | **PASS** | Categories A/B/C with explicit frontmatter per category; exec-office and shared-group handled separately |
| C-08 | AMEND section with three options | **PASS** | Phase 4 AMEND with three concrete options; option 1 propagates back to Phase 1 (re-derive resistance profile) and Phase 2 (rewrite), then updates headcount table |
| C-09 | Inertia Advocate team-contextualized | **PASS** | Phase 1 exit condition: "all vocabulary sets distinct — do not proceed until all profiles have unique vocabulary." Phase 2 traceability: orientation ← rational objection, lens ← domain vocabulary, expertise ← status-quo investment. Duplication detected → return to Phase 1 and differentiate before continuing. |
| C-10 | Cross-reference integrity chart/roles | **PASS** | Phase 3 exit check: "confirm that Total in Section 1 equals the file count from Phase 2. If they differ, identify which area is miscounted before adding the AMEND section." |

**Composite**: 60 + 30 + 5 + 5 = **100** | All essential pass: **YES** | **GOLDEN**

---

## Ranking

| Rank | Variation | Score | All Essential | Status |
|------|-----------|-------|--------------|--------|
| 1 | **V-05** Combination | **100** | YES | GOLDEN |
| 2 | **V-04** Inertia Framing | **97.5** | YES | GOLDEN |
| 3 | **V-01** Role Sequence | **95** | YES | GOLDEN |
| 4 | **V-02** Table-First | **95** | YES | GOLDEN — ranked below V-01 due to complete C-09 FAIL vs PARTIAL |
| 5 | **V-03** Narrative Register | **89** | NO (C-01 partial) | PARTIAL PASS — remediate parse count commitment to qualify |

---

## Excellence Signals from V-05

**Signal 1 — Pre-commit thinking phases produce locked-in differentiation.** V-05's Phase 1 does not write files — it derives resistance profiles with an explicit distinctness exit condition ("do not proceed until all profiles have unique vocabulary"). The model cannot move to Phase 2 without having committed to distinct vocabulary per team. This eliminates the C-09 failure mode structurally rather than rhetorically.

**Signal 2 — Phase exit checks surface count discrepancies before they compound.** Phase 2 exit check (file count = declared slots) and Phase 3 exit check (chart Total = Phase 2 count) create two independent verification points. Errors caught at Phase 2 are fixed before the chart is drawn; errors caught at Phase 3 are fixed before AMEND is offered. Neither check exists in V-01 through V-04 (V-04 has no exit checks; V-02 has one implicit count instruction but no phase gate).

**Signal 3 — Table-first order forces count commitment before visual representation.** When the headcount table is Section 1 and the ASCII diagram is Section 3, the model counts before it draws. This inverts the natural temptation to draw the org and then count from the drawing — which produces drift. V-02 uses this pattern alone; V-05 amplifies it with a phase exit check that requires table Total = Phase 2 file count.

**Signal 4 — AMEND options propagate back through the causal chain.** V-05's AMEND option 1 says "re-derive resistance profile (Phase 1) and rewrite role files (Phase 2). Update headcount table." This ensures that regenerating an area re-runs the profiling step, not just the file write — preventing the case where AMEND regenerates boilerplate because it skips Phase 1.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-commit thinking phases with distinctness exit conditions lock in differentiation before any files are written, eliminating boilerplate by construction rather than instruction", "phase exit checks that verify numeric equality at phase boundaries catch completeness gaps before downstream sections compound them"]}
```
