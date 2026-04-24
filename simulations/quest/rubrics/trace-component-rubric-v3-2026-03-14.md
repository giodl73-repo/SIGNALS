Here is the complete updated rubric:

---

# Rubric: trace-component (v3)

**15 criteria across 3 tiers:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 through C-05 | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 Fix Recommendations, C-10 Render Quantification, C-11 Inline Phase-Close Gates, C-12 Mandatory Comparison Column, **C-13 Exact-Phrase Gate Family**, **C-14 Column-Header Escape Instruction**, **C-15 Do-Nothing Cost** | 14 |

---

## Essential Criteria (weight: 60 points total, 12 pts each)

All five must pass. Failing any one essential criterion fails the entire output regardless of composite score.

### C-01 · Event Anchor
- **Category**: correctness
- **Weight**: essential
- **Text**: The output names the exact event that triggered the trace: the event type (click, submit, input, etc.), the specific UI component that fired it (not a generic description like "the button"), the event payload or input value if relevant, and the handler function or lifecycle hook that received it.
- **Pass condition**: The event type, the exact component name, and the handler function are all named. "The button fires a click event" without naming the handler does not pass. "The input" without naming the component does not pass.

### C-02 · Component Tree Traversal
- **Category**: correctness
- **Weight**: essential
- **Text**: The output traces the path of the action through the component hierarchy — from the event-receiving leaf up through handlers, context providers, or HOCs to the root of the affected subtree. Each hop names the component.
- **Pass condition**: At least two named components in the traversal path are shown with a clear parent→child or handler→provider direction. A flat list of components with no structural relationship does not pass.

### C-03 · State Update Map
- **Category**: correctness
- **Weight**: essential
- **Text**: The output identifies every state mutation triggered by the action: local component state (`useState`, `this.setState`), context state, and store state (Redux, Zustand, Pinia, etc.). For each mutation: the state key, old value shape, new value shape, and the component or store that owns it.
- **Pass condition**: At least one concrete state mutation is named with its owner. "State updates" as a section header with no specifics does not pass.

### C-04 · Re-render Inventory
- **Category**: correctness
- **Weight**: essential
- **Text**: The output lists which components re-render as a result of the state changes, explaining why each one re-renders (owns the state, subscribes to context, receives new props, etc.).
- **Pass condition**: At least one component is listed with its re-render cause. "Several components re-render" does not pass.

### C-05 · Final UI State
- **Category**: correctness
- **Weight**: essential
- **Text**: The output describes the observable UI state after all synchronous effects and at least one async settle point (e.g., after a loading state resolves). This is the "what the user sees" close to the trace.
- **Pass condition**: A concrete final state is described — visible elements, disabled states, error messages, or confirmed no-change. "UI updates accordingly" does not pass.

---

## Recommended Criteria (weight: 30 points total)

Output is meaningfully better with these. Missing one is acceptable; missing all three is a gap.

### C-06 · Side Effect Coverage
- **Category**: coverage / **Weight**: recommended
- **Pass condition**: At least one side effect identified with its mechanism. If none, explicitly state "no side effects detected" — silence does not pass.

### C-07 · Issue Detection
- **Category**: depth / **Weight**: recommended
- **Pass condition**: At least one issue named with its component or state path. "May have performance issues" does not pass.

### C-08 · Framework Vocabulary
- **Category**: behavior / **Weight**: recommended
- **Pass condition**: At least two framework-specific terms correctly applied in context.

---

## Aspirational Criteria (weight: 14 points total, 2 pts each)

### C-09 · Fix Recommendations
- **Category**: depth
- **Pass condition**: At least one issue has a fix naming a specific API or pattern.

### C-10 · Render Quantification
- **Category**: depth
- **Pass condition**: At least one component has a numeric render annotation AND verdict co-located in the same table row or sentence. Separation into two columns or two sections does not satisfy.

### C-11 · Inline Phase-Close Gates
- **Category**: behavior
- **Pass condition**: At least two phase boundaries carry an inline close condition naming the exact failure mode. A preamble instruction does not satisfy — gate must appear at the boundary.

### C-12 · Mandatory Comparison Column
- **Category**: behavior
- **Pass condition**: At least one table column prohibits N/A by instruction, has per-row entries, and demonstrates the escape pattern with a substantive claim. Section-level once-clearance does not satisfy.

### C-13 · Exact-Phrase Gate Family *(new)*
- **Category**: behavior
- **Text**: A phase gate or section close names 2+ distinct exact failure strings that cover the family of likely evasions — not a single category description. The category description ("a flat list does not close this phase") intercepts any flat-list failure. The exact-phrase family ("'State updates' does not close this phase. 'state changes in response to the action' does not close this phase. 'the store is modified' without naming the slice does not close this phase") intercepts the specific strings the model is most likely to produce. When a dominant failure mode has predictable output strings, exact-phrase interception is strictly more adversarially effective.
- **Pass condition**: At least one gate names 2+ distinct exact failure strings. A single canonical failure phrase does not satisfy — the full evasion family must be named.

