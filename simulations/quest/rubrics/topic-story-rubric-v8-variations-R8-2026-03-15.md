# R8 Variations — `topic-story` (v8 Rubric, 30 Criteria)

**Round**: 8
**Skill**: `topic-story`
**Base rubric**: `topic-story-rubric-v8-2026-03-14.md`
**New criteria this round**: C-28, C-29, C-30

---

## R7 State Summary

R7: All five variations scored 100.0. Every criterion C-01 through C-27 passed across
all variations. The three new R8 criteria were implicitly satisfied by R7's V-01
(checklist invariant stated in preamble, three separate inertia fields, recommendation
sentence form with `[**Disproof condition**]` cross-reference). R8 formalizes these
properties as distinct auditable criteria.

**R7 status of each new criterion (baseline for R8)**:
- C-28: V-01/V-02/V-03/V-04 pass (invariant present in preamble). V-05 passes.
- C-29: V-01/V-02/V-03/V-04 pass (three separate fields). V-05 FAILS (consolidated
  `**Position delta**:` — the one R7 variation that fails a new R8 criterion).
- C-30: All five pass (sentence form includes `[**Disproof condition**]` cross-reference).

**R8 compound design requirement**: Satisfy C-28, C-29, C-30 in forms that are
explicitly structural — not just satisfied incidentally:
- C-28: The checklist must carry a *named, stated* design invariant (not just satisfy it)
- C-29: Section 4 must have three *separate* labeled fields for the inertia measurement
  (`**Prior position**:`, `**Baseline distance**:`, `**Signals establish**:`) — never consolidated
- C-30: The recommendation sentence form must structurally cross-reference `**Disproof
  condition**:` from Section 2 by field name in a required template slot

**Variation axes explored**:
- Single-axis: Output format (C-28 invariant as named block with heading) — V-01
- Single-axis: Output format (C-30 via explicit `**Revision condition**:` artifact field) — V-02
- Single-axis: Phrasing register (lean imperative — C-28/C-29/C-30 extension of R7 V-03) — V-03
- Compound: Lifecycle emphasis + role sequence (baseline-first, dual C-30 cross-reference) — V-04
- Compound: Output format + inertia framing (field inventory with Structural Role column) — V-05

---

## V-01 — Single-Axis: C-28 Invariant as Named Design Rule Block

**Variation axis**: Output format (C-28 invariant presentation)
**Hypothesis**: Promoting the checklist invariant from a preamble sentence to a named,
set-apart rule block with its own heading makes C-28 an auditable artifact element —
any auditor can locate the invariant by scanning for the heading "Checklist Design
Invariant" without reading all preamble prose. The rule also names the repair operation
for violations ("must be rewritten as a structural presence check"), not just the pass
condition. The section architecture and all field assignments are unchanged from R7 V-01;
the only structural change is the invariant's presentation form.

---

### PROMPT BODY — V-01

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal — it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes**

This template was built from two named design axes. Every required labeled field belongs
to one axis. The Layer 1 checklist is produced by a single pass over the complete field
inventory — one binary-verifiable presence-verification item per required labeled field.

| Axis | Required labeled fields introduced |
|------|-------------------------------------|
| **Falsifiability axis** | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` |
| **Inertia-framing axis** | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` |

Any future extension must: (1) name the design axis, (2) register every new field in
the axis table, (3) add one binary-verifiable checklist item per new field before writing
any section that uses it.

---

**Checklist Design Invariant**

> **No item tests content quality; each item locates a label string or reports it
> missing.** Any checklist item that requires editorial judgment to answer violates
> this invariant and must be rewritten as a structural presence check before it is used.

Apply this invariant to every item below. Apply it when extending the checklist.

---

**Layer 1 — Pre-Artifact Checklist**

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

*(Items 1–4: section structure. Items 5–12: one item per required labeled field, derived
from the two-axis field inventory. Each item answered by locating the label string or
reporting it missing — consistent with the Checklist Design Invariant above.)*

---

**Layer 2 — Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience — not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding change whether to build `{topic}`?**

For each signal, write:

```
**[Signal name]** — [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES — this moves the prior position /
                     NO — this confirms the prior position /
                     PARTIAL — [one clause naming what specifically shifts]]
```

If `**Inertia verdict**:` is NO and the finding does not affect any other decision
dimension, omit the signal. Close this section with a one-line note stating how many
signals were excluded and the shared basis for exclusion.

