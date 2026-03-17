Now I have everything I need. Let me score all five variations.

---

## Scorecard: corps-build — Round 1

**Rubric version**: v1 | **Variations**: V-01 through V-05 | **Date**: 2026-03-16

---

## Criterion-by-Criterion Evaluation

### C-01 — Role file completeness (essential)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | STEP 7 BUILD-COMPLETE block explicitly compares org.yaml slots declared vs .craft/roles/ files written with match check and missing-list. IA-WRITTEN + TEAM-COMPLETE confirmations per team create an audit trail. |
| V-02 | **PASS** | TABLE-CLOSED gate emits authoritative count before any files written. AREA-WRITTEN running totals per area. CROSS-REF final check catches total mismatch with named missing/extra lists. |
| V-03 | **PASS** | ROLES-GATE in Phase 4 explicitly checks declared vs written with named list of any missing roles. Phase gate structure prevents advancement if count fails. |
| V-04 | **PASS** | Step 7 BUILD-COMPLETE has a dedicated "total files written: [n]" vs "org.yaml slots declared: [n]" match check with list on failure. Per-team TEAM-COMPLETE confirmations throughout. |
| V-05 | **PASS** | ROLES-GATE PASS emits count. Phase 4 CROSS-REF C1 independently verifies headcount table total == .craft/roles/ file count with full mismatch decomposition. |

---

### C-02 — org-chart.md with ASCII diagram (essential)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Step 5a: box-drawing characters required, minimum two levels, group names matched character-for-character to org.yaml, leaf nodes show headcount. Written after all role files. |
| V-02 | **PASS** | Step 4 derives ASCII exclusively from headcount table rows. DIAGRAM-DERIVED gate confirms all nodes sourced from table. Group names must match org.yaml. |
| V-03 | **PASS** | Phase 3a: ASCII diagram written first in WRITE-CHART phase. DIAGRAM-WRITTEN gate: "[n] team nodes, [n] group nodes, max depth [n]." Group names matched character-for-character. |
| V-04 | **PASS** | Step 5a: full hierarchy, minimum two levels, box-drawing characters, group names matched exactly. Headcount in parentheses on each team node. |
| V-05 | **PASS** | Phase 2a: org structure opens with prose sentence, then ASCII hierarchy. Group names matched character-for-character. Minimum two levels enforced. |

---

### C-03 — Inertia Advocate present in every team (essential)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | IA written as Step 2a (first per team) before any standard or specialized role. IA-WRITTEN confirmation after each. BUILD-COMPLETE checks "teams with IA files: [n of n]." IA-first ordering eliminates omission by construction. |
| V-02 | **PARTIAL** | IA written last per team (step 5c, after standard and specialized). AREA-WRITTEN tracks area file count but not per-team IA presence specifically. CROSS-REF checks total count only — a team missing its IA would be caught only if total count mismatches, not if the shortfall is masked by an extra file elsewhere. No explicit per-team IA audit. |
| V-03 | **PASS** | IA written last per team but TEAM-WRITTEN explicitly shows "(1 IA + [n] std + [n] spec)" per team — any team with 0 IA would surface immediately. BUILD SUMMARY has "IA coverage: [n of n] teams" as a named check field. |
| V-04 | **PASS** | All IA files written in a dedicated Step 3 before any standard or specialized roles. IA-PHASE-COMPLETE gate: "All [n] teams covered." BUILD-COMPLETE checks "IA files written: [n of n teams]." Two-layer verification (phase gate + build summary). |
| V-05 | **PASS** | Phase 4 CROSS-REF C2: "every team has an IA file — teams in org diagram: [n], IA files found: [n], result: MATCH/MISMATCH, if MISMATCH: teams missing IA: [list]." Dedicated check with named-team failure output. |

---

### C-04 — org.yaml structural fidelity (essential)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | PARSE step extracts all groups/teams/roles with explicit echo. Role writing follows declaration order from parsed output. BUILD-COMPLETE file count catch. No phantom-directory check but structural discipline of writing from parsed data makes phantom directories unlikely. |
| V-02 | **PASS** | Headcount table rows are sourced exclusively from org.yaml nodes (one row per team/area). CROSS-REF C3 checks: "every area in headcount table has a .craft/roles/{area-slug}/ directory" — catches both missing and extra directories. |
| V-03 | **PASS** | Phase 2 VALIDATE explicitly checks structural integrity before any files written: V-3 (no duplicate team names), V-2 (no role-name collision within a team). VALIDATE GATE FAIL halts the build. Structural problems caught pre-write. |
| V-04 | **PASS** | PARSE step emits full org structure. Role writing derived from PARSED output. BUILD-COMPLETE file count check. Weaker than V-03 (no VALIDATE phase) but structural discipline enforced through PARSED output. |
| V-05 | **PASS** | Phase 4 CROSS-REF C3: "every area in headcount table has a .craft/roles/{area-slug}/ directory" with lists of table areas vs directories present. MATCH/MISMATCH result. Catches both phantom and missing directories. |

