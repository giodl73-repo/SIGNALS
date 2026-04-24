Written to `simulations/quest/variations/scout-inertia-variations-R4-2026-03-17.md`.

---

## scout-inertia R4 — Variations Summary

**State of the quest entering R4:**
- R3 V-05 scores 100/100 on rubric v3. On rubric v4 it drops to **98.89** — C-16 already passes (separate Trigger/Impact columns exist), but C-17 fails (heading mandate text is present in STEP 2, but no standalone pre-committed list appears *before* the sections begin).
- R4 is a single-mechanism round. All five variations target C-17.

### Variation map

| ID | Axis | C-17 mechanism |
|----|------|----------------|
| V-01 | Step-local bulleted manifest before Section A | Bulleted list before first section content |
| V-02 | Step-local numbered + backtick manifest before Section A | Numbered list with backtick headings (V-03 R3 pattern) |
| V-03 | Global preamble manifest before STEP 1 | "Structural Manifest" section before any step runs |
| V-04 | Combined section + column manifest table at STEP 2 header | Single table pre-committing both section headings AND required columns |
| V-05 | Triple-layer: global preamble + STEP 2 numbered list + inline column manifests | Maximum structural pre-commitment at three depths |

All five predict **100/100** on rubric v4. The differentiator is reliability gradient, not score: global preamble (V-03) > step-local insertion (V-01/V-02) for structural non-skippability. V-05 makes C-17 violation structurally impossible by declaring the manifest at three separate locations.

**R4 delta = 1 mechanism.** R1→R2 required three. R2→R3 required one. R3→R4 requires one. The scaffold convergence pattern holds. If V-05 scores 100/100 and no new excellence signals emerge that extend the rubric, the scaffold is mature.
its the required columns for Section C (Failure Mode Table) and Section D (Why
Inertia Loses) in the same manifest block. A reader can verify both the section structure
and the column structure from the manifest without entering any cell. This tests whether
pre-committing columns alongside sections provides stronger C-16 reliability and cleaner
C-17 coverage than section-only manifests.

**V-05 converges all mechanisms.** R3 V-05 scaffold (Replication Fidelity Standard,
Verification Command column, STRONGEST CLAIM / NAMED CLAIM anchored rebuttal, Impact
column) plus: global preamble manifest, column manifests embedded before each table section,
and numbered list manifest in STEP 2 header. This is the maximum-explicit version. It
should produce 100/100 on v4 and also serve as the candidate scaffold for v5 criteria
extraction.

**Expected convergence shape.** R3 needed one mechanism (Impact column). R4 needs one
mechanism (C-17 manifest). The delta again narrows to a single axis. If all five variations
score 100/100 on v4, the scaffold is mature and the differentiator becomes reliability
under adversarial prompting, not score.

**Key principle from R3 carried forward:** structural pre-commitment eliminates compliance
escape hatches better than implicit contract language. The C-17 manifest is the section-
level analog to the Impact column: both convert an implicit expectation into a structural
declaration where non-compliance is detectable before reading content.

---

## V-01 -- Axis: Bulleted Manifest Before Section A in STEP 2 (C-17 target)

**Hypothesis**: Adding a short bulleted manifest list immediately before Section A in
STEP 2 -- "Required sections: - A. Switching Cost Table / - B. Threat Score / ..." --
converts V-05's implicit heading contract into a C-17-passing pre-commitment. The manifest
appears before any content is rendered; a reader can verify coverage by comparing this list
against the final artifact headings without reading prose. This is R3 V-05 with one
insertion: the bulleted manifest block before Section A. All other sections unchanged.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

## Inertia Analysis -- Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

---

### STEP 1 -- ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months
and finds it acceptable.

**Workaround Profile -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently:
- Name each tool by product, not by category. "GitHub Actions" not "CI system."
  "Confluence page" not "doc." "Custom Python script invoked by a Makefile target"
  not "automation script."
- Enumerate the major steps in numbered sequence.
- Flag institutional knowledge: any step requiring tribal context, undocumented
  conventions, or shared credentials that a new team member would not have.

State why the workaround is good enough: what it handles correctly, for which team
sizes and usage patterns.

**Strongest Objection to Switching**

Write the single strongest argument for staying on the workaround -- the one a
skeptical senior engineer would stake their credibility on. One complete declarative
sentence.

Label it: **STRONGEST CLAIM: [exact text of claim]**

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 -- ANALYST PASS

You have read the Advocate Pass. Produce the full inertia assessment.

Required sections manifest -- all must appear as headings in the final artifact,
in this order, with these exact labels. A section is absent if its heading is not
present. Do not rename, merge, or omit:
- A. Switching Cost Table
- B. Threat Score
- C. Failure Mode Table
- D. Why Inertia Loses
- E. Long-Term Risk of Staying
- F. Anchored Rebuttal

