# R11 Variations -- `topic-story` (v11 Rubric, 39 Criteria)

**Round**: 11
**Skill**: `topic-story`
**Base rubric**: `topic-story-rubric-v11-2026-03-15.md`
**New criteria this round**: C-37, C-38, C-39

---

## R10 State Summary

R10: V-05 scored 100.0 on all 39 criteria under v11 (the three new v11 criteria were
already structurally present in R10 V-05):

- **C-37**: R10 V-05 repair block named `[Section name]` and `[field name]` with source
  declarations inline: "`[Section name]` → the section's heading text... `[field name]` →
  the field's label string from the inventory... Do not derive -- substitute directly from
  these two sources." Instantiation prescribed; no derivation required.
- **C-38**: R10 V-05 Section 4 directive: "field inventory above, Structural Constraint
  column, Inertia-framing axis row -- that cell is the single point of update for this
  constraint; this directive is a reference to it, not an independent restatement."
  Row and column named; auditor reaches one cell without scanning.
- **C-39**: R10 V-05 checklist footer: "The inventory is the authoritative constraint
  source. Items 10-12 are references to the inventory's Structural Constraint column,
  Inertia-framing axis row -- not independent restatements. Updating that inventory cell
  propagates to the Section 4 directive and to these items; the checklist is not separately
  authoritative for constraint content." Propagation rule and authority denial both present.

**R10 baseline under v11**: V-05 passes all 32 aspirational criteria -- 100.0.

**R11 design requirement**: All five variations must preserve C-37, C-38, C-39. Variation
axes explore three structural properties not yet captured by any existing criterion:

- **C-37/C-38/C-39 upgrade (axis: inertia framing)**: The field inventory names two design
  axes but the S1 build-decision filter does not name the competitor (the status quo -- not
  building) that inertia is measured against. The `**Inertia verdict**:` labels say "this
  moves the prior position" without naming what the prior position IS relative to the
  decision. An author satisfies the filter by asking any binary decision question; a filter
  that names the status quo competitor ties S1 curation to the same baseline that S4 measures
  against `**Prior position**:`. The inertia axis is architecturally present in the field
  inventory but semantically absent from the S1 operation.

- **Axis: output format (inventory section column)**: The field inventory maps axis →
  fields → structural constraint. An auditor verifying an output knows what fields exist
  and what constraints apply, but must read section templates to know WHERE each field
  appears. Adding a Section column extends the "auditable from this table alone" principle
  from constraints to placement: field presence, placement section, and structural constraint
  are all derivable from the inventory without reading any section template.

- **Axis: lifecycle emphasis (per-section entry conditions)**: The Layer 1 checklist is a
  pre-artifact gate verifying template compliance before writing begins, but it does not
  enforce section sequencing. An author could write S4 before S2 and the checklist would
  not detect the violation. Per-section entry conditions make the writing sequence
  structurally explicit: each section names what must be completed in the prior section
  before entry is valid.

**R11 baseline per criterion (R10 V-01 through V-04 scored against v11)**:

| Criterion | V-01 (R10) | V-02 (R10) | V-03 (R10) | V-04 (R10) | V-05 (R10) |
|-----------|------------|------------|------------|------------|------------|
| C-37 (repair substitution variable labels) | PASSES | FAILS | FAILS | PASSES | PASSES |
| C-38 (directive exact row+column cell) | FAILS | PASSES | FAILS | PASSES | PASSES |
| C-39 (footer propagation rule + authority denial) | FAILS | FAILS | PASSES | FAILS | PASSES |

R10 V-01 through V-04 under v11: each fails 1-3 new criteria. R10 V-05 passes all 39.

**Variation axes for R11**:
- Single-axis: Inertia framing (status quo competitor named in S1 filter) -- V-01
- Single-axis: Output format (Section column in field inventory -- placement auditable
  from table) -- V-02
- Single-axis: Lifecycle emphasis (per-section entry conditions) -- V-03
- Compound: Inertia framing + output format (V-01 + V-02) -- V-04
- Compound: Inertia framing + output format + lifecycle emphasis + integration
  (V-01 + V-02 + V-03 + entry conditions cross-referenced to inventory Section column) -- V-05

---

## V-01 -- Single-Axis: Inertia Framing Through S1

