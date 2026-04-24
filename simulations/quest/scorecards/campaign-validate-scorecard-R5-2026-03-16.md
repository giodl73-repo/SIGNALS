# campaign-validate — Quest Score R5

## Scoring Pass

---

### V-01 — C-01 Fix on R4 V-01 Pipeline

| Tier | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01 | **PASS** | All 5 listed explicitly: listen-adoption, listen-feedback, review-users, review-design, review-code. No review-customers. |
| Essential | C-02 | **PASS** | "Rank ALL findings by adoption impact — not by severity." |
| Essential | C-03 | **PASS** | Explicit GO / NO-GO / CONDITIONAL GO section with named conditions. |
| Essential | C-04 | **PASS** | Source Sub-Skill column in ranked findings table; verdict attributes blockers. |
| Essential | C-05 | **PASS** | Write instruction to `simulations/{{topic}}/validate-{{date}}.md`. |
| Recommended | C-06 | **PASS** | Cross-Signal Synthesis section with anti-concatenation rule (prose). |
| Recommended | C-07 | **PASS** | Phase 1–5 labeled sections. |
| Recommended | C-08 | **PASS** | P1/P2/P3 tiers applied in all phases. |
| Aspirational | C-09 | **PASS** | "Segment Affected (~N%)" column in ranked findings table. |
| Aspirational | C-10 | **PASS** | Remediation in CONDITIONAL GO: "Name each condition explicitly." |
| Aspirational | C-11 | **FAIL** | No pre-declared table skeleton per sub-skill; phases are prose instructions only. |
| Aspirational | C-12 | **PASS** | Severity and Adoption Impact are separate columns. |
| Aspirational | C-13 | **PASS** | "Confirm with: `Artifact written: …`" present. |
| Aspirational | C-14 | **PASS** | Categorical separation declared: "listen-feedback and listen-adoption are categorically different questions. Do NOT merge." |
| Aspirational | C-15 | **PASS** | All five Rogers segments with % anchors in Phase 1. |
| Aspirational | C-16 | **PASS** | "Status-Quo Workaround" is a required column in the ranked findings table. |
| Aspirational | C-17 | **PARTIAL** | Adoption-first sequencing enforces some cascade, but no explicit schema architecture declaration. Same R4 finding: cascade via ordering logic, not deliberate schema design. |
| Aspirational | C-18 | **PASS** | "Switching Cost" is a required column in the ranked findings table. |
| Aspirational | C-19 | **FAIL** | No pre-declared required rows in phase sections; absent content = absent prose. |
| Aspirational | C-20 | **FAIL** | Synthesis is a prose section with document-level anti-concatenation rule. Not a table with per-row constraint. |
| Aspirational | C-21 | **FAIL** | Only one explicit table (ranked findings). Sub-skill coverage, P1 blockers+remediation, synthesis, Rogers segments not in dedicated tables. |
| Aspirational | C-22 | **FAIL** | Remediation lives in CONDITIONAL GO verdict prose, not as a required column in a dedicated blockers table. |

**Score: 60 + 30 + 42.5 = 132.5 / 160**
All essential: PASS

---

### V-02 — Synthesis Table Axis (C-20)

| Tier | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01–C-05 | **PASS** (all) | Same as V-01: review-code present, all 5 sub-skills, verdict, attribution, artifact instruction. |
| Recommended | C-06–C-08 | **PASS** (all) | Synthesis now a dedicated table; phases labeled; P1/P2/P3 throughout. |
| Aspirational | C-09 | **PASS** | Segment (~N%) column present. |
| Aspirational | C-10 | **PASS** | Remediation in verdict framing. |
| Aspirational | C-11 | **FAIL** | No sub-skill table skeleton; phases remain prose instructions. |
| Aspirational | C-12 | **PASS** | Separate Severity / Adoption Impact columns. |
| Aspirational | C-13 | **PASS** | Confirm string present. |
| Aspirational | C-14 | **PASS** | Categorical separation declared. |
| Aspirational | C-15 | **PASS** | All five Rogers segments with % anchors. |
| Aspirational | C-16 | **PASS** | Workaround column in ranked findings table. |
| Aspirational | C-17 | **PARTIAL** | Synthesis table is a structural decision but cascade not explicitly declared as schema architecture. |
| Aspirational | C-18 | **PASS** | Switching Cost column. |
| Aspirational | C-19 | **FAIL** | Required rows not pre-declared. |
| Aspirational | C-20 | **PASS** | Synthesis encoded as dedicated table with named per-row anti-concatenation constraint. Each row must name a relationship not visible in either sub-skill alone. |
| Aspirational | C-21 | **FAIL** | Two tables now (ranked findings + synthesis), but sub-skill coverage, blockers+remediation, and Rogers segments still in prose. Not one-table-per-concern for all five concerns. |
| Aspirational | C-22 | **FAIL** | Remediation remains in verdict prose. Verdict does not reference a blockers table by row. |

