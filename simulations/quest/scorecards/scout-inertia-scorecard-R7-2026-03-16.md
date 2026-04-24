# scout-inertia — Quest Score Round 7

## Scoring System

| Tier | Weight |
|------|--------|
| Essential (C-01 to C-05) | 10 pts each (PASS) / 5 pts (PARTIAL) / 0 (FAIL) |
| Recommended (R-01 to R-03) | 5 pts each / 2 pts (PARTIAL) / 0 (FAIL) |
| Advanced (A-08, A-10–A-15) | 5 pts each / 2–3 pts (PARTIAL) / 0 (FAIL) |
| **Ceiling** | **100** |

> **Note**: V-05 prompt text was not provided. The axis map lists it as "Tabular + FM inventory + BRIDGE dual-closure (A-13 + A-14 + A-12)" but no prompt body exists. Scored as absent below.

---

## V-01 — Role Sequence: FM Analyst First

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | Role 1 requires "actual practice (not 'a manual process')", role, cadence, cost with unit |
| C-02 | Switching cost quantified | **PASS** | Role 2: two categories, units required, "significant without a number fails" |
| C-03 | Inertia threat score declared | **PASS** | Role 2: explicit HIGH/MEDIUM/LOW with default and justification rule |
| C-04 | Defeat conditions identified | **PASS** | Role 3: 3+ conditions, falsifiable, team-type named, FM citation required |
| C-05 | Failure modes identified | **PASS** | Role 1: 3+ FMs with FM-[N] labels, scenario + role + trigger + silent/visible |
| R-01 | Trigger scoped to team type | **PASS** | Role 3: "(a) name a specific team type or segment — not 'users'" |
| R-02 | Role-level precision | **PASS** | Role 1: "name the role affected" per FM; Role 2: cost "cited to a specific role" |
| R-03 | Cost cited to role | **PASS** | Role 2: migration effort "cited to a specific role" |
| A-08 | FM before DC | **PASS** | Role 1 (FM) → Role 2 (Cost) → Role 3 (DC) sequentially enforced |
| A-10 | Fail-first declaration | **PARTIAL** | FM structurally first via role ordering, but no explicit "FAIL-FIRST DECLARATION" label |
| A-11 | Question-per-criterion mapping | **FAIL** | No embedded prompts per criterion; no self-check block |
| A-12 | BRIDGE dual-closure | **FAIL** | No named bridge artifacts; no Q3/Q4 marker closing FM→actor and FM→trigger chains |
| A-13 | Tabular column schema | **FAIL** | Prose role blocks; no column schemas enforced |
| A-14 | FM inventory as dedicated named table | **FAIL** | FM enumerated in prose roles; no titled FM Inventory table |
| A-15 | Trailing completeness checklist | **FAIL** | No trailing section |

**Score: 50 + 15 + 7 = 72/100**

---

## V-02 — Output Format: Tabular Column Schema

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | Section 1 prose: named practice, role, cadence, ongoing cost with unit |
| C-02 | Switching cost quantified | **PASS** | Section 3 table: "Quantified Cost is a number. Unit required; blank Unit cells fail C-02" |
| C-03 | Inertia threat score declared | **PASS** | Section 4: declared value, default HIGH, one-sentence justification rule |
| C-04 | Defeat conditions identified | **PASS** | Section 5 table: "Falsifiable? Y or N — only Y rows count toward C-04 minimum" |
| C-05 | Failure modes identified | **PASS** | Section 2 table: FM-[N] labeling, Trigger Condition, Silent or Visible columns |
| R-01 | Trigger scoped to team type | **PASS** | Section 5: "Team Type" required column |
| R-02 | Role-level precision | **PASS** | Section 2: "Role Affected" column; Section 3: "Role Bearing Cost" column |
| R-03 | Cost cited to role | **PASS** | Section 3: "Role Bearing Cost" required column |
| A-08 | FM before DC | **PASS** | Section 2 (FM) precedes Section 5 (DC) |
| A-10 | Fail-first declaration | **FAIL** | No explicit declaration; Section 1 is Workaround Profile (prose), not FM |
| A-11 | Question-per-criterion mapping | **FAIL** | No embedded per-criterion prompts; column headers serve as implicit but not explicit questions |
| A-12 | BRIDGE dual-closure | **FAIL** | No named bridge artifacts; FM→actor/trigger closure achieved by columns but not named Q3/Q4 |
| A-13 | Tabular column schema | **PASS** | All major sections use named column schemas; blank cell = visible criterion gap |
| A-14 | FM inventory as dedicated named table | **PARTIAL** | "SECTION 2 — FM INVENTORY" titled with FM-[N] assignment before DC table, but no primary key constraint ("no FM-[N] may appear later unless assigned here") |
| A-15 | Trailing completeness checklist | **FAIL** | No trailing section |

