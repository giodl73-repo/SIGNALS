---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 4
rubric: v4
---

# Variations: `topic:echo` — Round 4

**Rubric:** v4 | **Date:** 2026-03-16

---

## Design Context

R3 V-03 (Institutional Archaeologist) produced two unproven excellence signals that
became C-15 and C-16 in v4:

- **C-15: Structural Counterfactual Induction** — V-03's Archaeologist role structurally
  induces counterfactual reasoning via "would the next team carry this as a false
  assumption?" without requiring an explicit clause per entry. V-03 earned C-09 PARTIAL
  (not PASS) because the role framing could be bypassed — entries could still be written
  without truly reasoning from future-team ignorance. For C-15 PASS, the structural
  device must make it impossible to fill the entry template without answering "what
  would a new team, reading today's materials, assume wrongly?" The schema fields
  themselves must be defined in terms of the inherited assumption, not the original
  team's surprise.

- **C-16: Misunderstanding-Category Synthesis** — V-03's Step 4 groups by "category of
  misunderstanding," which is higher-order than root-cause or topic grouping. V-03
  earned PARTIAL because: (a) the group labels could still be expressed as topic labels
  rather than blind-spot type labels, and (b) no non-derivability constraint was
  enforced — the synthesis block's claims could be derived by re-reading the individual
  entries. For C-16 PASS, the synthesis must (1) name the *type* of wrong thinking
  (not the topic area), and (2) state something not visible from reading individual
  entries.

**R4 structural goal:** Three single-axis variations isolate one mechanism each; two
combined variations test pairwise and full-set interaction. All five must maintain
C-01 through C-07 (essential + recommended) without degradation.

**Variation axes selected:**

1. **Role sequence** — Archaeologist orientation embedded throughout the entire schema
   (field names, field definitions, filter rules), making counterfactual reasoning
   structurally unavoidable at entry-production time. Targets C-15.

2. **Output format** — Blind Spot Map section with explicit category-naming requirements
   and a non-derivability constraint applied at synthesis time. Targets C-16.

3. **Phrasing register** — Future-team-oriented field vocabulary in the schema (not a
   named role, but field names that encode the purpose: "What today's materials imply"
   instead of "Expected"). The register of the field definitions, not a persona, induces
   the same counterfactual orientation as V-01. Tests whether C-15 can be achieved via
   vocabulary rather than role identity. Targets C-15 via alternative mechanism.

**Predicted score map (v4 rubric, max 100):**

| Variant | C-15 | C-16 | Predicted |
|---------|------|------|-----------|
| V-01    | PASS | FAIL | higher    |
| V-02    | FAIL | PASS | higher    |
| V-03    | PASS | FAIL | higher    |
| V-04    | PASS | PASS | highest of singles |
| V-05    | PASS | PASS | max       |

