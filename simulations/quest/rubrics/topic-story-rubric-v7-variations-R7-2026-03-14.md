# R7 Variations — `topic-story` (v7 Rubric, 27 Criteria)

**Round**: 7
**Skill**: `topic-story`
**Base rubric**: `topic-story-rubric-v7-2026-03-14.md`
**New criteria this round**: C-25, C-26, C-27 (checklist-under-composition discipline)

---

## R6 State Summary

R6 top scorer: V-05 (99.4). Failed C-24 only: `**Baseline distance**:`,
`**Prior position**:`, `**Signals establish**:` are required labeled fields in Layer 2
with no corresponding Layer 1 checklist items. The fix is mechanical — add 3 items —
but those items must be binary-verifiable (C-22), introduced via axis-registration
(C-26), and the combined checklist must satisfy both C-22 and C-24 through a single
design procedure (C-27). No variation in R6 demonstrated this compound property.

**R7 compound design requirement**: a checklist that simultaneously satisfies:
- C-22: every item is a locate-and-find operation
- C-24: every labeled field has a checklist item, every checklist item maps to a labeled field
- C-25: each new item independently audited for binary-verifiability at addition time
- C-26: each design axis registers its labeled fields in the checklist at incorporation time
- C-27: both C-22 and C-24 achieved through the same design procedure (one presence-verification item per required labeled field, derived from a single pass over the complete field inventory)

**Variation axes explored**:
- Single-axis: Inertia framing (axis registration visible in preamble) — V-01
- Single-axis: Checklist architecture (field-inventory-first derivation) — V-02
- Single-axis: Phrasing register (lean imperative) — V-03
- Compound: Lifecycle emphasis + role sequence (baseline-first section order) — V-04
- Compound: Output format + inertia framing (consolidated position-delta field) — V-05

---

## V-01 — Single-Axis: Explicit Design-Axis Registration

**Variation axis**: Inertia framing
**Hypothesis**: Naming both design axes in a template preamble and showing each axis's
registered fields produces a visible C-26 audit trail. The checklist is then built by
a single pass over the complete field inventory (one binary-verifiable presence item
per required labeled field), satisfying C-27. The section architecture is unchanged
from R6 V-05; only the preamble and checklist item count change (9 → 12).

---

### PROMPT BODY — V-01

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal — it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes**

This template was built from two named design axes. Every required labeled field belongs
to one axis. The Layer 1 checklist below was produced by a single pass over the complete
field inventory — one binary-verifiable presence-verification item per required labeled
field. No item tests content quality; each item locates a label string or reports it
missing.

| Axis | Required labeled fields introduced |
|------|-------------------------------------|
| **Falsifiability axis** | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` |
| **Inertia-framing axis** | `**Prior position**:` · `**Baseline distance**:` · `**Signals establish**:` |

Any future extension to this template must: (1) name the design axis being incorporated,
(2) list every labeled field that axis introduces in the axis table, and (3) add one
binary-verifiable checklist item per new field before writing any section that uses it.

---

**Layer 1 — Pre-Artifact Checklist**

Run every item before writing any section. Answer YES by locating the named element
in the template. Do not write until all items are YES.

**Section structure (C-01):**
1. [ ] Does this output include a labeled **Signal Findings** section?
2. [ ] Does this output include a labeled **What the Signals Say Together** section?
3. [ ] Does this output include a labeled **What Remains Uncertain** section?
4. [ ] Does this output include a labeled **Recommendation** section?

**Falsifiability-axis field registration:**
5. [ ] Does the Signal Findings section template include the `**Inertia verdict**:` field on each finding entry?
6. [ ] Does the What the Signals Say Together section include the `**Pattern claim**:` field?
7. [ ] Does the What the Signals Say Together section include the `**Disproof condition**:` field?
8. [ ] Does the What Remains Uncertain section include the `**Verdict consequence**:` field?
9. [ ] Does the Recommendation section include the `**Verdict**:` field?

**Inertia-framing-axis field registration (registered at incorporation time):**
10. [ ] Does the Recommendation section include the `**Prior position**:` field?
11. [ ] Does the Recommendation section include the `**Baseline distance**:` field?
12. [ ] Does the Recommendation section include the `**Signals establish**:` field?

*(All items are locate-and-find operations: locate the label string or report it missing.
Items 5–9 cover the Falsifiability axis. Items 10–12 cover the Inertia-framing axis.
No item requires quality assessment.)*

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
dimension, omit the signal. Signal omission is explicit: close this section with a
one-line note stating how many signals were excluded and the shared basis for exclusion.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the shape the signals collectively form.*

Write the cross-signal claim. It must be true of the signal set as a whole, not
directly stated in any single signal artifact, and causal: it names WHY the signals
converge, not THAT they converge.

Required labeled fields:

```
**Pattern claim**: [one sentence. Cross-signal. Causal account required —
                   not "signals agree" but "signals agree because [structural reason]."]