**Score: 50 + 15 + 12 = 77/100**

---

## V-03 — Lifecycle Emphasis: Fail-First

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | Section 1: "specific practice, role that owns it, ongoing cost with a unit" |
| C-02 | Switching cost quantified | **PASS** | Section 2: "at least two categories with units. Cite the role bearing each cost." |
| C-03 | Inertia threat score declared | **PASS** | Section 2: "Declare Inertia Threat Score (HIGH default; justify any non-HIGH)" |
| C-04 | Defeat conditions identified | **PASS** | Section 3: 3+ conditions, falsifiable, team type, FM label cited |
| C-05 | Failure modes identified | **PASS** | Section 1: 3+ FMs with FM-[N] labels, scenario + role + trigger + silent/visible |
| R-01 | Trigger scoped to team type | **PASS** | Section 3: "name a team type (not 'users')" |
| R-02 | Role-level precision | **PASS** | Section 1: role per FM; Section 2: role bearing each cost |
| R-03 | Cost cited to role | **PASS** | Section 2: "Cite the role bearing each cost" |
| A-08 | FM before DC | **PASS** | Section 1 (FM) → Section 2 (Cost) → Section 3 (DC) |
| A-10 | Fail-first declaration | **PASS** | "FAIL-FIRST DECLARATION" used as explicit structural label with justification text |
| A-11 | Question-per-criterion mapping | **PARTIAL** | SELF-CHECK covers C-05 (SQ-1), C-02 (SQ-2), C-04 (SQ-3/SQ-4) — missing explicit questions for C-01 and C-03 |
| A-12 | BRIDGE dual-closure | **FAIL** | No named bridge artifacts |
| A-13 | Tabular column schema | **FAIL** | Prose-based; no column schemas |
| A-14 | FM inventory as dedicated named table | **FAIL** | FM enumerated in prose; no titled FM Inventory table |
| A-15 | Trailing completeness checklist | **PARTIAL** | Section 4 SELF-CHECK is trailing and verification-oriented, but uses essay prompts ("answer with one sentence") not binary checkboxes; does not map all 5 essential criteria |

**Score: 50 + 15 + (5+5+3+0+0+0+2) = 50 + 15 + 15 = 80/100**

---

## V-04 — Combined: Tabular Column Schema + FM Inventory Table

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | Section 1: named practice, role, execution cadence, cost with unit |
| C-02 | Switching cost quantified | **PASS** | Section 3 table: "Quantified Cost is a number. Unit required; blank Unit cells fail C-02." Min 2 rows |
| C-03 | Inertia threat score declared | **PASS** | Section 4: declared value, default HIGH, reference to Section 3 cost required for non-HIGH |
| C-04 | Defeat conditions identified | **PASS** | Section 5: "Falsifiable? Y or N; only Y rows count toward C-04 minimum." FM-[N] Link required |
| C-05 | Failure modes identified | **PASS** | Section 2 FM Inventory table: 3+ rows with FM-[N] assignment, Trigger Condition, Failure Type columns |
| R-01 | Trigger scoped to team type | **PASS** | Section 5: "Team Type" required column |
| R-02 | Role-level precision | **PASS** | Section 2: "Role Affected" column; Section 3: "Role Bearing Cost" column |
| R-03 | Cost cited to role | **PASS** | Section 3: "Role Bearing Cost" required column |
| A-08 | FM before DC | **PASS** | Section 2 (FM Inventory) precedes Section 5 (Defeat Conditions) |
| A-10 | Fail-first declaration | **FAIL** | No FAIL-FIRST DECLARATION language; ordering note "(write before Sections 3-5)" is structural constraint, not declaration |
| A-11 | Question-per-criterion mapping | **FAIL** | No embedded per-criterion prompts; no self-check block |
| A-12 | BRIDGE dual-closure | **FAIL** | No named bridge artifacts; DC table FM-[N] Link column closes one chain but unnamed |
| A-13 | Tabular column schema | **PASS** | All sections use named column schemas; blank cells expose criterion gaps without full read |
| A-14 | FM inventory as dedicated named table | **PASS** | "Title this section exactly: 'FM Inventory'"; explicit primary key constraint: "No FM-[N] identifier may appear in any later section unless it was first assigned here" |
| A-15 | Trailing completeness checklist | **FAIL** | No trailing section |