The predicted differential between V-04 and V-05 tests whether V-02's non-derivability
constraint (which becomes the Blind Spot Map's synthesis requirement in V-05) adds
detectable improvement in C-16 quality over V-04's version.

**What C-15 requires over R3 V-03:**

R3 V-03 framed the Archaeologist role as an orientation — "you are reading their record
18 months later." But the schema fields still used original-team vocabulary ("Prior
assumption", "Correction"). A model could adopt the role framing and then fill fields
using discovery-narrative thinking. C-15 requires the schema fields themselves to be
defined in future-team terms: "Inherited assumption" (what today's materials still imply
to a new reader), "Consequence if missing" (what the next team would build wrong). No
field can be answered from original-team perspective; each field forces reasoning about
the next team's state.

**What C-16 requires over R3 V-03:**

R3 V-03's grouping step said "category of misunderstanding — the same blind spot in how
the original design materials frame the problem." This was the right framing but two
failure modes remained open: (a) group labels could be written as topic labels in
practice ("state management issues" rather than "we assumed state was caller-managed;
it is not"), and (b) the synthesis sentence could be derivable by re-reading individual
entries. C-16 adds explicit requirements: category labels must characterize the *type*
of wrong thinking (a named failure pattern with examples of passing and failing labels),
and the synthesis sentence must state something a reader cannot derive from reading any
one or all of the individual entries.

---

## V-01 — Single-axis: Role sequence — Archaeologist Schema Embedding

**Variation axis:** Role sequence — the Archaeologist orientation is embedded in the
schema field names and definitions, not stated as a framing section. Every field asks
for information about the next team's epistemic state ("Inherited assumption," "Consequence
if missing"), making it structurally impossible to answer the schema from the original
team's perspective.

**Hypothesis:** R3 V-03 framed the Archaeologist role in an orientation section, then
used original-team vocabulary in the schema fields. A model that adopts the role framing
but encounters "Prior assumption:" can write the original team's historical belief, not
necessarily what today's materials still imply. When the field is named "Inherited
assumption" and defined as "what a new team reading today's materials would assume," the
model cannot answer from historical perspective — the field is only answerable from the
future-team vantage point. C-15's pass condition ("structural device makes counterfactual
reasoning unavoidable") is satisfied at the schema-field level. C-16 is not structurally
enforced (the synthesis step is present but lacks category-naming requirements and
non-derivability constraint).

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be something
the next team needs before they begin — a correction the current design materials do
not contain.

== SCHEMA =====================================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [A label that encodes the correction, not the discovery. The next
                   team should be able to cite this name in conversation without
                   reading the full entry. "The Cascade Inversion" encodes what
                   changed; "Unexpected Cascade Behavior" labels only that something
                   happened. Not "Finding 1" or "Surprise A".]

  Source:          [namespace:skill:artifact — e.g., listen:adoption:signal-adoption-
                   2026-03-14.md. Not "signals indicated" / "research showed" /
                   "the data suggested".]

  Inherited assumption:
                   [The belief a new team would carry into this design today, reading
                   only the current spec, proposal, and design documents. State it as
                   what today's materials still imply: "Today's materials imply..." or
                   "A new team reading the current spec would assume..."
                   This is not the original team's historical belief. It is what the
                   current materials still lead a reader to assume.
                   Test: "If a new engineer joined tomorrow and read only the current
                   design docs, would they hold this assumption?" If no, rewrite.]

  What the signals showed instead:
                   [The correction — must directly contradict the inherited assumption.
                   Not a degree variant: "Today's materials imply adoption will be high;
                   adoption was moderate" records a degree difference. Name the
                   assumption the finding factually overturns.
                   Direct claim. No hedges. Prohibited everywhere: "may suggest" /
                   "appears to indicate" / "seems like" / "could mean" / "might be" /
                   "it is possible that". Uncertainty is a rewrite instruction.]

  Consequence if missing:
                   [What the next team would design wrong if they carried the inherited
                   assumption. Name the specific component, flow, or decision affected.
                   One sentence minimum. Prohibited: "this is worth noting" /
                   "bears watching" / "important to keep in mind" / "has implications".
                   Name the consequence, not the severity.]

  Before proceeding, the next team must:
                   [The specific decision, investigation, or design choice the next
                   team cannot skip. Not "further investigation needed" / "keep an eye
                   on this" / "monitor this". A specific next action or a blocking
                   open question.]

  Severity:        [HIGH / MEDIUM / LOW — relative to consequence if missing]

== FILTER =====================================================================

Before drafting any entry, apply the still-consequential filter:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES → this correction is still load-bearing. Draft the entry.
  NO  → the current materials have absorbed this finding. It is no longer a
        correction the next team needs. Exclude it. Absorbed findings belong in
        topic-story, not topic-echo.

This filter is not optional — it is the primary selection criterion. Apply before
writing any field. Do not produce entries for findings that today's materials already
reflect.

== RULES ======================================================================

Rule 1 — Correction framing, not discovery framing:
  Every entry is written for the next team, not narrated from the original team's
  experience. "We found that X" is discovery framing — rewrite as "Today's materials
  imply X; they should not, because the signals showed Y." The Inherited assumption
  field has no "we" — it has only "today's materials" and "a new team."

Rule 2 — Claim-only voice:
  State every correction as a direct claim. The prohibited constructs from "What the
  signals showed instead" apply to every field. Uncertainty is a rewrite instruction.

Rule 3 — Entry completeness:
  Write each entry so that a new team member reading only that entry — without the
  introduction, without other entries — can understand what today's materials imply,
  what they should imply instead, and what the next team would build wrong if they
  never read this. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one correction must emerge from the intersection of two or more signals.
Source field names both sources. After the "What the signals showed instead" field,
add one sentence:
  "Neither [source A] nor [source B] alone revealed this gap — their intersection
   showed that today's materials still imply [X], which the original team corrected
   in [A]+[B] together."
Co-citation without a named gap statement fails this requirement.

== SEVERITY ORDERING ==========================================================

Order all entries HIGH → MEDIUM → LOW by Severity. Unordered lists fail.

== SYNTHESIS ==================================================================

After all entries, write one section: "Pattern of inherited assumptions."

Do two or more corrections share a structural origin — a family of things today's
materials systematically lead new readers to assume wrongly? Write 2-4 sentences.
Name any pattern; if none exists, state that explicitly: "The corrections address
independent inherited assumptions with no shared structural origin in today's materials."

== FORWARD GUIDANCE ===========================================================

Write 1-3 sentences addressed directly to the next team. Register: "Before you build
{topic}, the correction record requires you to know that..." or "Today's design
materials do not warn you that..." Specific to these corrections — not generic.

== SCOPE NEGATION =============================================================

Final section: "What this artifact excludes."
Name at least two excluded categories with counts:
  e.g., "Absorbed findings: [N] items the current materials already reflect"
       "Degree differences: [N] items where signals confirmed direction but adjusted
        magnitude, not assumption"
Implicit exclusion (simply not including non-corrections) does not satisfy this.

== OUTPUT =====================================================================

Structure:
  1. Corrections — ordered HIGH → MEDIUM → LOW
  2. Pattern of inherited assumptions
  3. Forward guidance
  4. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-02 — Single-axis: Output format — Blind Spot Map with Non-Derivability Constraint

**Variation axis:** Output format — the synthesis section is restructured into a
mandatory "Blind Spot Map" that requires naming the *type* of wrong thinking (not the
topic area) and includes an explicit non-derivability constraint on the synthesis
sentence. Explicit pass/fail examples are embedded in the section definition.

**Hypothesis:** R3 V-03's grouping step said "category of misunderstanding — the same
blind spot" but provided no guard against topic-label group names and no requirement
for non-derivable synthesis. A Blind Spot Map section that (a) names passing vs. failing
label patterns ("Actor misidentification" passes; "Unexpected user behavior" fails),
(b) requires assignment of each entry to exactly one category, and (c) explicitly
requires the synthesis sentence to state something not visible from individual entries
forces the model to produce genuinely higher-order synthesis. C-15 is not structurally
enforced (the schema uses original-team vocabulary; the counterfactual orientation
comes only from rules, not from field definitions).

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be something
that could not have been written before the signals were gathered.

== SCHEMA =====================================================================

Apply to every surprise. All fields required.

  Name:            [memorable label specific to this finding — e.g., "The Adoption
                   Inversion", "The Silent Veto Problem". Not "Finding 1" / "Surprise A".]

  Source:          [namespace:skill:artifact — specific artifact, not vague attribution.
                   Not "signals indicated" / "research showed" / "the data suggested".]

  Expected:        [The team's prior belief — a direct, confident claim stating the
                   assumption the finding contradicts. Must oppose in direction,
                   mechanism, or actor, not merely differ in degree. "Expected high
                   adoption; adoption was moderate" records a degree difference.
                   Name the assumption the finding factually overturns.]

  Finding:         [The surprise — direct claim, no hedges. Prohibited: "may suggest" /
                   "appears to indicate" / "seems like" / "could mean" / "might be".]

  Design impact:   [Specific design consequence — one sentence minimum. Prohibited:
                   "this is worth noting" / "bears watching" / "important to keep in mind".]

  Next move:       [Specific action or open question. Not "further investigation needed" /
                   "keep an eye on this" / "monitor this".]

  Severity:        [HIGH / MEDIUM / LOW]

== RULES ======================================================================

Rule 1 — Counterfactual filter:
  Before drafting any surprise: "Could a passive, attentive team have found this
  through normal observation without running signals?" If yes, exclude it.

Rule 2 — Claim-only voice:
  No hedges. Prohibited constructs from Finding apply to every field.

Rule 3 — Entry readability:
  Write each entry so that a new team member reading only that entry can understand
  what was expected, what was found, and why it matters. Define domain terms within
  each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one surprise must emerge from two or more signals. Source names both.
Name the convergence delta: "Neither [A] nor [B] alone showed this — together they
revealed [Y], which neither source would have produced independently."

== SEVERITY ORDERING ==========================================================

Order all entries HIGH → MEDIUM → LOW. Unordered lists fail.

== BLIND SPOT MAP ==============================================================

After all entries, write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem — a category of wrong thinking that produced multiple independent surprises.
Two surprises share a blind spot if they were both caused by the same type of error
in the original materials, not merely the same topic area.

STEP 1 — NAME THE BLIND SPOT CATEGORIES.

A category name must characterize the *type* of wrong thinking, not the subject matter.

  PASS examples:
    "Actor misidentification — materials assumed resistance originates from end users;
     signals showed it originates from platform operators"
    "Sequence inversion — materials assumed validation precedes authorization; signals
     showed authorization must precede validation to prevent partial-commit state"
    "Scope underspecification — materials assumed the problem space was bounded by
     the current API surface; signals showed the problem extends to downstream consumers"

  FAIL examples:
    "Unexpected user behavior" — labels a topic, not a type of wrong thinking
    "State management issues" — labels a domain, not a structural error
    "Performance-related findings" — labels a concern, not a misunderstanding pattern

  A group label that could appear unchanged in a different echo about a different topic
  fails this requirement.

STEP 2 — ASSIGN EACH SURPRISE TO EXACTLY ONE CATEGORY.

If a surprise does not share a blind spot type with any other entry, list it as
"Unclassified" and state in one sentence why it does not fit any named category.

STEP 3 — WRITE THE SYNTHESIS.

Write 2-3 sentences under the heading "What the blind spot map reveals."

NON-DERIVABILITY CONSTRAINT: The synthesis must state something not visible from
reading individual entries. A synthesis that merely tallies category assignments
("Three surprises share an actor-misidentification blind spot") fails — this is
derivable by reading the category labels above it. The synthesis must state what the
*pattern of blind spots* reveals about the original materials as a whole — a claim
that requires seeing the full map to make, not just reading one or all of the entries.

If no cross-entry pattern exists, state that explicitly: "The surprises address
independent blind spots; the map reveals no shared structural origin in today's
materials."

== META-REFLECTION ============================================================

One section: "What the surprise distribution reveals."

Where did surprises concentrate (namespace, phase, signal type)? Prescribe the
gathering adjustment: "For topics like this one, run [X] before [Y] to surface [Z
class of surprise] earlier." Prescribe — do not only observe.

== SCOPE NEGATION =============================================================

"What this artifact excludes."

Name at least two excluded categories with counts or examples. Implicit exclusion
(simply not including non-surprises) does not satisfy this.

== OUTPUT =====================================================================

Structure:
  1. Surprises — ordered HIGH → MEDIUM → LOW
  2. Blind Spot Map
  3. What the surprise distribution reveals
  4. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-03 — Single-axis: Phrasing register — Future-Team Schema Vocabulary

**Variation axis:** Phrasing register — the schema field names and definitions use
future-team-oriented vocabulary throughout (no Archaeologist role is named; no role
framing section exists). The field names encode purpose: "What today's materials imply"
instead of "Expected," "What the next team would build wrong" instead of "Design impact."
The vocabulary of the fields induces the same counterfactual orientation as V-01's
Archaeologist embedding, through a different mechanism.

**Hypothesis:** V-01 achieves C-15 by embedding the Archaeologist role's question into
the schema field definitions. V-03 tests whether the same structural effect can be
achieved through phrasing register alone — without naming a role, without an orientation
section, purely through field vocabulary. If "What today's materials imply" and "What the
next team would build wrong" induce the same forced counterfactual reasoning as the
Archaeologist schema embedding, the two variations are mechanically equivalent for C-15.
If they are not equivalent, the difference reveals whether role identity (V-01) or field
vocabulary (V-03) is the load-bearing component of C-15's structural induction. C-16 is
not structurally enforced.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be something
the next team needs before they begin — a correction the current design materials do
not contain, and that a new team would not know to look for.

== SCHEMA =====================================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [A label the next team can cite without reading the full entry.
                   Encode the correction: "The Cascade Inversion" (what changed)
                   over "Unexpected Cascade Behavior" (something happened).
                   Not "Finding 1" or "Surprise A".]

  Source:          [namespace:skill:artifact — e.g., flow:resilience:signal-resilience-
                   2026-03-14.md. Not "signals indicated" / "research showed" /
                   "the data suggested".]

  What today's materials imply:
                   [State what a new team reading only the current spec, proposal, and
                   design documents would assume. Write as: "Today's materials imply
                   that..." or "A new team reading the current spec would assume..."
                   This is the live assumption the correction must overturn — not the
                   original team's historical belief, but what today's documents still
                   lead a reader toward.
                   Degree variants fail: "Materials imply X will be high; it was
                   moderate" records a magnitude difference, not a false assumption.
                   Name the assumption that the finding factually reverses.]

  What the signals showed instead:
                   [The correction — must directly contradict what today's materials
                   imply. Not a degree difference. Direct claim. Prohibited: "may
                   suggest" / "appears to indicate" / "seems like" / "could mean" /
                   "might be" / "it is possible that".]

  What the next team would build wrong:
                   [The specific design error a new team makes if they carry the
                   inherited assumption. Name the component, flow, or decision that
                   would be wrong. One sentence minimum. Prohibited: "this is worth
                   noting" / "bears watching" / "important to keep in mind". Name
                   the consequence.]

  What the next team must decide before proceeding:
                   [The specific question or action that cannot be deferred. Not
                   "further investigation needed" / "keep an eye on this". A specific
                   decision point or blocking open question.]

  Severity:        [HIGH / MEDIUM / LOW — relative to the design error if missing]

== RULES ======================================================================

Rule 1 — Still-live filter:
  Before drafting any entry: "Does today's design material still imply the false
  assumption this finding corrects?" If the current materials have already absorbed
  this correction — if they no longer lead a new reader toward the wrong assumption —
  exclude this entry. It is no longer load-bearing. Apply as a discard filter.

Rule 2 — Claim-only voice:
  State every correction as a direct claim. No hedges. Apply the prohibited constructs
  from "What the signals showed instead" to every field.

Rule 3 — Entry completeness:
  Write each entry so that a new team member reading only that entry can understand
  what today's materials lead them to assume, what they should assume instead, and
  what they would build wrong without this correction. Define domain terms within
  each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from the intersection of two or more signals. Source
names both. After "What the signals showed instead," add:
  "Neither [source A] nor [source B] alone revealed this — their intersection showed
   that today's materials still imply [X], which [A]+[B] together corrected."
Co-citation without a named convergence gap fails this requirement.

== SEVERITY ORDERING ==========================================================

Order all entries HIGH → MEDIUM → LOW. Unordered lists fail.

== SYNTHESIS ==================================================================

After all entries, write one section: "Pattern of inherited assumptions."

Do two or more corrections share a structural source — a family of false assumptions
today's materials systematically produce? Write 2-4 sentences. Name any pattern; if
none exists, state that explicitly.

== FORWARD GUIDANCE ===========================================================

Write 1-3 sentences to the next team. Register: "Before you build {topic}, today's
design materials do not warn you that..." or "The correction record requires you to
know before you start..." Specific to these corrections.

== SCOPE NEGATION =============================================================

"What this artifact excludes."
Name at least two excluded categories with counts:
  e.g., "Absorbed corrections: [N] findings the current materials already reflect"
       "Degree differences: [N] items where signals confirmed direction but adjusted
        magnitude, not the underlying assumption"
Implicit exclusion does not satisfy this.

== OUTPUT =====================================================================

Structure:
  1. Corrections — ordered HIGH → MEDIUM → LOW
  2. Pattern of inherited assumptions
  3. Forward guidance
  4. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-04 — Combined: Role sequence + Output format (C-15 + C-16)

**Axes combined:** V-01's Archaeologist schema embedding (C-15) + V-02's Blind Spot
Map with non-derivability constraint (C-16).

**Hypothesis:** The two mechanisms address orthogonal structural properties. The
Archaeologist schema embedding fires at entry-production time — it determines what
fields are filled and how. The Blind Spot Map fires after all entries are drafted —
it determines how they are organized and what the synthesis must state. No interaction
surface exists between them: filling the "Inherited assumption" field correctly does
not constrain or influence the blind-spot category naming step. Together they provide
full coverage of both new criteria without either interfering with the other. The
combination does not add cognitive overhead beyond V-01 and V-02 individually because
the schema phase and the synthesis phase are sequentially separated.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a correction
the next team needs before they begin — something today's design materials do not
contain, and that a new team would carry as a false assumption.

== SCHEMA =====================================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [A label that encodes the correction — what changed, not that
                   something happened. Citable by the next team without reading the
                   full entry. Not "Finding 1" or "Surprise A".]

  Source:          [namespace:skill:artifact — e.g., prove:interview:signal-interview-
                   2026-03-14.md. Not "signals indicated" / "research showed" /
                   "the data suggested".]

  Inherited assumption:
                   [The belief a new team would carry into this design today, reading
                   only the current spec, proposal, and design documents. State as:
                   "Today's materials imply..." or "A new team reading the current
                   spec would assume..."
                   Test: "If a new engineer joined tomorrow and read only the current
                   design docs, would they hold this assumption?" If no, rewrite.
                   Degree variants fail: name the assumption the finding overturns,
                   not a magnitude of the same direction.]

  What the signals showed instead:
                   [The correction — directly contradicts the inherited assumption.
                   Direct claim. No hedges. Prohibited: "may suggest" / "appears to
                   indicate" / "seems like" / "could mean" / "might be" / "it is
                   possible that".]

  Consequence if missing:
                   [The specific design error the next team makes if they carry the
                   inherited assumption. Name the component, flow, or decision. One
                   sentence minimum. Prohibited: "worth noting" / "bears watching" /
                   "important to keep in mind". Name the consequence.]

  Before proceeding, the next team must:
                   [The specific action or blocking question. Not "further investigation
                   needed" / "keep an eye on this" / "monitor this".]

  Severity:        [HIGH / MEDIUM / LOW]

== FILTER =====================================================================

Before drafting any entry, apply the still-consequential filter:
  "Would a new team, reading only today's design materials, carry this as a false
   assumption going in?"

  YES → correction is load-bearing. Draft the entry.
  NO  → the current materials have absorbed this finding. Exclude it. Absorbed
        findings belong in topic-story, not topic-echo.

== RULES ======================================================================

Rule 1 — Correction framing:
  Every entry is written for the next team, not narrated from the original team's
  experience. "We found that X" is discovery framing. "Today's materials imply X;
  they should not" is correction framing. The Inherited assumption field has no "we."

Rule 2 — Claim-only voice:
  Direct claims only. No hedges. Apply the prohibited constructs from "What the
  signals showed instead" to every field.

Rule 3 — Entry completeness:
  Write each entry so that a new team member reading only that entry can understand
  what today's materials imply, what they should imply instead, and what the next
  team would build wrong without this correction. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one correction must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this — their intersection showed that today's
   materials still imply [X], which the original team corrected in [A]+[B] together."

== SEVERITY ORDERING ==========================================================

Order all entries HIGH → MEDIUM → LOW. Unordered lists fail.

== BLIND SPOT MAP ==============================================================

After all entries, write one section: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem — a type of wrong thinking that produced multiple independent corrections.

STEP 1 — NAME THE BLIND SPOT CATEGORIES.

Category names must characterize the *type* of wrong thinking, not the subject matter.

  PASS: "Sequence inversion — materials assumed X precedes Y; signals showed Y precedes
         X, invalidating the commit ordering assumption"
  PASS: "Actor misidentification — materials assumed friction originates from end users;
         signals showed it originates from platform infrastructure"
  FAIL: "State management" — labels a domain, not a type of wrong thinking
  FAIL: "User behavior issues" — labels a topic, not a structural error

A category label that could appear unchanged in an echo about a different topic fails.

STEP 2 — ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

If a correction shares no blind spot type with any other, list it as "Unclassified"
and state in one sentence why it does not fit any named category.

STEP 3 — SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences.

NON-DERIVABILITY CONSTRAINT: The synthesis must state something not visible from
reading individual corrections or from tallying category assignments. A synthesis
that says "Three corrections share an actor-misidentification blind spot" is derivable
from the category assignments above it — it fails. The synthesis must state what the
*pattern of blind spots* reveals about the original materials as a system — a claim
that requires seeing the full map, not just reading one entry or all entries.

If no pattern exists: "The corrections address independent blind spots with no shared
structural origin in today's materials."

== META-REFLECTION ============================================================

"What the surprise distribution reveals."

Where did corrections concentrate (namespace, phase, signal type)? Prescribe:
"For topics like this one, run [X] before [Y] to surface [Z class of correction]
earlier." Prescribe — do not only observe.

== SCOPE NEGATION =============================================================

"What this artifact excludes."
Name at least two excluded categories with counts:
  e.g., "Absorbed corrections: [N] findings the current materials already reflect"
       "Discovery narratives: excluded as past-team experience, not next-team corrections"
Implicit exclusion does not satisfy this.

== OUTPUT =====================================================================

Structure:
  1. Corrections — ordered HIGH → MEDIUM → LOW
  2. Blind Spot Map
  3. What the surprise distribution reveals
  4. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-05 — Combined: All three axes (C-15 via vocabulary + C-16 + PORTABILITY PHASE)

**Axes combined:** V-03's future-team schema vocabulary (C-15 via phrasing register) +
V-02's Blind Spot Map with non-derivability constraint (C-16) + a PORTABILITY AUDIT
phase that includes vocabulary-specific failure patterns for the new field names.

**Hypothesis:** V-03's vocabulary-based approach to C-15 (field names that encode
future-team purpose) and V-02's Blind Spot Map (C-16) are the two mechanisms under
test. Adding a PORTABILITY AUDIT as a third mechanism serves a different function:
it tests whether the new field vocabulary ("What today's materials imply") is prone
to generic-content drift that the standard field names ("Expected") are not. When a
field is named "What today's materials imply," a writer may drift toward generic
material-critique language that is portable across topics ("Materials tend to
underspecify X") rather than specific inherited assumptions. The PORTABILITY AUDIT
explicitly lists failure patterns for the new field vocabulary, creating a post-draft
enforcement layer that V-03 alone does not have. V-04 does not have this because its
schema uses Archaeologist vocabulary and the Archaeologist filter step partially
serves the same function. V-05 tests the combination: vocabulary induction + Blind
Spot Map + explicit post-draft generic-content prevention.

---

### Prompt Body

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be a correction
the next team needs before they begin — something today's design materials do not
contain, and that a new team would carry as a false assumption without this artifact.

== SCHEMA =====================================================================

Apply to every correction. All fields required. No field may be blank or N/A.

  Name:            [A label the next team can cite without reading the full entry.
                   Encode the correction: "The Cascade Inversion" (what changed)
                   over "Unexpected Cascade Behavior" (something happened).
                   Not "Finding 1" or "Surprise A".]

  Source:          [namespace:skill:artifact — e.g., scout:feasibility:signal-
                   feasibility-2026-03-14.md. Not "signals indicated" / "research
                   showed" / "the data suggested".]

  What today's materials imply:
                   [What a new team reading only the current spec, proposal, and
                   design documents would assume. Write as: "Today's materials imply
                   that..." or "A new team reading the current spec would assume..."
                   Degree variants fail: "Materials imply X will be high; it was
                   moderate" records magnitude, not a reversed assumption. Name the
                   assumption the finding factually overturns.
                   Generic-material-critique language fails: "Materials tend to
                   underspecify concurrency behavior" is a category observation, not
                   a specific inherited assumption a specific new team would carry.]

  What the signals showed instead:
                   [The correction — directly contradicts what today's materials imply.
                   Direct claim. Prohibited: "may suggest" / "appears to indicate" /
                   "seems like" / "could mean" / "might be" / "it is possible that".]

  What the next team would build wrong:
                   [The specific design error a new team makes if they carry the
                   inherited assumption. Name the component, flow, or decision. One
                   sentence minimum. Prohibited: "worth noting" / "bears watching" /
                   "important to keep in mind". Name the specific wrong design.]

  What the next team must decide before proceeding:
                   [Specific question or action — not "further investigation needed" /
                   "keep an eye on this" / "monitor this". A specific blocking
                   decision or open question.]

  Severity:        [HIGH / MEDIUM / LOW]

== RULES ======================================================================

Rule 1 — Still-live filter:
  Before drafting any entry: "Does today's design material still imply the false
  assumption this finding corrects?" If the current materials have already absorbed
  this correction, exclude it. Apply as a discard filter.

Rule 2 — Claim-only voice:
  State every correction as a direct claim. No hedges. Apply prohibited constructs
  from "What the signals showed instead" to every field.

Rule 3 — Entry completeness:
  Write each entry so that a new team member reading only that entry can understand
  what today's materials lead them to assume, what they should assume instead, and
  what they would build wrong. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one entry must emerge from two or more signals. Source names both.
Name the convergence gap:
  "Neither [A] nor [B] alone revealed this — their intersection showed that today's
   materials still imply [X], which [A]+[B] together corrected."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all entries using the schema above. Order HIGH → MEDIUM → LOW by Severity.
Do not write the Blind Spot Map or later sections yet.

== PHASE 2: PORTABILITY AUDIT =================================================

Before writing the Blind Spot Map, execute this audit against every entry.

Portability test (apply to every non-Name field):
  "Could this exact text appear unchanged in an echo about a different topic?"
  If YES, rewrite it.

Named failure patterns — automatic rewrite triggers:

  Source field:
    "signals indicated" / "research showed" / "the data suggested" / "findings revealed"
    → Replace with: namespace:skill:artifact

  What today's materials imply:
    Generic-category language: "Materials tend to underspecify X" / "Specs rarely
    address Y" / "Teams typically assume Z" — these describe categories, not what
    today's specific materials imply to a new reader of this specific topic.
    → Replace with: the specific assumption a new engineer reading today's docs would hold.

  What the next team would build wrong:
    "this is worth noting" / "important to keep in mind" / "bears watching" /
    "has implications for design"
    → Replace with: the specific component, flow, or decision that would be wrong.

  What the next team must decide before proceeding:
    "further investigation needed" / "keep an eye on this" / "monitor this" /
    "investigate further"
    → Replace with: the specific decision or blocking open question.

Clear the PORTABILITY AUDIT for all entries before proceeding.

== PHASE 3: BLIND SPOT MAP ====================================================

After the portability audit: "Blind Spot Map."

A blind spot is a structural flaw in how the original design materials framed the
problem — a type of wrong thinking, not a topic area.

STEP 1 — NAME THE BLIND SPOT CATEGORIES.

Category names must characterize the *type* of wrong thinking:

  PASS: "Ownership inversion — materials assumed the caller owns X; signals showed
         the callee owns X, reversing the allocation model"
  PASS: "Actor scope underestimation — materials bounded the problem to internal
         consumers; signals showed external consumers are the primary failure surface"
  FAIL: "State management" — labels a domain
  FAIL: "Unexpected behavior" — labels that something happened, not what was wrong

A category label transferable to a different topic without rewriting fails.

STEP 2 — ASSIGN EACH CORRECTION TO EXACTLY ONE CATEGORY.

Unclassified entries require a one-sentence explanation.

STEP 3 — SYNTHESIS: "What the blind spot map reveals."

Write 2-3 sentences.

NON-DERIVABILITY CONSTRAINT: The synthesis must state something not visible from
reading individual entries or from reading the category assignments. Do not tally the
assignments ("Two corrections share an ownership-inversion blind spot"). State what the
*pattern of blind spots* reveals about the original materials as a whole — a systemic
claim about how the materials failed, not a count of who failed the same way.

If no pattern: "The corrections address independent blind spots; the map reveals no
shared structural origin in today's materials."

== PHASE 4: META-REFLECTION ===================================================

"What the surprise distribution reveals."

Where did corrections concentrate? Prescribe: "For topics like this one, run [X]
before [Y] to surface [Z class of correction] earlier." Prescribe — do not only observe.

== PHASE 5: SCOPE NEGATION ====================================================

"What this artifact excludes."
Name at least two excluded categories with counts:
  e.g., "Absorbed corrections: [N] findings the current materials already reflect"
       "Degree differences: [N] items where signals confirmed direction but adjusted
        magnitude, not the underlying assumption"
Implicit exclusion does not satisfy this.

== OUTPUT =====================================================================

Structure:
  1. Corrections — ordered HIGH → MEDIUM → LOW
  2. Blind Spot Map
  3. What the surprise distribution reveals
  4. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## Round 4 Design Notes

**Why these three axes:**

- **Role sequence** (V-01) targets C-15 by moving the Archaeologist's question from
  a framing section into the schema field definitions. The "Inherited assumption" field
  can only be answered by reasoning about what today's materials still imply to a new
  reader — not by recalling what the original team once believed. The structural
  enforcement operates at field-fill time.

- **Output format** (V-02) targets C-16 by introducing explicit category-naming
  requirements with pass/fail examples and a non-derivability constraint on the synthesis
  sentence. The FAIL examples are critical: without them, "State management issues"
  and similar topic labels satisfy the grouping requirement nominally while delivering
  no blind-spot insight.

- **Phrasing register** (V-03) tests whether C-15 can be achieved without naming a
  role — through schema field vocabulary alone. If V-03 and V-01 produce equivalent
  C-15 outcomes, the load-bearing component is the vocabulary (answerable only from
  future-team perspective), not the role identity. If they differ, the Archaeologist
  role orientation provides something beyond vocabulary.

**Predicted interaction in V-04:**

The Archaeologist schema embedding (V-01) and the Blind Spot Map (V-02) operate at
non-overlapping execution points. The schema fields fire during entry production; the
Blind Spot Map fires after all entries are drafted. The only possible interaction: do
Archaeologist-framed entries (written with "Inherited assumption" vocabulary) produce
better blind-spot category assignments than standard-framed entries? If yes, V-04 would
show better C-16 quality than V-02 alone, even though V-04's Blind Spot Map structure
is identical to V-02's.

**Predicted interaction in V-05:**

V-05 adds the PORTABILITY AUDIT to V-03 + V-02. The audit explicitly lists failure
patterns for the new field vocabulary ("Materials tend to underspecify X" as a generic
material-critique that fails). This tests whether vocabulary-based C-15 induction
(V-03) is more susceptible to generic drift than role-based C-15 induction (V-01), and
whether the PORTABILITY AUDIT's named failure patterns for the new vocabulary catch that
drift before the artifact is written to disk.