A reader scanning only the headings must be able to locate every analytical
component without reading prose.

**A. Switching Cost Table**

| Dimension | Estimate | What Drives This |
|-----------|----------|-----------------|
| Time | [X hours/days per project] | [migration steps] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [coordination impact] | [who and what changes] |

All three rows required. Numeric or range-based estimates required.
"Significant" is not an estimate.

**B. Threat Score**

```
Inertia Threat: HIGH
```

Required. Downgrade below HIGH only with written justification and supporting
evidence. Omitting this field = analysis failure.

**C. Failure Mode Table**

Failure modes are distinct from switching costs. Failure modes = what goes wrong
if teams stay.

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH |
| 2 | [short name] | [observable event or threshold] | [what happens to whom] | MED |
| + | ... | | | |

Minimum 2 rows. Column constraints:
- **Failure Mode**: a short label for the failure (e.g., "silent event drop", "audit
  gap"). Not a full description -- the effect belongs in Impact.
- **Trigger**: the observable event or condition that causes the failure. Must be
  detectable by the team. "Breaks under load" does not pass. "Queue depth exceeds
  500 messages" does pass.
- **Impact**: what happens when the trigger fires, and to whom. "Fails" does not
  pass. "Events silently dropped with no error surfaced to caller; data
  inconsistency accumulates until manually discovered" does pass. The Impact
  column must be interpretable without reading the Trigger column.
- Trigger and Impact are separate columns. Do not merge them. A blank Impact cell
  is an automatic fail for that row.

Severity column required. HIGH = data loss or compliance risk; MED = incorrect
results; LOW = inefficiency only.

**D. Why Inertia Loses**

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition must be falsifiable -- a team can check it against
their actual situation.

**Verification Command format**: `[Tool or artifact]: [what you open or run] ->
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open the active sprint board -> count rows where Status = Active.
  If >= 4, condition applies."
- "GitHub: run `gh pr list --state open | wc -l` -> if output >= 10, threshold met."

Examples that fail:
- "You can check project count"
- "Review your sprint board"

The column must name a specific tool and specify a concrete action a team member
could follow without a follow-up question.

**E. Long-Term Risk of Staying**

One paragraph. What accumulates over 6-12 months for teams that keep the
workaround? Name a specific compounding cost, growing debt, or divergence risk
with a time horizon.

**F. Anchored Rebuttal**

Three-step sequence -- execute in order, do not merge:

1. Copy the STRONGEST CLAIM from the Advocate Pass word-for-word.
   Label it: `NAMED CLAIM: "[exact text from Advocate Pass]"`

2. Rebut only that named claim. One paragraph. State specifically why it fails --
   with evidence or reasoning tied to the claim's content.

3. Constraint: do not redirect to a different benefit. Do not address a weaker
   claim instead. The rebuttal must be traceable to the named claim -- a reader
   must be able to match the rebuttal to the specific claim above it.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-02 -- Axis: Numbered Backtick Manifest Before Section A in STEP 2 (C-17 target)

**Hypothesis**: A numbered manifest using backtick-formatted heading names -- matching
V-03's proven pattern from R3 -- is a structurally stronger pre-commitment than a bulleted
list. Numbered entries with explicit heading text make the manifest a verifiable checklist:
a reader can tick off each numbered item against the artifact's headings without scanning
prose. This is R3 V-05 with one insertion: a numbered backtick manifest before Section A.
The format difference vs V-01 (numbered + backtick vs plain bullets) tests which manifest
form produces more reliable C-17 behavior.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

## Inertia Analysis -- Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

---

### STEP 1 -- ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months
and finds it acceptable.

**Workaround Profile -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently:
- Name each tool by product, not by category. "GitHub Actions" not "CI system."
  "Confluence page" not "doc." "Custom Python script invoked by a Makefile target"
  not "automation script."
- Enumerate the major steps in numbered sequence.
- Flag institutional knowledge: any step requiring tribal context, undocumented
  conventions, or shared credentials that a new team member would not have.

State why the workaround is good enough: what it handles correctly, for which team
sizes and usage patterns.

**Strongest Objection to Switching**

Write the single strongest argument for staying on the workaround -- the one a
skeptical senior engineer would stake their credibility on. One complete declarative
sentence.

Label it: **STRONGEST CLAIM: [exact text of claim]**

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 -- ANALYST PASS

You have read the Advocate Pass. Produce the full inertia assessment.

The synthesized artifact must use these exact section headings, in this order.
Each heading must be present even if content under it is brief. Do not rename,
merge, or omit any heading. A reader scanning only headings must be able to
identify every analytical component without reading prose.

1. `## A. Switching Cost Table`
2. `## B. Threat Score`
3. `## C. Failure Mode Table`
4. `## D. Why Inertia Loses`
5. `## E. Long-Term Risk of Staying`
6. `## F. Anchored Rebuttal`

Fail condition: role labels appearing as section headings instead of the analytical
labels above; prose summary replacing named sections; any two adjacent components
merged under one heading.

**A. Switching Cost Table**

| Dimension | Estimate | What Drives This |
|-----------|----------|-----------------|
| Time | [X hours/days per project] | [migration steps] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [coordination impact] | [who and what changes] |

All three rows required. Numeric or range-based estimates required.
"Significant" is not an estimate.

**B. Threat Score**

```
Inertia Threat: HIGH
```

Required. Downgrade below HIGH only with written justification and supporting
evidence. Omitting this field = analysis failure.

**C. Failure Mode Table**

Failure modes are distinct from switching costs. Failure modes = what goes wrong
if teams stay.

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH |
| 2 | [short name] | [observable event or threshold] | [what happens to whom] | MED |
| + | ... | | | |

Minimum 2 rows. Column constraints:
- **Failure Mode**: a short label for the failure. Not a full description -- effect
  belongs in Impact.
- **Trigger**: the observable event or condition that causes the failure. Must be
  detectable. "Breaks under load" does not pass. "Queue depth exceeds 500 messages"
  does pass.
- **Impact**: what happens when the trigger fires, and to whom. "Fails" does not
  pass. "Events silently dropped with no error surfaced to caller; data
  inconsistency accumulates until manually discovered" does pass. Impact column
  must be interpretable without reading Trigger.
- Trigger and Impact are separate columns. A blank Impact cell = automatic fail.

Severity: HIGH = data loss or compliance risk; MED = incorrect results; LOW =
inefficiency only.

**D. Why Inertia Loses**

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition falsifiable -- a team can check it against their
actual situation.

**Verification Command format**: `[Tool or artifact]: [what you open or run] ->
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open the active sprint board -> count rows where Status = Active.
  If >= 4, condition applies."
- "GitHub: run `gh pr list --state open | wc -l` -> if output >= 10, threshold met."

Examples that fail: "You can check project count" / "Review your sprint board"

**E. Long-Term Risk of Staying**

One paragraph. What accumulates over 6-12 months? Name a specific compounding
cost, growing debt, or divergence risk with a time horizon.

**F. Anchored Rebuttal**

Three-step sequence -- execute in order, do not merge:

1. Copy the STRONGEST CLAIM from the Advocate Pass word-for-word.
   Label it: `NAMED CLAIM: "[exact text from Advocate Pass]"`

2. Rebut only that named claim. One paragraph. State specifically why it fails.

3. Constraint: rebuttal must be traceable to the named claim. Do not redirect to
   a different benefit. Do not address a weaker claim instead.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-03 -- Axis: Global Preamble Manifest Before STEP 1 (C-17 target, placement variant)

**Hypothesis**: Moving the section manifest to before STEP 1 -- the very top of the
prompt, before any content generation begins -- is the most absolute form of C-17
compliance. The manifest appears before the Advocate Pass exists; it is a document-global
structural contract, not a step-local synthesis instruction. If C-17 requires that "the
synthesis step opens with an explicit pre-committed list before content begins," a global
preamble satisfies the spirit maximally: no content has been requested yet when the
manifest is declared. Tests whether manifest placement (global vs step-local) changes
C-17 compliance reliability. All other mechanisms from R3 V-05 unchanged.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

---

### Structural Manifest

This analysis produces one artifact. The artifact must contain the following
sections in this order. A manifest violation (missing, renamed, or merged heading)
is an analysis failure.

Required sections:
- WORKAROUND PROFILE (Advocate)
- A. Switching Cost Table
- B. Threat Score
- C. Failure Mode Table
- D. Why Inertia Loses
- E. Long-Term Risk of Staying
- F. Anchored Rebuttal

A reader with only these section headings must be able to locate every analytical
component without reading any body text.

---

## Inertia Analysis -- Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

---

### STEP 1 -- ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months
and finds it acceptable.

**Workaround Profile -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently:
- Name each tool by product, not by category. "GitHub Actions" not "CI system."
  "Confluence page" not "doc." "Custom Python script invoked by a Makefile target"
  not "automation script."
- Enumerate the major steps in numbered sequence.
- Flag institutional knowledge: any step requiring tribal context, undocumented
  conventions, or shared credentials that a new team member would not have.

State why the workaround is good enough: what it handles correctly, for which team
sizes and usage patterns.

**Strongest Objection to Switching**

Write the single strongest argument for staying on the workaround -- the one a
skeptical senior engineer would stake their credibility on. One complete declarative
sentence.

Label it: **STRONGEST CLAIM: [exact text of claim]**

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 -- ANALYST PASS

You have read the Advocate Pass. Produce the full inertia assessment. Use the
section headings declared in the Structural Manifest above. Do not rename, merge,
or omit any heading.

**A. Switching Cost Table**

| Dimension | Estimate | What Drives This |
|-----------|----------|-----------------|
| Time | [X hours/days per project] | [migration steps] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [coordination impact] | [who and what changes] |

All three rows required. Numeric or range-based estimates required.
"Significant" is not an estimate.

**B. Threat Score**

```
Inertia Threat: HIGH
```

Required. Downgrade below HIGH only with written justification and supporting
evidence. Omitting this field = analysis failure.

**C. Failure Mode Table**

Failure modes are distinct from switching costs. Failure modes = what goes wrong
if teams stay.

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH |
| 2 | [short name] | [observable event or threshold] | [what happens to whom] | MED |
| + | ... | | | |

Minimum 2 rows. Column constraints:
- **Failure Mode**: short label for the failure. Effect belongs in Impact.
- **Trigger**: observable condition that causes the failure. Detectable by team.
  "Breaks under load" fails. "Queue depth exceeds 500 messages" passes.
- **Impact**: what happens to whom when trigger fires. "Fails" does not pass.
  "Events silently dropped; data inconsistency accumulates" passes. Impact column
  must be interpretable without reading Trigger.
- Trigger and Impact are separate columns. A blank Impact cell = automatic fail.

Severity: HIGH = data loss/compliance risk; MED = incorrect results; LOW =
inefficiency only.

**D. Why Inertia Loses**

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition must be falsifiable -- a team can check it.

**Verification Command format**: `[Tool or artifact]: [what you open or run] ->
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open active sprint board -> count Status = Active rows. If >= 4, applies."
- "GitHub: run `gh pr list --state open | wc -l` -> if >= 10, threshold met."

Examples that fail: "You can check project count" / "Review your sprint board"

**E. Long-Term Risk of Staying**

One paragraph. What accumulates over 6-12 months? Name a specific compounding
cost, growing debt, or divergence risk with a time horizon.

**F. Anchored Rebuttal**

Three-step sequence -- execute in order, do not merge:

1. Copy the STRONGEST CLAIM from the Advocate Pass word-for-word.
   Label it: `NAMED CLAIM: "[exact text from Advocate Pass]"`

2. Rebut only that named claim. One paragraph. State specifically why it fails --
   with evidence or reasoning tied to the claim's content.

3. Constraint: rebuttal must be traceable to the named claim. Do not address a
   weaker claim instead. Do not redirect to feature benefits unrelated to the claim.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-04 -- Combined: Section + Column Manifest Table at STEP 2 Header (C-16 + C-17)

**Hypothesis**: Beyond declaring section headings (C-17), pre-committing the required
columns for the two key tables -- Section C (Failure Mode Table) and Section D (Why
Inertia Loses) -- in the same manifest block creates a complete structural contract: a
reader can verify both section coverage and column coverage from the manifest without
entering any cell. The manifest is a single table that lists section name, purpose, and
required columns for tabular sections. This tests whether a richer pre-commitment (section
+ column level) produces stronger C-16 compliance reliability beyond what column header
text alone provides, while cleanly satisfying C-17.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

## Inertia Analysis -- Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

---

### STEP 1 -- ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months
and finds it acceptable.

**Workaround Profile -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently:
- Name each tool by product, not by category. "GitHub Actions" not "CI system."
  "Confluence page" not "doc." "Custom Python script invoked by a Makefile target"
  not "automation script."
- Enumerate the major steps in numbered sequence.
- Flag institutional knowledge: any step requiring tribal context, undocumented
  conventions, or shared credentials that a new team member would not have.

State why the workaround is good enough: what it handles correctly, for which team
sizes and usage patterns.

**Strongest Objection to Switching**

Write the single strongest argument for staying on the workaround -- the one a
skeptical senior engineer would stake their credibility on. One complete declarative
sentence.

Label it: **STRONGEST CLAIM: [exact text of claim]**

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 -- ANALYST PASS

You have read the Advocate Pass. Produce the full inertia assessment.

The artifact must satisfy this structural contract. Each row is a compliance
requirement. A violation at any row is an analysis failure -- not a content gap.

| Section | Required heading (exact) | Required columns (tabular sections only) |
|---------|--------------------------|------------------------------------------|
| Workaround | `WORKAROUND PROFILE (Advocate)` | -- (prose) |
| A | `A. Switching Cost Table` | Dimension / Estimate / What Drives This |
| B | `B. Threat Score` | -- (code block) |
| C | `C. Failure Mode Table` | # / Failure Mode / Trigger / Impact / Severity |
| D | `D. Why Inertia Loses` | # / Condition / Observable Threshold / Verification Command |
| E | `E. Long-Term Risk of Staying` | -- (paragraph) |
| F | `F. Anchored Rebuttal` | -- (3-step sequence) |

Violation conditions:
- A heading is absent from the artifact.
- A required column is absent from its table.
- A blank Impact cell appears in Section C (Trigger and Impact are separate columns;
  merging them into one cell leaves Impact blank).
- A blank Verification Command cell appears in Section D.

A reader scanning only headings and column headers must be able to verify full
coverage of all analytical components without reading any cell content.

**A. Switching Cost Table**

| Dimension | Estimate | What Drives This |
|-----------|----------|-----------------|
| Time | [X hours/days per project] | [migration steps] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [coordination impact] | [who and what changes] |

All three rows required. Numeric or range-based estimates required.

**B. Threat Score**

```
Inertia Threat: HIGH
```

Required. Downgrade below HIGH only with written justification. Omitting = failure.

**C. Failure Mode Table**

Failure modes = what goes wrong if teams stay. Distinct from switching costs.

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH |
| 2 | [short name] | [observable event or threshold] | [what happens to whom] | MED |

Minimum 2 rows. Trigger and Impact are separate columns -- do not merge.
A blank Impact cell = automatic fail for that row.

- **Trigger**: observable condition causing the failure. "Breaks under load" fails.
  "Queue depth exceeds 500 messages" passes.
- **Impact**: what happens to whom when trigger fires. "Fails" does not pass.
  "Events silently dropped; data inconsistency accumulates" passes. Must be
  interpretable without reading Trigger.
- **Severity**: HIGH = data loss/compliance; MED = incorrect results; LOW =
  inefficiency.

**D. Why Inertia Loses**

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition falsifiable.

**Verification Command format**: `[Tool]: [action] -> [result when threshold applies]`

Examples: "Jira: open sprint board -> count Status = Active. If >= 4, applies."
Failures: "You can check project count" / "Review your sprint board"

**E. Long-Term Risk of Staying**

One paragraph. What accumulates over 6-12 months? Specific compounding cost or
divergence risk with a time horizon.

**F. Anchored Rebuttal**

Three steps in order -- do not merge:

1. Copy the STRONGEST CLAIM word-for-word.
   Label: `NAMED CLAIM: "[exact text from Advocate Pass]"`

2. Rebut only that named claim. One paragraph. Tied to claim content.

3. Constraint: traceable to named claim only. No pivots to weaker claims or
   unrelated feature benefits.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-05 -- Full Combined: Global Preamble + Column Manifests + R3 V-05 Scaffold (C-16 + C-17)

**Hypothesis**: R3 V-05 scaffold is mature -- all C-01 through C-15 pass, C-16 passes via
existing Trigger/Impact columns, only C-17 fails. V-05 closes C-17 by adding (1) a global
preamble manifest before STEP 1 listing all required sections, (2) inline column manifests
as named pre-commitments immediately before each table (Section C, Section D), and (3) a
numbered section list at the STEP 2 header. The triple-layer approach -- global manifest +
pre-table column declaration + step-level section list -- makes structural pre-commitment
visible at three depths of reading: a scan of the preamble, a scan of STEP 2's opening,
and a scan immediately above each table. Predicted 100/100 on v4.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

---

### Structural Manifest

This analysis produces one artifact. Before any content is generated, the following
structural contract applies. Violations are analysis failures, not content gaps.

**Required sections** (must appear as headings, in this order):
1. `WORKAROUND PROFILE (Advocate)` -- produced by STEP 1
2. `A. Switching Cost Table` -- three-row table
3. `B. Threat Score` -- HIGH code block
4. `C. Failure Mode Table` -- four-column table with separate Trigger and Impact columns
5. `D. Why Inertia Loses` -- three-column table with Verification Command column
6. `E. Long-Term Risk of Staying` -- paragraph with time horizon
7. `F. Anchored Rebuttal` -- three-step sequence anchored to STRONGEST CLAIM

**Required columns** (missing column = row-level failure):
- Section C: `# | Failure Mode | Trigger | Impact | Severity`
- Section D: `# | Condition | Observable Threshold | Verification Command`

A reader with only the section headings and table headers must be able to verify
full coverage of all analytical components without reading any cell content.

---

## Inertia Analysis -- Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

---

### STEP 1 -- ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months
and finds it acceptable.

**Workaround Profile -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently:
- Name each tool by product, not by category. "GitHub Actions" not "CI system."
  "Confluence page" not "doc." "Custom Python script invoked by a Makefile target"
  not "automation script."
- Enumerate the major steps in numbered sequence.
- Flag institutional knowledge: any step requiring tribal context, undocumented
  conventions, or shared credentials that a new team member would not have.

State why the workaround is good enough: what it handles correctly, for which team
sizes and usage patterns.

**Strongest Objection to Switching**

Write the single strongest argument for staying on the workaround -- the one a
skeptical senior engineer would stake their credibility on. One complete declarative
sentence.

Label it: **STRONGEST CLAIM: [exact text of claim]**

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 -- ANALYST PASS

You have read the Advocate Pass. Produce the full inertia assessment.

Sections must appear with these exact headings, in this order:
1. `A. Switching Cost Table`
2. `B. Threat Score`
3. `C. Failure Mode Table`
4. `D. Why Inertia Loses`
5. `E. Long-Term Risk of Staying`
6. `F. Anchored Rebuttal`

Do not rename, merge, or omit any heading. A reader scanning only headings must
locate every analytical component without reading prose.

**A. Switching Cost Table**

| Dimension | Estimate | What Drives This |
|-----------|----------|-----------------|
| Time | [X hours/days per project] | [migration steps] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [coordination impact] | [who and what changes] |

All three rows required. Numeric or range-based estimates required.
"Significant" is not an estimate.

**B. Threat Score**

```
Inertia Threat: HIGH
```

Required. Downgrade below HIGH only with written justification and supporting
evidence. Omitting this field = analysis failure.

**C. Failure Mode Table**

Failure modes are distinct from switching costs. Failure modes = what goes wrong
if teams stay.

Required columns for this table: `# | Failure Mode | Trigger | Impact | Severity`
Trigger and Impact are separate columns. Do not merge them into one cell.
A blank Impact cell = automatic fail for that row.

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [short name] | [observable event or threshold] | [what happens to whom] | HIGH |
| 2 | [short name] | [observable event or threshold] | [what happens to whom] | MED |
| + | ... | | | |

Minimum 2 rows. Column constraints:
- **Failure Mode**: short label (e.g., "silent event drop"). Effect belongs in Impact.
- **Trigger**: observable condition causing the failure. Must be detectable.
  "Breaks under load" fails. "Queue depth exceeds 500 messages" passes.
- **Impact**: what happens to whom when trigger fires. "Fails" does not pass.
  "Events silently dropped with no error surfaced to caller; data inconsistency
  accumulates until manually discovered" passes. Interpretable without reading Trigger.
- **Severity**: HIGH = data loss or compliance risk; MED = incorrect results; LOW =
  inefficiency only.

**D. Why Inertia Loses**

Required columns for this table:
`# | Condition | Observable Threshold | Verification Command`

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition must be falsifiable -- a team can check it against
their actual situation.

**Verification Command format**: `[Tool or artifact]: [what you open or run] ->
[what the result looks like when the threshold applies]`

Examples that pass:
- "Jira: open the active sprint board -> count rows where Status = Active.
  If >= 4, condition applies."
- "GitHub: run `gh pr list --state open | wc -l` -> if output >= 10, threshold met."

Examples that fail:
- "You can check project count"
- "Review your sprint board"

The column must name a specific tool and specify a concrete action a team member
could follow without a follow-up question.

**E. Long-Term Risk of Staying**

One paragraph. What accumulates over 6-12 months for teams that keep the
workaround? Name a specific compounding cost, growing debt, or divergence risk
with a time horizon.

**F. Anchored Rebuttal**

Three-step sequence -- execute in order, do not merge:

1. Copy the STRONGEST CLAIM from the Advocate Pass word-for-word.
   Label it: `NAMED CLAIM: "[exact text from Advocate Pass]"`

2. Rebut only that named claim. One paragraph. State specifically why it fails --
   with evidence or reasoning tied to the claim's content.

3. Constraint: do not redirect to a different benefit. Do not address a weaker
   claim instead. The rebuttal must be traceable to the named claim -- a reader
   must be able to match the rebuttal to the specific claim above it.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## Predicted R4 Scores (rubric v4)

Rubric v4 scoring: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/9 * 10)`

Aspirational criteria (9): C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17.

R3 V-05 on rubric v4: all essential pass, all recommended pass, aspirational 8/9 (C-17
fails -- heading mandate text present but no standalone manifest list before sections begin).
Score: 60 + 30 + 8.89 = 98.89. R4 target: C-17 PASS in all five variations.

### V-01 Prediction

Base is R3 V-05: 98.89 on v4. V-01 adds bulleted manifest before Section A.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Section C Severity column; unchanged |
| C-10 | Steelman rebutted | PASS | Two-pass structure + Section F; unchanged |
| C-11 | Verification method | PASS | Section D Verification Command column; unchanged |
| C-12 | Anchored rebuttal | PASS | STRONGEST CLAIM -> NAMED CLAIM verbatim; unchanged |
| C-13 | Replication fidelity | PASS | Replication Fidelity Standard in STEP 1; unchanged |
| C-14 | Labeled sections | PASS | Sections A-F descriptive + heading mandate; unchanged |
| C-15 | Trigger/Impact decomposed | PASS | Section C has distinct Trigger and Impact content; unchanged |
| C-16 | Dedicated Trigger/Impact columns | PASS | Separate Trigger column + separate Impact column in Section C; unchanged |
| C-17 | Synthesis heading manifest | PASS | Bulleted manifest list before Section A -- "Required sections manifest: - A ... - F"; declared before first section content begins |

Aspirational: 9/9 * 10 = 10
**Predicted score**: 60 + 30 + 10 = **100**

---

### V-02 Prediction

Base is R3 V-05: 98.89 on v4. V-02 adds numbered backtick manifest before Section A.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Section C Severity column; unchanged |
| C-10 | Steelman rebutted | PASS | Two-pass structure; unchanged |
| C-11 | Verification method | PASS | Section D Verification Command column; unchanged |
| C-12 | Anchored rebuttal | PASS | STRONGEST CLAIM -> NAMED CLAIM; unchanged |
| C-13 | Replication fidelity | PASS | Replication Fidelity Standard; unchanged |
| C-14 | Labeled sections | PASS | Sections A-F + heading mandate; unchanged |
| C-15 | Trigger/Impact decomposed | PASS | Section C trigger/impact content distinction; unchanged |
| C-16 | Dedicated Trigger/Impact columns | PASS | Separate Trigger and Impact columns; unchanged |
| C-17 | Synthesis heading manifest | PASS | Numbered manifest "1. `## A. Switching Cost Table`... 6. `## F. Anchored Rebuttal`" before first section; fail condition defined |

