---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 6
rubric: v6
---

# Variations: `topic:echo` — Round 6

**Rubric:** v6 | **Date:** 2026-03-15

---

## Design Context

R5 differentiating evidence: the initial R6 pass captured two precision patterns from R5
execution (C-21: multi-stage sequential gate with named stages; C-22: inline VALID/INVALID
contrast examples for the "We believed:" field). Three additional structural patterns from
R5 V-05 were observable but not formalized as criteria in that pass:

1. R5 V-05 introduced a pre-write impact triage step (Step 4) that assigned HIGH/MEDIUM/LOW
   comparatively across all SURPRISE candidates before writing any entry and ordered entries
   HIGH → MEDIUM → LOW. This was load-bearing in V-05 — it made the Rules of Thumb section
   auditable — but was treated as an implementation detail rather than a standalone criterion.
   An output that writes entries in discovery order, or without any stated triage, cannot be
   verified to have ordered by impact. A pre-write triage step is the only structural
   mechanism that enforces impact ordering without depending on the author's judgment at
   write time.

2. R5 V-03 and V-05 introduced "What the next team would get wrong" as the design impact
   field under the Institutional Archaeologist (IA) frame. Standard "Design impact" fields
   name what changes in the design direction; the IA variant names the specific mis-design
   the next team would make if they carried the false assumption. These are structurally
   distinct: "This affects the permission model" could mean anything; "The next team would
   build a stateless permission cache, not knowing permissions are session-scoped" names
   a concrete wrong decision with a retrievable cause. The IA frame was formalized as a
   named role (C-20), but the field-level change — from general consequence to specific
   mis-design — was not captured as a separate criterion.

3. R5 V-05's Rules of Thumb section had an "Anchoring constraint" (the impact tier in a
   rule must match the tier assigned to the surprise it encodes in Step 4) and a
   "Traceability check" (after writing all rules, verify end-to-end that each rule's tier
   matches the tier header of the surprise entry it names). LOW surprises were explicitly
   excluded from generating rules. This section closed the chain: signal → routed finding
   → staged gate verdict → triage rank → echo entry → impact-anchored rule. None of this
   was a rubric criterion — the Rules of Thumb section existed in V-05 but was not a
   requirement, and the anchoring constraint was a note within V-05, not an auditable
   structural rule.

These three precision gaps became C-23, C-24, and C-25 in the updated v6 rubric:

- **C-23**: When >=3 SURPRISE candidates pass the gate, a pre-write impact triage step
  must assign each a comparative impact level (HIGH, MEDIUM, or LOW) before any echo
  entry is written. The triage is comparative — levels are assigned by reading candidates
  against each other, not against an absolute scale. The output must reflect triage order
  (HIGH entries before MEDIUM, MEDIUM before LOW). An output where entries appear in
  signal-reading order rather than triage order fails C-23 even if individual impact
  statements are strong. The triage step is execution scaffolding — do not include in
  output — but its result must be visible in the entry ordering. C-23 is N/A if fewer
  than 3 SURPRISE candidates pass the gate.

- **C-24**: When C-20 (named Institutional Archaeologist role) is present and passing,
  the design impact field in every echo entry must be framed as the specific mis-design
  the next team would make if they carried the false assumption — not as a general
  consequence for the current design direction. The field must name a concrete wrong
  decision: a component the next team would mis-design, a flow they would mis-implement,
  or a call they would make incorrectly. "This affects the design" fails. "The next team
  would implement X without knowing Y" passes. The IA frame requires this framing because
  the audience of the echo is a future team arriving with no context — the correction must
  be actionable for someone who does not know what went wrong. C-24 is N/A if C-20 is
  absent, failing, or N/A.

- **C-25**: When C-23 (pre-write impact triage) is present and passing, the artifact must
  close with a Rules of Thumb section containing <=3 rules. Each rule encodes one HIGH or
  MEDIUM surprise in <=20 words in quotable form. Every rule carries an impact label
  (HIGH or MEDIUM) that must match the triage label assigned to the surprise it encodes.
  LOW surprises do not generate rules — they are informative but too peripheral to anchor
  institutional guidance. After writing all rules, an explicit traceability check must
  confirm that each rule's label matches the surprise entry it names; a mismatch makes
  that rule structurally incomplete. C-25 is N/A if C-23 is absent, failing, or N/A.

**R6 strategy (revised):**

- V-01: Single-axis targeting C-23 — adds a pre-write impact triage step to a gate-chain
  structure (C-11, C-12, C-13, C-15, C-16, C-18, C-19, C-21, C-22 present). The triage
  step runs after the gate, before writing, and constrains entry ordering in the output.
- V-02: Single-axis targeting C-24 — adds the mis-design field to the Institutional
  Archaeologist variation (C-17, C-20 present). Demonstrates the structural difference
  between "Design impact" (general consequence) and "What the next team would get wrong"
  (concrete mis-design the next team would make).
- V-03: Single-axis targeting C-25 — adds Rules of Thumb with anchoring constraint and
  traceability check. Builds on a structure that includes pre-write triage (C-23), so the
  anchoring constraint has a tier-source to check against.