**Disproof condition**: [The claim fails if: [specific observable condition that, if
                        shown to hold, invalidates the pattern.]]
```

The causal account in `**Pattern claim**:` must name the mechanism. "Conditions are
favorable" is a conclusion. "Conditions are favorable because [specific constraint that,
if different, would change all three signals]" is a mechanism.

Write `**Disproof condition**:` last: after committing to the pattern claim, ask what
would someone need to show is false in order to disprove it. That answer goes in the
field — not in the prose above it.

Voice anchors: *What's striking is... / The convergence is not coincidental — it
reflects... / The evidence forces a conclusion I did not enter this investigation
expecting...*

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without surrendering the verdict.*

Every named uncertainty must complete the verdict-consequence arc. An uncertainty that
does not change the recommendation is decision-neutral and does not appear here.

Required labeled field:

```
**Verdict consequence**: [If [condition A holds / is shown false], the verdict
                         changes from [current] to [alternative A].
                         If [condition B], the verdict changes to [alternative B].]
```

**Anti-neutral directive — required for this section.** Before completing this section,
locate any sentence that names an uncertainty without naming its consequence for the
verdict. That sentence is a neutral uncertainty statement. Revise or remove it.

Strings to scan for and remove:
- "More research may be needed on X"
- "There is some uncertainty around X"
- "This area warrants further investigation"
- "It is unclear whether X"
- "Future work could explore X"

The required form: "We do not know [X]. If X is shown to be false, the verdict becomes
[Y]. Resolution method: [specific investigation]."

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Defend it against the adjacent alternative. Name the first action.
Do not assign the decision to the reader.

Required labeled fields:

```
**Prior position**: [What the team believed about {topic} before this investigation.]

**Baseline distance**: [How far the signals have moved the position from that baseline —
                        the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the delta
                        defensible — the compound inference.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] — specifically [action], because
[**Pattern claim**] forces this verdict rather than [adjacent alternative]. This call
stands unless [**Disproof condition**] is shown to hold."

**Anti-neutral directive — required for this section.** Before completing this section,
scan every sentence for strings that give the reader a way to not act.

Strings to scan for and remove:
- "Based on the available evidence, it would be reasonable to..."
- "The team should consider..."
- "It may be worth exploring..."
- "Given the above, a reasonable next step would be..."
- "The evidence supports moving forward, though caution is advised"
- "A possible path forward is..."
- "One option would be to..."
- "This suggests that..."

---

**Layer 3 — Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Signal Findings | **Contents-report** — transcribing what the signal said rather than naming what it changes for the build decision | Any finding entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** — naming each signal's contribution without naming the cross-signal claim | The pattern cannot be stated in one sentence that mentions no individual signal by name |
| What Remains Uncertain | **Verdict-consequence gap** — naming uncertainty without naming its effect on the recommendation | Any uncertainty sentence without an "if...verdict changes to..." clause |
| Recommendation | **Assigns-decision-to-reader** — presenting evidence without issuing the call | `**Verdict**:` field does not contain one of {proceed / pause / pivot / abandon} |

---

## V-02 — Single-Axis: Field-Inventory-First Checklist Architecture

**Variation axis**: Checklist architecture (output format)
**Hypothesis**: Prefacing the checklist with an explicit Required Labeled Fields inventory —
from which each checklist item is mechanically derived (one item per row, in inventory
order) — makes the C-27 single-pass procedure traceable, prevents future orphaning by
requiring any new field to first appear in the inventory before a checklist item is
written for it, and satisfies C-25 through the inventory discipline itself. The section
architecture is unchanged from V-01; the difference is entirely in how the checklist is
presented and derived.