**Variation axis**: Inertia framing (how prominently the status-quo competitor is featured)
**Hypothesis**: The build-decision filter in S1 asks "Does this finding change whether to
build `{topic}`?" -- a binary gate that names the positive decision (build) without naming
the null hypothesis (the status quo: not building, or the current approach). The
`**Inertia verdict**:` labels say "moves the prior position" without grounding the prior
position in the decision frame. S4 explicitly measures against `**Prior position**:`, but
S1 does not name the competitor that position represents. An author satisfying the S1 filter
can answer any binary question; an author satisfying a status-quo-named filter must answer
whether the finding DISPLACES the default outcome. The inertia axis is registered in the
field inventory and structurally enforced in S4 -- but S1, the section that decides which
signals reach S4's measurement at all, does not carry the same grounding. Naming the status
quo competitor in the S1 filter ties S1 curation directly to the baseline S4 measures
against, making the inertia thread coherent across the full document. All other structural
elements are unchanged from R10 V-05 (single-axis isolation: C-38, C-39 deliberately
identical to R10 V-05).

---

### PROMPT BODY -- V-01

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

Any future extension must follow this sequence in order: (1) name the design axis;
(2) register every new field with its structural constraint in the inventory table --
**inventory is updated first and is the authoritative source**; (3) add any required
co-location directives to the relevant section templates, cross-referencing the specific
inventory entry (column and row) rather than independently restating the constraint;
(4) add one binary-verifiable presence-verification checklist item per new field,
designating the item as a reference to the inventory entry -- not an independent
constraint restatement.

---

### Checklist Design Invariant

**Rule**: No item tests content quality; each item locates a label string or reports
it missing. An item that requires editorial judgment to answer violates this invariant.

**Repair operation**: Rewrite any failing item as:
> "Does [Section name] include the label `**[field name]**:`?"
>
> Substitution: `[Section name]` → the section's heading text (e.g., "Signal Findings",
> "Recommendation"). `[field name]` → the field's label string from the inventory (e.g.,
> "Prior position", "Verdict"). Do not derive -- substitute directly from these two sources.

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

*(Items 1-4: section structure. Items 5-12: field presence. The inventory is the
authoritative constraint source. Items 10-12 are references to the inventory's
Structural Constraint column, Inertia-framing axis row -- not independent restatements.
Updating that inventory cell propagates to the Section 4 directive and to these items;
the checklist is not separately authoritative for constraint content.)*

---

**Layer 2 -- Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience -- not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding move the decision away from the status quo (not building `{topic}`)?**
The status quo is the null outcome -- the case for not building. Name what specifically
shifts.

For each signal, write:

```
**[Signal name]** -- [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES -- this displaces the status quo: the case for not building
                         gets weaker /
                     NO -- this confirms the status quo holds: no reason to build
                         emerges /
                     PARTIAL -- [one clause naming what aspect of the status quo shifts]]
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

**Anti-consolidation directive (authoritative rule: field inventory above, Structural
Constraint column, Inertia-framing axis row -- that cell is the single point of update
for this constraint; this directive is a reference to it, not an independent restatement)**:
The three inertia fields below must appear as separate labeled entries. Do not consolidate
`**Prior position**:`, `**Baseline distance**:`, and `**Signals establish**:` into a
single field. Consolidation violates the constraint registered at that inventory cell and
fails C-29.

Required labeled fields:

```
**Prior position**: [What the team believed about {topic} before this investigation --
                    the status quo position the signals are measured against.]

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

## V-02 -- Single-Axis: Section Column in Field Inventory

**Variation axis**: Output format (field inventory completeness -- placement auditable
from table)
**Hypothesis**: The current field inventory maps axis → fields → structural constraint.
An auditor verifying an output knows WHAT fields must be present and WHAT consolidation
constraints apply, but must read section templates to know WHERE each field appears. The
"auditable from this table alone" statement (used for constraints) does not extend to
placement. Adding a Section column to the inventory -- mapping each field to its section
(S1, S2, S3, or S4) -- makes the inventory a complete four-way registry: for any required
field, the auditor can determine (a) which axis it belongs to, (b) which section it appears
in, (c) its structural constraint, without reading any section template. This extends the
existing "auditable from this table" principle from constraints to placement, completing
the inventory's authority over field governance. A v12 criterion may fire on whether the
Section column is present and the "auditable from this table" claim covers placement in
addition to constraints. C-37, C-38, C-39 are unchanged from R10 V-05 (single-axis
isolation; inertia framing and lifecycle emphasis deliberately absent).

---