**Score: 60 + 30 + 47.5 = 137.5 / 160**
All essential: PASS

---

### V-03 — Remediation Column Axis (C-22)

| Tier | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01–C-05 | **PASS** (all) | review-code present; all 5 sub-skills; verdict; attribution; artifact write. |
| Recommended | C-06–C-08 | **PASS** (all) | Synthesis prose with anti-concatenation; labeled phases; P1/P2/P3. |
| Aspirational | C-09 | **PASS** | Segment (~N%) column. |
| Aspirational | C-10 | **PASS** | Remediation as required column in dedicated blockers table — full pass (upgraded from PARTIAL). |
| Aspirational | C-11 | **FAIL** | Table skeleton per sub-skill not present; phases still prose. |
| Aspirational | C-12 | **PASS** | Severity / Adoption Impact separate columns. |
| Aspirational | C-13 | **PASS** | Confirm string. |
| Aspirational | C-14 | **PASS** | Categorical separation declared. |
| Aspirational | C-15 | **PASS** | All five Rogers segments with % anchors. |
| Aspirational | C-16 | **PASS** | Workaround column. |
| Aspirational | C-17 | **PARTIAL** | Blockers table adds structural weight but cascade not declared as an explicit schema architecture decision. |
| Aspirational | C-18 | **PASS** | Switching Cost column. |
| Aspirational | C-19 | **FAIL** | Required rows not pre-declared. |
| Aspirational | C-20 | **FAIL** | Synthesis remains prose; no per-row table constraint. |
| Aspirational | C-21 | **FAIL** | Two tables (ranked findings + P1 blockers), but sub-skill coverage, synthesis, Rogers segments still in prose. |
| Aspirational | C-22 | **PASS** | Remediation is a required column in the dedicated P1 blockers table. Verdict references table rows and explicitly does not restate remediations. |

**Score: 60 + 30 + 47.5 = 137.5 / 160**
All essential: PASS

---

### V-04 — One-Table-Per-Concern Schema Declaration (C-21)

| Tier | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01–C-05 | **PASS** (all) | review-code; all 5 sub-skills; verdict; attribution; artifact write. |
| Recommended | C-06–C-08 | **PASS** (all) | T4 synthesis table satisfies C-06; labeled phases; P1/P2/P3 throughout. |
| Aspirational | C-09 | **PASS** | T5 Rogers segments table with % anchors. |
| Aspirational | C-10 | **PASS** | T3 (P1 blockers) has Remediation as required column. |
| Aspirational | C-11 | **PASS** | T1 (sub-skill coverage table) serves as completeness gate: 5 pre-declared rows, absent content is a visible blank. |
| Aspirational | C-12 | **PASS** | T2 ranked findings has separate Severity / Adoption Impact columns. |
| Aspirational | C-13 | **PASS** | Confirm string. |
| Aspirational | C-14 | **PASS** | Categorical separation declared. |
| Aspirational | C-15 | **PASS** | T5 names all five Rogers segments with % anchors. |
| Aspirational | C-16 | **PASS** | Workaround as required column in T2 or T3. |
| Aspirational | C-17 | **PASS** | Explicitly declared: T5 schema decision (Rogers rows + required columns) satisfies C-09 / C-15 / C-16 / C-18 in a single architectural choice. Schema cascade note explicitly encodes C-17. |
| Aspirational | C-18 | **PASS** | Switching Cost as required column in T2. |
| Aspirational | C-19 | **PASS** | T5 Rogers rows pre-declared (5 segments); T3 P1 blocker rows pre-declared. Absent content = visible blank, not absent prose. |
| Aspirational | C-20 | **FAIL** | T4 exists as a dedicated synthesis table, but the per-row anti-concatenation constraint is not the axis. V-04 declares the table schema; it does not declare the per-row constraint within T4. |
| Aspirational | C-21 | **PASS** | 5-table schema declared upfront with single-concern labels (T1: coverage, T2: ranked findings, T3: blockers+remediation, T4: synthesis, T5: Rogers segments). Mixing concerns named as schema violation. |
| Aspirational | C-22 | **PASS** | T3 Remediation column is a required position. Verdict references T3 row numbers; does not restate remediation paths. |