---

### PROMPT BODY — V-02

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal — it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Required Labeled Fields Inventory**

This inventory lists every labeled field this template requires. The pre-artifact
checklist is derived from this inventory: exactly one binary-verifiable presence-
verification item per row. Adding a labeled field to a section template without first
adding it to this inventory violates the design discipline. Adding a checklist item for
a field not in this inventory also violates it.

| ID | Field label | Section | Design axis |
|----|-------------|---------|-------------|
| F-01 | `**Inertia verdict**:` | Signal Findings (per-entry) | Falsifiability |
| F-02 | `**Pattern claim**:` | What Signals Say Together | Falsifiability |
| F-03 | `**Disproof condition**:` | What Signals Say Together | Falsifiability |
| F-04 | `**Verdict consequence**:` | What Remains Uncertain | Falsifiability |
| F-05 | `**Verdict**:` | Recommendation | Falsifiability |
| F-06 | `**Prior position**:` | Recommendation | Inertia-framing |
| F-07 | `**Baseline distance**:` | Recommendation | Inertia-framing |
| F-08 | `**Signals establish**:` | Recommendation | Inertia-framing |

---

**Layer 1 — Pre-Artifact Checklist**

Items derived from the Required Labeled Fields Inventory above. One item per inventory
row plus four section-structure items. All items are locate-and-find operations.
Do not begin writing until all items are YES.

**Section structure:**
1. [ ] Does this output include a labeled **Signal Findings** section?
2. [ ] Does this output include a labeled **What the Signals Say Together** section?
3. [ ] Does this output include a labeled **What Remains Uncertain** section?
4. [ ] Does this output include a labeled **Recommendation** section?

**Field coverage (one item per inventory row F-01 through F-08):**
5. [ ] *(F-01)* Does the Signal Findings section template include `**Inertia verdict**:` on each finding entry?
6. [ ] *(F-02)* Does the What the Signals Say Together section include `**Pattern claim**:`?
7. [ ] *(F-03)* Does the What the Signals Say Together section include `**Disproof condition**:`?
8. [ ] *(F-04)* Does the What Remains Uncertain section include `**Verdict consequence**:`?
9. [ ] *(F-05)* Does the Recommendation section include `**Verdict**:`?
10. [ ] *(F-06)* Does the Recommendation section include `**Prior position**:`?
11. [ ] *(F-07)* Does the Recommendation section include `**Baseline distance**:`?
12. [ ] *(F-08)* Does the Recommendation section include `**Signals establish**:`?

*(Item 5 verifies F-01. Item 6 verifies F-02. ... Item 12 verifies F-08. The mapping is
one-to-one. No item asks whether a field's content meets a quality standard; each asks
whether the label string is present.)*

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

Signals where `**Inertia verdict**:` is NO and the finding changes nothing else are
omitted. State the count and shared basis for exclusion at the end of this section.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the shape the signals collectively form.*

Write the cross-signal claim: true of the signal set as a whole, not stated in any
single signal artifact, causal (names WHY signals converge, not THAT they do).

```
**Pattern claim**: [one sentence. Cross-signal. Causal: "signals converge because
                   [specific structural reason]", not "signals agree".]

**Disproof condition**: [The claim fails if: [specific observable condition that would
                        invalidate the pattern.]]
```

Write `**Disproof condition**:` after committing to the pattern: ask what would need
to be shown false to disprove it, then put that in the field.

Voice anchors: *What's striking is... / The convergence reflects a specific constraint,
not coincidence... / The evidence forces a conclusion I did not expect...*

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without surrendering the verdict.*

Each named uncertainty must complete the verdict-consequence arc. Uncertainties that do
not change the recommendation are omitted.

```
**Verdict consequence**: [If [condition A], verdict changes from [current] to [alt A].
                         If [condition B], verdict changes to [alt B].]
```

**Anti-neutral directive — required for this section.** Locate any sentence naming
uncertainty without naming a verdict consequence. That sentence is a neutral uncertainty
statement — revise or remove it.

Strings to scan for and remove: "More research may be needed" / "There is some
uncertainty around X" / "This area warrants further investigation" / "It is unclear
whether X" / "Future work could explore X"

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Defend it against the adjacent alternative. Name the first action.

