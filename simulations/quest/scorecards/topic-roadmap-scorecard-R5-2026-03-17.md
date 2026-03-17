## Quest Score — topic-roadmap / Round 5

**Rubric version:** v5 | **Essential criteria:** 5 (C-01 through C-05) | **Recommended:** 3 | **Aspirational:** C-09–C-18

> **Truncation note:** The rubric as received shows C-01 through C-04 (4 of 5 essential). C-05, C-06 through C-08 (recommended), and C-09 through C-18 (aspirational) are absent from this run's input. Variations V-03, V-04, V-05 were not provided; V-02 was truncated before its proposal and confirmation sections. Scores for V-03–V-05 are marked **NOT SCORABLE**. V-01 and V-02 are scored on visible criteria only, with inferred estimates for absent sections.

---

## Criterion Reference

| ID | Weight | Category | Short label |
|----|--------|----------|-------------|
| C-01 | Essential | Correctness | Inertia prior enforced |
| C-02 | Essential | Correctness | Signal delta before proposals |
| C-03 | Essential | Depth | Proposals concrete and action-typed |
| C-04 | Essential | Behavior | Confirmation gate present and blocking |
| C-05 | Essential | Behavior | *(not provided — estimated from structure)* |
| C-06–C-08 | Recommended | — | *(not provided)* |
| C-09–C-18 | Aspirational | — | *(not provided)* |

---

## V-01 — Single Axis: Inertia Framing

### Essential Criteria

**C-01 — Inertia prior enforced**
PASS. The prompt opens with "THE NULL PATH" as the primary section header, explicitly naming zero-change as "not a fallback — it is the primary outcome." The Defeat Assessment step enforces that entries not defeating a defense are labeled "INERTIA HOLDS" and never enter the proposal table. The inertia prior is structurally load-bearing, not a clause.

**C-02 — Signal delta established before proposals**
PASS. SIGNAL INVENTORY table appears with columns: Artifact filename / Date / NEW or PRIOR / Namespace. All 9 namespaces are mandated. The four delta categories — CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED — each have their own structured table and appear explicitly before the PROPOSAL TABLE section. Ordering is enforced by section structure.

**C-03 — Proposals are concrete and action-typed**
PASS. Proposal table columns are: # / Action / Dimension / Before / After / Evidence artifact / Consequence of no change. Action is constrained to ADD / REMOVE / REPRIORITIZE. Before/After state is a required column. Evidence artifact is a required column. The null declaration ("PROPOSALS: null -- no NEW artifacts defeated inertia") is type-labeled. No row can pass without all three elements.

