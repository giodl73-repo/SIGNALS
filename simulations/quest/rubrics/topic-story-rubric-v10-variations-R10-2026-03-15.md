# R10 Variations -- `topic-story` (v10 Rubric, 36 Criteria)

**Round**: 10
**Skill**: `topic-story`
**Base rubric**: `topic-story-rubric-v10-2026-03-14.md`
**New criteria this round**: C-34, C-35, C-36

---

## R9 State Summary

R9: All five variations scored 100.0 on C-01 through C-33 under the v9 rubric. The three
new v10 criteria were partially implicit in R9 forms:

- **C-34**: R9 V-01, V-04, V-05 had `### Checklist Design Invariant` heading blocks with
  `**Repair operation**:` and the parameterized formula `"Does [Section name] include the
  label \`**[field name]**:\`?"`. V-02 expressed the invariant in bold+blockquote form with
  no repair formula (C-34 fails). V-03 had a one-line invariant with no repair formula
  (C-34 fails). The formula in V-01/V-04/V-05 is a quotable template but its substitution
  variables (`[Section name]`, `[field name]`) are unnamed -- the author must infer what
  to substitute from context.
- **C-35**: R9 V-05 Section 4 had "Anti-consolidation directive (see inventory Structural
  Constraint column for the authoritative rule)" -- a named column reference forming a
  reference chain. V-01, V-04 had co-located directives without inventory cross-references
  (C-35 fails). V-02 had the inventory referenced in the "Required labeled fields" label
  line but no co-located directive block (C-32 partial, C-35 fails). V-03 had a co-located
  directive with no inventory reference (C-35 fails).
- **C-36**: R9 V-05 footer: "Structural constraints for items 10-12 are registered in the
  inventory table's Structural Constraint column -- the anti-consolidation rule is auditable
  from the inventory without re-reading this checklist." This implies inventory authority
  without asserting it. No variation used explicit "The inventory is the authoritative
  constraint source" or "items 10-12 are references, not independent restatements" language.

**R9 baseline (per new criterion, per R9 variation)**:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-34 (repair formula is instantiable -- parameterized template) | PASSES | FAILS | FAILS | PASSES | PASSES |
| C-35 (section directive forms reference chain to inventory) | FAILS | FAILS | FAILS | FAILS | PASSES |
| C-36 (checklist explicit authority + reference designation) | FAILS | FAILS | FAILS | FAILS | PARTIAL |

**R9 baseline under v10**: V-05 → 100.0 (per rubric scoring note).

**R10 compound design requirement**: V-05 satisfied C-34 and C-35 explicitly; C-36 was
satisfied by implication. R10 variations push three structural properties beyond V-05:

- **C-34 upgrade**: The repair formula names its substitution variables explicitly.
  `[Section name]` and `[field name]` are named as "section heading text" and "field label
  string from inventory" respectively -- making instantiation prescribed, not derived.
- **C-35 upgrade**: The section directive names the exact cell location in the inventory
  (column AND row), not just the column. An auditor directed to "Structural Constraint
  column, Inertia-framing axis row" reaches a single cell, not a column requiring row scan.
- **C-36 upgrade**: The checklist footer explicitly states "The inventory is the
  authoritative constraint source. Items 10-12 are references to the inventory's Structural
  Constraint column, not independent restatements." The reference-vs-restatement distinction
  is asserted, not implied.

**Variation axes explored**:
- Single-axis: Output format (repair formula substitution variable labels) -- V-01
- Single-axis: Output format (section directive exact row+column navigation) -- V-02
- Single-axis: Phrasing register (checklist footer explicit authority + reference designation, lean) -- V-03
- Compound: Output format + lifecycle emphasis (V-01 repair labels + V-02 exact navigation) -- V-04
- Compound: Output format + phrasing register + lifecycle emphasis (V-01 + V-02 + V-03 + extension protocol update sequence) -- V-05

---

## V-01 -- Single-Axis: Repair Formula Substitution Variable Labels