```
**Prior position**: [What the team believed before this investigation.]

**Baseline distance**: [How far the signals have moved the position.]

**Signals establish**: [The compound inference that makes the delta defensible.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Sentence form: "I recommend [verdict] — specifically [action], because [**Pattern
claim**] forces this verdict rather than [adjacent alternative]. This call stands unless
[**Disproof condition**] is shown to hold."

**Anti-neutral directive — required for this section.** Scan for strings that give the
reader a way not to act.

Strings to scan for and remove: "Based on the available evidence, it would be reasonable
to..." / "The team should consider..." / "It may be worth exploring..." / "Given the
above, a reasonable next step would be..." / "The evidence supports moving forward,
though caution is advised" / "A possible path forward is..." / "One option would be
to..."

---

**Layer 3 — Per-Section Failure Modes**

| Section | Wrong operation | Detection |
|---------|----------------|-----------|
| Signal Findings | **Contents-report** | Any entry missing `**Inertia verdict**:` |
| What Signals Say Together | **Signal-list** | Pattern cannot be stated without naming individual signals |
| What Remains Uncertain | **Verdict-consequence gap** | Any uncertainty sentence without "if...verdict changes to..." |
| Recommendation | **Assigns-decision-to-reader** | `**Verdict**:` not one of {proceed / pause / pivot / abandon} |

---

## V-03 — Single-Axis: Lean Imperative Register

**Variation axis**: Phrasing register
**Hypothesis**: Stripping meta-explanation and framing language, and expressing all
requirements in short direct imperatives, reduces cognitive overhead at write-time
without sacrificing structural compliance. If V-03 scores identically to V-01 on all
structural criteria, the rubric confirms that register is orthogonal to structure.
The field inventory, checklist, and section fields are identical to V-01.

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

What's striking is... / The convergence reflects... / The evidence forces...

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

Issue the call. Defend it. Name the action. Do not hand the decision to the reader.

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

## V-04 — Compound: Baseline-First Architecture + Role Sequence

**Variation axes**: Lifecycle emphasis + role sequence
**Hypothesis**: Establishing the prior position in a dedicated opening section (Section 0:
Baseline) — before signal findings — changes the narrative arc: findings are measured
against an already-named position rather than building toward a position that is named
at the end. The inertia-framing fields are distributed across two sections (Baseline:
`**Prior position**:`; Recommendation: `**Baseline distance**:`, `**Signals establish**:`).
This restructuring tests whether C-26's axis-registration procedure is robust to
distributed field placement: the Inertia-framing axis still registers all three fields
at incorporation time, but they appear in different sections. The checklist is rebuilt
against the restructured field inventory using the C-27 single-pass procedure.

---

### PROMPT BODY — V-04

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal — it is an
editorial synthesis in your voice interpreting what the signals say together, measured
from a named prior position.

---

**Template Design Axes**

| Axis | Required labeled fields introduced | Section |
|------|-------------------------------------|---------|
| **Falsifiability axis** | `**Inertia verdict**:` | Signal Findings |
| | `**Pattern claim**:` | What the Signals Say Together |
| | `**Disproof condition**:` | What the Signals Say Together |
| | `**Verdict consequence**:` | What Remains Uncertain |
| | `**Verdict**:` | Recommendation |
| **Inertia-framing axis** | `**Prior position**:` | Baseline *(Section 0)* |
| | `**Baseline distance**:` | Recommendation |
| | `**Signals establish**:` | Recommendation |

The Inertia-framing axis introduces `**Prior position**:` in Section 0 (Baseline) and
`**Baseline distance**:`/`**Signals establish**:` in the Recommendation section. All
three fields are registered in this table at incorporation time.

---

**Layer 1 — Pre-Artifact Checklist**

One binary-verifiable item per required labeled field plus section-structure items.
Derived from the complete field inventory above. All items are locate-and-find
operations. Answer YES by locating the named element.

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
12. [ ] Does the Recommendation section include `**Baseline distance**:`?
13. [ ] Does the Recommendation section include `**Signals establish**:`?

*(All items are presence-verification operations. Items 11–13 cover all three
Inertia-framing-axis fields, distributed across two sections — the checklist tracks
both locations.)*

---

**Layer 2 — Section Templates**

---

**Section 0: Baseline**

*Your stance: the archivist who names where the team stood before the signals arrived.*

Name the prior position first. Every subsequent section measures against this baseline.

```
**Prior position**: [What the team believed about {topic} before this investigation
                    began — the hypothesis, assumption, or working position that
                    was in place when the signal-gathering started.]