- V-04: Combination targeting C-23 + C-24 + C-25 — pre-write triage before writing,
  mis-design field under IA frame, Rules of Thumb closing the chain. All three new
  criteria plus IA frame (C-17, C-20) and gate chain (C-11, C-12, C-13, C-15, C-16,
  C-18, C-19, C-21, C-22).
- V-05: Full combination — all 17 active criteria at structurally distinct moments.
  C-23 (pre-write triage), C-24 (mis-design field), C-25 (impact-anchored rules) join
  C-09 through C-22. The Institutional Archaeologist and the Gatekeeper remain distinct
  roles with distinct functions; each step identifies which role is active.

**What C-23 adds over R5 V-05 Step 4:**

R5 V-05's pre-write triage was a structural step in V-05's prompt but was not a rubric
criterion — it existed as an implementation of V-05's full-combination structure, not as
a requirement a variation could be evaluated against independently. C-23 makes the step
required when >=3 candidates pass the gate, specifies that the comparison is across
candidates (not against an absolute scale), and makes the output ordering the visible
artifact of the triage. An output that has rich individual impact statements but writes
entries in discovery order has not performed a pre-write triage — it has made impact
judgments at write time, which is harder to audit.

**What C-24 adds over C-20 (named IA role):**

C-20 required the Institutional Archaeologist to be a named role invoked at each sub-step.
The IA framing changed the perspective (what a new team would inherit from the current
materials) but did not constrain the field format of the impact statement. C-24 closes the
last degree of freedom: when C-20 is active, the impact field must name a concrete wrong
decision the next team would make — not a consequence for the current team's design.
"The next team would build the retry handler without knowing the queue preserves order" is
a different structural unit than "This affects the retry handler design." The first is
actionable for someone who was not present; the second requires reconstruction.

**What C-25 adds over R5 V-05 Step 8:**

R5 V-05's Rules of Thumb section appeared in the prompt body as a step, but was not a
rubric criterion. C-25 formalizes three things: (1) the section is required when C-23 is
passing, making the rules a structural close for the chain; (2) the anchoring constraint
(rule label must match triage label) is a named audit requirement, not a design note; (3)
the exclusion of LOW surprises from rules is a structural rule, not a guideline. These
three constraints together make the Rules of Thumb section independently auditable:
a future reader can verify that each rule traces to a named surprise entry and that its
impact label matches without access to the author's judgment.

---

## V-01 — Pre-Write Impact Triage axis

**Variation axis:** Lifecycle emphasis — a pre-write impact triage step runs after the
gate and before writing any entry, assigning each SURPRISE candidate a comparative
impact level (HIGH/MEDIUM/LOW) and ordering entries accordingly. Builds on the gate-chain
structure (C-11, C-12, C-13, C-15, C-16, C-18, C-19, C-21, C-22). Targets C-23.

**Hypothesis:** R5 V-04's gate-chain produced a cleaned and validated set of SURPRISE
candidates ready to write. The remaining gap: the write step had no pre-write constraint
on ordering. An author who writes entries in signal-reading order produces an echo whose
impact gradient is implicit rather than explicit — a reader cannot determine whether the
most impactful surprise appears first or third. C-23 closes this by requiring a comparative
triage before any entry is written. The triage is comparative (candidates ranked against
each other, not scored absolutely), the ordering is enforced by step sequencing (write
must receive the triage output before beginning), and the ordering is visible in the output
(HIGH entries appear before MEDIUM, MEDIUM before LOW). This gives a reader two things:
the ability to extract the most impactful surprises quickly, and confidence that the
author made triage decisions before rather than during writing.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not
expect? It is institutional memory for the next team that walks this path. Each entry is
a named surprise — sourced, contrasted with a named falsifiable prior belief, and assessed
for specific design impact. Entries appear in impact order: highest impact first.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted
an assumption.
*Test:* "Is this finding included because it overturned an assumption, or because it
happened and was notable?" If the latter → cut.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each was investigating.
Internal scaffolding — do not include in the output artifact.

---

**Step 2 — Pre-Write Prediction Sort (Routing Layer).**

This step runs before any candidates enter the gate. It is a routing layer: every finding
is assigned a typed destination.

For each noteworthy finding, record:

```
Finding: {one phrase}
Predicted? YES | NO
Route: {one named artifact type — required}
```

> "Before this investigation began — reading only the original design materials for
> `{topic}` — would we have predicted this finding?"

Valid route values:
- `topic-story` — YES finding; validation of what the design assumed
- `topic-report` — YES finding; process or method observation
- `gate-pipeline` — NO finding; proceeds to the gate

Invalid routes: "excluded from echo," blank, any disposal language. Every finding must
carry a named typed destination. Collect at least 3 `Route: gate-pipeline` findings.
Sort log is execution scaffolding — do not include in output.

---

**Step 3 — Multi-Stage Epistemic Gate.**

You are now the **Gatekeeper**. For each `gate-pipeline` candidate, run the three stages
below in sequence. Record each stage result before proceeding to the next stage.

**Stage 1 — Prediction Test** (novelty)
> "Would a reader of only the original design materials have predicted this finding?"

- YES → `Stage 1: CUT — finding-as-surprise substitution`. Stop.
- NO → `Stage 1: PASS`. Proceed to Stage 2.

