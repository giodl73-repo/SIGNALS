Looking at the three excellence signals from the R6 scorecard, I'll extract them as A-13, A-14, A-15 and rebuild the complete v7 rubric.

---

# scout-inertia Rubric — v7

## Changes from v5 to v6

| # | Change | Source |
|---|--------|--------|
| 1 | **A-09 → baseline** | Universally passed R5; no longer a scoring differentiator |
| 2 | **A-10 strengthened** | "fail-first" declaration requires C-05 section structurally first; advocacy-first use is a vocabulary collision, now explicitly named with V-02/V-04 as the canonical example |
| 3 | **A-11 — Question-per-criterion mapping** | R5 V-05 pattern: one explicit question/prompt per essential criterion; unanswered prompt = structurally visible missing criterion, not a content gap caught on full read |
| 4 | **A-12 — BRIDGE dual-closure** | R5 bridge-marker pattern: two named bridge artifacts — Q3 closes A-06 (FM→actor), Q4 closes A-09 baseline (FM→trigger); structural guarantee, not output property |
| 5 | **Ceiling 110 → 115** | A-09 exits scoring (−5); A-11 +5; A-12 +5 |

## Changes from v6 to v7

| # | Change | Source |
|---|--------|--------|
| 1 | **A-13 — Tabular column schema structural visibility** | R6 V-02 excellence signal: table columns make criterion gaps visible as blank cells without full-read; prose descriptions cannot satisfy this even if comprehensive |
| 2 | **A-14 — FM inventory as dedicated named table** | R6 V-02 excellence signal: FM# pre-assignment in a titled table before the defeat condition table enforces A-08 structurally — FM-[N] identifiers exist as typed references before DC-[N] can cite them |
| 3 | **A-15 — Trailing completeness checklist** | R6 V-02 excellence signal: per-criterion binary checkboxes at output end convert content gaps into visible unchecked items; distinguishes post-hoc verification (A-15) from per-criterion embedded prompts (A-11) |
| 4 | **Ceiling 115 → 130** | A-13 +5; A-14 +5; A-15 +5 |

**Key structural note on A-14 vs A-08**: A-08 requires positional ordering (FM before DC); A-14 requires that ordering to be enforced via a *named inventory table* whose first column assigns FM-[N] identifiers. An output can pass A-08 through prose ordering and fail A-14 for lack of a dedicated table. A-14 implies A-08 but not the reverse.

**Key structural note on A-15 vs A-11**: A-11 requires per-criterion prompts *embedded in the template body* so that unanswered prompts are visible gaps during authoring. A-15 requires a *trailing named checklist* that maps each essential criterion to a binary observable after the output is complete. Both can be present simultaneously; neither substitutes for the other.

**R7 target**: R6 uniformly failed A-12. The high-potential untested combination is A-13 + A-14 + A-12 — tabular column schema (A-13) exposes FM→actor and FM→trigger as column slots, FM inventory table (A-14) pre-assigns FM-[N] before DC-[N] are written, and BRIDGE dual-closure (A-12) names the artifacts that close both chains structurally.

---

## Essential Criteria

*All five must pass. Any essential failure caps the output as non-useful regardless of advanced scores.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-01 | **Workaround named specifically** | specificity | essential |
| C-02 | **Switching cost quantified** | quantification | essential |
| C-03 | **Inertia threat score declared** | assessment | essential |
| C-04 | **Defeat conditions identified** | analysis | essential |
| C-05 | **Workaround failure modes identified** | analysis | essential |

### C-01 — Workaround named specifically

**Pass condition**: Output names the specific workaround currently in use (not "a manual process" but "weekly CSV export to shared drive"), names the role that performs it, and quantifies the ongoing cost with a unit. "The data-ops team spends 2 hours per week exporting and cleaning CSV files before pipeline ingestion" passes. "Teams use manual methods" fails on every dimension.

### C-02 — Switching cost quantified

