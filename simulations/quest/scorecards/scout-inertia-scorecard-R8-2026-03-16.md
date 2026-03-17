# scout-inertia — Quest Score R8

## Rubric v8 Scoring

---

### V-01 — Tabular column schema

**Axis**: Output format — every section uses pre-specified table template with column schema
**Targets**: A-13, A-14, A-16

#### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | Section 2 table has explicit fields: "Workaround name (specific tool/file type/procedure name)", "Role that performs it", "Ongoing cost with unit (e.g., 2 hours/week)"; rule prohibits generic labels |
| C-02 | Switching cost quantified | **PASS** | Section 3 table lists all 4 cost categories with column schema requiring units; rule states "Every estimate must carry a unit… 'Significant' without a number fails" |
| C-03 | Inertia threat score declared | **PASS** | Section 4 table has explicit "Threat score (HIGH / MEDIUM / LOW)" field; default HIGH stated; deviation requires quantified condition |
| C-04 | Defeat conditions identified | **PASS** | Section 5 DC table requires 2+ rows; falsifiability rule with pass/fail example embedded in rules block |
| C-05 | Failure modes identified | **PASS** | Section 1 FM Inventory table requires 2+ rows; Actor and Trigger are named columns; rules prohibit "sometimes" or role-less entries |

All essential criteria: **PASS** (100/100)

#### Advanced Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-10 | Fail-first declaration | **PASS** | Section 1 is "FAILURE MODE INVENTORY" (C-05) — structurally first before workaround profile; opening framing is analytic ("answer the central question: Why does inertia lose?"), no advocacy-first vocabulary collision |
| A-11 | Embedded question per criterion | **FAIL** | No per-criterion embedded questions within authoring sections; structural enforcement is via table column schema and section rules, not prose prompts |
| A-12 | BRIDGE dual-closure | **FAIL** | No Q3/Q4 named bridge artifacts; FM Inventory has Actor and Trigger as columns but neither is named as a closing bridge artifact |
| A-13 | Tabular column schema | **PASS** | FM Inventory exposes FM→Actor and FM→Trigger as named columns — blank cells visible without full read; DC table exposes FM Reference column; Switching Cost table exposes Estimate and Unit columns |
| A-14 | FM Inventory dedicated named table | **PASS** | Section 1 titled "FAILURE MODE INVENTORY"; FM-[N] is first column; table appears before Section 5 DC table; satisfies pre-assignment structural requirement |
| A-15 | Trailing completeness checklist | **PASS** | "COMPLETENESS CHECK" section at output end; per-criterion verification items present |
| A-16 | FM Inventory primary key constraint declared | **PASS** | Bold callout in Section 1 body: "PRIMARY KEY CONSTRAINT: No FM-[N] identifier may appear in any downstream section unless it has an assigned row in this table"; reinforced by referential integrity rule in Section 5 header |
| A-17 | Question-per-criterion full coverage (all 5) | **FAIL** | Section rules and table schema enforce criteria structurally but no criterion-labeled embedded questions within authoring sections; A-11 and A-17 both require prompts, not just constraints |
| A-18 | Trailing checklist binary format + full coverage | **PASS** | COMPLETENESS CHECK uses "| Criterion | Check (Y / N) |" binary column format; all five C-01 through C-05 criteria listed with criterion codes |

Advanced subtotal: A-10(5) + A-13(5) + A-14(5) + A-15(5) + A-16(5) + A-18(5) = **30/45**

**V-01 Total: 130/145**

---

### V-02 — Lifecycle emphasis (fail-first declaration)

**Axis**: Lifecycle emphasis — failure modes section structurally first
**Targets**: A-10

#### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround named specifically | **PASS** | Section 2 has explicit questions: "What is the specific name… not 'a manual process'… Who performs it… What is the ongoing cost per week or sprint, with a unit?"; pass/fail example embedded |
| C-02 | Switching cost quantified | **PASS** | Section 3 lists 4 named categories; "Each entry must carry a number and a unit. 'Significant' without a unit fails" — unit requirement explicit |
| C-03 | Inertia threat score declared | **PASS** | Section 4 has fill-in "Inertia threat score: ___"; deviation requires "specific quantified condition (a percentage, threshold, or measurable state)" |
| C-04 | Defeat conditions identified | **PASS** | Section 5 requires 2+ falsifiable conditions; embedded question "at what point does this failure become severe enough that teams abandon the workaround?"; pass/fail example present |
| C-05 | Failure modes identified | **PASS** | Section 1 explicitly labeled "(C-05 — answer first)"; requires 3-part answers: what goes wrong / who experiences it / what triggers it; minimum 2 failure modes numbered FM-01, FM-02 |