### C-14 · Column-Header Escape Instruction *(new)*
- **Category**: behavior
- **Text**: The escape pattern for a mandatory column is embedded in the column header instruction itself — not in a preamble processed before the table begins. At cell-fill time, the required format is visible as a sentence stub: "Invisible: [specific thing]." / "Observable: [specific tab]. Exception — [specific structural reason why this row is transparent to ad-hoc inspection]. Exception requires justification — not just claiming it." The path of least resistance at the writing moment is the required format, not a retrieved constraint.
- **Pass condition**: At least one mandatory column's escape pattern appears as a fill-in sentence stub inside the column header instruction. A preamble instruction does not satisfy — the stub must be encountered at column-fill time.

### C-15 · Do-Nothing Cost *(new)*
- **Category**: depth
- **Text**: Each fix recommendation includes an explicit do-nothing cost — a statement of what the unfixed issue ships to production as a user-visible or system-visible consequence. Forces the model to articulate the stakes of each issue rather than leaving priority implicit.
- **Pass condition**: At least one fix recommendation includes a concrete do-nothing cost naming a specific consequence (e.g., "Do-nothing cost: ButtonGroup re-renders on every keystroke — at 10 items, this produces 40+ wasted renders per typing session, measurable as input latency on mid-range devices"). "This could cause performance issues" does not pass.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 14)
```

**Pass condition**: all 5 essential criteria pass AND composite >= 80.
**Ceiling**: 104 (V-05 R2 equivalent scores 98 — the three new criteria are open territory).

---

## v3 Changelog

**Three new criteria** extracted from R2 excellence signals:

**C-13 (Exact-Phrase Gate Family)** — Signal 2 from R2: naming the exact strings the model will most likely produce is strictly more adversarially effective than naming the failure category. V-01/V-05 R2's Phase 3 gate demonstrates: three exact phrases intercept a family of evasions; a category gate describes the class but does not fire against specific strings.

**C-14 (Column-Header Escape Instruction)** — Signal 3 from R2: the escape fill-in stub belongs in the column header, not the preamble. R1 V-05 had the escape in the preamble (processed once before the table, then must be recalled). R2 V-02 and V-05 moved the stub into the column header itself, making the required format visible at cell-fill time.

**C-15 (Do-Nothing Cost)** — V-02/V-04 R2 FINDINGS pattern: "Do-nothing cost: [What ships to production without this fix]" per finding. Forces specific production consequences rather than leaving priority implicit. Did not converge across all R2 passing variations — open territory.

**Aspirational pool**: 10 pts → 14 pts. All 7 criteria at 2 pts each (C-09–C-12 reduced from 2.5 to 2). Pass threshold (80) and essential gate unchanged.
ass condition**: At least one gate or close condition names 2+ distinct exact failure
  strings rather than a single category description. A gate that names one canonical
  failure phrase does not satisfy this criterion — the full evasion family must be named.

### C-14 · Column-Header Escape Instruction *(new)*
- **Category**: behavior
- **Weight**: aspirational
- **Text**: The escape pattern for a mandatory column (what to write when the answer is
  "none" or "everything is observable") is embedded in the column header instruction
  itself — not in a preamble processed before the table begins. At cell-fill time, the
  required format is visible as a sentence stub: "Invisible: [specific thing]." /
  "Observable: [specific tab]. Exception — [specific structural reason why this row is
  transparent to ad-hoc inspection]. Exception requires justification — not just claiming
  it." The path of least resistance at the writing moment is the required format, not a
  retrieved constraint.
- **Pass condition**: At least one mandatory column's escape pattern appears as a fill-in
  sentence stub inside the column header instruction (not in a preamble). A preamble
  instruction that says "N/A is not allowed; if everything is observable, write X" does
  not satisfy this — the stub must be encountered at column-fill time.

### C-15 · Do-Nothing Cost *(new)*
- **Category**: depth
- **Weight**: aspirational
- **Text**: Each fix recommendation includes an explicit do-nothing cost — a statement of
  what the unfixed issue ships to production as a user-visible or system-visible
  consequence. The do-nothing cost forces the model to articulate the stakes of each
  issue rather than leaving the reader to infer them. It makes the fix's priority legible
  without general advice.
- **Pass condition**: At least one fix recommendation includes a concrete do-nothing cost
  that names a specific user-visible or system-visible consequence (e.g., "Do-nothing
  cost: ButtonGroup re-renders on every keystroke — at 10 items, this produces 40+ wasted
  renders per typing session, measurable as input latency on mid-range devices"). "This
  could cause performance issues" does not pass — the consequence must be specific.

---

## Criterion Summary Table

| ID   | Text (short)                     | Weight       | Category    | Pts |
|------|----------------------------------|--------------|-------------|-----|
| C-01 | Event Anchor                     | essential    | correctness | 12  |
| C-02 | Component Tree Traversal         | essential    | correctness | 12  |
| C-03 | State Update Map                 | essential    | correctness | 12  |
| C-04 | Re-render Inventory              | essential    | correctness | 12  |
| C-05 | Final UI State                   | essential    | correctness | 12  |
| C-06 | Side Effect Coverage             | recommended  | coverage    | 10  |
| C-07 | Issue Detection                  | recommended  | depth       | 10  |
| C-08 | Framework Vocabulary             | recommended  | behavior    | 10  |
| C-09 | Fix Recommendations              | aspirational | depth       |  2  |
| C-10 | Render Quantification            | aspirational | depth       |  2  |
| C-11 | Inline Phase-Close Gates         | aspirational | behavior    |  2  |
| C-12 | Mandatory Comparison Column      | aspirational | behavior    |  2  |
| C-13 | Exact-Phrase Gate Family         | aspirational | behavior    |  2  |
| C-14 | Column-Header Escape Instruction | aspirational | behavior    |  2  |
| C-15 | Do-Nothing Cost                  | aspirational | depth       |  2  |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 14)
```

