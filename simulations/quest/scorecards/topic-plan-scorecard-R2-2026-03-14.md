## /quest:score — topic-plan Round 2

**Rubric**: v2 (125 pts) | **Variations**: V-01, V-02, V-03 | **Trace**: placeholder (prompt-design evaluation)

---

## V-01 — Axis A: Strategy-First

### Essential (60 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Reads strategy.md before proceeding | PASS | Phase 1 is dedicated entirely to strategy.md first; extracts namespaces, rationale, gaps, implicit assumptions before Phase 2 starts. |
| C-02 | Reads signal artifacts before proceeding | PASS | Phase 2 explicitly globs `simulations/{{topic}}/` and reads every artifact; records namespace, skill, date, key finding. |
| C-03 | Identifies delta, not inventory | PASS | Phase 3 has explicit warning: "A plain inventory of signal contents is the failure mode." Forces "Strategy assumed [X]. Signal revealed [Y]." format with a stop condition. |
| C-04 | Proposes typed changes | PASS | Phase 4 requires ADD / REMOVE / REPRIORITIZE with explicit no-change rows if empty. |
| C-05 | Requires user confirmation before writing | PASS | Phase 8: "Reply **apply** to write these changes to strategy.md." Explicit gate. |

Essential: **60/60**

### Recommended (30 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Cites signal evidence per change | PASS | Phase 4 format includes `[artifact]` inline for every ADD/REMOVE/REPRIORITIZE entry. |
| C-07 | Before/after strategy summary | PASS | Phase 5 shows BEFORE / AFTER / WHY diff-style view per changed item. |
| C-08 | Addresses all three change types | PASS | Phase 4 mandates all three with explicit no-change rows. |

Recommended: **30/30**

### Aspirational (35 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Namespace coverage gaps | PASS | Phase 6 lists all 9 by name, requires stage-relative framing explicitly. 5 pts |
| C-10 | Conflicting signals | PASS | Phase 7 dedicated step; if none, must state explicitly. 5 pts |
| C-11 | Typed confirmation verb | PASS | "Reply **apply** to write..." — named verb closes rationalization path. 5 pts |
| C-12 | Explicit no-change rows per type | PASS | Phase 4 shows format for each empty category explicitly. 5 pts |
| C-13 | Inline evidence brackets in diff | PARTIAL | Phase 5 uses WHY as a separate line field, not an inline bracket `[+item: artifact]`. Evidence present but requires one-line cross-reference rather than in-place bracket. 2.5 pts |
| C-14 | Anti-inventory warning at delta step | PASS | Phase 3 opens with the warning at point of execution. 5 pts |
| C-15 | Enumerates all 9 namespaces | PASS | Phase 6: `scout \| draft \| review \| flow \| trace \| prove \| listen \| program \| topic` — explicit list. 5 pts |

Aspirational: **32.5/35**

**V-01 Composite: 122.5/125** | All essential: YES | Golden: YES

---

## V-02 — Axis B: Table-Driven

### Essential (60 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Reads strategy.md before proceeding | PASS | Step 1 reads strategy.md; Step 2 builds Strategy Baseline Table extracting namespaces, rationale, acknowledged gaps. |
| C-02 | Reads signal artifacts before proceeding | PASS | Step 1 reads every signal artifact; Step 3 produces Signal Inventory Table (namespace / skill / date / key finding). |
| C-03 | Identifies delta, not inventory | PASS | Step 4 opens with explicit warning: "NOT what signals exist." Forces "What strategy assumed / What signal revealed" columns. One-row stop condition if no surprises. |
| C-04 | Proposes typed changes | PASS | Step 5 Proposals Table has explicit Type column; no-change row shown as concrete example. |
| C-05 | Requires user confirmation before writing | PASS | Step 9: "Reply **apply** to write all changes to strategy.md." |

Essential: **60/60**

### Recommended (30 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Cites signal evidence per change | PASS | Step 5 table has "Evidence Artifact" column AND "Delta Row" column linking proposal to delta to artifact — two-level traceability. |
| C-07 | Before/after strategy summary | PASS | Step 6 Before/After Diff Table with explicit columns. |
| C-08 | Addresses all three change types | PASS | Step 5 table requires all three types; no-change row shown (`— REMOVE No changes.`). |