**Stage 2 — Contradiction Test** (prior-belief falsification)
> "Does this finding oppose a specific belief the team held before the investigation —
> not just 'it was unusual,' but 'it contradicted something we thought was true'?"

- NO → `Stage 2: CUT — summary-in-disguise`. Stop.
- YES → complete "We believed {X}" where X is a testable proposition.

  VALID: "We believed the scheduler deduplicated events before dispatching callbacks."
  VALID: "We believed the compliance check ran at write time, not read time."
  These are propositions that could have been confirmed — signals showed otherwise.

  INVALID: "We hadn't thought through this edge case." Absence of consideration.
  INVALID: "This area felt uncertain." An impression, not a proposition.
  INVALID: "We were surprised." A reaction, not a falsifiable belief.

  A Stage 2 PASS with an invalid "We believed X" is structurally incomplete.
  → `Stage 2: PASS — We believed: {statement}`. Proceed to Stage 3.

**Stage 3 — Attribution Test** (verifiability)
> "Can this finding be traced to a specific named signal artifact or skill type?"

- NO → `Stage 3: CUT — orphan-attribution`. Stop.
- YES → `Stage 3: PASS — Source: {artifact name or skill type}`.
  Full SURPRISE verdict: candidate passes all three stages.

Valid final verdicts: `SURPRISE` (all three stages pass) or `CUT — {anti-pattern label}`.
Bare `CUT` without label is not valid. Minimum 2 SURPRISE verdicts required. Gate log is
execution scaffolding — do not include in output.

---

**Step 4 — Pre-Write Impact Triage.**

Receive the SURPRISE candidates from the Gatekeeper. Before writing any entry, assign each
a comparative impact level. Compare candidates against each other — not against an absolute
scale.

- **HIGH**: Forces a design decision to change or invalidates a major assumption. Design
  cannot proceed as planned without addressing this.
- **MEDIUM**: Requires adjustment to a specific component, flow, or decision. Design can
  proceed but must change.
- **LOW**: Informative; peripheral detail. Does not change the design trajectory.

Assign levels by comparing all candidates simultaneously. If all candidates feel "HIGH,"
you have not compared — re-read them against each other until at least one level differs.
Order the list: HIGH first, MEDIUM second, LOW last. Ties within a level: break by
specificity of impact.

This triage log is execution scaffolding — do not include in output — but the write step
in Step 5 must reflect the triage order.

---

**Step 5 — Write echo entries (in triage order).**

Write entries for SURPRISE candidates in the order established by Step 4: HIGH first,
MEDIUM second, LOW last.

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
*2-5 words, capitalized, distinct, reusable as a citation.*

- **Source signal**: The artifact or skill type from Stage 3 of the gate.
- **We believed**: The falsifiable prior belief from Stage 2. Expand to one full sentence.
  Preserve its falsifiable form — do not convert it to a hedge.
- **Finding**: What the signal revealed. Must directly contradict "We believed." One
  sentence.
- **Design impact**: The specific component, flow, or decision this changes, constrains,
  or challenges. Must name something specific. One sentence minimum.

Minimum 2 entries.

---

**Step 6 — Synthesize.**

Do the surprises cluster? Write 2-4 sentences: do 2+ share a root cause, reveal the same
blind spot, or together indicate a design direction not previously visible? Name any
pattern; state its absence if none is evident.

---

**Step 7 — Forward guidance.**

1-3 sentences for the next team building `{topic}`. Specific to these surprises.
Register: "If you are about to build X, know that Y because we found Z."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 5-7. Steps 1-4 are execution scaffolding.

---

## V-02 — Mis-Design Field axis

**Variation axis:** Output format — the design impact field is replaced by "What the next
team would get wrong," framing the consequence of the false assumption as the concrete
mis-design the next team would make. The Institutional Archaeologist (IA) holds this frame
throughout. Builds on R5 V-03 (C-17, C-20 present). Targets C-24.

**Hypothesis:** R5 V-03 introduced the Institutional Archaeologist as a named role (C-20)
invoked at each sub-step and specified the future-reader frame at each field (C-17). The
IA frame changed the perspective but left the design impact field structurally similar to
the standard "Design impact" field — a named component or decision the current team would
revisit. C-24 closes this gap: when the IA frame is active, the impact field must name a
concrete wrong decision the next team would make, not a general consequence. The difference
is in the audience: "This affects the permission model" targets the current team who knows
the context; "The next team would build a stateless permission cache without knowing
permissions are session-scoped" targets a future team who does not. The IA frame requires
the second form because the echo's audience is the team that does not yet exist — and a
general consequence statement requires context reconstruction that the echo is meant to
prevent. When C-24 is active, an output with "Design impact: this affects the permission
model" fails; "What the next team would get wrong: they would build X not knowing Y" passes.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

**Your role for this artifact: Institutional Archaeologist.**

An Institutional Archaeologist arrives at a body of work after the original team has
dispersed. You have only the current design materials for `{topic}` (spec, proposal,
drafts) and the signal artifacts the team produced. Your task: identify which false
assumptions the current materials still carry — the ones a new team reading those materials
would inherit and act on, incorrectly, without this artifact to correct them.