**Score: 60 + 30 + 65 = 155 / 160**
All essential: PASS

---

### V-05 — Full Integration

| Tier | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01–C-05 | **PASS** (all) | review-code; all 5 sub-skills; verdict; attribution; artifact write. |
| Recommended | C-06–C-08 | **PASS** (all) | T4 synthesis table; labeled phases; P1/P2/P3. |
| Aspirational | C-09 | **PASS** | T5 Rogers table with (segment, ~N%) format. |
| Aspirational | C-10 | **PASS** | T3 Remediation column — full pass. |
| Aspirational | C-11 | **PASS** | T1 sub-skill coverage table with pre-declared rows functions as completeness gate. |
| Aspirational | C-12 | **PASS** | Separate Severity / Adoption Impact columns in T2. |
| Aspirational | C-13 | **PASS** | Confirm string. |
| Aspirational | C-14 | **PASS** | Categorical separation declared. |
| Aspirational | C-15 | **PASS** | All five Rogers segments with % anchors in T5. |
| Aspirational | C-16 | **PASS** | Status-Quo Workaround as required column. |
| Aspirational | C-17 | **PASS** | Explicit schema cascade note: T5 Rogers table satisfies C-09/C-15/C-16/C-18 as a single declared architectural decision. |
| Aspirational | C-18 | **PASS** | Switching Cost as required column in T2. |
| Aspirational | C-19 | **PASS** | Required rows pre-declared in T1 (5 sub-skills), T3 (P1 blockers), T5 (5 Rogers segments). |
| Aspirational | C-20 | **PASS** | T4 is a dedicated synthesis table with explicit per-row anti-concatenation constraint: each row must name a relationship not visible in either sub-skill alone. Constraint operates at row granularity. |
| Aspirational | C-21 | **PASS** | 5-table schema declared upfront; each table has single-concern label; combining concerns is a named schema violation. |
| Aspirational | C-22 | **PASS** | Remediation is a required column in T3. Verdict section references T3 by row number; explicitly does not restate paths. |

**Score: 60 + 30 + 70 = 160 / 160**
All essential: PASS

---

## Ranking

| Rank | Variation | Score | All Essential |
|------|-----------|-------|---------------|
| 1 | V-05 Full Integration | **160 / 160** | Yes |
| 2 | V-04 Schema Declaration | **155 / 160** | Yes |
| 3 | V-02 Synthesis Table | **137.5 / 160** | Yes |
| 3 | V-03 Remediation Column | **137.5 / 160** | Yes |
| 5 | V-01 C-01 Fix | **132.5 / 160** | Yes |

All five variations are golden-eligible (all essential pass + composite >= 80).

---

## Excellence Signals

**V-05 vs V-04 delta (C-20): +5 pts.** The single gap between V-04 and V-05 is the per-row anti-concatenation constraint in T4. V-04 declares a synthesis table; V-05 additionally enforces at row granularity that each relationship must be invisible in either source sub-skill alone. The constraint is the difference between a table that *contains* synthesis and one that *enforces* synthesis.

**V-04 vs V-02/V-03 delta (C-11, C-17, C-19, C-21, C-22): +17.5 pts.** The 5-table schema declaration is the structural inflection point in this round. Declaring all five analytical concerns upfront with named single-concern labels simultaneously unlocks: T1 as sub-skill completeness gate (C-11), explicit schema cascade (C-17), pre-declared required rows (C-19), one-concern-per-table enforcement (C-21), and remediation as a column position in T3 (C-22). This is the largest single-axis gain in R5.

**Patterns from top scorer (V-05):**

1. **`5-table-schema-as-forcing-function`** — Declaring all five analytical concerns upfront with single-concern labels before execution instructions transforms missing concerns from absent prose into structural gaps. A missing table is visually detectable in a way a missing paragraph is not.

2. **`schema-cascade-explicit-declaration`** — Naming which schema decision satisfies which criterion cluster (T5 Rogers → C-09/C-15/C-16/C-18) is not just a documentation choice; it encodes intentionality about why the table has those specific columns and rows, making future modifications predictable.

3. **`verdict-as-pointer-not-container`** — The verdict section that references T3 by row number and explicitly does not restate remediation paths achieves two things simultaneously: the verdict stays focused on the go/no-go decision, and remediation paths are enforced by column position rather than authorial choice.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": []}
```