---

### C-05 — Role file typed fields present (essential)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Steps 2a–2c all enumerate all five fields. 2a explicitly forbids "generic 'stability' language" in IA files. No placeholder language instruction. |
| V-02 | **PASS** | Step 5: "No placeholder text ('TBD', empty sections)" named explicitly. All five fields listed for every role type. Scope values enumerated as a closed set. |
| V-03 | **PASS** | Phase 4 WRITE-ROLES: "no placeholder text allowed" stated. All five fields listed. Scope field has four canonical values. |
| V-04 | **PASS** | Steps 3 and 4 enumerate all five fields. IA fields are populated *from* the resistance profile (orientation from "Status quo defended," lens from IA lens phrase, expertise from "Credibility source"), which prevents placeholder content by construction. |
| V-05 | **PASS** | Phase 3 WRITE ROLE FILES: "no placeholder text" stated. All five fields listed. Scope field has four explicit values. |

---

### C-06 — Headcount by group/area table + level distribution (recommended)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Steps 5b and 5c both provide explicit table templates with required columns. Level labels drawn from org.yaml. Total row required. |
| V-02 | **PASS** | Table is primary artifact, built before any files (Step 2). Standard Roles / Specialized Roles / Levels columns. Level distribution table in Step 3 with % of Org column. Richest table schema across all variations. |
| V-03 | **PASS** | Phases 3b and 3c both present with templates. Headcount per area = sum of role slots. Level distribution with % column. |
| V-04 | **PASS** | Steps 5b and 5c present. Bonus: "Inertia Advocate Lens Summary" table provides a third table section not in other variations. Level distribution with % column. |
| V-05 | **PASS** | Phase 2b has table plus 2–3 sentences of narrative (largest area, level concentration, teams with no declared levels). Phase 2c has level distribution plus 1-sentence seniority profile. Richest narrative depth. |

---

### C-07 — Standard vs specialized role distinction honored (recommended)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Step 2b scope: "`standard — present in all teams`"; Step 2c scope: "`specialized — [team name]`". Distinction in scope field, not derivable from directory alone. |
| V-02 | **PASS** | Step 5: "Standard vs specialized distinction must be explicit in the `scope` field — not derivable only from directory placement." Explicitly named rule. Four canonical scope values enumerated. |
| V-03 | **PASS** | Phase 4 WRITE-ROLES: "Standard vs specialized: must be explicit in the `scope` field — not derivable only from directory placement." Identical explicit instruction. |
| V-04 | **PASS** | Step 4a scope: "`standard — present in all teams`"; Step 4b scope: "`specialized — [team name]`". Shared group and exec office scopes also enumerated. |
| V-05 | **PASS** | Phase 3: "Standard vs specialized: explicit in `scope` field — not derivable only from directory placement." Closed set of four scope values. |

---

### C-08 — AMEND section with three actionable options (recommended)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Step 6: all three options with `--area "[area name]"`, `--levels "[old]:[new]"`, `--restructure "[team] > [new-parent]"`. Each option references actual org.yaml elements via placeholder-populated lists. |
| V-02 | **PASS** | Step 7: same three options. Option 1 references "areas from headcount table," Option 2 references "Level Distribution table," Option 3 references "nesting relationships from headcount table." Concrete references. |
| V-03 | **PASS** | Phase 3d: three options. Phase 5 VERIFY uniquely checks that all three options reference actual org.yaml elements, emitting AMEND-VERIFIED or AMEND-WARNING. Only variation with an AMEND post-write verification step. |
| V-04 | **PASS** | Step 6: three options. Option 1 adds "regenerating resistance profile" to the area-regenerate action. Concrete area, level, and nesting references. |
| V-05 | **PASS** | Phase 2d: three options. Option 3 includes a worked example of nesting relationship format: `"Platform > Infrastructure, Platform > Reliability, Growth > Acquisition"`. Most concrete example across all variations. |

---