**Score: 50 + 15 + (5+0+0+0+5+5+0) = 50 + 15 + 15 = 80/100**

---

## V-05 — Combined: Tabular + FM Inventory + BRIDGE dual-closure

**Status: Prompt not provided.** Axis map listed this as the R7 target combination (A-13 + A-14 + A-12) but no prompt body was included in the input.

**Score: N/A**

---

## Rankings

| Rank | Variation | Score | Essential Pass | Key Strengths |
|------|-----------|-------|---------------|---------------|
| **1** | **V-04** | **80/100** | ✓ All 5 | A-13 + A-14 both clean; primary key constraint; column-level criterion annotation |
| **1** | **V-03** | **80/100** | ✓ All 5 | A-10 explicit fail-first; partial A-11 (3/5 criteria); partial A-15 trailing |
| 3 | V-02 | 77/100 | ✓ All 5 | A-13 clean; partial A-14 (titled but no primary key constraint) |
| 4 | V-01 | 72/100 | ✓ All 5 | A-08 clean; partial A-10 via role ordering |
| — | V-05 | N/A | — | Not provided |

**Tie-break V-04 over V-03**: V-04 earns two clean advanced PASSes (A-13 + A-14) where the structural guarantees are mechanically complete. V-03's equivalent advanced points come from partial credit on A-11 and A-15, indicating incomplete implementations of those criteria.

---

## Uniform Failures — R7

- **A-12 (BRIDGE dual-closure)**: Failed all four provided variations. This is the third consecutive round (R5, R6, R7) where no variation achieved BRIDGE naming. The requirement for two explicitly named artifacts (Q3 closes FM→actor, Q4 closes FM→trigger) has not been attempted in prompt form. R8 should target this directly.

---

## Excellence Signals from V-04

**Signal 1 — Primary key constraint formalization**
The phrase "This table is the primary key. No FM-[N] identifier may appear in any later section unless it was first assigned here" creates a typed citation lock at template level, not just ordering preference. This is stronger than A-14 as written — it creates a referential integrity rule, not just positional guidance. A v8 criterion could distinguish "FM table ordered first" (A-14 current) from "FM table as primary key with citation enforcement" (elevated A-14 or A-16).

**Signal 2 — Column-level criterion failure annotation**
V-04 embeds criterion failure conditions directly in column descriptions: "blank Unit cells fail C-02." This converts the rubric into executable table validation — an author can check their own output against the rubric without consulting an external document. Neither A-13 nor A-14 currently require this annotation; they only require named columns. Annotated column schemas are a distinct and measurable pattern.

**Signal 3 — FM-to-cost linkage (emerging)**
V-04 Section 3 adds "FM-[N] Link" as an optional column in the switching cost table. This creates a chain FM → cost separate from the FM → DC chain that A-12 targets. No rubric criterion currently scores this bridge. If validated in R8, this could become the basis for a third closure type beyond A-12's FM→actor and FM→trigger.

---

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["primary key constraint on FM inventory blocks forward citation of unassigned FM-[N] identifiers", "column-level criterion failure annotation embeds rubric enforcement at template level"]}
```