**Pass condition**: all 5 essential criteria pass AND composite >= 80.

---

## Scoring Examples

**Minimum passing output** (all essential, no recommended):
- C-01 through C-05 pass, C-06/07/08 fail, C-09 through C-15 fail
- composite = (5/5 * 60) + (0/3 * 30) + (0/7 * 14) = 60
- Result: FAIL (composite < 80, even though all essential pass)

**Solid output** (all essential + two recommended):
- C-01 through C-05 pass, C-06 + C-07 pass, C-08 fail, C-09 through C-15 fail
- composite = (5/5 * 60) + (2/3 * 30) + (0/7 * 14) = 60 + 20 = 80
- Result: PASS (all essential pass AND composite >= 80)

**Strong output** (all essential + all recommended + three aspirational):
- C-01 through C-08 pass, C-11 + C-12 + C-13 pass, C-09/10/14/15 fail
- composite = (5/5 * 60) + (3/3 * 30) + (3/7 * 14) = 60 + 30 + 6 = 96
- Result: PASS

**V-05 equivalent** (R2 ceiling — all 12 v2 criteria pass):
- C-01 through C-12 pass, C-13/14/15 fail
- composite = (5/5 * 60) + (3/3 * 30) + (4/7 * 14) = 60 + 30 + 8 = 98
- Result: PASS

**Perfect output** (all 15 criteria):
- C-01 through C-15 all pass
- composite = (5/5 * 60) + (3/3 * 30) + (7/7 * 14) = 60 + 30 + 14 = 104
- Result: PASS (ceiling)

---

## v3 Changelog

**Source**: Round 2 scorecard excellence signals
(trace-component-scorecard-R2-2026-03-14.md)

**C-13 added** (Exact-Phrase Gate Family): Extracted from V-01/V-05 R2 pattern. Signal 2
from the R2 excellence analysis: exact-phrase interception is strictly more adversarially
effective than category interception when the dominant failure mode has predictable output
strings. V-01 R2's Phase 3 gate names three exact phrases: "'State updates' does not
close this phase. 'state changes in response to the action' does not close this phase.
'the store is modified' without naming the slice does not close this phase." A category
gate describes the failure class; an exact-phrase gate family intercepts the specific
strings at composition time.

**C-14 added** (Column-Header Escape Instruction): Extracted from V-02/V-05 R2 pattern.
Signal 3 from the R2 excellence analysis: embedding the escape fill-in stub directly in
the column header instruction makes the required format available at cell-fill time, not
as a constraint to retrieve from a preamble. R1 V-05 had the escape in the preamble. R2
V-02 and V-05 moved the stub — "Invisible: [...] / Observable: [...]. Exception —
[specific structural reason]" — into the column header itself, where the model encounters
it at the moment of filling.

**C-15 added** (Do-Nothing Cost): Extracted from V-02/V-04 R2 FINDINGS pattern. V-02 and
V-04 add "Do-nothing cost: [What ships to production without this fix]" as a required
field per finding. This forces the model to articulate specific user-visible or
system-visible consequences rather than leaving priority implicit. V-01, V-03, and V-05
did not carry this field — it was the one depth signal that did not converge across all
R2 passing variations.

**Aspirational pool expanded**: Pool grows from 10 pts (4 criteria at 2.5 each) to
14 pts (7 criteria at 2 each). All C-09–C-12 weights adjusted from 2.5 to 2 to maintain
even distribution. Pass threshold (80) and essential gate unchanged. New ceiling: 104.

**R2 convergence note**: C-07, C-08, and C-12 — R1's three discriminators — all
converged across R2. C-07 (mandatory comparison column) now appears in V-02, V-04, V-05.
C-08 (vocabulary pre-declaration with threading mandate) appears in V-02, V-03, V-04,
V-05. C-12 (N/A-prohibited column with escape) appears in V-02, V-04, V-05. The R2
discriminators are C-11 (format-gated: sequential-phase templates only), C-13 (exact
phrase family depth), C-14 (escape instruction location), and C-15 (do-nothing cost).
C-11 remains structurally incompatible with table-format templates — any template that
wins C-12 via a comparison column loses C-11 unless it also uses sequential phases.
