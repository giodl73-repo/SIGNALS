# Quest Score — corps-build R2

## Rubric v2 Scoring

---

### Evaluation per Variation

#### V-01 — Lifecycle: VALIDATE as Hard Pre-write Gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role file completeness | PASS | WRITE-GATE checks org.yaml slots vs files written; VERIFY C1 cross-references |
| C-02 org-chart.md ASCII diagram | PASS | Section 3b specifies box-drawing, 2+ nesting levels, exact group name matching |
| C-03 IA in every team | PASS | Phase 3a writes all IA before any standard/specialized; IA-PHASE-COMPLETE confirms n/n |
| C-04 org.yaml structural fidelity | PASS | 5-check VALIDATE + VERIFY C3 maps every area to directory |
| C-05 Typed fields present | PASS | All five fields required, no-placeholder enforced explicitly |
| C-06 Headcount table + levels | PASS | Section 3b headcount table + Level Distribution section both present |
| C-07 Standard vs specialized | PASS | scope field must be exactly one of four canonical values; explicit in field |
| C-08 AMEND with 3 options | PASS | --area, --levels, --restructure with populated lists |
| C-09 IA team-contextualized | PASS | lens must use ≥1 term from team's responsibilities; expertise must be unique per team |
| C-10 Cross-reference integrity | PASS | VERIFY phase: C1 headcount==file count, C2 IA per team, C3 area dirs |
| C-11 Pre-write VALIDATE gate | PASS | Explicit 5-check VALIDATE phase; VALIDATE-PASS required before first write; halts with VALIDATE-FAIL |
| C-12 IA-first ordering | PASS | Phase 3a dedicated IA phase; IA-PHASE-COMPLETE before 3b/3c |
| C-13 Table as build contract | FAIL | Table in 3b written after IA files; no TABLE-CLOSED gate; "file writes derived from table rows" absent |
| C-14 Analytic narrative prose | FAIL | Headcount table and Level Distribution specified but no 2-3 sentence prose requirement |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/6 = 6.7
**Composite: 96.7**

---

#### V-02 — Output Format: Table-first Build Contract + Narrative Prose

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role file completeness | PASS | CROSS-REF checks TABLE-CLOSED declared vs files written |
| C-02 org-chart.md ASCII diagram | PASS | STEP 4 specifies +-- diagram derived from table rows; group names match org.yaml |
| C-03 IA in every team | PASS | Per-area ordering: IA first; CROSS-REF IA check confirms n/n teams |
| C-04 org.yaml structural fidelity | PASS | Table rows derived from org.yaml; CROSS-REF dir check |
| C-05 Typed fields present | PASS | All five fields, no placeholder; IA lens/expertise uniqueness enforced |
| C-06 Headcount table + levels | PASS | STEP 2 headcount table; STEP 3 Level Distribution table |
| C-07 Standard vs specialized | PASS | scope field explicit; "not inferred from directory placement" stated |
| C-08 AMEND with 3 options | PASS | STEP 5 AMEND with --area, --levels, --restructure |
| C-09 IA team-contextualized | PASS | lens must reference team context from org.yaml; no two IA files share lens or expertise |
| C-10 Cross-reference integrity | PASS | CROSS-REF step: table count vs file count, IA check, dir check |
| C-11 Pre-write VALIDATE gate | FAIL | No VALIDATE phase; STEP 1 goes directly to PARSE → STEP 2 headcount → writes |
| C-12 IA-first ordering | PASS | "Order within each area: IA first, then standard, then specialized" — satisfies per-team IA-first pass condition |
| C-13 Table as build contract | PASS | STEP 2 emits table before any file; TABLE-CLOSED gate = authoritative file count; STEP 6 processes table rows as work list |
| C-14 Analytic narrative prose | PASS | Required 2-3 sentences after TABLE-CLOSED (largest area %, concentration, levels); seniority sentence after level table |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 5/6 = 8.3
**Composite: 98.3**

---