You hold this identity throughout. Where a step or field is prefixed with
**(Institutional Archaeologist:)**, your answer must come from that perspective: not the
original team's experience of running the signals, but the position of someone arriving
cold and asking — what would the next team get wrong?

---

**Step 1 — Read the signal record.**

Read all signal artifacts from `simulations/{topic}/` across all namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). For each artifact, note what it was
investigating and its key findings. This is your source material.

---

**Step 2 — Future-Reader Filter.**

For each notable finding, apply the Archaeologist test:

> **(Institutional Archaeologist:)** "If a new team read only the current design materials
> for `{topic}` and began building, would they carry a false assumption that this finding
> corrects? Is the false assumption still present in the current materials — not already
> corrected by a later revision, not obvious from context the next team would have?"

YES → candidate for the echo. The false assumption persists.
NO → even if the finding surprised the original team, route it to `topic-story`.

Note: this test is stricter than "was it surprising?" A finding that updated the current
materials does not qualify — the echo corrects assumptions the materials *still* carry.

Collect at least 2 YES candidates. Filter log is internal scaffolding.

---

**Step 3 — Write echo entries.**

For each candidate (minimum 2), produce one entry. The Institutional Archaeologist holds
the perspective at every field:

**[Surprise Name]**
**(Institutional Archaeologist:)** Encode the correction the next team needs, not the
discovery the original team made. "The Cascade Inversion" — what the next team must correct
for — passes; "Unexpected Cascade Behavior" — what the original team experienced — does not.
A name passes if a future reader can cite it without having been present.

- **Source signal**: The specific artifact or skill type a future team can locate
  independently (e.g., `flow-resilience`, `prove-interview`, `scout-feasibility`).
- **The assumption the next team carries**: **(Institutional Archaeologist:)** What a new
  team reading the current materials would assume. State it as their belief, not the
  original team's history: "A team building `{topic}` today would assume..." or "The
  current spec implies..." Do not restate assumptions already corrected in the materials.
- **The correction**: What the signal showed instead. Must directly contradict the
  assumption as stated. One sentence.
- **What the next team would get wrong**: **(Institutional Archaeologist:)** Name the
  specific wrong decision the next team would make if they carried the false assumption.
  Format: "The next team would [build/implement/decide] X, [not knowing / without
  accounting for] Y." A named wrong decision — not a general consequence, not "this would
  cause problems." One sentence.

---

**Step 4 — Cross-materials synthesis.**

**(Institutional Archaeologist:)** Look across the entries: do two or more corrections
address the same category of misunderstanding — the same structural flaw in how the current
materials frame the problem? Write 2-4 sentences. You are looking for a pattern in how the
materials mislead future teams, not the original team's discovery sequence. Name any such
pattern; state its absence if none is evident.

---

**Step 5 — Handover guidance.**

**(Institutional Archaeologist:)** Write 1-3 sentences as if handing this artifact to the
next team at the start of their investigation. Register: "The current materials will lead
you to assume X — they are wrong about this because..." or "Before you commit to Y,
read `{source signal}` because the spec does not warn you that..." Specific to these
corrections.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 3-5. Steps 1-2 are execution scaffolding.

---

## V-03 — Impact-Anchored Rules of Thumb axis

**Variation axis:** Output format — the artifact closes with a Rules of Thumb section
containing <=3 impact-anchored, quotable rules. Each rule encodes one HIGH or MEDIUM
surprise; its impact label must match the surprise entry's triage label. LOW surprises
do not generate rules. An explicit traceability check closes the chain. Builds on V-01's
structure (C-23 present, so triage labels exist to anchor against). Targets C-25.