**Pass condition**: Output identifies and quantifies at least two categories of switching cost: migration effort (time or money, cited to a role), and at least one of: training overhead, process disruption, or in-flight work at risk. Costs must carry units — "significant" without a number or unit fails.

### C-03 — Inertia threat score declared

**Pass condition**: Output declares an explicit inertia threat score (HIGH / MEDIUM / LOW) for the feature. The default is HIGH; any deviation from HIGH must be justified with a quantified condition. An output that lists switching costs without aggregating them into a threat level has not completed the analysis.

### C-04 — Defeat conditions identified

**Pass condition**: Output identifies at least two specific, distinct, and testable conditions under which teams abandon the workaround in favor of the feature. Conditions must be falsifiable ("teams switch when workaround fails to handle files > 10MB" passes; "teams switch when they see the value" fails). This is the central question of the skill — if it is absent, the output is not useful.

### C-05 — Workaround failure modes identified

**Pass condition**: Output identifies at least two specific scenarios where the current workaround breaks, produces errors, causes re-work, or cannot scale. These are the observable cracks in the inertia armor. Generic pain points ("manual is slow") do not pass; concrete failure modes ("CSV export silently truncates rows over 65,536 — no error message") pass.

---

## Recommended Criteria

*Strong outputs satisfy all three. Missing one is a quality signal, not a blocker.*

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| R-01 | **Trigger scoped to team type** | precision | recommended |
| R-02 | **Role-level precision** | precision | recommended |
| R-03 | **At least one cost cited to role** | depth | recommended |

### R-01 — Trigger scoped to team type

**Pass condition**: Defeat conditions (from C-04) name a specific team type or segment rather than applying uniformly to all users. "Engineering teams switch when..." or "PMs in regulated industries switch when..." passes. "Users switch when..." fails. Different team types face different inertia profiles; a trigger that ignores team type is underspecified.

### R-02 — Role-level precision

**Pass condition**: Every actor named in the analysis (workaround performer, decision-maker, affected party) is identified at role level, not department or group level. "The PM" or "a data analyst" passes. "The team", "users", or "marketing" fails. Role-level precision is required because switching cost and trigger conditions vary by role — a department label cannot carry that weight.

### R-03 — At least one cost cited to role

**Pass condition**: At least one quantified cost from C-02 is tied to a specific actor or role named in the analysis. "The data-ops team spends 2h/week" becomes "the data-ops engineer spends 2h/week" — role specificity transforms a cost category into an ownership claim. Department attribution does not pass.

---

## Advanced Criteria

*Ceiling scores. Missing any is acceptable; achieving all signals a structurally excellent output.*

| ID | Criterion | Category | Points |
|----|-----------|----------|--------|
| A-08 | **FM numbers precede defeat conditions** | ordering | +5 |
| A-09 | *(baseline — universally passed R5, not scored)* | — | — |
| A-10 | **C-05 structurally first (fail-first)** | structure | +5 |
| A-11 | **Question-per-criterion mapping** | completeness | +5 |
| A-12 | **BRIDGE dual-closure** | closure | +5 |
| A-13 | **Tabular column schema structural visibility** | visibility | +5 |
| A-14 | **FM inventory as dedicated named table** | structure | +5 |
| A-15 | **Trailing completeness checklist** | verification | +5 |

**Ceiling: 130**

### A-08 — FM numbers precede defeat conditions

**Pass condition**: Output assigns FM-[N] identifiers to all failure modes before any defeat condition (DC-[N]) is written. The failure mode inventory must appear as a section or table that precedes the defeat conditions section or table. Positional ordering is a structural requirement, not a prose recommendation — FM-[N] must be assigned and visible before DC-[N] references them. An output that names failure modes in prose and then assigns numbers inline within the defeat conditions section does not pass.

### A-09 — *(baseline — not scored)*

A-09 is retained for numbering continuity. It universally passed in R5 and no longer differentiates output quality. Any output satisfying C-04 and C-05 will satisfy A-09.

### A-10 — C-05 structurally first (fail-first)