Aspirational: 9/9 * 10 = 10
**Predicted score**: 60 + 30 + 10 = **100**

---

### V-03 Prediction

Base is R3 V-05: 98.89 on v4. V-03 adds global preamble manifest before STEP 1.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Section C Severity column; unchanged |
| C-10 | Steelman rebutted | PASS | Two-pass structure; unchanged |
| C-11 | Verification method | PASS | Section D Verification Command column; unchanged |
| C-12 | Anchored rebuttal | PASS | STRONGEST CLAIM -> NAMED CLAIM; unchanged |
| C-13 | Replication fidelity | PASS | Replication Fidelity Standard; unchanged |
| C-14 | Labeled sections | PASS | Sections A-F + heading mandate; unchanged |
| C-15 | Trigger/Impact decomposed | PASS | Section C trigger/impact distinction; unchanged |
| C-16 | Dedicated Trigger/Impact columns | PASS | Separate columns; unchanged |
| C-17 | Synthesis heading manifest | PASS | "Structural Manifest" section before STEP 1: "Required sections: - WORKAROUND PROFILE ... - F. Anchored Rebuttal" -- maximally pre-committed, before any content step begins |

Aspirational: 9/9 * 10 = 10
**Predicted score**: 60 + 30 + 10 = **100**

---

### V-04 Prediction