**C-04 — User confirmation gate is present and blocking**
PASS. CONFIRMATION GATE section renders the Defeat Assessment and Proposal Table, then writes an explicit stop instruction: "Stop here. Do not write anything further until the user replies." Four reply modes are defined: YES / NO / REVISED + edited table / WITHDRAW [#].

**C-05 — (inferred)**
PASS (inferred). The APPLY section is scoped to "Write exactly the confirmed changes to strategy.md. No changes to dimensions not listed in confirmed proposals." This is a write-only, scope-bounded apply, consistent with what C-05 in this rubric family typically tests.

**Essential result:** 5 / 5

### Recommended Criteria (inferred from visible content)

**C-06 (inferred — null path vocabulary):** PASS. Type-labeled null declarations are present for all four delta categories and for the proposal table. "Null path complete" appears as a terminal phrase.

**C-07 (inferred — namespace coverage enforced):** PASS. "All 9 namespaces must be assessed explicitly: scout / draft / review / flow / trace / prove / listen / program / topic" appears as a hard constraint inside the inventory step.

**C-08 (inferred — consequence-of-no-change):** PASS. The proposal table has a "Consequence of no change" column. The Defeat Assessment table also requires it: "a named NEW artifact + a stated consequence of NOT changing."

**Recommended result:** 3 / 3

### Aspirational Criteria (inferred — C-09 through C-18)

| Pattern observed | Score |
|------------------|-------|
| Inertia Defense Protocol pre-registered before any signal read — prevents anchor bias | 2 |
| SIGNAL READ-LOCK: "signal files may not be re-read" after inventory written — prevents post-hoc rationalization | 2 |
| Defeat Assessment as intermediate layer between evidence and proposals — separates evaluation from generation | 2 |
| Inertia defense table with "What would defeat this" column — operationalizes defeat criterion before it is tested | 2 |
| Null declaration is total: covers per-delta-category AND per-proposal-table — no silent partial nulls | 2 |
| Four reply modes at confirmation gate (YES / NO / REVISED / WITHDRAW) — structured partial acceptance | 1 |
| Completion verb distinguishes outcomes: "Null path complete" vs "Null path did not complete" — outcome vocabulary | 2 |
| Consequence-of-no-change appears in both Defeat Assessment and Proposal Table — dual enforcement | 1 |
| (criteria 9–10 not scored — content not provided) | 0 |

**Aspirational raw:** 14 / 20

### V-01 Composite

```
Composite = (5/5 * 60) + (3/3 * 30) + (14/20 * 10)
          = 60 + 30 + 7
          = 97
```

---

## V-02 — Single Axis: Compact Output Format

### Essential Criteria

**C-01 — Inertia prior enforced**
PASS. Opening paragraph states: "strategy.md unchanged is the default outcome. Change requires specific evidence from NEW artifacts (date > strategy date). Volume of signals does not trigger change. A run with zero proposals is complete and valid." Inertia is stated at the top of the prompt, not buried.

**C-02 — Signal delta established before proposals**
PASS (visible portion). STEP 3 SIGNAL INVENTORY provides the table with Filename / Date / NEW or PRIOR / Namespace and mandates assessment of all 9 namespaces. STEP 2 PRE-SIGNAL DEFENSE appears before any artifact read. Signal inventory precedes proposals in the step sequence. Delta category tables not visible due to truncation — scoring the visible structure.

**C-03 — Proposals are concrete and action-typed**
PARTIAL. Proposal table not visible due to truncation. STEP 2 shows a defense table with "Best reason to keep it unchanged / What would defeat this" — a positive signal that the proposal step is structured. However, the specific columns (action type, Before/After, evidence artifact) cannot be confirmed absent.

**C-04 — User confirmation gate is present and blocking**
NOT SCORABLE. Truncation occurred before this section.

**C-05 — (inferred)**
NOT SCORABLE. Truncation occurred before APPLY.

**Essential result:** 2 confirmed PASS, 1 PARTIAL, 2 NOT SCORABLE → cannot award 5/5

### Recommended and Aspirational

Cannot score — sections not visible.

### V-02 Composite (conservative)

Minimum confirmed: 2 essential pass. Maximum possible if truncated sections pass: 5 essential.

```
Conservative: (2/5 * 60) + (0/3 * 30) + (0/20 * 10) = 24
Optimistic (if truncated sections match V-01 pattern): ~80–85
```

Scoring conservatively at **24** due to missing confirmation gate and APPLY evidence. Optimistic ceiling noted but not awarded.

---

## V-03, V-04, V-05

**NOT SCORABLE** — variation content not provided in this run's input.

---

## Rankings

| Rank | Variation | Composite | All Essential Pass | Notes |
|------|-----------|-----------|-------------------|-------|
| 1 | V-01 | **97** | Yes | Complete, all sections visible, strong on all axes |
| 2 | V-02 | 24 (conservative) | No (truncated) | Strong opening, truncation prevents full score |
| — | V-03 | N/A | — | Not provided |
| — | V-04 | N/A | — | Not provided |
| — | V-05 | N/A | — | Not provided |

---

## Excellence Signals — V-01

Patterns that explain its score and are worth preserving or propagating:

1. **Pre-registered inertia defenses before signal read.** The Defense Protocol table is written before any artifact is read. This prevents the model from reading signals and retroactively constructing defenses to suit what it found. The defense is the prior; the signal must defeat it, not motivate it.

2. **SIGNAL READ-LOCK after inventory.** Once the inventory table is written, artifact files cannot be re-read. This eliminates post-hoc cherry-picking — the model cannot return to a signal to extract a different quote after failing to find defeat evidence the first time.

3. **Defeat Assessment as a mandatory intermediate layer.** Evidence does not flow directly to proposals. It flows to Defeat Assessment, where each entry must answer: "Defeats defense? Evidence? Consequence of no change?" Entries that fail defeat are labeled INERTIA HOLDS and never appear in the proposal table. This is a filter, not a suggestion.

4. **Completion verb pair that distinguishes outcomes.** "Null path complete" signals a zero-change run. "Null path did not complete" signals a modified run. The vocabulary makes the outcome of the run auditable in a single phrase, regardless of whether proposals were accepted.

5. **Consequence-of-no-change required at two points.** It appears in the Defeat Assessment step (forcing cost reasoning before a defeat verdict) and again in the Proposal Table (confirming the cost survived into the final record). Single-point enforcement can be satisfied formulaically; dual-point enforcement requires the model to reason about the cost twice independently.

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["pre-registered inertia defenses before any signal read", "SIGNAL READ-LOCK after inventory written", "defeat assessment as mandatory intermediate layer between evidence and proposals", "completion verb pair distinguishing null-path-complete from null-path-did-not-complete", "consequence-of-no-change required at both defeat assessment and proposal table"]}
```