```

This section has one job: name the baseline. Do not report findings here. Do not issue
the verdict here. The entire document gains meaning from the distance between what is
written in this field and what the signals establish.

Wrong operation: **Baseline-omission** — writing the prior position as hedged context
("we had some assumptions about X") rather than as a named position that can be
measured against. Detection: can you write "the prior position was [specific claim]"?
If not, you have context, not a baseline.

---

**Section 1: Signal Findings**

*Your stance: the investigator who measures each finding against the named baseline.*

Every finding is evaluated against the `**Prior position**:` established in Section 0.
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

Wrong operation: **Contents-report** — transcribing signal artifacts without measuring
against the baseline. Detection: any entry missing `**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the emergent claim the signal set produces.*

Write the cross-signal claim. It must be: true of the signal set as a whole, not stated
in any single artifact, causal (names why signals converge, not that they do).

```
**Pattern claim**: [One sentence. Cross-signal. Causal account required.]

**Disproof condition**: [The claim fails if: [specific observable condition that would
                        invalidate the pattern.]]
```

Write `**Disproof condition**:` after committing to the pattern. Ask: what would someone
need to demonstrate is false to disprove this? That answer is the field's content.

Voice anchors: *What's striking is... / The signals collectively establish... / The
distance from the prior position is not incremental — it reflects a structural shift...*

Wrong operation: **Signal-list** — presenting each signal's contribution without naming
the cross-signal claim. Detection: pattern cannot be stated in one sentence that
mentions no individual signal by name.

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without collapsing the verdict.*

Every named uncertainty must complete the verdict-consequence arc. Uncertainties that
do not change the recommendation are omitted.

```
**Verdict consequence**: [If [condition A holds / is shown false], the verdict changes
                         from [current] to [alternative A].
                         If [condition B], the verdict changes to [alternative B].]
```

**Anti-neutral directive — required for this section.** Locate any sentence that names
an uncertainty without naming its consequence for the verdict. That sentence is a
neutral uncertainty statement — it names the unknown without naming why it matters.
Revise or remove it.

Strings to scan for and remove:
- "More research may be needed on X"
- "There is some uncertainty around X"
- "This area warrants further investigation"
- "It is unclear whether X"
- "Future work could explore X"

Required form: "We do not know [X]. If X is shown to be false, the verdict becomes [Y].
Resolution method: [specific investigation]."

Wrong operation: **Verdict-consequence gap** — naming uncertainty without naming its
effect on the verdict. Detection: any uncertainty sentence lacking an "if...verdict
changes to..." clause.

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call — who can name exactly
how far the signals have moved the position from the baseline.*

Issue one verdict. Name the distance traveled from `**Prior position**:`. Defend the
verdict against the adjacent alternative. Name the first action.

```
**Baseline distance**: [How far the signals have moved the team's position from the
                        prior position named in Section 0 — the measurable delta.]

**Signals establish**: [What the signals collectively establish that makes the distance
                        defensible — the compound inference.]

**Verdict**: [proceed / pause / pivot / abandon]
```

Recommendation sentence form: "I recommend [verdict] — specifically [action], because
[**Pattern claim**] establishes a [**Baseline distance**] from [**Prior position**],
and this movement forces this verdict rather than [adjacent alternative]. This call
stands unless [**Disproof condition**] is shown to hold."

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
the call. Detection: `**Verdict**:` field does not contain one of
{proceed / pause / pivot / abandon}.

---

**Layer 3 — Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Baseline | Baseline-omission | `**Prior position**:` names context rather than a specific, measurable position |
| Signal Findings | Contents-report | Any entry missing `**Inertia verdict**:` |
| What Signals Say Together | Signal-list | Pattern cannot be stated without naming individual signals |
| What Remains Uncertain | Verdict-consequence gap | Any uncertainty sentence without "if...verdict changes to..." |
| Recommendation | Assigns-decision-to-reader | `**Verdict**:` not one of {proceed / pause / pivot / abandon} |