### PROMPT BODY -- V-02

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal -- it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes and Field Inventory**

This template was built from two named design axes. Every required labeled field belongs
to one axis and one section. The Structural Constraint column is the authoritative source
for consolidation rules; the Section column is the authoritative source for field
placement. Any consolidation violation and any misplaced field are auditable from this
table alone without reading section templates or checklists.

| Axis | Section | Required labeled fields | Structural constraint |
|------|---------|-------------------------|-----------------------|
| **Falsifiability axis** | S1 | `**Inertia verdict**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Falsifiability axis** | S2 | `**Pattern claim**:` · `**Disproof condition**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Falsifiability axis** | S3 | `**Verdict consequence**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Falsifiability axis** | S4 | `**Verdict**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Inertia-framing axis** | S4 | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` | **Required separate in S4 (anti-consolidation -- C-29).** Do not merge into a single field (e.g., `**Position delta**:`). Constraint is auditable from this table alone. |

Any future extension must follow this sequence in order: (1) name the design axis;
(2) register every new field with its section AND structural constraint in the inventory
table -- **inventory is updated first and is the authoritative source for both placement
and constraints**; (3) add any required co-location directives to the relevant section
templates, cross-referencing the specific inventory entry (axis row, Section column, and
Structural Constraint column) rather than independently restating the constraint;
(4) add one binary-verifiable presence-verification checklist item per new field,
designating the item as a reference to the inventory entry -- not an independent
constraint restatement.

---

### Checklist Design Invariant

**Rule**: No item tests content quality; each item locates a label string or reports
it missing. An item that requires editorial judgment to answer violates this invariant.

**Repair operation**: Rewrite any failing item as:
> "Does [Section name] include the label `**[field name]**:`?"
>
> Substitution: `[Section name]` → the section's heading text (e.g., "Signal Findings",
> "Recommendation"). `[field name]` → the field's label string from the inventory (e.g.,
> "Prior position", "Verdict"). Do not derive -- substitute directly from these two sources.

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

*(Items 1-4: section structure. Items 5-12: field presence, organized by axis. The
inventory is the authoritative constraint source. Items 10-12 are references to the
inventory's Structural Constraint column, Inertia-framing axis row -- not independent
restatements. Updating that inventory cell propagates to the Section 4 directive and
to these items; the checklist is not separately authoritative for constraint content.)*

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

**Anti-consolidation directive (authoritative rule: field inventory above, Structural
Constraint column, Inertia-framing axis row -- that cell is the single point of update
for this constraint; this directive is a reference to it, not an independent restatement)**:
The three inertia fields below must appear as separate labeled entries. Do not consolidate
`**Prior position**:`, `**Baseline distance**:`, and `**Signals establish**:` into a
single field. Consolidation violates the constraint registered at that inventory cell and
fails C-29.

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

## V-03 -- Single-Axis: Per-Section Entry Conditions

**Variation axis**: Lifecycle emphasis (how explicitly section boundaries are stated as
entry gates)
**Hypothesis**: The Layer 1 checklist is a pre-artifact gate -- it verifies template
compliance before any writing begins, but it does not enforce the section writing sequence.
An author who writes S4 before S2 would pass the Layer 1 checklist (all template slots are
specified) but would be issuing a verdict before committing to a pattern claim and disproof
condition. The section stances establish cognitive roles but not entry conditions: they say
what to do, not what must be true before entry is valid. Per-section entry conditions close
this gap by naming the predecessor completion state each section requires. S2 cannot be
entered until S1's inertia verdicts are written. S3 cannot be entered until S2's
`**Pattern claim**:` and `**Disproof condition**:` are committed. S4 cannot be entered
until S3's `**Verdict consequence**:` is written. A v12 criterion may fire on whether
per-section entry conditions are present and correctly name the predecessor fields. C-37,
C-38, C-39 are unchanged from R10 V-05 (single-axis isolation; inertia framing and
inventory format deliberately absent).

---

### PROMPT BODY -- V-03

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

Any future extension must follow this sequence in order: (1) name the design axis;
(2) register every new field with its structural constraint in the inventory table --
**inventory is updated first and is the authoritative source**; (3) add any required
co-location directives to the relevant section templates, cross-referencing the specific
inventory entry (column and row) rather than independently restating the constraint;
(4) add one binary-verifiable presence-verification checklist item per new field,
designating the item as a reference to the inventory entry -- not an independent
constraint restatement.

---

### Checklist Design Invariant

**Rule**: No item tests content quality; each item locates a label string or reports
it missing. An item that requires editorial judgment to answer violates this invariant.

**Repair operation**: Rewrite any failing item as:
> "Does [Section name] include the label `**[field name]**:`?"
>
> Substitution: `[Section name]` → the section's heading text (e.g., "Signal Findings",
> "Recommendation"). `[field name]` → the field's label string from the inventory (e.g.,
> "Prior position", "Verdict"). Do not derive -- substitute directly from these two sources.

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

*(Items 1-4: section structure. Items 5-12: field presence. The inventory is the
authoritative constraint source. Items 10-12 are references to the inventory's
Structural Constraint column, Inertia-framing axis row -- not independent restatements.
Updating that inventory cell propagates to the Section 4 directive and to these items;
the checklist is not separately authoritative for constraint content.)*

---

**Layer 2 -- Section Templates**

---

**Section 1: Signal Findings**

**Entry condition**: Layer 1 checklist complete. All 12 items YES. Do not write any
finding until the checklist passes.

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

**Entry condition**: S1 complete. Every included finding has `**Inertia verdict**:`
written. Do not begin S2 until all S1 entries carry this field.

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

**Entry condition**: S2 complete. Both `**Pattern claim**:` and `**Disproof condition**:`
written and committed. Do not begin S3 until both S2 fields are present -- the uncertainty
section names what would trigger the disproof condition, and that condition must be
committed before uncertainty can be characterized against it.

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

**Entry condition**: S3 complete. `**Verdict consequence**:` written with at least one
condition-consequence pair. Do not begin S4 until S3's uncertainty accounting is done --
the verdict must be informed by the consequence analysis, not issued before it.

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Measure position against the prior. Defend the verdict against the
adjacent alternative. Name the first action. Do not assign the decision to the reader.

**Anti-consolidation directive (authoritative rule: field inventory above, Structural
Constraint column, Inertia-framing axis row -- that cell is the single point of update
for this constraint; this directive is a reference to it, not an independent restatement)**:
The three inertia fields below must appear as separate labeled entries. Do not consolidate
`**Prior position**:`, `**Baseline distance**:`, and `**Signals establish**:` into a
single field. Consolidation violates the constraint registered at that inventory cell and
fails C-29.

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

## V-04 -- Compound: V-01 Inertia Framing + V-02 Section Column

**Variation axes**: Inertia framing + output format (field inventory placement)
**Hypothesis**: V-01 makes the status quo competitor explicit in S1 (tying the curation
filter to the same baseline S4 measures). V-02 adds the Section column to the field
inventory (making field placement derivable from the table alone). The two changes target
structurally distinct locations -- V-01 modifies the S1 section body; V-02 modifies the
inventory table header and row structure. Neither change interacts with the other: V-01
does not affect the inventory; V-02 does not affect the S1 filter language. Both can fire
in the same variation without conflict. Together they advance two complementary
properties: the inertia axis is grounded in S1 as well as S4, and the inventory's
authority is extended from constraints to placement. V-03 (per-section entry conditions)
is deliberately absent -- compound of V-01 + V-02 only.

---

### PROMPT BODY -- V-04

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal -- it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes and Field Inventory**

This template was built from two named design axes. Every required labeled field belongs
to one axis and one section. The Structural Constraint column is the authoritative source
for consolidation rules; the Section column is the authoritative source for field
placement. Any consolidation violation and any misplaced field are auditable from this
table alone without reading section templates or checklists.

| Axis | Section | Required labeled fields | Structural constraint |
|------|---------|-------------------------|-----------------------|
| **Falsifiability axis** | S1 | `**Inertia verdict**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Falsifiability axis** | S2 | `**Pattern claim**:` · `**Disproof condition**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Falsifiability axis** | S3 | `**Verdict consequence**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Falsifiability axis** | S4 | `**Verdict**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Inertia-framing axis** | S4 | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` | **Required separate in S4 (anti-consolidation -- C-29).** Do not merge into a single field (e.g., `**Position delta**:`). Constraint is auditable from this table alone. |