#### V-03 — Phrasing Register: Output-forward / Reviewer Perspective

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role file completeness | PASS | Build verification summary: "role files: [n] written / [n] declared — MATCH/MISMATCH" |
| C-02 org-chart.md ASCII diagram | PASS | Section 1 specifies +-- and \| characters; group names exactly as in org.yaml |
| C-03 IA in every team | PASS | "Every team has an Inertia Advocate file. No team is exempt." Verification confirms n/n |
| C-04 org.yaml structural fidelity | PASS | Output-forward description implies correct structure; verify summary matches declared slots |
| C-05 Typed fields present | PASS | All five fields described; "No field is empty, contains 'TBD,' or generic boilerplate" |
| C-06 Headcount table + levels | PASS | Section 2 headcount table; Section 3 level distribution; both described in detail |
| C-07 Standard vs specialized | PASS | scope must distinguish standard vs specialized explicitly — "not by directory path alone" |
| C-08 AMEND with 3 options | PASS | Section 4 AMEND with 3 options described |
| C-09 IA team-contextualized | PASS | Strong/weak example pair provided; "portrait of a specific person, not a generic role" — highest qualitative signal of any variation |
| C-10 Cross-reference integrity | PASS | Build verification: "cross-ref: headcount table total [n] == file count [n] — MATCH/MISMATCH" |
| C-11 Pre-write VALIDATE gate | PASS | "Before writing any file, check org.yaml for structural problems... If any problem is found, list each in a VALIDATE: block and halt" — 4 named checks, halt on problem |
| C-12 IA-first ordering | FAIL | No IA-first instruction; output-forward format describes role content, not write ordering |
| C-13 Table as build contract | FAIL | Table is in Section 2 of org-chart.md; no table-first sequencing, no TABLE-CLOSED gate, no "derives from table" mechanism |
| C-14 Analytic narrative prose | PASS | Section 2 requires "2-3 sentences that interpret the numbers" with strong/weak prose examples; Section 3 requires seniority sentence |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/6 = 6.7
**Composite: 96.7**

---

#### V-04 — Resistance Profiles + Table Contract + IA-first Ordering

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role file completeness | PASS | BUILD-COMPLETE: "total files: [n], org.yaml declared: [n], match: YES/NO" |
| C-02 org-chart.md ASCII diagram | PASS | STEP 6 org-chart.md Section 1: box-drawing, 2+ levels, exact group name match |
| C-03 IA in every team | PASS | STEP 4 dedicated IA phase writes all teams; IA-PHASE-COMPLETE: "[n of n] teams. All IA files written before standard or specialized roles." |
| C-04 org.yaml structural fidelity | PASS | PARSE extracts full structure; table maps all areas; BUILD-COMPLETE match check |
| C-05 Typed fields present | PASS | All five fields; no placeholder; unique lens/expertise across IA files |
| C-06 Headcount table + levels | PASS | STEP 2 headcount table; STEP 6 Level Distribution section |
| C-07 Standard vs specialized | PASS | STEP 5 scope values explicit; "must be explicit in scope field — not derivable from directory path alone" |
| C-08 AMEND with 3 options | PASS | STEP 6 AMEND with --area, --levels, --restructure |
| C-09 IA team-contextualized | PASS | Resistance profiles (STEP 3) force individualized IA content — strongest mechanism for C-09; "Status quo defended: specific system... not 'stability'"; IA lens phrase derived from profile |
| C-10 Cross-reference integrity | PASS | BUILD-COMPLETE: "headcount contract: table [n] == files [n] — YES/NO" |
| C-11 Pre-write VALIDATE gate | FAIL | No VALIDATE phase; sequence goes PARSE → HEADCOUNT TABLE → RESISTANCE PROFILES → IA WRITES — no structural check before writes |
| C-12 IA-first ordering | PASS | STEP 4 is dedicated IA phase; IA-PHASE-COMPLETE confirms completion "before standard or specialized roles" |
| C-13 Table as build contract | PASS | STEP 2 "Before writing any files or resistance profiles, emit the headcount table"; TABLE-CLOSED = authoritative file count; STEP 5 processes per table rows |
| C-14 Analytic narrative prose | PASS | After TABLE-CLOSED: required 2-3 sentences (largest area %, concentration, level flag); Level Distribution followed by seniority sentence |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 5/6 = 8.3
**Composite: 98.3**

---

