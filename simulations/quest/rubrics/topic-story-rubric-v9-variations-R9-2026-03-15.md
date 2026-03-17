# R9 Variations -- `topic-story` (v9 Rubric, 33 Criteria)

**Round**: 9
**Skill**: `topic-story`
**Base rubric**: `topic-story-rubric-v9-2026-03-14.md`
**New criteria this round**: C-31, C-32, C-33

---

## R8 State Summary

R8: All five variations scored 100.0 on C-01 through C-30. The three new R9 criteria were
partially implicit in R8 forms:

- **C-31**: R8 V-01 had a bold-text block (`**Checklist Design Invariant**`) with a
  blockquote naming a repair instruction. The block was present but expressed as bold +
  blockquote rather than a navigable heading. Scan-anchor navigability was structural but
  not heading-level. The repair instruction was present ("must be rewritten as a structural
  presence check") but unnamed -- no formula was prescribed.
- **C-32**: R8 V-03 had "Three inertia fields required -- separate, not consolidated:" in
  Section 4 (satisfies C-32). R8 V-01 and V-02 did not -- Section 4 said "Required labeled
  fields:" without an anti-consolidation directive.
- **C-33**: No R8 variation annotated anti-consolidation constraints in the field inventory.
  The axis table had no Structural Constraint column. Consolidation violations were not
  auditable from the inventory alone.

**R9 baseline (per new criterion, per R8 variation)**:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-31 (heading block + repair formula) | PARTIAL | PARTIAL | FAILS | PARTIAL | PARTIAL |
| C-32 (anti-consolidation in S4 template) | FAILS | FAILS | PASSES | FAILS | FAILS |
| C-33 (inventory annotation) | FAILS | FAILS | FAILS | FAILS | FAILS |

**R9 compound design requirement**: Satisfy C-31, C-32, C-33 in explicitly structural forms:
- **C-31**: Invariant expressed as a heading (scan anchor), AND names a prescribed repair
  operation formula -- not just a pass condition. The repair formula must be quotable.
- **C-32**: Section 4 must contain an explicit anti-consolidation directive co-located with
  the three inertia fields -- directive visible at field-entry time, not only at checklist
  review time.
- **C-33**: Field inventory table must annotate that `**Prior position**:`, `**Baseline
  distance**:`, and `**Signals establish**:` must not be consolidated. The inventory alone
  must be sufficient to audit consolidation violations without touching section templates
  or checklists.

**Variation axes explored**:
- Single-axis: Output format (C-31 -- invariant as heading block with named repair formula) -- V-01
- Single-axis: Output format (C-33 -- Structural Constraint column in field inventory) -- V-02
- Single-axis: Phrasing register (C-32 -- anti-consolidation directive in S4 template, lean imperative) -- V-03
- Compound: Output format + lifecycle emphasis (C-31 heading block + C-32 section directive) -- V-04
- Compound: Output format + inertia framing (C-31 + C-32 + C-33 all three, inventory-first) -- V-05

---

## V-01 -- Single-Axis: C-31 Invariant as Heading Block with Named Repair Formula

**Variation axis**: Output format (C-31 invariant presentation)
**Hypothesis**: Promoting the invariant from a bold-text + blockquote form to a named
heading block (`### Checklist Design Invariant`) with an explicit labeled `**Repair
operation**:` formula makes C-31 fire unambiguously. The heading creates a scan anchor
locatable without reading prose; the repair formula prescribes the exact rewrite a
non-conforming item must undergo, converting "must be rewritten" (generic) into
"rewrite as: `Does [Section name] include the label \`**[field name]**:\`?`" (quotable).
C-32 and C-33 are deliberately absent -- this is a single-axis variation isolating C-31.
All other structural properties are unchanged from R8 V-01.

---

### PROMPT BODY -- V-01

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal -- it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes**

This template was built from two named design axes. Every required labeled field belongs
to one axis. The Layer 1 checklist is produced by a single pass over the complete field
inventory -- one binary-verifiable presence-verification item per required labeled field.

| Axis | Required labeled fields introduced |
|------|-------------------------------------|
| **Falsifiability axis** | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` |
| **Inertia-framing axis** | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` |

Any future extension must: (1) name the design axis, (2) register every new field in
the axis table, (3) add one binary-verifiable checklist item per new field before writing
any section that uses it.

---

### Checklist Design Invariant

**Rule**: No item tests content quality; each item locates a label string or reports
it missing. An item that requires editorial judgment to answer violates this invariant.

**Repair operation**: Rewrite any failing item as:
> "Does [Section name] include the label `**[field name]**:`?"

Apply this invariant to every item in Layer 1. Apply it when extending the checklist.

---

**Layer 1 -- Pre-Artifact Checklist**

Run every item before writing any section. Answer YES by locating the named element.
Do not write until all items are YES.

**Section structure:**
1. [ ] Does this output include a labeled **Signal Findings** section?
2. [ ] Does this output include a labeled **What the Signals Say Together** section?
3. [ ] Does this output include a labeled **What Remains Uncertain** section?
4. [ ] Does this output include a labeled **Recommendation** section?

**Falsifiability-axis field registration:**
5. [ ] Does the Signal Findings section template include `**Inertia verdict**:` on each finding entry?
6. [ ] Does the What the Signals Say Together section include `**Pattern claim**:`?
7. [ ] Does the What the Signals Say Together section include `**Disproof condition**:`?
8. [ ] Does the What Remains Uncertain section include `**Verdict consequence**:`?
9. [ ] Does the Recommendation section include `**Verdict**:`?

**Inertia-framing-axis field registration (registered at incorporation time):**
10. [ ] Does the Recommendation section include `**Prior position**:`?
11. [ ] Does the Recommendation section include `**Baseline distance**:`?
12. [ ] Does the Recommendation section include `**Signals establish**:`?

*(Items 1-4: section structure. Items 5-12: one item per required labeled field, derived
from the two-axis field inventory. Each item answered by locating the label string or
reporting it missing -- consistent with the Checklist Design Invariant above.)*

---

**Layer 2 -- Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience -- not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding change whether to build `{topic}`?**

For each signal, write:

```
**[Signal name]** -- [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES -- this moves the prior position /
                     NO -- this confirms the prior position /
                     PARTIAL -- [one clause naming what specifically shifts]]
```

If `**Inertia verdict**:` is NO and the finding does not affect any other decision
dimension, omit the signal. Close this section with a one-line note stating how many
signals were excluded and the shared basis for exclusion.

Wrong operation: **Contents-report** -- transcribing what the signal said rather than
naming what it changes for the build decision. Detection: any entry missing
`**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the shape the signals collectively form.*

Write the cross-signal claim. It must be true of the signal set as a whole, not
directly stated in any single signal artifact, and causal: it names WHY the signals
converge, not THAT they converge.

```
**Pattern claim**: [one sentence. Cross-signal. Causal: "signals converge because
                   [specific structural reason]", not "signals agree".]

**Disproof condition**: [The claim fails if: [specific observable condition that,
                        if shown to hold, invalidates the pattern.]]
```

Write `**Disproof condition**:` last: after committing to the pattern claim, ask what
would someone need to show is false in order to disprove it. That answer belongs in
this field -- not in the prose above it.

Voice anchors: *What's striking is... / The convergence is not coincidental -- it
reflects... / The evidence forces a conclusion I did not enter this investigation
expecting...*

Wrong operation: **Signal-list** -- naming each signal's contribution without naming
the cross-signal claim. Detection: the pattern cannot be stated in one sentence that
mentions no individual signal by name.

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without surrendering the verdict.*

Every named uncertainty must complete the verdict-consequence arc. An uncertainty that
does not change the recommendation is decision-neutral and does not appear here.

```
**Verdict consequence**: [If [condition A holds / is shown false], the verdict
                         changes from [current] to [alternative A].
                         If [condition B], the verdict changes to [alternative B].]
```

**Anti-neutral directive -- required for this section.** Locate any sentence that names
an uncertainty without naming its consequence for the verdict. That sentence is a
neutral uncertainty statement. Revise or remove it.

Strings to scan for and remove:
- "More research may be needed on X"
- "There is some uncertainty around X"
- "This area warrants further investigation"
- "It is unclear whether X"
- "Future work could explore X"

Required form: "We do not know [X]. If X is shown to be false, the verdict becomes
[Y]. Resolution method: [specific investigation]."

Wrong operation: **Verdict-consequence gap** -- naming uncertainty without naming its
effect on the verdict. Detection: any uncertainty sentence without an
"if...verdict changes to..." clause.

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Measure position against the prior. Defend the verdict against the
adjacent alternative. Name the first action. Do not assign the decision to the reader.

Required labeled fields:

```
**Prior position**: [What the team believed about {topic} before this investigation.]

**Baseline distance**: [How far the signals have moved the position from that
                        baseline -- the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the delta
                        defensible -- the compound inference.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] -- specifically [action], because
[**Pattern claim**] forces this verdict rather than [adjacent alternative]. This call
stands unless [**Disproof condition**] is shown to hold."

*(The sentence form names `**Disproof condition**:` from Section 2 by field reference.
The recommendation is structurally conditioned by the falsifiability analysis: the
verdict is issued and its revision condition is named in the same required template slot.)*

**Anti-neutral directive -- required for this section.** Scan every sentence for strings
that give the reader a way not to act.

Strings to scan for and remove:
- "Based on the available evidence, it would be reasonable to..."
- "The team should consider..."
- "It may be worth exploring..."
- "Given the above, a reasonable next step would be..."
- "The evidence supports moving forward, though caution is advised"
- "A possible path forward is..."
- "One option would be to..."
- "This suggests that..."

Wrong operation: **Assigns-decision-to-reader** -- presenting evidence without issuing
the call. Detection: `**Verdict**:` does not contain one of
{proceed / pause / pivot / abandon}.

---

**Layer 3 -- Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Signal Findings | **Contents-report** -- transcribing what the signal said rather than naming what it changes for the build decision | Any finding entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** -- naming each signal's contribution without naming the cross-signal claim | The pattern cannot be stated in one sentence that mentions no individual signal by name |
| What Remains Uncertain | **Verdict-consequence gap** -- naming uncertainty without naming its effect on the recommendation | Any uncertainty sentence without an "if...verdict changes to..." clause |
| Recommendation | **Assigns-decision-to-reader** -- presenting evidence without issuing the call | `**Verdict**:` does not contain one of {proceed / pause / pivot / abandon} |

---

## V-02 -- Single-Axis: C-33 via Structural Constraint Column in Field Inventory

**Variation axis**: Output format (C-33 inventory annotation)
**Hypothesis**: Adding a third column to the field inventory table -- "Structural
constraint" -- converts the inventory from a field registry into a constraint registry.
The inertia-framing axis row annotates that its three fields are required separate in S4
and must never be consolidated; the annotation names the violation form (`**Position
delta**:`) and states that the constraint is auditable from this table alone without
reading section templates or checklists. The falsifiability axis row confirms its fields
are independently verifiable (no anti-consolidation constraint applies). This satisfies
C-33 unambiguously. C-31 and C-32 are deliberately absent: the invariant remains in
R8 V-01's bold+blockquote form (C-31 fails -- no heading), and Section 4 has no
anti-consolidation directive (C-32 fails). Single-axis isolation confirmed.

---

### PROMPT BODY -- V-02

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal -- it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes**

This template was built from two named design axes. Every required labeled field belongs
to one axis. The Layer 1 checklist is produced by a single pass over the complete field
inventory -- one binary-verifiable presence-verification item per required labeled field.
The Structural Constraint column is the authoritative source for consolidation rules --
auditable from this table alone.

| Axis | Required labeled fields | Structural constraint |
|------|-------------------------|-----------------------|
| **Falsifiability axis** | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` | Independent -- each field separately verifiable; no anti-consolidation constraint applies |
| **Inertia-framing axis** | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` | **Required separate in S4 (anti-consolidation -- C-29).** Do not merge into a single field (e.g., `**Position delta**:`). This constraint is auditable from this table alone without reading Section 4 or the checklist. |

Any future extension must: (1) name the design axis, (2) register every new field in
the axis table with its structural constraint, (3) add one binary-verifiable checklist
item per new field before writing any section that uses it.

---

**Checklist Design Invariant**

> **No item tests content quality; each item locates a label string or reports it
> missing.** Any checklist item that requires editorial judgment to answer violates
> this invariant and must be rewritten as a structural presence check before it is used.

Apply this invariant to every item below. Apply it when extending the checklist.

---

**Layer 1 -- Pre-Artifact Checklist**

Run every item before writing any section. Answer YES by locating the named element.
Do not write until all items are YES.

**Section structure:**
1. [ ] Does this output include a labeled **Signal Findings** section?
2. [ ] Does this output include a labeled **What the Signals Say Together** section?
3. [ ] Does this output include a labeled **What Remains Uncertain** section?
4. [ ] Does this output include a labeled **Recommendation** section?

**Falsifiability-axis field registration:**
5. [ ] Does the Signal Findings section template include `**Inertia verdict**:` on each finding entry?
6. [ ] Does the What the Signals Say Together section include `**Pattern claim**:`?
7. [ ] Does the What the Signals Say Together section include `**Disproof condition**:`?
8. [ ] Does the What Remains Uncertain section include `**Verdict consequence**:`?
9. [ ] Does the Recommendation section include `**Verdict**:`?

**Inertia-framing-axis field registration (registered at incorporation time):**
10. [ ] Does the Recommendation section include `**Prior position**:`?
11. [ ] Does the Recommendation section include `**Baseline distance**:`?
12. [ ] Does the Recommendation section include `**Signals establish**:`?

*(Items 1-4: section structure. Items 5-12: one item per required labeled field, derived
from the two-axis field inventory. Each item answered by locating the label string or
reporting it missing -- consistent with the Checklist Design Invariant above. Structural
constraints on the inertia-framing axis fields are registered in the inventory table's
Structural Constraint column.)*

---

**Layer 2 -- Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience -- not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding change whether to build `{topic}`?**

For each signal, write:

```
**[Signal name]** -- [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES -- this moves the prior position /
                     NO -- this confirms the prior position /
                     PARTIAL -- [one clause naming what specifically shifts]]
```

If `**Inertia verdict**:` is NO and the finding does not affect any other decision
dimension, omit the signal. Close this section with a one-line note stating how many
signals were excluded and the shared basis for exclusion.

Wrong operation: **Contents-report** -- transcribing what the signal said rather than
naming what it changes for the build decision. Detection: any entry missing
`**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the shape the signals collectively form.*

Write the cross-signal claim. It must be true of the signal set as a whole, not
directly stated in any single signal artifact, and causal: it names WHY the signals
converge, not THAT they converge.

```
**Pattern claim**: [one sentence. Cross-signal. Causal: "signals converge because
                   [specific structural reason]", not "signals agree".]

**Disproof condition**: [The claim fails if: [specific observable condition that,
                        if shown to hold, invalidates the pattern.]]
```

Write `**Disproof condition**:` last: after committing to the pattern claim, ask what
would someone need to show is false in order to disprove it. That answer belongs in
this field -- not in the prose above it.

Voice anchors: *What's striking is... / The convergence is not coincidental -- it
reflects... / The evidence forces a conclusion I did not enter this investigation
expecting...*

Wrong operation: **Signal-list** -- naming each signal's contribution without naming
the cross-signal claim. Detection: the pattern cannot be stated in one sentence that
mentions no individual signal by name.

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without surrendering the verdict.*

Every named uncertainty must complete the verdict-consequence arc. An uncertainty that
does not change the recommendation is decision-neutral and does not appear here.

```
**Verdict consequence**: [If [condition A holds / is shown false], the verdict
                         changes from [current] to [alternative A].
                         If [condition B], the verdict changes to [alternative B].]
```

**Anti-neutral directive -- required for this section.** Locate any sentence that names
an uncertainty without naming its consequence for the verdict. Revise or remove it.

Strings to scan for and remove:
- "More research may be needed on X"
- "There is some uncertainty around X"
- "This area warrants further investigation"
- "It is unclear whether X"
- "Future work could explore X"

Required form: "We do not know [X]. If X is shown to be false, the verdict becomes
[Y]. Resolution method: [specific investigation]."

Wrong operation: **Verdict-consequence gap** -- naming uncertainty without naming its
effect on the verdict. Detection: any uncertainty sentence without an
"if...verdict changes to..." clause.

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Measure position against the prior. Defend the verdict against the
adjacent alternative. Name the first action. Do not assign the decision to the reader.

Required labeled fields (see inventory Structural Constraint column for consolidation rules):

```
**Prior position**: [What the team believed about {topic} before this investigation.]

**Baseline distance**: [How far the signals have moved the position from that
                        baseline -- the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the delta
                        defensible -- the compound inference.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] -- specifically [action], because
[**Pattern claim**] forces this verdict rather than [adjacent alternative]. This call
stands unless [**Disproof condition**] is shown to hold."

**Anti-neutral directive -- required for this section.** Scan every sentence for strings
that give the reader a way not to act.

Strings to scan for and remove:
- "Based on the available evidence, it would be reasonable to..."
- "The team should consider..."
- "It may be worth exploring..."
- "Given the above, a reasonable next step would be..."
- "The evidence supports moving forward, though caution is advised"
- "A possible path forward is..."
- "One option would be to..."
- "This suggests that..."

Wrong operation: **Assigns-decision-to-reader** -- presenting evidence without issuing
the call. Detection: `**Verdict**:` does not contain one of
{proceed / pause / pivot / abandon}.

---

**Layer 3 -- Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Signal Findings | **Contents-report** -- transcribing what the signal said rather than naming what it changes for the build decision | Any finding entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** -- naming each signal's contribution without naming the cross-signal claim | The pattern cannot be stated in one sentence that mentions no individual signal by name |
| What Remains Uncertain | **Verdict-consequence gap** -- naming uncertainty without naming its effect on the recommendation | Any uncertainty sentence without an "if...verdict changes to..." clause |
| Recommendation | **Assigns-decision-to-reader** -- presenting evidence without issuing the call | `**Verdict**:` does not contain one of {proceed / pause / pivot / abandon} |

---

## V-03 -- Single-Axis: C-32 Anti-Consolidation Directive at Section 4 Template Level

**Variation axis**: Phrasing register (C-32 anti-consolidation directive, lean imperative)
**Hypothesis**: Extending R8 V-03's lean imperative register to carry C-32: the Section 4
template opens with an explicit anti-consolidation directive block co-located with the
field definitions, stating the prohibition before the fields appear. The directive names
the violation form. At field-entry time the author cannot miss the constraint: it precedes
the field list. Register is lean throughout -- consistent with R8 V-03's pattern, which
confirmed register orthogonality to C-28/C-29/C-30. R9 confirms the same orthogonality
for C-32. C-31 (heading block) and C-33 (inventory annotation) are deliberately absent.

---

### PROMPT BODY -- V-03

Produce the `topic-story` artifact for `{topic}`. Synthesize signals into a decision
narrative. Not a summary -- an editorial synthesis in your voice.

---

**Design Axes and Field Inventory**

Two axes. One field inventory. One checklist item per field.

| Axis | Fields |
|------|--------|
| Falsifiability | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` |
| Inertia-framing | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` |

---

**Checklist Invariant**: No item tests content quality; each item locates a label string
or reports it missing.

**Layer 1 -- Pre-Artifact Checklist**

Locate each element or stop. All YES before writing.

1. [ ] **Signal Findings** section labeled?
2. [ ] **What the Signals Say Together** section labeled?
3. [ ] **What Remains Uncertain** section labeled?
4. [ ] **Recommendation** section labeled?
5. [ ] `**Inertia verdict**:` on each finding entry?
6. [ ] `**Pattern claim**:` in synthesis section?
7. [ ] `**Disproof condition**:` in synthesis section?
8. [ ] `**Verdict consequence**:` in uncertainty section?
9. [ ] `**Verdict**:` in recommendation section?
10. [ ] `**Prior position**:` in recommendation section?
11. [ ] `**Baseline distance**:` in recommendation section?
12. [ ] `**Signals establish**:` in recommendation section?

---

**Layer 2 -- Section Templates**

---

**Section 1: Signal Findings**

Curate. Do not transcribe.

Per finding: apply the build-decision filter first. **Does this finding change whether
to build `{topic}`?**

Write:

```
**[Signal name]** -- [one to three sentences. Key finding only.]
**Inertia verdict**: [YES / NO / PARTIAL -- one clause naming what shifts]
```

NO with nothing else changed: omit the signal. Note exclusion count at section end.

Wrong operation: Contents-report. Detection: any entry missing `**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

Name the shape. Not the list.

The cross-signal claim must be: true of the set as a whole, absent from any individual
signal, causal.

```
**Pattern claim**: [One sentence. Why signals converge, not that they do.]

**Disproof condition**: [The claim fails if: [specific observable condition.]]
```

Write `**Disproof condition**:` last. Ask: what would disprove this? Put that in the field.

*What's striking is... / The convergence reflects... / The evidence forces...*

Wrong operation: Signal-list. Detection: pattern cannot be stated without naming
individual signals.

---

**Section 3: What Remains Uncertain**

Name limits. Do not surrender the verdict.

Every uncertainty must close the arc. Decision-neutral uncertainties are omitted.

```
**Verdict consequence**: [If [condition A], verdict changes to [alt A].
                         If [condition B], verdict changes to [alt B].]
```

**Anti-neutral scan -- required.** Locate sentences naming uncertainty without naming
verdict consequence. Remove them.

Strings to remove: "More research may be needed" / "There is some uncertainty around X"
/ "This area warrants further investigation" / "It is unclear whether X" /
"Future work could explore X"

Wrong operation: Verdict-consequence gap. Detection: any uncertainty sentence without
an "if...verdict changes to..." clause.

---

**Section 4: Recommendation**

Issue the call. Measure the distance. Defend the verdict. Name the action.
Do not hand the decision to the reader.

**Anti-consolidation directive**: The three inertia fields below are required as
separate labeled entries. Do not consolidate `**Prior position**:`, `**Baseline
distance**:`, and `**Signals establish**:` into a single field. A consolidated
`**Position delta**:` field or equivalent fails C-29 and fails this section directive.

```
**Prior position**: [Team's position before this investigation.]
**Baseline distance**: [How far signals moved that position.]
**Signals establish**: [The inference that makes the movement defensible.]
**Verdict**: [proceed / pause / pivot / abandon]
```

Sentence: "I recommend [verdict] -- specifically [action], because [**Pattern claim**]
forces this verdict rather than [adjacent alternative]. This call stands unless
[**Disproof condition**] is shown to hold."

**Anti-neutral scan -- required.** Scan for reader-escape strings.

Strings to remove: "Based on the available evidence, it would be reasonable to..." /
"The team should consider..." / "It may be worth exploring..." / "Given the above, a
reasonable next step would be..." / "The evidence supports moving forward, though
caution is advised" / "A possible path forward is..." / "One option would be to..." /
"This suggests that..."

Wrong operation: Assigns-decision-to-reader. Detection: `**Verdict**:` not one of
{proceed / pause / pivot / abandon}.

---

**Layer 3 -- Per-Section Failure Modes**

| Section | Wrong operation | Detection |
|---------|----------------|-----------|
| Signal Findings | Contents-report | Any entry missing `**Inertia verdict**:` |
| What Signals Say Together | Signal-list | Pattern cannot be stated without naming individual signals |
| What Remains Uncertain | Verdict-consequence gap | Any uncertainty sentence without "if...verdict changes to..." |
| Recommendation | Assigns-decision-to-reader | `**Verdict**:` not one of {proceed / pause / pivot / abandon} |

---

## V-04 -- Compound: C-31 Heading Block + C-32 Section Directive

**Variation axes**: Output format + lifecycle emphasis
**Hypothesis**: Combining C-31 and C-32 in one variation tests whether the two criteria
reinforce each other without conflict. C-31 fires at the pre-section layer (the invariant
heading is the last thing an author reads before the checklist); C-32 fires inside Section
4 (the directive is the first thing an author reads before writing inertia fields). The
lifecycle boundary between these two locations is explicit: the invariant governs checklist
design, the section directive governs field-entry behavior. When both are present, the
anti-consolidation constraint is enforced at two structurally distinct moments: pre-write
(checklist item 10-12 verifying separate fields) and at-write (Section 4 directive naming
the prohibition before the fields). C-33 is deliberately absent -- this compound targets
C-31 + C-32 while leaving the inventory as a two-column table.

---

### PROMPT BODY -- V-04

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal -- it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes**

This template was built from two named design axes. Every required labeled field belongs
to one axis. The Layer 1 checklist is produced by a single pass over the complete field
inventory -- one binary-verifiable presence-verification item per required labeled field.

| Axis | Required labeled fields introduced |
|------|-------------------------------------|
| **Falsifiability axis** | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` |
| **Inertia-framing axis** | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` |

Any future extension must: (1) name the design axis, (2) register every new field in
the axis table, (3) add one binary-verifiable checklist item per new field before writing
any section that uses it.

---

### Checklist Design Invariant

**Rule**: No item tests content quality; each item locates a label string or reports
it missing. An item that requires editorial judgment to answer violates this invariant.

**Repair operation**: Rewrite any failing item as:
> "Does [Section name] include the label `**[field name]**:`?"

Apply this invariant to every item in Layer 1. Apply it when extending the checklist.

---

**Layer 1 -- Pre-Artifact Checklist**

Run every item before writing any section. Answer YES by locating the named element.
Do not write until all items are YES.

**Section structure:**
1. [ ] Does this output include a labeled **Signal Findings** section?
2. [ ] Does this output include a labeled **What the Signals Say Together** section?
3. [ ] Does this output include a labeled **What Remains Uncertain** section?
4. [ ] Does this output include a labeled **Recommendation** section?

**Falsifiability-axis field registration:**
5. [ ] Does the Signal Findings section template include `**Inertia verdict**:` on each finding entry?
6. [ ] Does the What the Signals Say Together section include `**Pattern claim**:`?
7. [ ] Does the What the Signals Say Together section include `**Disproof condition**:`?
8. [ ] Does the What Remains Uncertain section include `**Verdict consequence**:`?
9. [ ] Does the Recommendation section include `**Verdict**:`?

**Inertia-framing-axis field registration (registered at incorporation time):**
10. [ ] Does the Recommendation section include `**Prior position**:`?
11. [ ] Does the Recommendation section include `**Baseline distance**:`?
12. [ ] Does the Recommendation section include `**Signals establish**:`?

*(Items 1-4: section structure. Items 5-12: one item per required labeled field, derived
from the two-axis field inventory. Each item answered by locating the label string or
reporting it missing -- consistent with the Checklist Design Invariant above.)*

---

**Layer 2 -- Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience -- not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding change whether to build `{topic}`?**

For each signal, write:

```
**[Signal name]** -- [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES -- this moves the prior position /
                     NO -- this confirms the prior position /
                     PARTIAL -- [one clause naming what specifically shifts]]
```

If `**Inertia verdict**:` is NO and the finding does not affect any other decision
dimension, omit the signal. Close this section with a one-line note stating how many
signals were excluded and the shared basis for exclusion.

Wrong operation: **Contents-report** -- transcribing what the signal said rather than
naming what it changes for the build decision. Detection: any entry missing
`**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the shape the signals collectively form.*

Write the cross-signal claim. It must be true of the signal set as a whole, not
directly stated in any single signal artifact, and causal: it names WHY the signals
converge, not THAT they converge.

```
**Pattern claim**: [one sentence. Cross-signal. Causal: "signals converge because
                   [specific structural reason]", not "signals agree".]

**Disproof condition**: [The claim fails if: [specific observable condition that,
                        if shown to hold, invalidates the pattern.]]
```

Write `**Disproof condition**:` last: after committing to the pattern claim, ask what
would someone need to show is false in order to disprove it. That answer belongs in
this field -- not in the prose above it.

Voice anchors: *What's striking is... / The convergence is not coincidental -- it
reflects... / The evidence forces a conclusion I did not enter this investigation
expecting...*

Wrong operation: **Signal-list** -- naming each signal's contribution without naming
the cross-signal claim. Detection: the pattern cannot be stated in one sentence that
mentions no individual signal by name.

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without surrendering the verdict.*

Every named uncertainty must complete the verdict-consequence arc. An uncertainty that
does not change the recommendation is decision-neutral and does not appear here.

```
**Verdict consequence**: [If [condition A holds / is shown false], the verdict
                         changes from [current] to [alternative A].
                         If [condition B], the verdict changes to [alternative B].]
```

**Anti-neutral directive -- required for this section.** Locate any sentence that names
an uncertainty without naming its consequence for the verdict. Revise or remove it.

Strings to scan for and remove:
- "More research may be needed on X"
- "There is some uncertainty around X"
- "This area warrants further investigation"
- "It is unclear whether X"
- "Future work could explore X"

Required form: "We do not know [X]. If X is shown to be false, the verdict becomes
[Y]. Resolution method: [specific investigation]."

Wrong operation: **Verdict-consequence gap** -- naming uncertainty without naming its
effect on the verdict. Detection: any uncertainty sentence without an
"if...verdict changes to..." clause.

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Measure position against the prior. Defend the verdict against the
adjacent alternative. Name the first action. Do not assign the decision to the reader.

**Anti-consolidation directive**: The three inertia fields below must appear as separate
labeled entries. Do not consolidate `**Prior position**:`, `**Baseline distance**:`, and
`**Signals establish**:` into a single field. A consolidated `**Position delta**:` field
or equivalent fails C-29 and fails this section template.

Required labeled fields:

```
**Prior position**: [What the team believed about {topic} before this investigation.]

**Baseline distance**: [How far the signals have moved the position from that
                        baseline -- the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the delta
                        defensible -- the compound inference.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] -- specifically [action], because
[**Pattern claim**] forces this verdict rather than [adjacent alternative]. This call
stands unless [**Disproof condition**] is shown to hold."

*(The sentence form names `**Disproof condition**:` from Section 2 by field reference.
The recommendation is structurally conditioned by the falsifiability analysis: the
verdict is issued and its revision condition is named in the same required template slot.)*

**Anti-neutral directive -- required for this section.** Scan every sentence for strings
that give the reader a way not to act.

Strings to scan for and remove:
- "Based on the available evidence, it would be reasonable to..."
- "The team should consider..."
- "It may be worth exploring..."
- "Given the above, a reasonable next step would be..."
- "The evidence supports moving forward, though caution is advised"
- "A possible path forward is..."
- "One option would be to..."
- "This suggests that..."

Wrong operation: **Assigns-decision-to-reader** -- presenting evidence without issuing
the call. Detection: `**Verdict**:` does not contain one of
{proceed / pause / pivot / abandon}.

---

**Layer 3 -- Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Signal Findings | **Contents-report** -- transcribing what the signal said rather than naming what it changes for the build decision | Any finding entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** -- naming each signal's contribution without naming the cross-signal claim | The pattern cannot be stated in one sentence that mentions no individual signal by name |
| What Remains Uncertain | **Verdict-consequence gap** -- naming uncertainty without naming its effect on the recommendation | Any uncertainty sentence without an "if...verdict changes to..." clause |
| Recommendation | **Assigns-decision-to-reader** -- presenting evidence without issuing the call | `**Verdict**:` does not contain one of {proceed / pause / pivot / abandon} |

---

## V-05 -- Compound: C-31 + C-32 + C-33 (Inventory-First, All Three Satisfied)

**Variation axes**: Output format + inertia framing
**Hypothesis**: All three new criteria can be satisfied simultaneously without
architectural conflict by promoting the field inventory to the authoritative constraint
source (C-33), adding a heading-block invariant with repair formula (C-31), and
cross-referencing the inventory annotation from within Section 4 (C-32). The key design
claim is that C-33 (inventory annotation) and C-32 (section directive) are not redundant
-- they serve different audit procedures. C-33 enables inventory-only audits: any reader
with the field table can identify consolidation violations without reading section templates.
C-32 enables at-write enforcement: any author writing Section 4 encounters the constraint
before the fields. Both are required because they fire on different moments in the artifact
lifecycle. V-05 is the "full structural saturation" variation: all three R9 criteria
present, no criterion deliberately omitted.

---

### PROMPT BODY -- V-05

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal -- it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes and Field Inventory**

This template was built from two named design axes. Every required labeled field belongs
to one axis. The Structural Constraint column is the authoritative source for
consolidation rules -- any consolidation violation is auditable from this table alone
without reading section templates or checklists.

| Axis | Required labeled fields | Structural constraint |
|------|-------------------------|-----------------------|
| **Falsifiability axis** | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` | Independent -- each field separately verifiable; no anti-consolidation constraint |
| **Inertia-framing axis** | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` | **Required separate in S4 (anti-consolidation -- C-29).** Do not merge into a single field (e.g., `**Position delta**:`). Constraint is auditable from this table alone without reading Section 4 template or the checklist. |

Any future extension must: (1) name the design axis, (2) register every new field with
its structural constraint in the axis table, (3) add one binary-verifiable checklist item
per new field before writing any section that uses it.

---

### Checklist Design Invariant

**Rule**: No item tests content quality; each item locates a label string or reports
it missing. An item that requires editorial judgment to answer violates this invariant.

**Repair operation**: Rewrite any failing item as:
> "Does [Section name] include the label `**[field name]**:`?"

Apply this invariant to every item in Layer 1. Apply it when extending the checklist.

---

**Layer 1 -- Pre-Artifact Checklist**

Run every item before writing any section. Answer YES by locating the named element.
Do not write until all items are YES.

**Section structure:**
1. [ ] Does this output include a labeled **Signal Findings** section?
2. [ ] Does this output include a labeled **What the Signals Say Together** section?
3. [ ] Does this output include a labeled **What Remains Uncertain** section?
4. [ ] Does this output include a labeled **Recommendation** section?

**Falsifiability-axis field registration:**
5. [ ] Does the Signal Findings section template include `**Inertia verdict**:` on each finding entry?
6. [ ] Does the What the Signals Say Together section include `**Pattern claim**:`?
7. [ ] Does the What the Signals Say Together section include `**Disproof condition**:`?
8. [ ] Does the What Remains Uncertain section include `**Verdict consequence**:`?
9. [ ] Does the Recommendation section include `**Verdict**:`?

**Inertia-framing-axis field registration (registered at incorporation time):**
10. [ ] Does the Recommendation section include `**Prior position**:`?
11. [ ] Does the Recommendation section include `**Baseline distance**:`?
12. [ ] Does the Recommendation section include `**Signals establish**:`?

*(Items 1-4: section structure. Items 5-12: one item per required labeled field, derived
from the two-axis field inventory. Structural constraints for items 10-12 are registered
in the inventory table's Structural Constraint column -- the anti-consolidation rule
is auditable from the inventory without re-reading this checklist.)*

---

**Layer 2 -- Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience -- not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding change whether to build `{topic}`?**

For each signal, write:

```
**[Signal name]** -- [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES -- this moves the prior position /
                     NO -- this confirms the prior position /
                     PARTIAL -- [one clause naming what specifically shifts]]
```

If `**Inertia verdict**:` is NO and the finding does not affect any other decision
dimension, omit the signal. Close this section with a one-line note stating how many
signals were excluded and the shared basis for exclusion.

Wrong operation: **Contents-report** -- transcribing what the signal said rather than
naming what it changes for the build decision. Detection: any entry missing
`**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the shape the signals collectively form.*

Write the cross-signal claim. It must be true of the signal set as a whole, not
directly stated in any single signal artifact, and causal: it names WHY the signals
converge, not THAT they converge.

```
**Pattern claim**: [one sentence. Cross-signal. Causal: "signals converge because
                   [specific structural reason]", not "signals agree".]

**Disproof condition**: [The claim fails if: [specific observable condition that,
                        if shown to hold, invalidates the pattern.]]
```

Write `**Disproof condition**:` last: after committing to the pattern claim, ask what
would someone need to show is false in order to disprove it. That answer belongs in
this field -- not in the prose above it.

Voice anchors: *What's striking is... / The convergence is not coincidental -- it
reflects... / The evidence forces a conclusion I did not enter this investigation
expecting...*

Wrong operation: **Signal-list** -- naming each signal's contribution without naming
the cross-signal claim. Detection: the pattern cannot be stated in one sentence that
mentions no individual signal by name.

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without surrendering the verdict.*

Every named uncertainty must complete the verdict-consequence arc. An uncertainty that
does not change the recommendation is decision-neutral and does not appear here.

```
**Verdict consequence**: [If [condition A holds / is shown false], the verdict
                         changes from [current] to [alternative A].
                         If [condition B], the verdict changes to [alternative B].]
```

**Anti-neutral directive -- required for this section.** Locate any sentence that names
an uncertainty without naming its consequence for the verdict. Revise or remove it.

Strings to scan for and remove:
- "More research may be needed on X"
- "There is some uncertainty around X"
- "This area warrants further investigation"
- "It is unclear whether X"
- "Future work could explore X"

Required form: "We do not know [X]. If X is shown to be false, the verdict becomes
[Y]. Resolution method: [specific investigation]."

Wrong operation: **Verdict-consequence gap** -- naming uncertainty without naming its
effect on the verdict. Detection: any uncertainty sentence without an
"if...verdict changes to..." clause.

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Measure position against the prior. Defend the verdict against the
adjacent alternative. Name the first action. Do not assign the decision to the reader.

**Anti-consolidation directive (see inventory Structural Constraint column for the
authoritative rule)**: The three inertia fields below must appear as separate labeled
entries. Do not consolidate `**Prior position**:`, `**Baseline distance**:`, and
`**Signals establish**:` into a single field. Consolidation violates the constraint
registered in the field inventory and fails C-29.

Required labeled fields:

```
**Prior position**: [What the team believed about {topic} before this investigation.]

**Baseline distance**: [How far the signals have moved the position from that
                        baseline -- the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the delta
                        defensible -- the compound inference.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] -- specifically [action], because
[**Pattern claim**] forces this verdict rather than [adjacent alternative]. This call
stands unless [**Disproof condition**] is shown to hold."

*(The sentence form names `**Disproof condition**:` from Section 2 by field reference.
The recommendation is structurally conditioned by the falsifiability analysis: the
verdict is issued and its revision condition is named in the same required template slot.)*

**Anti-neutral directive -- required for this section.** Scan every sentence for strings
that give the reader a way not to act.

Strings to scan for and remove:
- "Based on the available evidence, it would be reasonable to..."
- "The team should consider..."
- "It may be worth exploring..."
- "Given the above, a reasonable next step would be..."
- "The evidence supports moving forward, though caution is advised"
- "A possible path forward is..."
- "One option would be to..."
- "This suggests that..."

Wrong operation: **Assigns-decision-to-reader** -- presenting evidence without issuing
the call. Detection: `**Verdict**:` does not contain one of
{proceed / pause / pivot / abandon}.

---

**Layer 3 -- Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Signal Findings | **Contents-report** -- transcribing what the signal said rather than naming what it changes for the build decision | Any finding entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** -- naming each signal's contribution without naming the cross-signal claim | The pattern cannot be stated in one sentence that mentions no individual signal by name |
| What Remains Uncertain | **Verdict-consequence gap** -- naming uncertainty without naming its effect on the recommendation | Any uncertainty sentence without an "if...verdict changes to..." clause |
| Recommendation | **Assigns-decision-to-reader** -- presenting evidence without issuing the call | `**Verdict**:` does not contain one of {proceed / pause / pivot / abandon} |