Any future extension must follow this sequence in order: (1) name the design axis;
(2) register every new field with its section AND structural constraint in the inventory
table -- **inventory is updated first and is the authoritative source for both placement
and constraints**; (3) add any required co-location directives to the relevant section
templates, cross-referencing the specific inventory entry (axis row, Section column, and
Structural Constraint column) rather than independently restating the constraint;
(4) add one binary-verifiable presence-verification checklist item per new field,
designating the item as a reference to the inventory entry -- not an independent
constraint restatement.

---

### Checklist Design Invariant

**Rule**: No item tests content quality; each item locates a label string or reports
it missing. An item that requires editorial judgment to answer violates this invariant.

**Repair operation**: Rewrite any failing item as:
> "Does [Section name] include the label `**[field name]**:`?"
>
> Substitution: `[Section name]` → the section's heading text (e.g., "Signal Findings",
> "Recommendation"). `[field name]` → the field's label string from the inventory (e.g.,
> "Prior position", "Verdict"). Do not derive -- substitute directly from these two sources.

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

*(Items 1-4: section structure. Items 5-12: field presence, organized by axis. The
inventory is the authoritative constraint source. Items 10-12 are references to the
inventory's Structural Constraint column, Inertia-framing axis row -- not independent
restatements. Updating that inventory cell propagates to the Section 4 directive and
to these items; the checklist is not separately authoritative for constraint content.)*