All essential criteria: **PASS** (100/100)

#### Advanced Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-10 | Fail-first declaration | **PASS** | Section 1 is "WHERE THE WORKAROUND FAILS (C-05 — answer first)"; opening: "Start there. The first question is always: where does the current workaround fail? Answer that before you describe the workaround itself." No advocacy framing before failure analysis |
| A-11 | Embedded question per criterion | **PASS** | Each criterion has an embedded prompt: Section 1 (C-05) — "answer three things"; Section 2 (C-01) — "Answer these before writing"; Section 3 (C-02) — "For each cost: Name… State… Name"; Section 4 (C-03) — "Inertia threat score: ___"; Section 5 (C-04) — "ask: at what point does this failure become severe enough?" |
| A-12 | BRIDGE dual-closure | **FAIL** | No Q3/Q4 named bridge artifacts; FM identifier chain is present but no explicitly named closing bridge for FM→actor and FM→trigger |
| A-13 | Tabular column schema | **FAIL** | Prose format throughout; FM entries use numbered list structure, not column-schema tables; blank cells not available as visibility mechanism |
| A-14 | FM Inventory dedicated named table | **FAIL** | Section 1 is FM section in prose form — numbered FM entries, not a titled table with FM-[N] as first column; no dedicated named table pre-assigns identifiers |
| A-15 | Trailing completeness checklist | **FAIL** | "COMPLETENESS REVIEW" section header present but body is empty ("Before submitting, verify:" with no items listed); verification section declared but not populated |
| A-16 | FM Inventory primary key constraint | **FAIL** | No FM Inventory table; no primary key constraint statement anywhere in template body |
| A-17 | Question-per-criterion full coverage (all 5) | **PASS** | All five sections are criterion-labeled in headers (C-05, C-01, C-02, C-03, C-04); each has criterion-labeled embedded prompts; all five covered |
| A-18 | Trailing checklist binary format + full coverage | **FAIL** | COMPLETENESS REVIEW section has no items — no binary checkboxes, no criterion coverage |

Advanced subtotal: A-10(5) + A-11(5) + A-17(5) = **15/45**

**V-02 Total: 115/145**

---

## Composite Scores and Ranking

| Rank | Variation | Essential | Advanced | Total | All Essential Pass |
|------|-----------|-----------|----------|-------|--------------------|
| 1 | V-01 | 100/100 | 30/45 | **130/145** | Yes |
| 2 | V-02 | 100/100 | 15/45 | **115/145** | Yes |

---

## Excellence Signals from V-01

**1. Bidirectional referential integrity enforcement**
The primary key constraint is stated at the FM Inventory assignment point (Section 1 bold callout) AND reinforced as a separate referential integrity rule at the DC table reference point (Section 5 rule block). This creates structural enforcement at both ends of the identifier chain — a template author can fail at either the source or the citation point but will see a named rule at whichever end they violated. A-16 captures only the source constraint; the reinforcement at the citation point is additional structure not yet reflected in any criterion.

**2. Inline example format embedded in table cell label definitions**
The Switching Cost table defines "Ongoing cost with unit" as a column label and embeds "(e.g., 2 hours/week)" directly in the Section 2 table cell label. This reduces unit-ambiguity in the tabular prompt without requiring a separate instructional prose block — the example is structurally co-located with the cell that must be filled. Prior criteria specify that units are required; this pattern specifies where the reminder lives.

---

## A-12 Status

A-12 (BRIDGE dual-closure) fails in both V-01 and V-02 — consistent with its history of never passing R5–R7. V-01 satisfies the structural prerequisites the rubric identifies as necessary for A-12 to become achievable (A-10 + A-13 + A-14 + A-16 are all present), but the explicit Q3/Q4 naming convention for bridge artifacts is absent. This is the identified gap for V-05 design in R8.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Bidirectional referential integrity — primary key constraint stated at FM Inventory assignment point AND reinforced as rule at DC table reference point; structural enforcement at both ends of the identifier chain without requiring full-read compliance", "Inline example format in table cell label definitions — embedding unit examples directly in cell header (e.g., '2 hours/week') co-locates the unit requirement with the field that must be filled, eliminating the need for a separate instructional prose block"]}
```