---

## V-05 — Compound: Consolidated Position-Delta Field + Minimal Checklist Design

**Variation axes**: Output format + inertia framing
**Hypothesis**: Replacing the three Inertia-framing-axis fields (`**Prior position**:`,
`**Baseline distance**:`, `**Signals establish**:`) with a single
`**Position delta**:` field reduces the orphaning surface to zero at the cost of one
field merging semantic content that was previously separated. The checklist shrinks from
12 to 10 items. This tests whether semantic consolidation is a valid C-27 strategy:
can a merged field satisfy C-13's inertia-document-wide requirement and C-27's
single-pass design requirement simultaneously? The consolidated field must carry a
template structure that forces the three semantic components (prior position, current
distance, supporting inference) without requiring separate labeled fields.

---

### PROMPT BODY — V-05

You are producing the `topic-story` artifact for `{topic}`. Synthesize all gathered
signals into a decision narrative. This is NOT a summary of each signal — it is an
editorial synthesis in your voice interpreting what the signals say together.

---

**Template Design Axes**

| Axis | Required labeled fields introduced |
|------|-------------------------------------|
| **Falsifiability axis** | `**Inertia verdict**:` · `**Pattern claim**:` · `**Disproof condition**:` · `**Verdict consequence**:` · `**Verdict**:` |
| **Inertia-framing axis** | `**Position delta**:` *(consolidated: prior position → distance → signals establish)* |

The Inertia-framing axis introduces one field. The field's internal template structure
carries all three semantic components; three separate labeled fields are not needed.

---

**Layer 1 — Pre-Artifact Checklist**

One binary-verifiable presence-verification item per required labeled field.
Derived from the field inventory above. All items are locate-and-find operations.

**Section structure:**
1. [ ] Does this output include a labeled **Signal Findings** section?
2. [ ] Does this output include a labeled **What the Signals Say Together** section?
3. [ ] Does this output include a labeled **What Remains Uncertain** section?
4. [ ] Does this output include a labeled **Recommendation** section?

**Falsifiability-axis field coverage:**
5. [ ] Does the Signal Findings section include `**Inertia verdict**:` on each finding entry?
6. [ ] Does the What the Signals Say Together section include `**Pattern claim**:`?
7. [ ] Does the What the Signals Say Together section include `**Disproof condition**:`?
8. [ ] Does the What Remains Uncertain section include `**Verdict consequence**:`?
9. [ ] Does the Recommendation section include `**Verdict**:`?

**Inertia-framing-axis field coverage (registered at incorporation time):**
10. [ ] Does the Recommendation section include `**Position delta**:`?

*(The Inertia-framing axis contributes one field (F-06, `**Position delta**:`).
Item 10 covers it. Items 1–9 cover section structure and Falsifiability-axis fields.
All items are locate-and-find operations. The field's internal structure [Prior: /
Delta: / Established by:] is a template prompt, not a separate labeled field, and
requires no additional checklist item.)*

---

**Layer 2 — Section Templates**

---

**Section 1: Signal Findings**

*Your stance: the investigator who curates for salience — not the reporter who
transcribes.*

The build-decision filter governs every entry. Before writing each finding, answer:
**Does this finding change whether to build `{topic}`?**

For each signal:

```
**[Signal name]** — [one to three sentences. Key finding only. Not a summary.]
**Inertia verdict**: [YES — this moves the position /
                     NO — this confirms the prior position /
                     PARTIAL — [one clause naming what specifically shifts]]
```

Signals where `**Inertia verdict**:` is NO and nothing else changes are omitted.
Close this section noting count and shared basis for exclusion.

Wrong operation: **Contents-report** — transcribing rather than curating. Detection:
any entry missing `**Inertia verdict**:`.

---

**Section 2: What the Signals Say Together**

*Your stance: the analyst who names the shape the signals collectively form.*

Write the cross-signal claim: true of the set as a whole, not stated in any single
artifact, causal (names WHY signals converge).

```
**Pattern claim**: [One sentence. Cross-signal. Causal account required.]

**Disproof condition**: [The claim fails if: [specific observable condition.]]
```