Recommended: **30/30**

### Aspirational (35 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Namespace coverage gaps | PASS | Step 7 table lists all 9 namespaces as rows with Stage-Required column — stage-relative assessment structurally enforced. 5 pts |
| C-10 | Conflicting signals | PASS | Step 8 Conflict Table; explicit one-row "No conflicts" statement if none. 5 pts |
| C-11 | Typed confirmation verb | PASS | Step 9: "Reply **apply**..." 5 pts |
| C-12 | Explicit no-change rows per type | PASS | Step 5 shows `— REMOVE No changes. — — —` as a concrete example row. Structural, not instructed. 5 pts |
| C-13 | Inline evidence brackets in diff | PASS | Step 6 diff table has dedicated `[Evidence]` column with inline bracket `[market-signal-YYYY.md]` on each changed row. Evidence travels with the item. 5 pts |
| C-14 | Anti-inventory warning at delta step | PASS | Step 4 opens: "This table records what signals revealed... NOT what signals exist." At the point of execution. 5 pts |
| C-15 | Enumerates all 9 namespaces | PASS | Step 7 table rows: scout / draft / review / flow / trace / prove / listen / program / topic — all 9 explicit. 5 pts |

Aspirational: **35/35**

**V-02 Composite: 125/125** | All essential: YES | Golden: YES

---

## V-03 — Axis C: Inertia Framing

**Status: Prompt truncated.** V-03 contains only the opening line (`You are executing /topic:plan...`). No instructions for reading inputs, delta analysis, proposals, or confirmation gate are present.

### Essential (60 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Reads strategy.md | FAIL | No instruction present. |
| C-02 | Reads signal artifacts | FAIL | No instruction present. |
| C-03 | Identifies delta | FAIL | No instruction present. |
| C-04 | Proposes typed changes | FAIL | No instruction present. |
| C-05 | Requires confirmation | FAIL | No instruction present. |

Essential: **0/60** — all essential fail; score capped.

Recommended: **0/30** | Aspirational: **0/35**

**V-03 Composite: 0/125** | All essential: NO | Golden: NO

*(Note: The inertia-framing hypothesis — treating no-change as the default outcome — is a valid design axis and worth completing. The truncation is the failure, not the concept.)*

---

## Rankings

| Rank | Variation | Score | All Essential | Golden |
|------|-----------|-------|---------------|--------|
| 1 | V-02 (Table-Driven) | 125/125 | YES | YES |
| 2 | V-01 (Strategy-First) | 122.5/125 | YES | YES |
| 3 | V-03 (Inertia Framing) | 0/125 (incomplete) | NO | NO |

---

## Excellence Signals — V-02

V-02 achieves perfect score. Three patterns distinguish it from V-01 and from prior rounds:

**1. Traceable change chains via IDs**
Delta rows carry IDs (D-01, D-02…). Proposals table has a "Delta Row" column. Every proposal traces to a delta; every delta traces to an artifact. This makes the delta → proposal chain auditable at a glance rather than requiring prose inference.

**2. Signal inventory as an explicitly-labeled intermediate step**
V-02 separates Step 3 (signal inventory table — "intermediate work only") from Step 4 (delta table). The label "intermediate work only — not the delta" at Step 3 performs the same function as the anti-inventory warning but earlier — it names the difference between the two outputs *before* the delta step, preventing conflation before it can happen.

**3. Stage-Required as a structural column, not prose guidance**
V-02's gap audit table has a mandatory "Stage-Required" column alongside "Signals Present." V-01 says "thin coverage is not automatically a gap — only flag it if the stage requires it" in prose. V-02 makes the stage-relative comparison an explicit column that *must be filled in*, forcing the reasoning structurally rather than relying on instruction compliance.

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["traceable-change-chains: delta IDs linked in proposals table create auditable D-01 -> P-01 -> artifact chain", "labeled-intermediate-step: signal inventory explicitly labeled 'not the delta' before the delta step prevents conflation structurally", "stage-required-column: gap audit forces stage-relative reasoning as a mandatory table column rather than prose instruction"]}
```