---

**Layer 2 -- Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience -- not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding move the decision away from the status quo (not building `{topic}`)?**
The status quo is the null outcome -- the case for not building. Name what specifically
shifts.

For each signal, write:

```
**[Signal name]** -- [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES -- this displaces the status quo: the case for not building
                         gets weaker /
                     NO -- this confirms the status quo holds: no reason to build
                         emerges /
                     PARTIAL -- [one clause naming what aspect of the status quo shifts]]
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

**Anti-consolidation directive (authoritative rule: field inventory above, Structural
Constraint column, Inertia-framing axis row -- that cell is the single point of update
for this constraint; this directive is a reference to it, not an independent restatement)**:
The three inertia fields below must appear as separate labeled entries. Do not consolidate
`**Prior position**:`, `**Baseline distance**:`, and `**Signals establish**:` into a
single field. Consolidation violates the constraint registered at that inventory cell and
fails C-29.

Required labeled fields:

```
**Prior position**: [What the team believed about {topic} before this investigation --
                    the status quo position the signals are measured against.]

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

## V-05 -- Compound: V-01 + V-02 + V-03 + Entry-Condition/Inventory Integration

**Variation axes**: Inertia framing + output format + lifecycle emphasis + integration
**Hypothesis**: Full structural saturation for R11. V-01 makes the status quo competitor
explicit in S1 (grounding curation in the inertia axis's baseline). V-02 adds the Section
column to the field inventory (making field placement derivable from the table without
reading section templates). V-03 adds per-section entry conditions (making the section
writing sequence structurally explicit with prerequisite field checks). The fourth addition
integrates V-02 and V-03: each per-section entry condition (V-03) cross-references the
inventory row (V-02) that registers the prerequisite fields rather than naming those fields
independently. S2's entry condition names the S1 row of the inventory as its authority for
which fields must be present before entry; S3's entry condition names the S2 row; S4's
entry condition names the S3 row. This creates a governance chain in which: (a) the
inventory registers fields WITH their sections (V-02); (b) each section's entry condition
names the inventory row for the prior section rather than independently listing the fields
(V-03 + integration); and (c) a maintainer adding a new field to an inventory row
automatically propagates to the entry condition that references that row without a separate
update. The reference hierarchy is complete: one inventory row → section template (for that
row's section) → the next section's entry condition (reference to that row as prerequisite).
Update the inventory row; the entry condition chain follows.

---

### PROMPT BODY -- V-05

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal -- it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes and Field Inventory**

This template was built from two named design axes. Every required labeled field belongs
to one axis and one section. The Structural Constraint column is the authoritative source
for consolidation rules; the Section column is the authoritative source for field
placement. Any consolidation violation and any misplaced field are auditable from this
table alone without reading section templates or checklists.

| Axis | Section | Required labeled fields | Structural constraint |
|------|---------|-------------------------|-----------------------|
| **Falsifiability axis** | S1 | `**Inertia verdict**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Falsifiability axis** | S2 | `**Pattern claim**:` · `**Disproof condition**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Falsifiability axis** | S3 | `**Verdict consequence**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Falsifiability axis** | S4 | `**Verdict**:` | Independent -- separately verifiable; no anti-consolidation constraint |
| **Inertia-framing axis** | S4 | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` | **Required separate in S4 (anti-consolidation -- C-29).** Do not merge into a single field (e.g., `**Position delta**:`). Constraint is auditable from this table alone. |

Any future extension must follow this sequence in order: (1) name the design axis;
(2) register every new field with its section AND structural constraint in the inventory
table -- **inventory is updated first and is the authoritative source for both placement
and constraints**; (3) add any required co-location directives to the relevant section
templates, cross-referencing the specific inventory entry (axis row, Section column, and
Structural Constraint column) rather than independently restating the constraint;
(4) update the entry condition of the section FOLLOWING the new field's section, adding
a cross-reference to the new inventory row as the authority for prerequisite fields;
(5) add one binary-verifiable presence-verification checklist item per new field,
designating the item as a reference to the inventory entry -- not an independent
constraint restatement.

---

### Checklist Design Invariant

**Rule**: No item tests content quality; each item locates a label string or reports
it missing. An item that requires editorial judgment to answer violates this invariant.

**Repair operation**: Rewrite any failing item as:
> "Does [Section name] include the label `**[field name]**:`?"
>
> Substitution: `[Section name]` → the section's heading text (e.g., "Signal Findings",
> "Recommendation"). `[field name]` → the field's label string from the inventory (e.g.,
> "Prior position", "Verdict"). Do not derive -- substitute directly from these two sources.

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