### C-09 — Inertia Advocate files team-contextualized (aspirational)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | "Two teams with identical `lens` text is a build error." IA-WRITTEN confirmation requires emitting "lens: [one phrase from team context used]" — creates an audit trail. IA written as first file per team while team context is freshest in attention. Strong stated rule with implicit enforcement through confirmation line. |
| V-02 | **PARTIAL** | Rule stated: "No identical `lens` or `expertise` text across two IA files." But IA is written last per team (after standard and specialized roles), after the model has processed multiple table rows. Team context is most diluted at IA-write time. No pre-writing content plan to anchor the IA to specific team terms. |
| V-03 | **PARTIAL** | Rule stated: "No two IA files may share identical `lens` or `expertise` body text." IA written last per team (std → spec → IA). Same structural weakness as V-02 — context dilution at write time. Per-team TEAM-WRITTEN tracks "(1 IA + ...)" but doesn't enforce contextualization quality. |
| V-04 | **PASS** | Strongest mechanism: Step 2 resistance profiles force the model to generate specific IA lens phrases *before* writing any files. RESISTANCE-COMPLETE gate lists all phrases — any duplicate would be visible. Each profile has four structured slots ("Status quo defended," "Credibility source," "Failure mode seen," "IA lens phrase") that prevent generic content. IA lens phrase carries directly into the IA file lens field. |
| V-05 | **PARTIAL** | Rule stated: "lens must reference at least one domain-specific term drawn from the team's declared context in org.yaml." IA written last per team (std → spec → IA). Same structural weakness — no pre-writing profiling step to lock in team-specific content before context dilution. Rule alone, no structural enforcement. |

---

### C-10 — Cross-reference integrity (aspirational)

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PARTIAL** | BUILD-COMPLETE checks org.yaml declared vs files written. But C-10 requires headcount chart total == file count (a three-way check: org.yaml → chart → files). V-01 checks org.yaml vs files only. No explicit verification that the chart's headcount table total matches the file count. |
| V-02 | **PASS** | TABLE-CLOSED gate establishes authoritative count before any file writing. CROSS-REF step explicitly checks table-declared vs files-written with named missing/extra lists. "CROSS-REF PASS: [n] files match [n] declared. Build is consistent." Chart is the source of truth for the count by design. |
| V-03 | **PARTIAL** | BUILD SUMMARY has ".craft/roles/: [n] files / [n] declared" but this checks org.yaml vs files, not chart-headcount vs files. No dedicated cross-reference phase. Phase 5 VERIFY checks AMEND content but not file-chart consistency. |
| V-04 | **PARTIAL** | BUILD-COMPLETE checks total files written vs org.yaml slots declared. No explicit check that chart headcount table total equals .craft/roles/ file count. Same three-way gap as V-01. |
| V-05 | **PASS** | Phase 4 VALIDATE CROSS-REFERENCE is a dedicated lifecycle phase with three named checks: C1 (headcount table total == file count), C2 (every team has IA file), C3 (every area in table has directory). CROSS-REF GATE PASS/FAIL enforces all three. The C-10 criterion is a first-class phase, not a build-summary afterthought. |

---

## Composite Scores

Scoring: PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

### V-01

| Criterion | Tier | Rating | Pass Weight |
|-----------|------|--------|-------------|
| C-01 | essential | PASS | 1.0 |
| C-02 | essential | PASS | 1.0 |
| C-03 | essential | PASS | 1.0 |
| C-04 | essential | PASS | 1.0 |
| C-05 | essential | PASS | 1.0 |
| C-06 | recommended | PASS | 1.0 |
| C-07 | recommended | PASS | 1.0 |
| C-08 | recommended | PASS | 1.0 |
| C-09 | aspirational | PASS | 1.0 |
| C-10 | aspirational | PARTIAL | 0.5 |

```
= (5.0/5 * 60) + (3.0/3 * 30) + (1.5/2 * 10)
= 60 + 30 + 7.5
= 97.5
```

**All essential pass: YES**

---

### V-02

| Criterion | Tier | Rating | Pass Weight |
|-----------|------|--------|-------------|
| C-01 | essential | PASS | 1.0 |
| C-02 | essential | PASS | 1.0 |
| C-03 | essential | PARTIAL | 0.5 |
| C-04 | essential | PASS | 1.0 |
| C-05 | essential | PASS | 1.0 |
| C-06 | recommended | PASS | 1.0 |
| C-07 | recommended | PASS | 1.0 |
| C-08 | recommended | PASS | 1.0 |
| C-09 | aspirational | PARTIAL | 0.5 |
| C-10 | aspirational | PASS | 1.0 |

```
= (4.5/5 * 60) + (3.0/3 * 30) + (1.5/2 * 10)
= 54 + 30 + 7.5
= 91.5
```

**All essential pass: NO** (C-03 PARTIAL — no per-team IA audit, total-count-only cross-reference)

---

### V-03

| Criterion | Tier | Rating | Pass Weight |
|-----------|------|--------|-------------|
| C-01 | essential | PASS | 1.0 |
| C-02 | essential | PASS | 1.0 |
| C-03 | essential | PASS | 1.0 |
| C-04 | essential | PASS | 1.0 |
| C-05 | essential | PASS | 1.0 |
| C-06 | recommended | PASS | 1.0 |
| C-07 | recommended | PASS | 1.0 |
| C-08 | recommended | PASS | 1.0 |
| C-09 | aspirational | PARTIAL | 0.5 |
| C-10 | aspirational | PARTIAL | 0.5 |