Base is R3 V-05 with combined section + column manifest table at STEP 2 header.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Section C Severity column |
| C-10 | Steelman rebutted | PASS | Two-pass structure + Section F |
| C-11 | Verification method | PASS | Section D Verification Command column |
| C-12 | Anchored rebuttal | PASS | STRONGEST CLAIM -> NAMED CLAIM |
| C-13 | Replication fidelity | PASS | Replication Fidelity Standard in STEP 1 |
| C-14 | Labeled sections | PASS | Sections A-F declared in manifest table + present as headings |
| C-15 | Trigger/Impact decomposed | PASS | Section C trigger/impact distinction in both manifest and column |
| C-16 | Dedicated Trigger/Impact columns | PASS | Manifest pre-declares "# / Failure Mode / Trigger / Impact / Severity"; columns enforced structurally + "blank Impact cell = automatic fail" |
| C-17 | Synthesis heading manifest | PASS | Manifest table before Section A: rows list Section, Required heading, Required columns -- explicit structural contract before first content heading appears |

Aspirational: 9/9 * 10 = 10
**Predicted score**: 60 + 30 + 10 = **100**

---

### V-05 Prediction

Full combined: R3 V-05 scaffold + global preamble manifest + inline column manifests +
numbered list at STEP 2 header.

| ID | Criterion | Predicted | Evidence |
|----|-----------|-----------|---------|
| C-09 | Severity ranked | PASS | Section C Severity column; unchanged from R3 V-05 |
| C-10 | Steelman rebutted | PASS | Two-pass structure; Section F; unchanged |
| C-11 | Verification method | PASS | Section D Verification Command column; unchanged |
| C-12 | Anchored rebuttal | PASS | STRONGEST CLAIM -> NAMED CLAIM verbatim -> traceable rebuttal; unchanged |
| C-13 | Replication fidelity | PASS | Replication Fidelity Standard in STEP 1; unchanged |
| C-14 | Labeled sections | PASS | Preamble manifest lists sections + STEP 2 numbered list + sections present as headings |
| C-15 | Trigger/Impact decomposed | PASS | Section C: separate Trigger / Impact columns + inline column manifest declares separation |
| C-16 | Dedicated Trigger/Impact columns | PASS | Preamble manifest declares "Section C: # / Failure Mode / Trigger / Impact / Severity"; STEP 2 Section C inline: "Required columns... Trigger and Impact are separate columns"; blank cell = automatic fail |
| C-17 | Synthesis heading manifest | PASS | Preamble "Structural Manifest" section + STEP 2 numbered list both declare sections before content; triple-layer: global preamble + step header + inline per-table reinforcement |