*(Items 1-4: section structure. Items 5-12: field presence, organized by axis and section
per the field inventory. The inventory is the authoritative constraint source. Items 10-12
are references to the inventory's Structural Constraint column, Inertia-framing axis row --
not independent restatements. Updating that inventory cell propagates to the Section 4
directive and to these items; the checklist is not separately authoritative for constraint
content.)*

---

**Layer 2 -- Section Templates**

---

**Section 1: Signal Findings**

**Entry condition**: Layer 1 checklist complete. All 12 items YES. Do not write any
finding until the checklist passes.

*Your stance: the investigator who curates for salience -- not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding move the decision away from the status quo (not building `{topic}`)?**
The status quo is the null outcome -- the case for not building. Name what specifically
shifts.

For each signal, write:

```
**[Signal name]** -- [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES -- this displaces the status quo: the case for not building
                         gets weaker /
                     NO -- this confirms the status quo holds: no reason to build
                         emerges /
                     PARTIAL -- [one clause naming what aspect of the status quo shifts]]
```

If `**Inertia verdict**:` is NO and the finding does not affect any other decision
dimension, omit the signal. Close this section with a one-line note stating how many
signals were excluded and the shared basis for exclusion.

Wrong operation: **Contents-report** -- transcribing what the signal said rather than
naming what it changes for the build decision. Detection: any entry missing
`**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

**Entry condition**: S1 complete -- all fields registered in the inventory's Falsifiability
axis, S1 row (`**Inertia verdict**:`) are written on every included finding. Do not begin
S2 until the S1 inventory row is satisfied. The pattern claim is built on inertia verdicts;
writing it before they are committed produces a claim without a grounded curation basis.

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

**Entry condition**: S2 complete -- all fields registered in the inventory's Falsifiability
axis, S2 row (`**Pattern claim**:` and `**Disproof condition**:`) are written and committed.
Do not begin S3 until the S2 inventory row is satisfied. Uncertainty is characterized
against the committed pattern claim and disproof condition; uncertainty written before
those fields are fixed cannot be anchored to them.

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

**Entry condition**: S3 complete -- all fields registered in the inventory's Falsifiability
axis, S3 row (`**Verdict consequence**:`) are written with at least one condition-consequence
pair. Do not begin S4 until the S3 inventory row is satisfied. The verdict is issued against
the uncertainty accounting; a verdict issued before `**Verdict consequence**:` is committed
has not been conditioned by the limits named in S3.

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Measure position against the prior. Defend the verdict against the
adjacent alternative. Name the first action. Do not assign the decision to the reader.

**Anti-consolidation directive (authoritative rule: field inventory above, Structural
Constraint column, Inertia-framing axis row -- that cell is the single point of update
for this constraint; this directive is a reference to it, not an independent restatement)**:
The three inertia fields below must appear as separate labeled entries. Do not consolidate
`**Prior position**:`, `**Baseline distance**:`, and `**Signals establish**:` into a
single field. Consolidation violates the constraint registered at that inventory cell and
fails C-29.

Required labeled fields:

```
**Prior position**: [What the team believed about {topic} before this investigation --
                    the status quo position the signals are measured against.]

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