```
= (5.0/5 * 60) + (3.0/3 * 30) + (1.0/2 * 10)
= 60 + 30 + 5
= 95
```

**All essential pass: YES**

---

### V-04

| Criterion | Tier | Rating | Pass Weight |
|-----------|------|--------|-------------|
| C-01 | essential | PASS | 1.0 |
| C-02 | essential | PASS | 1.0 |
| C-03 | essential | PASS | 1.0 |
| C-04 | essential | PASS | 1.0 |
| C-05 | essential | PASS | 1.0 |
| C-06 | recommended | PASS | 1.0 |
| C-07 | recommended | PASS | 1.0 |
| C-08 | recommended | PASS | 1.0 |
| C-09 | aspirational | PASS | 1.0 |
| C-10 | aspirational | PARTIAL | 0.5 |

```
= (5.0/5 * 60) + (3.0/3 * 30) + (1.5/2 * 10)
= 60 + 30 + 7.5
= 97.5
```

**All essential pass: YES**

---

### V-05

| Criterion | Tier | Rating | Pass Weight |
|-----------|------|--------|-------------|
| C-01 | essential | PASS | 1.0 |
| C-02 | essential | PASS | 1.0 |
| C-03 | essential | PASS | 1.0 |
| C-04 | essential | PASS | 1.0 |
| C-05 | essential | PASS | 1.0 |
| C-06 | recommended | PASS | 1.0 |
| C-07 | recommended | PASS | 1.0 |
| C-08 | recommended | PASS | 1.0 |
| C-09 | aspirational | PARTIAL | 0.5 |
| C-10 | aspirational | PASS | 1.0 |

```
= (5.0/5 * 60) + (3.0/3 * 30) + (1.5/2 * 10)
= 60 + 30 + 7.5
= 97.5
```

**All essential pass: YES**

---

## Ranking

| Rank | Variation | Score | All Essential | Key Advantage |
|------|-----------|-------|---------------|---------------|
| 1 | **V-04** | 97.5 | YES | C-09 PASS: pre-writing resistance profiles enforce IA contextualization by construction; C-03 PASS: IA-phase-complete gate; AMEND enhanced with resistance-profile regeneration |
| 2 | **V-05** | 97.5 | YES | C-10 PASS: dedicated CROSS-REF phase as first-class lifecycle step; richest narrative depth in org-chart.md |
| 3 | **V-01** | 97.5 | YES | Cleanest single-axis; IA-first per team is the simplest structural guarantee; no resistance profiling complexity |
| 4 | **V-03** | 95.0 | YES | VALIDATE phase (pre-write structural checks) is unique; AMEND-VERIFIED step is unique; weakest on both aspirational |
| 5 | **V-02** | 91.5 | NO | Best C-10 audit trail via TABLE-CLOSED authoritative count; C-03 structural weakness disqualifies from golden threshold |

**Tiebreaker V-04 over V-05**: V-04 passes C-09 via a structural mechanism (pre-writing resistance profiles with an enumerated lens phrase list), while V-05 only passes C-10 via a structural mechanism. C-09 failure risk is higher in practice (boilerplate IA files are the most common observed failure mode in org skill outputs), making V-04's mechanism more valuable.

---

## Excellence Signals — V-04 (Top Variation)

**Signal 1: Pre-writing content planning phase for high-risk fields**
The resistance profiles step (Step 2) forces the model to generate IA content answers — "Status quo defended," "Credibility source," "Failure mode seen," "IA lens phrase" — *before* writing any files. This separates content planning from content writing, preventing the in-context dilution that happens when IA files are written after multiple other files have been processed. The pattern: *plan the highest-risk field before writing any output, not while writing it.*

**Signal 2: Enumerated lens phrases as a gate artifact**
RESISTANCE-COMPLETE emits all lens phrases in a single list: "[list one per team]." This creates a scannable in-context audit: any duplicated phrase is immediately visible before any IA file is written. The gate artifact serves as a pre-write C-09 check.

**Signal 3: Separating IA into its own sequential phase (all IA before any other roles)**
Writing all IA files across all teams before writing any standard or specialized roles (IA-PHASE-COMPLETE: "All [n] teams covered") makes C-03 structurally impossible to fail silently. A team missed in the IA phase cannot be completed later — its absence is visible at the phase gate.

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["pre-writing resistance profiling phase generates IA content plan before any files written, preventing context dilution on high-risk fields", "separating all-IA into a dedicated phase with enumerated lens-phrase gate makes C-03 coverage auditable mid-build", "dedicated cross-reference lifecycle phase (VALIDATE CROSS-REFERENCE) makes chart-to-files integrity a first-class phase not a build-summary afterthought"]}
```