#### V-05 — Full Integration: All Four New Aspirational Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role file completeness | PASS | ROLES-GATE checks declared vs written; CROSS-REF C1 confirms contract vs file count |
| C-02 org-chart.md ASCII diagram | PASS | Phase 5: "box-drawing characters, minimum two levels. Group names exactly as in org.yaml." |
| C-03 IA in every team | PASS | Phase 4a writes all IA files; IA-PHASE-COMPLETE "[n of n] teams"; CROSS-REF C2 |
| C-04 org.yaml structural fidelity | PASS | VALIDATE V-1 (every team has roles), CROSS-REF C3 (every table area has directory) |
| C-05 Typed fields present | PASS | All five fields; no placeholder; IA lens/expertise uniqueness enforced |
| C-06 Headcount table + levels | PASS | Phase 3 headcount table; Phase 5 Level Distribution table |
| C-07 Standard vs specialized | PASS | "scope field must be explicit — not derivable from directory path alone" |
| C-08 AMEND with 3 options | PASS | Phase 5 AMEND section with --area, --levels, --restructure |
| C-09 IA team-contextualized | PASS | Phase 4a: lens "domain-specific phrase tied to this team's responsibilities; must differ from every other team's"; expertise "must differ from every other team's" |
| C-10 Cross-reference integrity | PASS | Phase 6 CROSS-REF: C1 (TABLE-CLOSED vs files), C2 (IA per team), C3 (area directories) |
| C-11 Pre-write VALIDATE gate | PASS | Phase 2 VALIDATE: 4 named checks (V-1 through V-4); "No files written during this phase"; VALIDATE-PASS required before Phase 3; VALIDATE-FAIL halts with details |
| C-12 IA-first ordering | PASS | Phase 4a named IA-PHASE; IA-PHASE-COMPLETE: "All IA files written. Standard and specialized role files may now be written." gates 4b and 4c |
| C-13 Table as build contract | PASS | Phase 3 "BUILD CONTRACT" — first artifact after VALIDATE-PASS; TABLE-CLOSED establishes file count; ROLES-GATE references TABLE-CLOSED n; final summary: "headcount table: written pre-roles (contract: [n] files)" |
| C-14 Analytic narrative prose | PASS | Phase 3 mandatory prose with sentence-level prescription: Sentence 1 (largest area + %), Sentence 2 (dominant level), Sentence 3 (structural observation); CONTRACT-GATE confirms prose written; seniority sentence after Phase 5 level table |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 6/6 = 10
**Composite: 100**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Rank |
|-----------|-----------|-------------|--------------|-----------|------|
| **V-05** | 5/5 (60) | 3/3 (30) | 6/6 (10.0) | **100** | 1 |
| **V-02** | 5/5 (60) | 3/3 (30) | 5/6 (8.3) | **98.3** | 2 (tie) |
| **V-04** | 5/5 (60) | 3/3 (30) | 5/6 (8.3) | **98.3** | 2 (tie) |
| **V-01** | 5/5 (60) | 3/3 (30) | 4/6 (6.7) | **96.7** | 4 (tie) |
| **V-03** | 5/5 (60) | 3/3 (30) | 4/6 (6.7) | **96.7** | 4 (tie) |

All essential criteria pass across all five variations. The aspirational layer is the sole differentiator.

**C-11 (VALIDATE gate)**: Only V-01, V-03, V-05 pass. V-02 and V-04 jump from parse to table/writes with no structural check phase.

**C-12 (IA-first)**: Only V-03 fails — output-forward register describes content, not sequence.

**C-13 (table as contract)**: V-01 and V-03 fail — table appears inside WRITE phase, not as first artifact.

**C-14 (analytic prose)**: V-01 fails — headcount and level tables specified but no prose requirement.

---

## Excellence Signals from V-05

**1. Phase-gate chain as structural enforcement**
V-05 uses six named phases where each phase requires its predecessor's gate token before any work begins. PARSE-PASS unlocks VALIDATE; VALIDATE-PASS unlocks CONTRACT-GATE; CONTRACT-GATE unlocks ROLES-GATE; ROLES-GATE unlocks CHART-GATE. No phase can be skipped without an explicit protocol violation visible in the output. This is more robust than V-01's 4-phase chain: V-05 separates BUILD CONTRACT into its own phase, making the table a first-class artifact rather than a WRITE sub-step.

**2. Sentence-level prose prescription**
V-05 specifies not just "write 2-3 sentences" but assigns each sentence a discrete content contract: Sentence 1 = largest area + % of total, Sentence 2 = dominant level label, Sentence 3 = structural observation the table rows don't convey. This prevents the model from satisfying C-14 with generic templates ("The org has several teams...") by specifying the finding each sentence must reference. No other R2 variation prescribes at sentence granularity.

**3. IA-PHASE gate token unlocking subsequent sub-phases**
Phase 4a emits IA-PHASE-COMPLETE with the explicit statement "Standard and specialized role files may now be written." This gate token is the entry condition for 4b and 4c — it makes IA omission structurally impossible by the same mechanism V-05 uses throughout: a named token that must appear before the next write can begin.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-gate chain: each phase requires prior gate token in output as entry condition, making phase-skipping a visible protocol violation rather than a silent omission", "sentence-level prose prescription: each required prose sentence assigned a discrete content contract (specific finding it must reference), preventing generic templates from satisfying the narrative prose criterion"]}
```