Aspirational: 9/9 * 10 = 10
**Predicted score**: 60 + 30 + 10 = **100**

---

## Variation Rankings

| Rank | Variation | Predicted Score | Band | C-16 | C-17 | Key gap vs 100 |
|------|-----------|----------------|------|------|------|----------------|
| 1 | V-05 | 100 | Gold | PASS | PASS | none |
| 1 | V-04 | 100 | Gold | PASS | PASS | none |
| 1 | V-03 | 100 | Gold | PASS | PASS | none |
| 1 | V-02 | 100 | Gold | PASS | PASS | none |
| 1 | V-01 | 100 | Gold | PASS | PASS | none |

All five variations predict 100/100. The differentiation is reliability under
adversarial prompting, not predicted score. Key reliability gradient:

V-01 (step-local bullets) < V-02 (step-local numbered + backtick) < V-03 (global preamble)
V-04 (combined section + column manifest) < V-05 (triple-layer: global + step + inline)

The gradient hypothesis: a manifest declared globally before STEP 1 is harder for a
model to "skip" than one inserted between STEP 2's heading and its first section. The
triple-layer in V-05 makes C-17 non-compliance structurally impossible -- the manifest
appears at three separate locations.

---

## Excellence Signals from R4 Design

**Signal 1 -- C-17 is the terminal mechanism; R4 delta = 1 manifest**