Wrong operation: **Contents-report** — transcribing what the signal said rather than
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
this field — not in the prose above it.

Voice anchors: *What's striking is... / The convergence is not coincidental — it
reflects... / The evidence forces a conclusion I did not enter this investigation
expecting...*

Wrong operation: **Signal-list** — naming each signal's contribution without naming
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

**Anti-neutral directive — required for this section.** Locate any sentence that names
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

Wrong operation: **Verdict-consequence gap** — naming uncertainty without naming its
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
                        baseline — the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the delta
                        defensible — the compound inference.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] — specifically [action], because
[**Pattern claim**] forces this verdict rather than [adjacent alternative]. This call
stands unless [**Disproof condition**] is shown to hold."

*(The sentence form names `**Disproof condition**:` from Section 2 by field reference.
The recommendation is structurally conditioned by the falsifiability analysis: the
verdict is issued and its revision condition is named in the same required template slot.)*

**Anti-neutral directive — required for this section.** Scan every sentence for strings
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

Wrong operation: **Assigns-decision-to-reader** — presenting evidence without issuing
the call. Detection: `**Verdict**:` does not contain one of
{proceed / pause / pivot / abandon}.

---

**Layer 3 — Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Signal Findings | **Contents-report** — transcribing what the signal said rather than naming what it changes for the build decision | Any finding entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** — naming each signal's contribution without naming the cross-signal claim | The pattern cannot be stated in one sentence that mentions no individual signal by name |
| What Remains Uncertain | **Verdict-consequence gap** — naming uncertainty without naming its effect on the recommendation | Any uncertainty sentence without an "if...verdict changes to..." clause |
| Recommendation | **Assigns-decision-to-reader** — presenting evidence without issuing the call | `**Verdict**:` does not contain one of {proceed / pause / pivot / abandon} |

---

## V-02 — Single-Axis: C-30 via Explicit `**Revision condition**:` Artifact Field

**Variation axis**: Output format (C-30 structural cross-reference form)
**Hypothesis**: Expressing C-30's structural cross-reference through a required labeled
field `**Revision condition**:` in Section 4 — rather than through a template instruction
to use a field from another section — produces an output artifact where the disproof
cross-reference is verifiable without reading prose. The field definition requires the
author to copy `**Disproof condition**:` from Section 2 verbatim; the recommendation
sentence form then references the local `**Revision condition**:` field. The structural
closure is field-to-field, not sentence-to-section. A new axis ("Cross-reference axis")
registers the field at incorporation time. The three inertia fields remain separate (C-29
satisfied). The checklist grows to 13 items. The checklist invariant is stated in the
preamble (C-28 satisfied).

---

### PROMPT BODY — V-02

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal — it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes**

This template was built from three named design axes. Every required labeled field belongs
to one axis. The Layer 1 checklist is produced by a single pass over the complete field
inventory — one binary-verifiable presence-verification item per required labeled field.

| Axis | Required labeled fields introduced |
|------|-------------------------------------|
| **Falsifiability axis** | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` |
| **Inertia-framing axis** | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` |
| **Cross-reference axis** | `**Revision condition**:` |

The Cross-reference axis introduces one field that structurally closes the gap between
Section 2's falsifiability analysis and Section 4's recommendation: `**Revision
condition**:` is `**Disproof condition**:` from Section 2, copied into Section 4 as the
named condition under which the recommendation should be revised. This makes the disproof
cross-reference a required output field — verifiable without reading template instructions.

Any future extension must: (1) name the design axis, (2) register every new field in
the axis table, (3) add one binary-verifiable checklist item per new field before writing
any section that uses it.

No item tests content quality; each item locates a label string or reports it missing.

---

**Layer 1 — Pre-Artifact Checklist**

Run every item before writing any section. Answer YES by locating the named element.
Do not write until all items are YES.

**Section structure:**
1. [ ] Does this output include a labeled **Signal Findings** section?
2. [ ] Does this output include a labeled **What the Signals Say Together** section?
3. [ ] Does this output include a labeled **What Remains Uncertain** section?
4. [ ] Does this output include a labeled **Recommendation** section?

**Falsifiability-axis field registration:**
5. [ ] Does the Signal Findings section include `**Inertia verdict**:` on each finding entry?
6. [ ] Does the What the Signals Say Together section include `**Pattern claim**:`?
7. [ ] Does the What the Signals Say Together section include `**Disproof condition**:`?
8. [ ] Does the What Remains Uncertain section include `**Verdict consequence**:`?
9. [ ] Does the Recommendation section include `**Verdict**:`?