**Pass condition**: The output names inertia failure modes (C-05 content) as the first substantive analytical section — before workaround costs, before defeat conditions, before threat score declaration. The rationale: understanding *how the workaround breaks* is the prerequisite for all downstream analysis. "Fail-first" here means *failure modes first*, not test-driven fail-first; outputs that use "fail-first" to mean advocacy-first are applying a vocabulary collision (V-02/V-04 is the canonical example) and do not pass A-10. An output that satisfies C-05 late in the document does not pass A-10 regardless of prose quality. A role registry or workaround profile section appearing before the FM section does not invalidate A-10 if the FM section is the first *analytical* section; non-analytical preamble is exempt.

### A-11 — Question-per-criterion mapping

**Pass condition**: The template or prompt structure contains one explicit question or prompt corresponding to each essential criterion (C-01 through C-05), embedded in the template body. An unanswered prompt is a structurally visible missing criterion — the blank or absent answer is detectable without reading the full output. Outputs where criteria are satisfied through undifferentiated prose, or where all criteria are covered by a single composite prompt, do not pass A-11. Note: a trailing checklist (A-15) is not a substitute for per-criterion embedded prompts; the distinction is *when* the gap becomes visible — during authoring (A-11) versus after completion (A-15).

### A-12 — BRIDGE dual-closure

**Pass condition**: Output contains two named bridge artifacts that close the FM-to-analysis chains:

- **BRIDGE-ACTOR (Q3)**: A named section that maps each FM-[N] identifier to the specific actor role who experiences that failure mode. This closes the A-06 chain (FM→actor).
- **BRIDGE-TRIGGER (Q4)**: A named section that maps each FM-[N] identifier to the defeat condition (DC-[N]) that the failure mode enables. This closes the A-09 chain (FM→trigger).

Both bridge markers must be present by name. A well-written output that connects FMs to actors and triggers through prose does not pass A-12 — the named markers must be structural: their absence causes visible damage to the output skeleton. Satisfying A-06 and C-04 via prose logic is not sufficient.

### A-13 — Tabular column schema structural visibility

**Pass condition**: Output uses a table schema where each column maps to a distinct required criterion field — for example, a dedicated "Unit" column for C-02, a dedicated "Team type" column for R-01, a dedicated "Connected FM#" column for C-04. A blank cell in any required column is a structurally visible missing criterion: no full-read is required to detect the gap. Prose descriptions, even if comprehensive, do not pass A-13. The criterion is about *format as enforcer*: the blank cell must be distinguishable from a filled cell without reading surrounding context. Outputs that use tables incidentally (e.g., a summary table appended after prose) do not pass if the primary criterion evidence is still carried in prose.

### A-14 — FM inventory as dedicated named table

**Pass condition**: Failure modes are collected in a dedicated, titled table — not inline prose, not a numbered list, not a bullet list — and this table appears before any defeat condition table or defeat condition section. The table must assign FM-[N] identifiers as the first column. This criterion strengthens A-08: A-08 requires positional ordering (FM before DC); A-14 requires that ordering to be enforced via a named inventory table so that FM-[N] identifiers exist as typed, citable references before any DC-[N] is written. An output can pass A-08 through prose ordering and fail A-14 for lack of a dedicated table. A-14 implies A-08; A-08 does not imply A-14.

### A-15 — Trailing completeness checklist

**Pass condition**: Output ends with a named completeness section containing one binary observable (checkbox, PASS/FAIL, Y/N) per essential criterion (C-01 through C-05). An unchecked or failed item names the specific criterion gap without requiring re-read of the full output. The checklist must be a trailing, named section — not inline commentary, not embedded in the analysis body, not a preamble. Post-hoc verification via named trailing checklist is the pass condition. Per-criterion prompts embedded in the template body (A-11) do not substitute for A-15 and vice versa. An output can satisfy both: A-11 makes gaps visible *during authoring*, A-15 makes gaps visible *after completion*.