Write `**Disproof condition**:` after committing to the pattern: name what would need
to be shown false to disprove it.

Voice anchors: *What's striking is... / The convergence reflects... / The evidence
forces a conclusion I did not expect...*

Wrong operation: **Signal-list** — listing signals rather than naming the cross-signal
claim. Detection: pattern cannot be stated without naming individual signals.

---

**Section 3: What Remains Uncertain**

*Your stance: the honest investigator who names limits without surrendering the verdict.*

Every named uncertainty must close the verdict-consequence arc. Decision-neutral
uncertainties are omitted.

```
**Verdict consequence**: [If [condition A], verdict changes to [alt A].
                         If [condition B], verdict changes to [alt B].]
```

**Anti-neutral directive — required for this section.** Locate any sentence naming
uncertainty without naming its verdict consequence. Revise or remove it.

Strings to scan for and remove: "More research may be needed" / "There is some
uncertainty around X" / "This area warrants further investigation" / "It is unclear
whether X" / "Future work could explore X"

Wrong operation: **Verdict-consequence gap**. Detection: any uncertainty sentence
without an "if...verdict changes to..." clause.

---

**Section 4: Recommendation**

*Your stance: the investigator held accountable for the call.*

Issue one verdict. Name the position delta — where the team stood before, how far the
signals moved that position, and what established the movement. Defend the verdict.
Name the first action.

```
**Position delta**: [Prior: [what the team believed before this investigation.]
                    Delta: [how far the signals have moved that position.]
                    Established by: [the compound inference that makes the movement
                    defensible.]]

**Verdict**: [proceed / pause / pivot / abandon]
```

The `**Position delta**:` field carries three semantic components in a single labeled
slot. Write all three; leaving any component blank produces an incomplete inertia
account.

Recommendation sentence: "I recommend [verdict] — specifically [action], because
[**Pattern claim**] establishes the delta described above, forcing this verdict rather
than [adjacent alternative]. This call stands unless [**Disproof condition**] is shown
to hold."

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

Wrong operation: **Assigns-decision-to-reader**. Detection: `**Verdict**:` not one of
{proceed / pause / pivot / abandon}.

---

**Layer 3 — Per-Section Failure Modes**

| Section | Wrong operation | Detection criterion |
|---------|----------------|---------------------|
| Signal Findings | Contents-report | Any entry missing `**Inertia verdict**:` |
| What Signals Say Together | Signal-list | Pattern cannot be stated without naming individual signals |
| What Remains Uncertain | Verdict-consequence gap | Any uncertainty sentence without "if...verdict changes to..." |
| Recommendation | Assigns-decision-to-reader | `**Verdict**:` not one of {proceed / pause / pivot / abandon} |

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
| C-13 | PASS | PASS | PASS | PASS | PASS† |
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

**Notes:**
- `*` V-04 has five sections; C-01 requires four. The Baseline section is a fifth
  structural section. C-01 requires four specific sections; V-04 provides all four
  plus one additional. PASS is predicted but the rubric may flag the five-section
  structure as a deviation.
- `†` V-05 consolidates three inertia fields into one. C-13 requires the inertia test
  in at least two non-synthesis sections. `**Inertia verdict**:` appears in Signal
  Findings; `**Position delta**:` appears in Recommendation. Two non-synthesis sections.
  PASS is predicted but requires verification that `**Position delta**:` constitutes
  an inertia test in the rubric's terms.

**Primary distinction across variations**: V-01/V-02/V-03 differ only in presentation
layer (axis registration visibility, checklist derivation explicitness, register
density). V-04 differs architecturally (five sections, distributed inertia fields).
V-05 differs in field design (consolidated inertia field, 10-item checklist).

**Key tests R7 scorecards should resolve:**
1. Whether the C-27 procedure is satisfiable by semantic consolidation (V-05) or
   requires one-field-one-item correspondence across separate fields
2. Whether C-01's "four sections" fires on V-04's five-section structure
3. Whether the axis-table preamble in V-01 constitutes demonstrable C-26 compliance
   vs. C-26 compliance being inferred from the checklist's coverage alone
4. Whether lean register (V-03) produces any structural differences in rubric scoring
   vs. verbose register (V-01/V-02)