**Inertia-framing-axis field registration (registered at incorporation time):**
10. [ ] Does the Recommendation section include `**Prior position**:`?
11. [ ] Does the Recommendation section include `**Baseline distance**:`?
12. [ ] Does the Recommendation section include `**Signals establish**:`?

**Cross-reference-axis field registration (registered at incorporation time):**
13. [ ] Does the Recommendation section include `**Revision condition**:`?

*(Items 1–4: section structure. Items 5–13: one item per required labeled field from
the three-axis inventory. All items are locate-and-find operations. Item 13 covers the
Cross-reference axis's one field — the structural closure between Section 2 and Section 4.)*

---

**Layer 2 — Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience — not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding change whether to build `{topic}`?**

For each signal, write:

```
**[Signal name]** — [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES — this moves the prior position /
                     NO — this confirms the prior position /
                     PARTIAL — [one clause naming what specifically shifts]]
```

If `**Inertia verdict**:` is NO and the finding does not affect any other decision
dimension, omit the signal. Close this section with a one-line note on excluded signals
and the shared basis for exclusion.

Wrong operation: **Contents-report**. Detection: any entry missing `**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the shape the signals collectively form.*

Write the cross-signal claim: true of the signal set as a whole, not directly stated
in any single artifact, causal (names WHY signals converge, not THAT they do).

```
**Pattern claim**: [one sentence. Cross-signal. Causal: "signals converge because
                   [specific structural reason]", not "signals agree".]

**Disproof condition**: [The claim fails if: [specific observable condition that,
                        if shown to hold, invalidates the pattern.]]
```

Write `**Disproof condition**:` last. After committing to the pattern, ask what would
need to be shown false to disprove it. That answer goes in the field.

*(The content of `**Disproof condition**:` will be carried into Section 4 as
`**Revision condition**:` — the structural closure field.)*

Voice anchors: *What's striking is... / The convergence reflects a specific constraint,
not coincidence... / The evidence forces a conclusion I did not enter this investigation
expecting...*

Wrong operation: **Signal-list**. Detection: pattern cannot be stated in one sentence
that mentions no individual signal by name.

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without surrendering the verdict.*

Every named uncertainty must complete the verdict-consequence arc. Decision-neutral
uncertainties are omitted.

```
**Verdict consequence**: [If [condition A holds / is shown false], the verdict
                         changes from [current] to [alternative A].
                         If [condition B], the verdict changes to [alternative B].]
```

**Anti-neutral directive — required for this section.** Locate any sentence naming
uncertainty without naming a verdict consequence. Revise or remove it.

Strings to scan for and remove:
- "More research may be needed on X"
- "There is some uncertainty around X"
- "This area warrants further investigation"
- "It is unclear whether X"
- "Future work could explore X"

Required form: "We do not know [X]. If X is shown to be false, the verdict becomes
[Y]. Resolution method: [specific investigation]."

Wrong operation: **Verdict-consequence gap**. Detection: any uncertainty sentence
without an "if...verdict changes to..." clause.

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Defend against the adjacent alternative. Name the first action.
Do not assign the decision to the reader.

Required labeled fields:

```
**Prior position**: [What the team believed about {topic} before this investigation.]

**Baseline distance**: [How far the signals have moved the position from that
                        baseline — the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the delta
                        defensible — the compound inference.]

**Revision condition**: [Copy from Section 2 `**Disproof condition**:` — the specific
                         condition under which this recommendation should be revised.
                         Form: "This recommendation requires revision if [condition]
                         is shown to hold."]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] — specifically [action], because
[**Pattern claim**] forces this verdict rather than [adjacent alternative]. This call
stands unless [**Revision condition**] is shown to hold."

*(The sentence form references `**Revision condition**:` — a Section 4 field whose
value is the `**Disproof condition**:` from Section 2. The structural closure is
field-to-field: the recommendation sentence conditions itself on a local field whose
definition requires it to carry Section 2's falsifiability analysis forward.)*

**Anti-neutral directive — required for this section.** Scan every sentence for strings
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

Wrong operation: **Assigns-decision-to-reader**. Detection: `**Verdict**:` does not
contain one of {proceed / pause / pivot / abandon}.

---

**Layer 3 — Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Signal Findings | **Contents-report** | Any entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** | Pattern cannot be stated without naming individual signals |
| What Remains Uncertain | **Verdict-consequence gap** | Any uncertainty sentence without "if...verdict changes to..." |
| Recommendation | **Assigns-decision-to-reader** | `**Verdict**:` not one of {proceed / pause / pivot / abandon} |

---

## V-03 — Single-Axis: Lean Imperative (C-28/C-29/C-30 Extension)

**Variation axis**: Phrasing register
**Hypothesis**: Extending R7's V-03 lean register to cover C-28 (invariant stated in one
labeled line), C-29 (three fields stated tersely with explicit "separate, not consolidated"
instruction), and C-30 (sentence form compressed) — confirming that C-28/C-29/C-30 are
structurally orthogonal to register density, just as C-25/C-26/C-27 were in R7. If V-03
scores identically to V-01 on all structural criteria, the rubric confirms register is
orthogonal to the three new criteria.

---

### PROMPT BODY — V-03

Produce the `topic-story` artifact for `{topic}`. Synthesize signals into a decision
narrative. Not a summary — an editorial synthesis in your voice.

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

**Layer 1 — Pre-Artifact Checklist**

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

**Layer 2 — Section Templates**

---

**Section 1: Signal Findings**

Curate. Do not transcribe.

Per finding: apply the build-decision filter first. **Does this finding change whether
to build `{topic}`?**

Write:

```
**[Signal name]** — [one to three sentences. Key finding only.]
**Inertia verdict**: [YES / NO / PARTIAL — one clause naming what shifts]
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

Write `**Disproof condition**:` last. Ask: what would disprove this? Put that in the
field.

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

**Anti-neutral scan — required.** Locate sentences naming uncertainty without naming
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

Three inertia fields required — separate, not consolidated:

```
**Prior position**: [Team's position before this investigation.]
**Baseline distance**: [How far signals moved that position.]
**Signals establish**: [The inference that makes the movement defensible.]
**Verdict**: [proceed / pause / pivot / abandon]
```

Sentence: "I recommend [verdict] — specifically [action], because [**Pattern claim**]
forces this verdict rather than [adjacent alternative]. This call stands unless
[**Disproof condition**] is shown to hold."

**Anti-neutral scan — required.** Scan for reader-escape strings.

Strings to remove: "Based on the available evidence, it would be reasonable to..." /
"The team should consider..." / "It may be worth exploring..." / "Given the above, a
reasonable next step would be..." / "The evidence supports moving forward, though
caution is advised" / "A possible path forward is..." / "One option would be to..."

Wrong operation: Assigns-decision-to-reader. Detection: `**Verdict**:` not one of
{proceed / pause / pivot / abandon}.

---

**Layer 3 — Per-Section Failure Modes**

| Section | Wrong operation | Detection |
|---------|----------------|-----------|
| Signal Findings | Contents-report | Any entry missing `**Inertia verdict**:` |
| What Signals Say Together | Signal-list | Pattern cannot be stated without naming individual signals |
| What Remains Uncertain | Verdict-consequence gap | Any uncertainty sentence without "if...verdict changes to..." |
| Recommendation | Assigns-decision-to-reader | `**Verdict**:` not one of {proceed / pause / pivot / abandon} |

---

## V-04 — Compound: Baseline-First Architecture + C-30 Dual Cross-Reference Sentence Form

**Variation axes**: Lifecycle emphasis + role sequence
**Hypothesis**: The baseline-first architecture (Section 0: Baseline) establishes the
prior position before findings arrive, giving every subsequent section a measurement
anchor. C-30 is extended: the recommendation sentence form explicitly cross-references
*both* `**Prior position**:` (the inertia measurement anchor) and `**Disproof condition**:`
(the falsifiability closure): "I recommend [verdict] — specifically [action], because
[**Pattern claim**] establishes a [**Baseline distance**] from [**Prior position**],
forcing this verdict rather than [adjacent alternative]. This call stands unless
[**Disproof condition**] is shown to hold." This dual cross-reference is the strongest
possible Section 4 structural closure: the verdict inherits both measurement axes.

C-29 is satisfied with all three inertia fields present in Section 4 (`**Prior
position**:` appears in both Section 0 as the primary archivist statement and Section 4
as the inertia measurement reference — both are required labeled fields; C-29 fires on
Section 4's field presence, which is satisfied). C-28 invariant stated in the design axes
block.

---

### PROMPT BODY — V-04

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative measured from a named prior position. This is NOT
a summary of each signal — it is an editorial synthesis in your voice interpreting
what the signals say together.

---

**Template Design Axes**

| Axis | Required labeled fields introduced | Section |
|------|-------------------------------------|---------|
| **Falsifiability axis** | `**Inertia verdict**:` | Signal Findings |
| | `**Pattern claim**:` | What the Signals Say Together |
| | `**Disproof condition**:` | What the Signals Say Together |
| | `**Verdict consequence**:` | What Remains Uncertain |
| | `**Verdict**:` | Recommendation |
| **Inertia-framing axis** | `**Prior position**:` | Baseline *(Section 0)* and Recommendation |
| | `**Baseline distance**:` | Recommendation |
| | `**Signals establish**:` | Recommendation |

The Inertia-framing axis registers `**Prior position**:` in two sections: Section 0
(primary archivist statement) and Section 4 (inertia measurement reference). All fields
are registered at incorporation time.

No item tests content quality; each item locates a label string or reports it missing.

---

**Layer 1 — Pre-Artifact Checklist**

One binary-verifiable item per required labeled field plus section-structure items.
All items are locate-and-find operations. Answer YES by locating the named element.
Do not begin writing until all items are YES.

**Section structure:**
1. [ ] Does this output include a labeled **Baseline** section?
2. [ ] Does this output include a labeled **Signal Findings** section?
3. [ ] Does this output include a labeled **What the Signals Say Together** section?
4. [ ] Does this output include a labeled **What Remains Uncertain** section?
5. [ ] Does this output include a labeled **Recommendation** section?

**Field coverage (Falsifiability axis):**
6. [ ] Does the Signal Findings section include `**Inertia verdict**:` on each finding entry?
7. [ ] Does the What the Signals Say Together section include `**Pattern claim**:`?
8. [ ] Does the What the Signals Say Together section include `**Disproof condition**:`?
9. [ ] Does the What Remains Uncertain section include `**Verdict consequence**:`?
10. [ ] Does the Recommendation section include `**Verdict**:`?

**Field coverage (Inertia-framing axis — registered at incorporation time):**
11. [ ] Does the Baseline section include `**Prior position**:`?
12. [ ] Does the Recommendation section include `**Prior position**:`?
13. [ ] Does the Recommendation section include `**Baseline distance**:`?
14. [ ] Does the Recommendation section include `**Signals establish**:`?

*(Items 11 and 12 both verify `**Prior position**:` in different sections. Both are
locate-and-find operations consistent with the checklist invariant. Items 12–14 together
confirm C-29: all three inertia measurement fields present separately in Section 4.)*

---

**Layer 2 — Section Templates**

---

**Section 0: Baseline**

*Your stance: the archivist who names where the team stood before the signals arrived.*

Name the prior position first. Every subsequent section measures against this baseline.

```
**Prior position**: [What the team believed about {topic} before this investigation
                    began — the specific hypothesis, assumption, or working position
                    in place when signal-gathering started.]
```

This section has one job: name the baseline. Do not report findings here. Do not issue
the verdict here. The document's meaning is the distance between what is written in
this field and what the signals establish.

Wrong operation: **Baseline-omission** — writing context ("we had some assumptions about
X") rather than a named position. Detection: can you complete "the prior position was
[specific claim]"? If not, you have context, not a baseline.

---

**Section 1: Signal Findings**

*Your stance: the investigator who measures each finding against the named baseline.*

Every finding is evaluated against `**Prior position**:` from Section 0.
The build-decision filter: **Does this finding move the team's position on `{topic}`
relative to that baseline?**

For each signal:

```
**[Signal name]** — [one to three sentences. Key finding only.]
**Inertia verdict**: [YES — moves position from baseline /
                     NO — confirms baseline /
                     PARTIAL — [one clause naming the specific dimension that shifts]]
```

Signals where `**Inertia verdict**:` is NO and nothing else changes are omitted.
Close this section with a one-line note on excluded signals and shared exclusion basis.

Wrong operation: **Contents-report** — transcribing without measuring against the
baseline. Detection: any entry missing `**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the emergent claim the signal set produces.*

Write the cross-signal claim: true of the signal set as a whole, not stated in any
single artifact, causal (names WHY signals converge, not THAT they do).

```
**Pattern claim**: [One sentence. Cross-signal. Causal account required.]

**Disproof condition**: [The claim fails if: [specific observable condition that
                        would invalidate the pattern.]]
```

Write `**Disproof condition**:` after committing to the pattern. Ask: what would need
to be demonstrated as false to disprove this? That answer goes in the field.

*(The `**Disproof condition**:` established here is cross-referenced in Section 4's
recommendation sentence form — both measurement axes close in Section 4.)*

Voice anchors: *What's striking is... / The signals collectively establish... / The
distance from the prior position is not incremental — it reflects a structural shift...*

Wrong operation: **Signal-list**. Detection: pattern cannot be stated in one sentence
that mentions no individual signal by name.

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without collapsing the verdict.*

Every named uncertainty must complete the verdict-consequence arc. Uncertainties that
do not change the recommendation are omitted.

```
**Verdict consequence**: [If [condition A holds / is shown false], the verdict
                         changes from [current] to [alternative A].
                         If [condition B], the verdict changes to [alternative B].]
```

**Anti-neutral directive — required for this section.** Locate any sentence that names
an uncertainty without naming its consequence for the verdict. Revise or remove it.

Strings to scan for and remove:
- "More research may be needed on X"
- "There is some uncertainty around X"
- "This area warrants further investigation"
- "It is unclear whether X"
- "Future work could explore X"

Required form: "We do not know [X]. If X is shown to be false, the verdict becomes [Y].
Resolution method: [specific investigation]."

Wrong operation: **Verdict-consequence gap**. Detection: any uncertainty sentence
lacking an "if...verdict changes to..." clause.

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call — who can name exactly how
far the signals have moved the position from the named baseline.*

Issue one verdict. Name the distance traveled. Defend against the adjacent alternative.
Name the first action.

Required labeled fields:

```
**Prior position**: [Brief restatement from Section 0 — one phrase naming the baseline.]

**Baseline distance**: [How far the signals have moved the team's position from the
                        prior position — the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the delta
                        defensible — the compound inference.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] — specifically [action], because
[**Pattern claim**] establishes a [**Baseline distance**] from [**Prior position**],
forcing this verdict rather than [adjacent alternative]. This call stands unless
[**Disproof condition**] is shown to hold."

*(This sentence form carries two structural cross-references: (1) `**Prior position**:`
and `**Baseline distance**:` from the Inertia-framing axis; (2) `**Disproof condition**:`
from Section 2's Falsifiability axis. Both cross-references are structural: they name
required labeled fields in this template.)*

**Anti-neutral directive — required for this section.** Scan every sentence for strings
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

Wrong operation: **Assigns-decision-to-reader**. Detection: `**Verdict**:` does not
contain one of {proceed / pause / pivot / abandon}.

---

**Layer 3 — Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Baseline | **Baseline-omission** — context rather than a named position | `**Prior position**:` cannot be completed as "the prior position was [specific claim]" |
| Signal Findings | **Contents-report** | Any entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** | Pattern cannot be stated without naming individual signals |
| What Remains Uncertain | **Verdict-consequence gap** | Any uncertainty sentence without "if...verdict changes to..." |
| Recommendation | **Assigns-decision-to-reader** | `**Verdict**:` not one of {proceed / pause / pivot / abandon} |

---

## V-05 — Compound: Field-ID Inventory + Structural Role Column

**Variation axes**: Output format + inertia framing
**Hypothesis**: Extending V-02 from R7's Required Labeled Fields Inventory with a
"Structural role" column that annotates each field's participation in C-29
(inertia measurement — required separate) and C-30 (cross-referenced in Section 4
sentence form) makes the inventory a complete structural specification for all three new
criteria. An auditor can verify C-28 (invariant in inventory preamble), C-29 (three
fields annotated "Inertia measurement — required separate"), and C-30 (disproof field
annotated "Cross-referenced in S4 sentence form") by reading the inventory alone —
without reading section templates. The three inertia fields remain separate and are
explicitly annotated as such, blocking the R7 V-05 consolidation failure.

---

### PROMPT BODY — V-05

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal — it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Required Labeled Fields Inventory**

This inventory lists every labeled field this template requires and its structural role.
The pre-artifact checklist is derived from this inventory: exactly one binary-verifiable
presence-verification item per row.

**Governing checklist invariant: no item tests content quality; each item locates a
label string or reports it missing.** Adding a field without adding it to this inventory
first violates the design discipline. Adding a checklist item for a field not in this
inventory also violates it.

| ID | Field label | Section | Design axis | Structural role |
|----|-------------|---------|-------------|-----------------|
| F-01 | `**Inertia verdict**:` | Signal Findings (per-entry) | Falsifiability | Per-finding decision gate |
| F-02 | `**Pattern claim**:` | What Signals Say Together | Falsifiability | Cross-referenced in S4 sentence form (C-30) |
| F-03 | `**Disproof condition**:` | What Signals Say Together | Falsifiability | Cross-referenced in S4 sentence form (C-30) |
| F-04 | `**Verdict consequence**:` | What Remains Uncertain | Falsifiability | Verdict-consequence arc |
| F-05 | `**Verdict**:` | Recommendation | Falsifiability | Output verdict — constrained to {proceed / pause / pivot / abandon} |
| F-06 | `**Prior position**:` | Recommendation | Inertia-framing | Inertia measurement — required separate in S4 (C-29) |
| F-07 | `**Baseline distance**:` | Recommendation | Inertia-framing | Inertia measurement — required separate in S4 (C-29) |
| F-08 | `**Signals establish**:` | Recommendation | Inertia-framing | Inertia measurement — required separate in S4 (C-29) |

*(F-02 and F-03 are cross-referenced by field name in the Section 4 recommendation
sentence form — C-30 fires on whether the sentence form includes this structural
cross-reference. F-06, F-07, F-08 are required as three separate labeled fields in
Section 4 — C-29 fires on whether all three appear separately. The "required separate"
annotation in this inventory makes the C-29 prohibition on consolidation auditable
without reading the section template.)*

---

**Layer 1 — Pre-Artifact Checklist**

Items derived from the Required Labeled Fields Inventory above. One item per inventory
row plus four section-structure items. All items are locate-and-find operations
consistent with the governing checklist invariant. Do not begin writing until all
items are YES.

**Section structure:**
1. [ ] Does this output include a labeled **Signal Findings** section?
2. [ ] Does this output include a labeled **What the Signals Say Together** section?
3. [ ] Does this output include a labeled **What Remains Uncertain** section?
4. [ ] Does this output include a labeled **Recommendation** section?

**Field coverage (one item per inventory row F-01 through F-08):**
5. [ ] *(F-01)* Does the Signal Findings section include `**Inertia verdict**:` on each finding entry?
6. [ ] *(F-02)* Does the What the Signals Say Together section include `**Pattern claim**:`?
7. [ ] *(F-03)* Does the What the Signals Say Together section include `**Disproof condition**:`?
8. [ ] *(F-04)* Does the What Remains Uncertain section include `**Verdict consequence**:`?
9. [ ] *(F-05)* Does the Recommendation section include `**Verdict**:`?
10. [ ] *(F-06)* Does the Recommendation section include `**Prior position**:`?
11. [ ] *(F-07)* Does the Recommendation section include `**Baseline distance**:`?
12. [ ] *(F-08)* Does the Recommendation section include `**Signals establish**:`?

*(Items 10–12 verify F-06, F-07, F-08 — the three separate inertia measurement fields
required in Section 4. Each must be present as its own labeled field. The inventory's
"required separate" annotation makes the design constraint auditable from the inventory
alone, without reading Section 4's template.)*

---

**Layer 2 — Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience — not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding change whether to build `{topic}`?**

For each signal, write:

```
**[Signal name]** — [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES — this moves the prior position /
                     NO — this confirms the prior position /
                     PARTIAL — [one clause naming what specifically shifts]]
```

If `**Inertia verdict**:` is NO and the finding does not affect any other decision
dimension, omit the signal. Close this section with a one-line note on excluded signals
and shared basis for exclusion.

Wrong operation: **Contents-report**. Detection: any entry missing `**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the shape the signals collectively form.*

Write the cross-signal claim: true of the set as a whole, not stated in any single
artifact, causal (names WHY signals converge, not THAT they do).

```
**Pattern claim**: [one sentence. Cross-signal. Causal: "signals converge because
                   [specific structural reason]", not "signals agree".]

**Disproof condition**: [The claim fails if: [specific observable condition.]]
```

Write `**Disproof condition**:` last. Ask: what would need to be shown false to
disprove the pattern? That answer goes in the field.

*(F-02 `**Pattern claim**:` and F-03 `**Disproof condition**:` are cross-referenced
by field name in Section 4's recommendation sentence form — see inventory Structural
Role column.)*

Voice anchors: *What's striking is... / The convergence reflects a specific constraint,
not coincidence... / The evidence forces a conclusion I did not enter this investigation
expecting...*

Wrong operation: **Signal-list**. Detection: pattern cannot be stated in one sentence
that mentions no individual signal by name.

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without surrendering the verdict.*

Every named uncertainty must complete the verdict-consequence arc. Decision-neutral
uncertainties are omitted.

```
**Verdict consequence**: [If [condition A holds / is shown false], the verdict
                         changes from [current] to [alternative A].
                         If [condition B], the verdict changes to [alternative B].]
```

**Anti-neutral directive — required for this section.** Locate any sentence naming
uncertainty without naming a verdict consequence. Revise or remove it.

Strings to scan for and remove:
- "More research may be needed on X"
- "There is some uncertainty around X"
- "This area warrants further investigation"
- "It is unclear whether X"
- "Future work could explore X"

Required form: "We do not know [X]. If X is shown to be false, the verdict becomes [Y].
Resolution method: [specific investigation]."

Wrong operation: **Verdict-consequence gap**. Detection: any uncertainty sentence
without an "if...verdict changes to..." clause.

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Defend against the adjacent alternative. Name the first action.
Do not assign the decision to the reader.

Required labeled fields (F-06, F-07, F-08 required separately — do not consolidate):

```
**Prior position**: [What the team believed about {topic} before this investigation.]

**Baseline distance**: [How far the signals have moved the position from that
                        baseline — the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the delta
                        defensible — the compound inference.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] — specifically [action], because
[**Pattern claim**] forces this verdict rather than [adjacent alternative]. This call
stands unless [**Disproof condition**] is shown to hold."

*(F-02 `**Pattern claim**:` and F-03 `**Disproof condition**:` appear in this sentence
form by field reference — as documented in the inventory Structural Role column. The
cross-reference is structural: the sentence form names fields from Section 2, making
Section 4's recommendation structurally conditioned by Section 2's falsifiability
analysis.)*

**Anti-neutral directive — required for this section.** Scan every sentence for strings
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

Wrong operation: **Assigns-decision-to-reader**. Detection: `**Verdict**:` does not
contain one of {proceed / pause / pivot / abandon}.

---

**Layer 3 — Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Signal Findings | **Contents-report** | Any entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** | Pattern cannot be stated without naming individual signals |
| What Remains Uncertain | **Verdict-consequence gap** | Any uncertainty sentence without "if...verdict changes to..." |
| Recommendation | **Assigns-decision-to-reader** | `**Verdict**:` not one of {proceed / pause / pivot / abandon} |

---

## Predicted Scoring

| C | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS* | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |
| C-24 | PASS | PASS | PASS | PASS | PASS |
| C-25 | PASS | PASS | PASS | PASS | PASS |
| C-26 | PASS | PASS | PASS | PASS | PASS |
| C-27 | PASS | PASS | PASS | PASS | PASS |
| C-28 | PASS | PASS | PASS | PASS | PASS |
| C-29 | PASS | PASS† | PASS | PASS‡ | PASS |
| C-30 | PASS | PASS§ | PASS | PASS | PASS |

**Notes:**
- `*` V-04 has five sections; C-01 fires on omission, not addition. PASS expected (precedent from R7).
- `†` V-02 C-29: three inertia fields present separately in Section 4. The additional `**Revision
  condition**:` field does not displace them. PASS.
- `‡` V-04 C-29: `**Prior position**:` appears in Section 4 as a brief restatement (items 12–14
  together verify all three fields in Section 4). PASS.
- `§` V-02 C-30: The sentence form references `**Revision condition**:` rather than
  `**Disproof condition**:` directly. The field definition makes `**Revision condition**:`
  the disproof condition by derivation. C-30 fires on structural cross-reference to the disproof
  condition — a derived field whose definition is the disproof condition satisfies this if the
  derivation is documented. PASS predicted; scorecards should verify.

**Key tests R8 scorecards should resolve:**
1. Whether C-28 fires differently on V-01's named block vs. V-02/V-03/V-04/V-05's inline
   statement — does the heading change the score, or is the stated invariant sufficient in any form?
2. Whether V-02's `**Revision condition**:` (a derived copy of `**Disproof condition**:`)
   satisfies C-30's "structural cross-reference to the disproof condition" — field-to-field
   derivation vs. direct field-name reference in the sentence form.
3. Whether V-04's five-section structure and dual C-30 sentence form (cross-referencing both
   `**Prior position**:` and `**Disproof condition**:`) constitutes a stronger C-30 demonstration
   than V-01's standard form.
4. Whether lean register (V-03) is structurally neutral to C-28/C-29/C-30 as it was to
   C-25/C-26/C-27 in R7.