R1 to R2 required three mechanisms. R2 to R3 required one (Impact column). R3 to R4
requires one (heading manifest). The pattern holds: each round closes a single structural
gap. V-05 now accumulates all prior excellence signals -- Replication Fidelity Standard,
Verification Command column, STRONGEST CLAIM / NAMED CLAIM, Impact column, heading
manifest -- with no gaps remaining against rubric v4.

**Signal 2 -- Manifest placement creates a reliability gradient, not a score gradient**

All five variations predict 100/100, but they differ in how hard it is for a model to
violate C-17 without the violation being detectable. A step-local bulleted list (V-01)
can be syntactically present but functionally ignored if the model treats the bullets as
decorative rather than structural. A global preamble (V-03) cannot be ignored -- it
appears before any content generation begins. The V-04/V-05 combined manifest pre-commits
both section headings AND column structure, making the structural contract auditable at
two levels simultaneously.

**Signal 3 -- Column manifests (V-04/V-05) extend structural pre-commitment to C-16**

V-04 and V-05 add something new: a pre-committed declaration of required columns for
Section C and Section D, separate from the tables themselves. This makes C-16 detectable
at the manifest level: if the final artifact's Section C table is missing the Impact
column, the violation is visible both at the manifest declaration site and at the table
site. Two detection points vs one. This is the structural pre-commitment principle applied
to column level, not just section level.

---

```json
{"top_score_predicted": 100, "all_essential_pass": true, "new_patterns": ["C-17 closes with a heading manifest -- multiple manifest placements tested (step-local vs global vs triple-layer); all predict 100/100 but differ in reliability gradient: global preamble > step-local bullets for structural non-skippability", "Column manifests (V-04/V-05) extend structural pre-commitment to column level -- declaring required columns before table content creates two detection sites for C-16 violations vs one", "R4 delta = 1 mechanism (C-17 manifest), confirming scaffold convergence -- four consecutive rounds of one-mechanism deltas (R1: three, R2: one, R3: one, R4: one) with V-05 accumulating all signals"]}
```