**Hypothesis:** V-01's pre-write impact triage produced a ranked set of echo entries.
The ranking was visible in entry ordering but was not captured in a retrievable,
quotable form. Rules of Thumb close this gap: they encode the highest-impact surprises
in <=20 words each, making them citable in design conversations without requiring a reader
to re-read the full echo. The anchoring constraint (rule's impact label must match the
surprise entry's triage label) prevents two failure modes: (1) a rule annotated HIGH that
encodes a MEDIUM surprise overclaims impact; (2) a rule without a label provides no
priority signal to the next team. The traceability check makes the chain independently
auditable: signal artifact → routed finding → gate verdict → triage rank → echo entry →
impact-anchored rule. A future reader can verify each link without access to the author's
session.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not
expect? It is institutional memory for the next team that walks this path. Each entry is
a named surprise — sourced, contrasted with a falsifiable prior belief, and assessed for
specific design impact. Entries appear in impact order. The echo closes with Rules of
Thumb that encode the most important surprises in quotable form.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted
an assumption.
*Test:* "Is this finding included because it overturned an assumption, or because it
happened?" If the latter → cut.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each was investigating.
Internal scaffolding.

---

**Step 2 — Pre-Write Prediction Sort (Routing Layer).**

For each noteworthy finding:

```
Finding: {one phrase}
Predicted? YES | NO
Route: {topic-story | topic-report | gate-pipeline}
```

> "Before this investigation began — reading only the original design materials —
> would we have predicted this finding?"

Invalid routes: "excluded from echo," blank, disposal language. Every finding needs a
named destination. Collect at least 3 `Route: gate-pipeline` findings. Sort log is
execution scaffolding.

---

**Step 3 — Multi-Stage Epistemic Gate.**

You are the **Gatekeeper**. For each `gate-pipeline` candidate, run stages in sequence:

**Stage 1 — Prediction Test** (novelty)
- YES → `Stage 1: CUT — finding-as-surprise substitution`. Stop.
- NO → `Stage 1: PASS`. Proceed to Stage 2.

**Stage 2 — Contradiction Test** (prior-belief falsification)
- NO → `Stage 2: CUT — summary-in-disguise`. Stop.
- YES → complete "We believed {X}" (testable proposition):

  VALID: "We believed the event bus deduplicated retries before delivery."
  VALID: "We believed the fallback path was exercised in staging, not just prod."
  INVALID: "We weren't sure about this area." Uncertainty is not a prior belief.
  INVALID: "We hadn't thought through this." Absence of consideration.

  → `Stage 2: PASS — We believed: {statement}`. Proceed to Stage 3.

**Stage 3 — Attribution Test** (verifiability)
- NO → `Stage 3: CUT — orphan-attribution`. Stop.
- YES → `Stage 3: PASS — Source: {artifact name or skill type}`.

Minimum 2 SURPRISE verdicts required. Gate log is execution scaffolding.

---

**Step 4 — Pre-Write Impact Triage.**

Before writing any entry, assign each SURPRISE candidate a comparative impact level:

- **HIGH**: Forces a design decision to change or invalidates a major assumption.
- **MEDIUM**: Requires adjustment to a specific component, flow, or decision.
- **LOW**: Informative; peripheral. Does not change the design trajectory.

Compare candidates against each other. If all feel "HIGH," you have not compared —
re-read until at least one level differs. Order: HIGH → MEDIUM → LOW.
Triage log is execution scaffolding, but entry ordering in Step 5 must reflect it.

---

**Step 5 — Write echo entries (in triage order).**

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`

- **Source signal**: Specific artifact or skill type.
- **We believed**: The falsifiable prior belief from Stage 2. Full sentence.
- **Finding**: What the signal revealed. Directly contradicts "We believed." One sentence.
- **Design impact**: Specific component, flow, or decision this changes. One sentence.

Minimum 2 entries.

---

**Step 6 — Synthesize.**

Write 2-4 sentences: do 2+ surprises share a root cause or reveal the same blind spot?
Name any pattern; state its absence if none is evident.

---

**Step 7 — Forward guidance.**

1-3 sentences for the next team. Register: "If you are about to build X, know that Y."

---

**Step 8 — Rules of Thumb (impact-anchored).**

Write <=3 rules encoding the most important surprises in quotable form:

```
[{HIGH | MEDIUM}] {Rule text — <=20 words, names a specific behavior or constraint}
(encodes: {Surprise Name from Step 5})
```

**Anchoring constraint**: The impact tier in the rule must match the tier in the surprise
entry header it names. A rule labeled `[HIGH]` that encodes a `MEDIUM` surprise is
malformed — revise the tier or re-examine the triage.

**Scope**: Only HIGH and MEDIUM surprises generate rules. LOW surprises are informative
but too peripheral to anchor institutional guidance.

**Traceability check**: After writing all rules, verify end-to-end: does each rule's
tier match the tier header of the named surprise entry? Yes on all rules closes the chain:
source signal → routed finding → staged gate verdict → triage rank → echo entry →
impact-anchored rule. Each link is independently auditable by a future reader.

Label the section **"Rules of Thumb"**.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 5-8. Steps 1-4 are execution scaffolding.

---

## V-04 — Combination: Pre-Write Triage + Mis-Design Field + Rules of Thumb (C-23+C-24+C-25)

**Variation axis:** Lifecycle emphasis + output format — the Institutional Archaeologist
holds the future-reader frame throughout; pre-write triage (C-23) orders candidates before
writing; the design impact field is framed as a concrete mis-design (C-24); Rules of Thumb
close the chain with impact-anchored quotable rules (C-25). Also includes gate chain
(C-11, C-12, C-13, C-15, C-16, C-18, C-19, C-21, C-22) and IA frame (C-17, C-20).

**Hypothesis:** V-01 closed C-23 by adding triage before the write step; V-02 closed C-24
by replacing the generic impact field with a concrete mis-design frame; V-03 closed C-25
by closing the chain with impact-anchored Rules of Thumb. None of these three criteria is
independent: C-24 requires C-20 (IA frame) to be present; C-25 requires C-23 (triage labels
exist to anchor against); C-23 benefits from the full gate chain (typed-routed, staged gate,
VALID/INVALID contrast examples) to produce reliably distinct SURPRISE candidates that can
be compared. This combination closes all three simultaneously. The interaction between C-23
and C-25 is the most important: when the triage assigns tiers comparatively and the rules
encode only HIGH and MEDIUM surprises, the rules section becomes a verified extract of the
triage — the traceability check can confirm that no rule overclaims impact and no HIGH
surprise was omitted from the rules without justification.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**Your operating role: Institutional Archaeologist.**

An Institutional Archaeologist recovers false assumptions from a body of work — specifically
the ones the current design materials still carry, that a new team would inherit and act on
incorrectly without this artifact. You hold this identity throughout. Where a step or field
is prefixed with **(Institutional Archaeologist:)**, your answer must come from that
perspective: what would a new team reading the current materials get wrong?

The Institutional Archaeologist is distinct from the Gatekeeper role in Step 3. The
Gatekeeper tests whether a finding qualifies as a surprise; the Institutional Archaeologist
frames what that surprise means for a reader who was not present.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted
an assumption.
*Test:* "Is this finding included because it overturned an assumption, or because it
happened?" If the latter → cut.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**What the echo is.** It answers one question: what did we learn that we did not expect?
Each entry is a named surprise — sourced, contrasted with a named falsifiable prior belief,
and framed as the concrete wrong decision the next team would make. Entries appear in
impact order. The echo closes with Rules of Thumb encoding the highest-impact surprises.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Internal scaffolding.

---

**Step 2 — Pre-Write Prediction Sort (Routing Layer).**

Every finding is assigned a typed destination before any candidate enters the gate.

```
Finding: {one phrase}
Predicted? YES | NO
Route: {one named artifact type — required}
```

> **(Institutional Archaeologist:)** "Before this investigation began — reading only the
> original design materials for `{topic}` — would a new team building `{topic}` today have
> predicted this finding? Does the current spec already account for it?"

Valid route values:
- `topic-story` — YES finding; confirmation of what the design assumed
- `topic-report` — YES finding; process or method observation
- `gate-pipeline` — NO finding; proceeds to the gate

Invalid routes: "excluded from echo," blank, disposal language. Every finding must carry
a named typed destination. Collect at least 3 `Route: gate-pipeline` findings. Sort log
is execution scaffolding.

---

**Step 3 — Multi-Stage Epistemic Gate.**

You are now the **Gatekeeper** (not the Institutional Archaeologist). Apply the Anti-Pattern
Catalog to each `gate-pipeline` candidate. Run three stages in sequence:

**Stage 1 — Prediction Test** (novelty)
- YES → `Stage 1: CUT — finding-as-surprise substitution`. Stop.
- NO → `Stage 1: PASS`. Proceed to Stage 2.

**Stage 2 — Contradiction Test** (prior-belief falsification)
- NO → `Stage 2: CUT — summary-in-disguise`. Stop.
- YES → complete "We believed {X}":

  VALID: "We believed the scheduler preserved event order across reconnects."
  VALID: "We believed the compliance check ran at write time, not read time."
  These could have been confirmed — the signals showed they were wrong instead.

  INVALID: "We hadn't thought through this." Absence of consideration.
  INVALID: "This area felt uncertain." An impression, not a proposition.
  INVALID: "We were surprised." A reaction, not a falsifiable belief.

  A Stage 2 PASS with an invalid "We believed X" is structurally incomplete.
  → `Stage 2: PASS — We believed: {statement}`. Proceed to Stage 3.

**Stage 3 — Attribution Test** (verifiability)
- NO → `Stage 3: CUT — orphan-attribution`. Stop.
- YES → `Stage 3: PASS — Source: {artifact name or skill type}`.

Minimum 2 SURPRISE verdicts. Gate log is execution scaffolding.

---

**Step 4 — Pre-Write Impact Triage.**

Receive the SURPRISE candidates. Before writing any entry, assign each a comparative
impact level. Compare candidates against each other:

- **HIGH**: Forces a design decision to change or invalidates a major assumption.
- **MEDIUM**: Requires adjustment to a specific component, flow, or decision.
- **LOW**: Informative; peripheral. Does not change the design trajectory.

Compare all candidates simultaneously. At least one level must differ from the others.
Order: HIGH → MEDIUM → LOW. Write step must reflect this order.

Triage log is execution scaffolding — do not include in output.

---

**Step 5 — Write echo entries (highest impact first).**

For each SURPRISE candidate in triage order:

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
**(Institutional Archaeologist:)** Encode the correction the next team needs, not the
discovery the original team made. A name passes if a future reader can cite it without
having been present.

- **Source signal**: Specific artifact or skill type.
- **We believed**: The falsifiable prior belief from Stage 2. Full sentence. Preserve its
  falsifiable form.
- **The correction**: What the signal showed instead. Directly contradicts "We believed."
  One sentence.
- **What the next team would get wrong**: **(Institutional Archaeologist:)** Name the
  specific wrong decision the next team would make if they carried the false assumption.
  Format: "The next team would [build/implement/decide] X, [not knowing / without
  accounting for] Y." Must name a concrete wrong decision — not a general consequence,
  not "this would cause problems." One sentence.

---

**Step 6 — Synthesis.**

**(Institutional Archaeologist:)** Look across the entries: do two or more corrections
address the same category of misunderstanding — the same structural flaw in how the current
materials frame the problem? Write 2-4 sentences. Name any pattern; state its absence if
none is evident.

---

**Step 7 — Handover guidance.**

**(Institutional Archaeologist:)** Write 1-3 sentences as if handing this artifact to the
next team at the start of their investigation. Register: "The current materials will lead
you to assume X — they are wrong about this because..." or "Before you commit to Y, read
`{source signal}` because the spec does not warn you that..."

---

**Step 8 — Rules of Thumb (impact-anchored).**

Write <=3 rules encoding the most important surprises in quotable form:

```
[{HIGH | MEDIUM}] {Rule text — <=20 words, names a specific behavior or constraint}
(encodes: {Surprise Name from Step 5})
```

**Anchoring constraint**: The impact tier in the rule must match the tier in the surprise
entry header it names. A `[HIGH]` rule encoding a `MEDIUM` surprise is malformed.

**Scope**: Only HIGH and MEDIUM surprises generate rules. LOW surprises do not anchor rules.

**Traceability check**: After writing all rules, verify end-to-end: does each rule's tier
match the tier header of the surprise entry it names? A yes on all rules closes the chain:
source signal → routed finding → staged gate verdict → triage rank → echo entry →
impact-anchored rule.

Label the section **"Rules of Thumb"**.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 5-8. Steps 1-4 are execution scaffolding.

---

## V-05 — Full Combination: All 17 Active Criteria

**Variation axis:** All 17 active aspirational criteria at structurally distinct moments —
C-23 (pre-write impact triage), C-24 (mis-design field under IA frame), C-25 (impact-
anchored Rules of Thumb with traceability check) added to the C-21/C-22 structure from
the initial R6 pass, and the full R5 V-05 base (C-09 through C-20).

**Hypothesis:** The initial R6 V-05 closed all 14 active criteria (C-09..C-22). Three
structural gaps remained: (1) triage existed in V-05 as a step but was not a standalone
criterion — C-23 formalizes it as a comparative pre-write requirement with output-order
consequences; (2) the design impact field used "What the next team would get wrong" in
V-05's IA fields but was not distinguished from "Design impact" at the criterion level —
C-24 makes this distinction explicit and auditable; (3) the Rules of Thumb section in V-05
carried an anchoring constraint and traceability check as guidance notes, not enforced
structural requirements — C-25 makes these requirements, with the traceability check as
a closing audit step. With all three gaps closed, the 17-criterion chain is structurally
unambiguous at every junction: every finding is typed-routed (C-16, C-19); the gate runs
three named sequential stages (C-21) with contrast examples in Stage 2 (C-22); SURPRISE
verdicts carry falsifiable prior beliefs (C-18); candidates are triaged before writing
(C-23); entries are written in triage order with mis-design fields (C-24); the echo closes
with impact-anchored rules and a traceability check (C-25). The Institutional Archaeologist
holds the future-reader frame (C-17, C-20); the Gatekeeper runs the adversarial tests
(C-11, C-12, C-13, C-14, C-15); the two roles remain distinct.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**Your operating role: Institutional Archaeologist.**

An Institutional Archaeologist recovers false assumptions from a body of work — specifically
the ones the current design materials still carry, that a new team would inherit and act on
incorrectly without this artifact. You hold this identity throughout. Where a step or field
is prefixed with **(Institutional Archaeologist:)**, your answer must come from that
perspective: not the original team's experience, but the position of someone arriving cold
asking — what would the next team get wrong?

The Institutional Archaeologist is distinct from the Gatekeeper role in Step 3. The
Gatekeeper tests whether a finding qualifies as a surprise. The Institutional Archaeologist
frames what that surprise means for a reader who was not present.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted
an assumption.
*Test:* "Could this output be described as a summary of what the investigation found?"
Yes → you have at least one of these.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**What the echo is.** It answers one question: what did we learn that we did not expect?
Each entry is a named surprise — sourced, contrasted with a named falsifiable prior belief,
ranked by design impact, and framed as the concrete wrong decision the next team would make.
Entries appear in impact order. The echo closes with impact-annotated Rules of Thumb
encoding the highest-impact surprises in quotable form. Its audience is the next team that
walks this path.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each was investigating.
Internal scaffolding.

---

**Step 2 — Pre-Write Prediction Sort (Routing Layer).**

This step runs before any candidates enter the gate. Every finding is assigned a typed
destination.

```
Finding: {one phrase}
Predicted? YES | NO
Route: {one named artifact type — required}
```

> **(Institutional Archaeologist:)** "Before this investigation began — reading only the
> original design materials for `{topic}` — would a new team building `{topic}` today have
> predicted this finding? Does the current spec already account for it?"

Route assignment:
- YES → `Route: topic-story`
- YES (process/method finding) → `Route: topic-report`
- NO → `Route: gate-pipeline`

Invalid routes: "excluded from echo," blank, any disposal language. Every finding must
carry a named typed destination. Collect at least 3 `Route: gate-pipeline` findings.
Sort log is execution scaffolding.

---

**Step 3 — Multi-Stage Epistemic Gate.**

You are now the **Gatekeeper** (not the Institutional Archaeologist — the Gatekeeper's
function is adversarial rejection, not future-reader framing). Apply the Anti-Pattern
Catalog to each `gate-pipeline` candidate. Run three stages in sequence:

**Stage 1 — Prediction Test** (novelty)
> "Would a reader of only the original design materials have predicted this finding?"

- YES → `Stage 1: CUT — finding-as-surprise substitution`. Stop.
- NO → `Stage 1: PASS`. Proceed to Stage 2.

**Stage 2 — Contradiction Test** (prior-belief falsification)
> "Does this finding oppose a specific belief the team held before the investigation —
> not 'it was unusual,' but 'it contradicted something we thought was true'?"

- NO → `Stage 2: CUT — summary-in-disguise`. Stop.
- YES → complete "We believed {X}" where X is a testable proposition:

  VALID: "We believed the scheduler preserved event order across reconnects."
  VALID: "We believed the compliance check ran at write time, not read time."
  These are propositions that could have been confirmed — the signals showed otherwise.

  INVALID: "We hadn't thought through this." Absence of consideration.
  INVALID: "This area felt uncertain." An impression, not a proposition.
  INVALID: "We were surprised by this." A reaction, not a falsifiable belief.

  A Stage 2 PASS with an invalid "We believed X" is structurally incomplete.
  → `Stage 2: PASS — We believed: {statement}`. Proceed to Stage 3.

**Stage 3 — Attribution Test** (verifiability)
> "Can this finding be traced to a specific named signal artifact or skill type?"

- NO → `Stage 3: CUT — orphan-attribution`. Stop.
- YES → `Stage 3: PASS — Source: {artifact name or skill type}`.
  Full SURPRISE verdict: all three stages pass.

Minimum 2 SURPRISE verdicts. Gate log is execution scaffolding.

---

**Step 4 — Pre-Write Impact Triage.**

Receive the SURPRISE candidates. Before writing any entry, assign each a comparative
impact level. Compare candidates against each other — not against an absolute scale.

- **HIGH**: Forces a design decision to change or invalidates a major assumption. Design
  cannot proceed as planned without addressing this.
- **MEDIUM**: Requires adjustment to a specific component, flow, or decision. Design can
  proceed but must change.
- **LOW**: Informative; peripheral detail. Does not change the design trajectory.

Compare all candidates simultaneously. At least one level must differ. If all candidates
feel HIGH, you have not compared — re-read them against each other. Order the list:
HIGH → MEDIUM → LOW. Ties within a level: break by specificity of impact.

Triage log is execution scaffolding — do not include in output — but Step 5 must reflect
triage order.

---

**Step 5 — Write echo entries (highest impact first).**

For each SURPRISE candidate in triage order:

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
**(Institutional Archaeologist:)** Encode the correction the next team needs, not the
discovery the original team made. "The Cascade Inversion" — what the next team must
correct for — passes; "Unexpected Cascade Behavior" — what the original team experienced
— does not. A name passes if a future reader can cite it without having been present.

- **Source signal**: Specific artifact or skill type (e.g., `flow-resilience`,
  `prove-interview`, `scout-feasibility`). Must pass the orphan-attribution test.
- **We believed**: The falsifiable prior belief from Stage 2 of the gate. Full sentence.
  Preserve its falsifiable form — do not convert to a hedge.
- **The correction**: What the signal showed instead. Directly contradicts "We believed."
  One sentence.
- **What the next team would get wrong**: **(Institutional Archaeologist:)** The specific
  wrong decision the next team would make if they carried the false assumption. Format:
  "The next team would [build/implement/decide] X, [not knowing / without accounting for]
  Y." Must name a concrete wrong decision — not "this would cause problems," not a general
  consequence. One sentence.

---

**Step 6 — Synthesis.**

**(Institutional Archaeologist:)** Look across the entries: do two or more corrections
address the same category of misunderstanding — the same structural flaw in how the current
materials frame the problem? Write 2-4 sentences. You are looking for a pattern in how the
materials mislead future teams, not the original team's discovery sequence. Name any
pattern; state its absence if none is evident — absence is itself information for the
next team.

---

**Step 7 — Handover guidance.**

**(Institutional Archaeologist:)** Write 1-3 sentences as if handing this artifact to the
next team at the start of their investigation. Register: "The current materials will lead
you to assume X — they are wrong about this because..." or "Before you commit to Y, read
`{source signal}` because the spec does not warn you that..." Specific to these corrections.

---

**Step 8 — Rules of Thumb (impact-anchored).**

Write <=3 rules encoding the most important surprises in quotable form:

```
[{HIGH | MEDIUM}] {Rule text — <=20 words, names a specific behavior or constraint}
(encodes: {Surprise Name from Step 5})
```

**Anchoring constraint**: The impact tier in the rule must match the tier in the surprise
entry header it names in Step 5. A rule labeled `[HIGH]` that encodes a `MEDIUM` surprise
is a malformed entry — revise the tier or re-examine the triage.

**Scope**: Only HIGH and MEDIUM surprises generate rules. LOW surprises are informative
but too peripheral to anchor institutional guidance.

**Traceability check**: After writing all rules, verify end-to-end: does each rule's tier
match the tier header of the surprise entry it names? A yes on all rules closes the full
chain: source signal → typed-route prediction sort → staged gate verdict (with falsifiable
"We believed:" field) → comparative triage rank → echo entry (with mis-design field) →
impact-anchored rule (with matching tier). The Institutional Archaeologist can confirm:
each link is independently auditable by a future reader arriving with no context.

Label the section **"Rules of Thumb"**.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 5-8. Steps 1-4 are execution scaffolding.