**Variation axis**: Output format (repair formula instantiation)
**Hypothesis**: The repair formula `"Does [Section name] include the label
\`**[field name]**:\`?"` is a parameterized template, but its substitution variables
`[Section name]` and `[field name]` are unnamed. An author applying this formula must
infer that `[Section name]` takes the section's heading text and `[field name]` takes
the field's label string from the inventory. Naming the variables explicitly -- "`[Section
name]` → the section's heading text; `[field name]` → the field's label string from the
inventory" -- prescribes instantiation: no derivation required. C-34 fires on whether
a quotable repair formula is present; a v11 criterion may fire on whether the substitution
variables are explicitly labeled, converting the template from parameterized-implicit to
parameterized-prescribed. C-35 and C-36 are unchanged from R9 V-05 (single-axis isolation).

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

Any future extension must: (1) name the design axis, (2) register every new field with
its structural constraint in the axis table, (3) add one binary-verifiable checklist item
per new field before writing any section that uses it.

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

---

## V-02 -- Single-Axis: Section Directive Names Exact Inventory Row and Column

**Variation axis**: Output format (section directive table navigation granularity)
**Hypothesis**: V-05's directive "see inventory Structural Constraint column for the
authoritative rule" names the column but not the row. An author following this reference
must scan all rows to find the inertia-framing constraint entry. Naming the exact cell --
"Structural Constraint column, Inertia-framing axis row" -- makes the reference scan-free:
the author is directed to a single cell without row scanning. C-35 fires on whether
the directive forms a reference chain anchored at the inventory; a v11 criterion may fire
on whether the reference is navigable at cell granularity rather than column granularity.
C-34 (repair formula unchanged from R9 V-05) and C-36 (footer unchanged) are deliberately
absent -- single-axis isolation confirmed.

---

### PROMPT BODY -- V-02

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

**Anti-consolidation directive (authoritative rule: field inventory above, Structural
Constraint column, Inertia-framing axis row -- that cell is the single point of update
for this constraint; this directive is a reference to it)**: The three inertia fields
below must appear as separate labeled entries. Do not consolidate `**Prior position**:`,
`**Baseline distance**:`, and `**Signals establish**:` into a single field. Consolidation
violates the constraint registered at that inventory cell and fails C-29.

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

## V-03 -- Single-Axis: Checklist Footer Explicit Authority and Reference Designation (Lean Register)

**Variation axis**: Phrasing register (lean) + checklist footer authority designation
**Hypothesis**: V-05's checklist footer says the anti-consolidation rule is "auditable from
the inventory without re-reading this checklist" -- this implies inventory authority without
asserting it. It does not say items 10-12 are references rather than independent restatements.
Explicitly stating "The inventory is the authoritative constraint source. Items 10-12 are
references to the inventory's Structural Constraint column, not independent restatements --
updating the inventory propagates to these items; the checklist is not separately authoritative
for constraint content" converts the implicit authority claim into an explicit authority
designation with a named propagation rule. Register is lean throughout -- confirming authority
designation is orthogonal to register, consistent with the R9 register-orthogonality finding.
C-34 (repair formula) and C-35 (section directive) are unchanged from R9 V-05.

---

### PROMPT BODY -- V-03

Produce the `topic-story` artifact for `{topic}`. Synthesize signals into a decision
narrative. Not a summary -- an editorial synthesis in your voice.

---

**Design Axes and Field Inventory**

Two axes. Structural Constraint column is authoritative for consolidation rules -- auditable
from this table alone without reading section templates or checklists.

| Axis | Required labeled fields | Structural constraint |
|------|-------------------------|-----------------------|
| **Falsifiability** | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` | Independent -- no anti-consolidation constraint |
| **Inertia-framing** | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` | **Required separate in S4 (anti-consolidation -- C-29).** Do not merge (e.g., `**Position delta**:`). Constraint auditable from this table alone. |

Extension: (1) name the axis; (2) register every new field with its structural constraint;
(3) one binary-verifiable checklist item per new field before writing any section using it.

---

### Checklist Design Invariant

**Rule**: No item tests content quality; each item locates a label string or reports it missing.

**Repair operation**: Rewrite any failing item as:
> "Does [Section name] include the label `**[field name]**:`?"

Apply to every item. Apply when extending the checklist.

---

**Layer 1 -- Pre-Artifact Checklist**

Locate each element or stop. All YES before writing.

**Section structure:**
1. [ ] **Signal Findings** section labeled?
2. [ ] **What the Signals Say Together** section labeled?
3. [ ] **What Remains Uncertain** section labeled?
4. [ ] **Recommendation** section labeled?

**Falsifiability-axis fields:**
5. [ ] `**Inertia verdict**:` on each finding entry in Signal Findings?
6. [ ] `**Pattern claim**:` in What the Signals Say Together?
7. [ ] `**Disproof condition**:` in What the Signals Say Together?
8. [ ] `**Verdict consequence**:` in What Remains Uncertain?
9. [ ] `**Verdict**:` in Recommendation?

**Inertia-framing-axis fields:**
10. [ ] `**Prior position**:` in Recommendation?
11. [ ] `**Baseline distance**:` in Recommendation?
12. [ ] `**Signals establish**:` in Recommendation?

*(Items 1-4: section structure. Items 5-12: field presence. The inventory is the
authoritative constraint source. Items 10-12 are references to the inventory's
Structural Constraint column, not independent restatements -- updating the inventory
propagates to these items; the checklist is not separately authoritative for
constraint content.)*

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

Cross-signal claim must be: true of the set as a whole, absent from any individual
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

**Anti-consolidation directive (see inventory Structural Constraint column for the
authoritative rule)**: The three inertia fields below must appear as separate labeled
entries. Do not consolidate `**Prior position**:`, `**Baseline distance**:`, and
`**Signals establish**:` into a single field. Consolidation violates the constraint
registered in the field inventory and fails C-29.

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

## V-04 -- Compound: V-01 Repair Labels + V-02 Exact Cell Navigation

**Variation axes**: Output format + lifecycle emphasis
**Hypothesis**: Combining repair formula substitution variable labels (V-01) with exact
inventory cell navigation in the section directive (V-02) tests whether the two changes
reinforce each other without architectural conflict. V-01 targets the pre-section invariant
block (making the repair formula prescriptively instantiable). V-02 targets Section 4 (making
the constraint reference navigable at cell granularity). The two locations are structurally
distinct and the changes do not interact -- both can fire in the same variation without
conflict. Together they advance two separate reference-chain properties: the invariant's repair
formula is prescriptively instantiable; the section directive is cell-navigable. C-36 (footer
unchanged from R9 V-05) is deliberately absent -- compound of V-01 + V-02 only.

---

### PROMPT BODY -- V-04

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

**Anti-consolidation directive (authoritative rule: field inventory above, Structural
Constraint column, Inertia-framing axis row -- that cell is the single point of update
for this constraint; this directive is a reference to it)**: The three inertia fields
below must appear as separate labeled entries. Do not consolidate `**Prior position**:`,
`**Baseline distance**:`, and `**Signals establish**:` into a single field. Consolidation
violates the constraint registered at that inventory cell and fails C-29.

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

## V-05 -- Compound: V-01 + V-02 + V-03 + Extension Protocol Update Sequence

**Variation axes**: Output format + phrasing register + lifecycle emphasis
**Hypothesis**: Full structural saturation for R10. V-01 makes the repair formula
prescriptively instantiable (substitution variable labels). V-02 makes the section
directive cell-navigable (exact row+column in inventory). V-03 makes the checklist footer
explicitly designate inventory authority and items 10-12 as references (not independent
restatements). The fourth addition targets the extension protocol: the current sequence
"(1) name the axis, (2) register field with constraint, (3) add checklist item" is unordered
and does not name which surface is updated first. Specifying the canonical update sequence
-- inventory first, then section template cross-referencing the inventory entry, then checklist
designating its items as references to that entry -- converts the extension protocol from a
parallel 3-step update into a constraint-propagation sequence with a single authoritative
origin. When all four properties are present, the template's constraint governance forms a
complete reference hierarchy: one inventory cell → section directive (reference to cell) →
checklist footer (declares items as references to cell). Update the inventory cell; the
reference chain is what auditors follow; the hierarchy has no divergence points.

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
