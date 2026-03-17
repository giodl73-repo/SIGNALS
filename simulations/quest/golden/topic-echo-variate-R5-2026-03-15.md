---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 5
rubric: v5
---

# Variations: `topic:echo` — Round 5

**Rubric:** v5 | **Date:** 2026-03-15

---

## Design Context

R4 differentiating evidence: V-01's Epistemic basis field required a named prior belief on
every SURPRISE verdict — but the field was still satisfied by impressions ("we hadn't fully
considered this") rather than falsifiable propositions ("we believed X"). V-02's per-finding
`Predicted? YES/NO` + `Route:` template directed YES findings to a named artifact, but the
Route: label was implied by general instruction ("belongs in topic-story") rather than being
a typed field per finding. V-03's Institutional Archaeologist role held the future-reader
frame throughout — but the role appeared as a framing device in the introduction, not as a
named identity invoked step-by-step.

These three precision gaps became C-18, C-19, and C-20 in v5:

- **C-18**: When C-15 is present and passing, every SURPRISE verdict must carry a
  *falsifiable* named-prior-belief field — "We believed X" where X is a testable proposition
  that could have been wrong, not an impression or an absence of consideration. R4 V-01's
  Epistemic basis field required a belief; C-18 requires that belief to be auditable: a
  future reader must be able to evaluate whether the belief was reasonable and whether it
  has since been reinstated. The field must complete "We believed {X}" as a sentence with
  a real predicate, not a hedge. "We believed the scheduler preserved event order across
  reconnects" passes. "We hadn't thought through reconnect behavior" does not.

- **C-19**: When C-16 is present and passing, every finding in the Pre-Write Prediction Sort
  must carry a `Route:` label naming a specific destination artifact type — not merely
  YES/NO or a general instruction to "exclude." R4 V-02 established the gate as a distinct
  structural step (C-16); C-19 requires that step to be a routing layer: each finding is
  dispatched to a named home, not discarded. "Route: topic-story" and "Route: gate-pipeline"
  are typed destinations; "excluded from echo" or a blank field are not. This converts the
  sort from a binary filter into a dispatch table — confirmed findings are preserved and
  directed, not dropped.

- **C-20**: When C-17 is present and passing, the future-reader frame must be held by a
  *named role* invoked at each sub-step — not by per-step instructions alone. R4 V-03
  required the frame in >=3 sub-steps by embedding explicit future-reader instructions at
  each field. C-20 requires those instructions to carry a named role identity: "Institutional
  Archaeologist:" before each sub-step instruction makes the frame auditable by role, not
  just by content. A model can satisfy a per-step instruction while drifting from its spirit;
  a named role is harder to drift from because each sub-step can be checked: is this answer
  "in role"? The role must also be distinct from the adversarial Gatekeeper when both are
  present — each serves a different epistemic function.

**R5 strategy:**

- V-01: Single-axis targeting C-18 — promotes the SURPRISE verdict's Epistemic basis to a
  first-class "We believed:" field with explicit falsifiability constraints. Builds on R4 V-01
  (which established C-11, C-12, C-13, C-15). The field must be independently auditable:
  a reader can check whether the stated belief was reasonable and whether subsequent updates
  have reinstated it.
- V-02: Single-axis targeting C-19 — promotes the Pre-Write Prediction Sort's route
  designation from an implied instruction to a mandatory typed label per finding. Builds on
  R4 V-02 (which established C-16). "Excluded from echo" and blank routes are explicitly
  invalid — every finding must name a destination artifact type.
- V-03: Single-axis targeting C-20 — instantiates the Institutional Archaeologist as a
  named role at the prompt header and invokes it by name at each sub-step (filter, naming,
  impact, synthesis). Builds on R4 V-03 (which established C-17). The role name creates
  an audit hook: each sub-step can be verified as "in role" independently.
- V-04: Combination targeting C-18 + C-19 — the complete upstream routing + typed-gate
  chain: prediction sort with per-finding Route: labels, adversarial gate with SURPRISE
  requiring falsifiable "We believed X," full anti-pattern catalog on cuts. Closes the two
  format precision gaps simultaneously.
- V-05: Full combination — all 12 active aspirational criteria at structurally distinct
  moments, adding C-18 (falsifiable prior belief field), C-19 (typed routing labels), and
  C-20 (named Institutional Archaeologist role threaded through all sub-steps) to the R4
  V-05 structure.

**What C-18 adds over R4 V-01:**

R4 V-01's Epistemic basis field made the pass verdict load-bearing: `SURPRISE` required
naming the prior belief contradicted rather than just clearing the anti-pattern tests. But
"Epistemic basis: we hadn't anticipated this class of failure" is a sentiment — it names
an area of uncertainty, not a proposition that could have been right or wrong. C-18 closes
this residual gap: the field must be falsifiable. A belief is falsifiable if it could have
been confirmed (signals might have shown it was correct) and was instead contradicted.
"We believed the migration endpoint was stateless" could have been confirmed; it names
something the team staked on. A field that cannot fail this test is not a prior belief —
it is a description of the team's epistemic state, which belongs in team notes, not in
institutional memory.

**What C-19 adds over R4 V-02:**

R4 V-02's sort step produced a clean input to the gate pipeline by routing confirmations to
`topic-story` via a general instruction. The `Route:` label appeared in the template but its
value was driven by the YES/NO outcome — YES findings were implicitly routed, the label was
illustrative. C-19 makes the label mandatory and typed per finding: the author must name the
destination explicitly, and "excluded from echo" or a blank field is structurally invalid.
This has an effect beyond format compliance: when every finding has a named destination, the
author must decide where each confirmation belongs rather than treating confirmation as
synonymous with discard. A confirmation might belong in `topic-report` rather than
`topic-story`. The routing decision is a classification act, not a disposal act.

---

## V-01 — Named Prior Belief Field axis

**Variation axis:** Output format — the SURPRISE verdict's Epistemic basis field is promoted
to a dedicated "We believed:" named prior belief field with explicit falsifiability
constraints. Builds on R4 V-01 (C-11 + C-12 + C-13 + C-15 present). Targets C-18.

**Hypothesis:** R4 V-01 made `SURPRISE` an affirmative epistemic claim (C-15) and required
the Epistemic basis to name the prior belief contradicted. The remaining gap: the field could
be satisfied by impressions or absences of consideration — sentiments with the shape of
beliefs. C-18 closes this by requiring the field to complete "We believed {X}" where X is
a proposition that could have been confirmed. When the template forces the author to
articulate a testable prior belief, two things follow: (1) the surprise is independently
verifiable — a future reader can check whether the belief was reasonable and whether it has
been reinstated; (2) vague surprises become structurally unproducible — you cannot pass C-18
with "we were uncertain about this area" because that is not a belief that could have been
right. Both sides of the gate are now falsifiable: the cut side names the anti-pattern
triggered, the pass side names the belief contradicted.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not
expect? It is institutional memory for the next team that walks this path. Each entry is
a named surprise — sourced, contrasted with a named falsifiable prior belief, and assessed
for specific design impact.

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

**Step 2 — Assemble raw candidates.**

Scan the signals for findings that are notable, non-trivial, or worth preserving. Write
a one-sentence description for each. Do not filter yet. Collect at least 4 candidates.

---

**Step 3 — Epistemic Gate.**

You are now the **Gatekeeper**. For each candidate, issue a verdict in this exact template:

```
Candidate: {one-sentence description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: {complete this sentence with the falsifiable prior belief this candidate
  contradicts. Format: "We believed {X}" where X is a testable proposition that could
  have been right.

  VALID — a falsifiable proposition: "We believed the migration endpoint preserved session
  tokens across reconnects."
  VALID — a falsifiable proposition: "We believed power users would resist the new flow
  because adoption friction was high in previous rollouts."

  INVALID — absence of consideration: "We hadn't thought through reconnect behavior."
  Absence of thought is not a belief that could have been right or wrong.
  INVALID — impression: "This area felt uncertain." Impressions are not propositions.
  INVALID — vague hedge: "We weren't sure about this." Uncertainty is not a prior belief.

  A SURPRISE verdict with an invalid "We believed:" field is structurally incomplete.
  If you cannot state a falsifiable prior belief for a candidate, it does not qualify —
  re-examine or cut.}
Destination: [SURPRISE → echo] [CUT → topic-story, not topic-echo]
```

Verdict state definitions:

- `SURPRISE` — an affirmative epistemic claim: this candidate contradicted a specific
  falsifiable prior belief and passes all three anti-pattern tests. The "We believed:" field
  must name a testable proposition — something the team staked on that the signals showed
  was wrong. A `SURPRISE` verdict is not a clearance; it is an assertion that requires a
  verifiable belief as evidence.
- `CUT — finding-as-surprise substitution`
- `CUT — summary-in-disguise`
- `CUT — orphan-attribution`

A bare `CUT` without an anti-pattern label is not valid. Combined labels valid when multiple
anti-patterns apply. Minimum 2 SURPRISE verdicts required. Gatekeeper log is execution
scaffolding — do not include in output.

---

**Step 4 — Write echo entries.**

Receive the SURPRISE candidates from the Gatekeeper. For each, produce one entry:

**[Surprise Name]**
*2-5 words, capitalized, distinct, reusable as a citation in conversation.*

- **Source signal**: Specific artifact name or skill type (e.g., `flow-resilience`,
  `prove-interview`, `scout-feasibility`). Must pass the orphan-attribution test.
- **We believed**: The "We believed:" statement from the Gatekeeper's verdict for this
  candidate. Expand to one full sentence if the template produced a phrase. This is the
  falsifiable prior belief this surprise contradicts — preserve its falsifiable form.
- **Finding**: What the signal actually revealed. Must directly contradict the "We believed:"
  statement. One sentence.
- **Design impact**: The specific component, flow, or decision this changes, constrains, or
  challenges. Must name something specific — not "this affects the design." One sentence
  minimum.

Minimum 2 entries.

---

**Step 5 — Synthesize.**

Do the surprises cluster? Write 2-4 sentences examining whether 2+ share a root cause,
reveal the same blind spot, or together indicate a design direction not previously visible.
Name any pattern you see. If there is none, state that explicitly.

---

**Step 6 — Forward guidance.**

Write 1-3 sentences addressed to the next team building `{topic}`. Specific to these
surprises. Register: "If you are about to build X, know that Y because we found Z."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 4-6 only. Steps 1-3 are execution scaffolding.

---

## V-02 — Explicit Artifact Routing Labels axis

**Variation axis:** Lifecycle emphasis — the Pre-Write Prediction Sort assigns a typed
`Route:` label naming a destination artifact type to every finding, converting the sort
from a binary filter into a routing layer. Builds on R4 V-02 (C-16 present). Targets C-19.

**Hypothesis:** R4 V-02 established a structurally distinct Pre-Write Prediction Sort that
ran before the gate pipeline (C-16). YES-routed findings were "excluded from the echo" and
"belong in topic-story" — but these were general instructions embedded in the sort step,
not per-finding typed labels. A finding classified YES was discarded from the prompt's
concern; whether it went to `topic-story` or `topic-report` or nowhere was not tracked.
C-19 closes this by requiring every finding to carry an explicit typed destination: "Route:
topic-story" is a named home, not a disposal. When every finding has a typed destination,
two effects follow: (1) confirmations are preserved and directed rather than dropped —
the team knows where evidence that validated assumptions belongs; (2) the gate pipeline
receives a cleanly typed input — only findings carrying `Route: gate-pipeline` proceed.
The sort becomes a dispatch table, not a trash bin.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

**What the echo is.** It answers one question: what did we learn that we did not expect?
It is institutional memory for the next team that walks this path. Each entry is a named
surprise — sourced, contrasted with prior expectation, and assessed for specific design
impact.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across all namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each was investigating.
Internal scaffolding.

---

**Step 2 — Pre-Write Prediction Sort (Routing Layer).**

This step runs before any candidates are assembled or written. It is a routing layer:
every finding is assigned a typed destination, not merely retained or discarded.

For each noteworthy finding from Step 1, apply the prediction test and assign a route:

```
Finding: {one phrase}
Predicted? YES | NO
Route: {one named artifact type — see valid values below}
```

> "Before this investigation began — reading only the original spec, design materials, and
> stated assumptions for `{topic}` — would we have predicted this finding?"

**Valid route values:**
- `topic-story` — confirmation: the finding validates what the design already assumed;
  belongs in the narrative of what the investigation found
- `topic-report` — process/method finding: about how the investigation ran, not what
  `{topic}` does; belongs in a report or retrospective
- `gate-pipeline` — non-confirmation: proceeds to the surprise filter

**Invalid route values — do not use:**
- "excluded from echo" — a disposal label, not a destination
- "not included" — a disposal label, not a destination
- blank — every finding must carry a named typed route

If the correct destination for a YES finding is unclear, use `topic-story` by default.

Collect at least 3 `Route: gate-pipeline` findings before proceeding. If you cannot,
re-read the signals — you may have over-predicted. The sort log is execution scaffolding —
do not include in the output artifact.

---

**Step 3 — Surprise filter.**

Working from the `gate-pipeline` findings in Step 2, apply a second test per candidate:

> "Does this finding contradict a specific prior belief — not just 'it was unusual,' but
> 'it opposed something we thought was true before we read this signal'?"

YES → retain as a surprise candidate. Note the prior belief it contradicts (one phrase).
NO → reassign route: `Route: topic-story`. An item can pass the prediction gate
(non-obvious) without being a surprise in the epistemic sense (contradicts a held belief).

Minimum 2 surprise candidates must survive. This filter log is internal scaffolding.

---

**Step 4 — Write echo entries.**

For each surprise candidate (minimum 2):

**[Surprise Name]**
*2-5 words, capitalized, distinct, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type. Traceable to a specific artifact,
  not to "the research" or "the interviews."
- **Prior assumption**: The specific prior belief this candidate contradicts (from Step 3).
  Expand to one full sentence.
- **Finding**: What the signal actually revealed. Must directly contradict the prior
  assumption. One sentence.
- **Design impact**: The specific component, flow, or decision this changes. One sentence
  minimum. Must name something specific — not "this affects the design."

---

**Step 5 — Synthesize.**

Do the surprises cluster? Write 2-4 sentences: do 2+ share a root cause, reveal the same
blind spot, or together indicate a design direction not previously visible? Name any pattern;
state its absence if none is evident.

---

**Step 6 — Forward guidance.**

1-3 sentences addressed to the next team building `{topic}`. Specific to these surprises.
Register: "If you are about to build X, know that Y."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 4-6. Steps 1-3 are execution scaffolding.

---

## V-03 — Named Future-Reader Role axis

**Variation axis:** Role sequence — the Institutional Archaeologist is introduced as a
named role at the prompt header and invoked by name at each sub-step (filter, naming,
impact, synthesis), making the future-reader frame auditable per step. Builds on R4 V-03
(C-17 present). Targets C-20.

**Hypothesis:** R4 V-03 required the future-reader frame to be present in >=3 sub-steps
by embedding per-step future-reader instructions at each field (C-17). This produced the
frame structurally — a model following the instructions could not accidentally adopt a
present-team frame without violating an explicit step requirement. The remaining gap: the
frame was held by instruction, not identity. Instructions can be satisfied with the letter
while losing the spirit: "write for a future reader" can produce text that sounds future-
reader-oriented without actually testing whether the assumption persists in the current
materials. A named role changes this dynamic. "Institutional Archaeologist:" before each
instruction creates an audit hook: each sub-step answer can be checked — is this "in role"?
A role identity is harder to drift from than a general instruction because the drift is
detectable by name, not only by content.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

**Your role for this artifact: Institutional Archaeologist.**

An Institutional Archaeologist arrives at a body of work after the original team has
dispersed. You do not have access to the team's discovery memory — what surprised them,
what they hoped for, what they feared. You have only the current design materials for
`{topic}` (spec, proposal, drafts) and the signal artifacts the team produced. Your task:
reconstruct which false assumptions the current materials still carry — the ones a new
team reading those materials would inherit and act on, incorrectly, without this artifact
to correct them.

You hold this identity throughout. Where a step or field is prefixed with
**(Institutional Archaeologist:)**, your answer must come from that perspective — not
from the original team's experience of running the signals, but from the position of
someone arriving cold to the materials and asking: what would the next team get wrong?

The Institutional Archaeologist is not the same role as an adversarial gatekeeper. If
both appear in a prompt, they serve different functions: the Gatekeeper tests whether
a finding qualifies as a surprise; the Institutional Archaeologist frames what that
surprise means for a reader who was not present.

---

**Step 1 — Read the signal record.**

Read all signal artifacts from `simulations/{topic}/` across all namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). For each artifact, note what it was
investigating and its key findings. This is your source material.

---

**Step 2 — Future-Reader Filter.**

For each notable finding in the signal record, apply the Archaeologist test:

> **(Institutional Archaeologist:)** "If a new team read only the current design materials
> for `{topic}` and began building, would they carry a false assumption that this finding
> corrects? Is the false assumption still present in the current materials — not corrected
> by a later update, not obvious from context that would reach the next team?"

YES → this finding is a candidate for the echo. The false assumption persists; the next
team would arrive with it.
NO → even if this finding surprised the original team, it is not load-bearing institutional
memory. Route to `topic-story`.

Note: this test is stricter than "was it surprising?" A vivid discovery that updated the
current materials does not qualify — the echo corrects assumptions the materials still carry,
not surprises the original team felt.

Collect at least 2 YES candidates.

---

**Step 3 — Write echo entries.**

For each candidate (minimum 2), produce one entry. The Institutional Archaeologist holds
the perspective at every field:

**[Surprise Name]**
**(Institutional Archaeologist:)** Encode the correction the next team needs, not the
discovery the original team made. "The Cascade Inversion" — what the next team must correct
for — is better than "Unexpected Cascade Behavior" — what the original team experienced.
A name passes if a future reader can use it as a reference without having been present at
the original investigation.

- **Source signal**: The specific artifact or skill type a future team can locate
  independently (e.g., `flow-resilience`, `prove-interview`, `scout-feasibility`).
- **The assumption the next team carries**: **(Institutional Archaeologist:)** What a new
  team reading the current materials would assume. State it as their belief, not the
  original team's history: "A team building `{topic}` today would assume..." or "The current
  spec implies..." Do not restate assumptions that have already been corrected in the
  materials — only what a new reader would carry.
- **The correction**: What the signal showed instead. Must directly contradict the assumption
  as stated above. One sentence.
- **What the next team would get wrong**: **(Institutional Archaeologist:)** The specific
  decision, component, or flow the next team would mis-design if they carried the false
  assumption. Name the concrete mis-design — not "this would cause problems." One sentence.

---

**Step 4 — Cross-materials synthesis.**

**(Institutional Archaeologist:)** Look across the entries: do two or more corrections
address the same category of misunderstanding — the same structural flaw in how the current
materials frame the problem? Write 2-4 sentences. You are looking for a pattern in how
the materials mislead future teams, not a pattern in the original team's discovery sequence.
Name any such pattern explicitly; state its absence if none is evident — absence is
itself information for the next team.

---

**Step 5 — Handover guidance.**

**(Institutional Archaeologist:)** Write 1-3 sentences as if handing this artifact to the
next team at the start of their investigation. Register: "The current materials will lead
you to assume X — they are wrong about this because..." or "Before you commit to Y, read
`{source signal}` because the spec does not warn you that..." Specific to these corrections.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 3-5. Steps 1-2 are execution scaffolding.

---

## V-04 — Combination: Routing Layer + Named Prior Belief (C-19 + C-18 + gate chain)

**Variation axis:** Lifecycle emphasis + output format — Pre-Write Prediction Sort with
per-finding typed Route: labels (C-19) before the gate, Typed Gate with SURPRISE verdict
requiring falsifiable "We believed:" field (C-18), full anti-pattern catalog on cuts
(C-11 + C-12 + C-13), affirmative pass verdict (C-15), prediction gate (C-16).

**Hypothesis:** R4 V-04 closed the gate chain's three structural gaps: upstream routing
before the gate (C-16), typed adversarial gate with anti-pattern labels on cuts
(C-11 + C-12 + C-13), and affirmative epistemic claims on passes (C-15). Two precision
gaps remained: (1) the prediction sort's Route: field allowed disposal language ("excluded")
rather than requiring typed artifact destinations; (2) the SURPRISE verdict's Epistemic
basis field allowed impressions alongside falsifiable beliefs. This combination closes both
simultaneously. When both additions are active, the chain reads: typed-route prediction sort
→ typed-cut adversarial gate → falsifiable-belief affirmative-claim pass. No finding enters
the echo without a named prior belief that can be evaluated; no finding is discarded without
a named destination that preserves it.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted
an assumption.
*Test:* "Could the output as a whole be described as a summary of what the investigation
found?" Yes → you have at least one of these.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**What the echo is.** It answers one question: what did we learn that we did not expect?
Each entry is a named surprise — sourced, contrasted with a named falsifiable prior belief,
and assessed for specific design impact. Its audience is the next team that walks this path.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each was investigating.
Internal scaffolding.

---

**Step 2 — Pre-Write Prediction Sort (Routing Layer).**

This step runs before any candidates enter the gate pipeline. It is a routing layer:
every finding is assigned a typed destination. No finding is discarded — each is directed.

For each noteworthy finding, record:

```
Finding: {one phrase}
Predicted? YES | NO
Route: {one named artifact type — required, see valid values}
```

> "Before this investigation began — reading only the original design materials for
> `{topic}` — would we have predicted this finding?"

**Valid route values:**
- `topic-story` — YES finding; confirmation of what the design assumed
- `topic-report` — YES finding; process or method observation, not a content finding
- `gate-pipeline` — NO finding; proceeds to the adversarial gate

**Structurally invalid routes — these are not destinations:**
- "excluded from echo" — disposal label
- "not included" — disposal label
- blank — every finding requires a named typed route

Collect at least 3 `Route: gate-pipeline` findings before proceeding. This sort log is
execution scaffolding — do not include in output.

---

**Step 3 — Typed Gate.**

You are now the **Gatekeeper**. Apply the Anti-Pattern Catalog to each `gate-pipeline`
candidate. Issue a verdict in this exact template:

```
Candidate: {one-sentence description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: {the falsifiable prior belief this candidate contradicts.
  Complete the sentence: "We believed {X}" where X is a testable proposition.

  VALID: "We believed the permission check was stateless and could be cached per session."
  VALID: "We believed bulk migration would fail silently under concurrent load."
  These could have been confirmed — the signals showed they were wrong instead.

  INVALID: "We hadn't thought through this part of the design."
  Absence of consideration is not a prior belief.
  INVALID: "This was surprising." A reaction is not a proposition.
  INVALID: "We were uncertain here." Uncertainty is not a falsifiable belief.

  If you cannot produce a valid "We believed X" for a candidate, it does not qualify
  as a SURPRISE — re-examine whether it is actually a surprise or a confirmation.}
Destination: [SURPRISE → echo] [CUT → topic-story, not topic-echo]
```

Valid verdict states only:
- `SURPRISE` — affirmative claim: contradicted a specific falsifiable prior belief, passes
  all three anti-pattern tests. "We believed:" must be a testable proposition — not an
  impression, not an absence of consideration.
- `CUT — finding-as-surprise substitution`
- `CUT — summary-in-disguise`
- `CUT — orphan-attribution`

Bare `CUT` without label is not valid. Multiple labels valid when more than one applies.
Minimum 2 SURPRISE verdicts required. Gatekeeper log is execution scaffolding — do not
include in output.

---

**Step 4 — Write echo entries.**

For each SURPRISE candidate (minimum 2):

**[Surprise Name]**
*2-5 words, capitalized, distinct, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type.
- **We believed**: The falsifiable prior belief from the Gatekeeper's "We believed:" field.
  Expand to one full sentence if the template produced a phrase. Preserve its falsifiable
  form — do not convert it to a hedge.
- **Finding**: What the signal revealed — must directly contradict the "We believed:"
  statement. One sentence.
- **Design impact**: The specific component, flow, or decision this changes. One sentence
  minimum. Must name something specific.

---

**Step 5 — Synthesize.**

Do the surprises cluster? Write 2-4 sentences: do 2+ share a root cause, reveal the same
blind spot, or together indicate a design direction not previously visible? Name any
pattern; state its absence if none is evident.

---

**Step 6 — Forward guidance.**

1-3 sentences for the next team building `{topic}`. Specific to these surprises.
Register: "If you are about to build X, know that Y because we found Z."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 4-6. Steps 1-3 are execution scaffolding.

---

## V-05 — Full Combination: All 12 Active Criteria

**Variation axis:** All 12 active aspirational criteria at structurally distinct moments —
C-18 (falsifiable "We believed:" field in gate), C-19 (typed Route: labels in prediction
sort), C-20 (Institutional Archaeologist named role invoked per sub-step) added to the R4
V-05 structure (C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17).

**Hypothesis:** R4 V-05 closed 9 aspirational criteria at structurally distinct moments.
Three structural ambiguities remained: (1) the SURPRISE verdict's Epistemic basis field
could be satisfied by impressions — C-18 closes this by renaming it "We believed:" and
constraining it to falsifiable propositions; (2) the prediction sort's Route: field used
disposal language rather than typed artifact names — C-19 closes this by requiring a named
destination per finding; (3) the future-reader frame was held by per-step instructions
rather than a named role — C-20 closes this by instantiating the Institutional Archaeologist
as a named role invoked at naming, filter, impact, and synthesis. With all three gaps closed,
the 12-criterion chain is structurally unambiguous at every junction: every finding is
typed-routed; every rejection names an anti-pattern; every pass carries a falsifiable prior
belief; every sub-step operates under a named role whose perspective can be verified. The
Institutional Archaeologist and the Gatekeeper are distinct roles with distinct functions —
each step identifies which role is active and why.

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
*Test:* "Could this output be described as a summary of what the investigation found?"
Yes → you have at least one of these.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**What the echo is.** It answers one question: what did we learn that we did not expect?
Each entry is a named surprise — sourced, contrasted with a named falsifiable prior belief,
ranked by design impact, and assessed for specific consequence. The echo closes with
impact-annotated rules of thumb encoding the highest-impact surprises in quotable form.
Its audience is the next team that walks this path.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each was investigating.
Internal scaffolding.

---

**Step 2 — Pre-Write Prediction Sort (Routing Layer).**

This step runs before any candidates enter the gate pipeline. It is a routing layer:
every finding is assigned a typed destination.

For each noteworthy finding, record:

```
Finding: {one phrase}
Predicted? YES | NO
Route: {one named artifact type — required}
```

> **(Institutional Archaeologist:)** "Before this investigation began — reading only the
> original design materials for `{topic}` — would a new team building `{topic}` today have
> predicted this finding? Does the current spec already account for it?"

Route assignment rules:
- YES → `Route: topic-story`
- YES (process/method finding) → `Route: topic-report`
- NO → `Route: gate-pipeline`

Invalid routes: "excluded from echo," blank, any disposal language. Every finding must
carry a named typed destination. Collect at least 3 `Route: gate-pipeline` findings before
proceeding. Sort log is execution scaffolding — do not include in output.

---

**Step 3 — Typed Gate.**

You are now the **Gatekeeper** (not the Institutional Archaeologist — the Gatekeeper's
function is adversarial rejection, not future-reader framing). Apply the Anti-Pattern
Catalog to each `gate-pipeline` candidate.

Issue a verdict in this exact template:

```
Candidate: {one-sentence description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: {the falsifiable prior belief this candidate contradicts.
  Complete the sentence: "We believed {X}" where X is a testable proposition.

  VALID: "We believed the scheduler deduplicated events before dispatching callbacks."
  VALID: "We believed the compliance check ran at write time, not read time."
  These are propositions that could have been confirmed — the signals showed otherwise.

  INVALID: "We hadn't considered this edge case." Absence of consideration.
  INVALID: "This was surprising to the team." A reaction, not a proposition.
  INVALID: "We were uncertain about this area." Uncertainty is not a falsifiable belief.

  A SURPRISE verdict without a valid "We believed X" is structurally incomplete.}
Destination: [SURPRISE → echo] [CUT → topic-story, not topic-echo]
```

Valid verdict states only:
- `SURPRISE` — affirmative claim: contradicted a specific falsifiable prior belief, passes
  all three anti-pattern tests. "We believed:" must be a testable proposition.
- `CUT — finding-as-surprise substitution`
- `CUT — summary-in-disguise`
- `CUT — orphan-attribution`

Bare `CUT` without label is not valid. Multiple labels valid. Minimum 2 SURPRISE verdicts.
Gatekeeper log is execution scaffolding — do not include in output.

---

**Step 4 — Impact triage (pre-write).**

Receive the SURPRISE candidates. Before writing any entry, assign each an impact level.
Compare candidates against each other — relative, not absolute.

- **HIGH**: Forces a design decision to change or invalidates a major assumption. Design
  cannot proceed as planned without addressing this.
- **MEDIUM**: Requires adjustment to a specific component, flow, or decision. Design can
  proceed but must change.
- **LOW**: Informative; peripheral detail. Does not change the design trajectory.

Order candidates HIGH → MEDIUM → LOW. Ties broken by specificity of impact. Do not include
the raw triage list in the artifact.

---

**Step 5 — Write echo entries (highest impact first).**

For each SURPRISE candidate in triage order:

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
**(Institutional Archaeologist:)** Encode the correction the next team needs, not the
discovery the original team made. "The Cascade Inversion" — what the next team must correct
for — passes; "Unexpected Cascade Behavior" — what the original team experienced — does not.
A name passes if a future reader can cite it without having been present.

- **Source signal**: Specific artifact or skill type (e.g., `flow-resilience`,
  `prove-interview`, `scout-feasibility`). Must pass the orphan-attribution test.
- **We believed**: The falsifiable prior belief from the Gatekeeper's "We believed:" field.
  Expand to one full sentence if needed. Preserve its falsifiable form.
- **The correction**: What the signal showed instead. Must directly contradict "We believed."
  One sentence.
- **What the next team would get wrong**: **(Institutional Archaeologist:)** The specific
  decision, component, or flow the next team would mis-design if they carried the false
  assumption. Name the concrete mis-design — not "this would cause problems."

---

**Step 6 — Synthesis.**

**(Institutional Archaeologist:)** Look across the entries: do two or more corrections
address the same category of misunderstanding — the same structural flaw in how the current
materials frame the problem? Write 2-4 sentences. You are looking for a pattern in how the
materials mislead future teams, not the original team's discovery sequence. Name any pattern;
state its absence if none is evident.

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
[{HIGH | MEDIUM | LOW}] {Rule text — <=20 words, names a specific behavior or constraint}
(encodes: {Surprise Name from Step 5})
```

**Anchoring constraint**: The impact tier in the rule must match the tier assigned to the
surprise it encodes in Step 4. A rule annotated `[HIGH]` that encodes a `MEDIUM` surprise
is a malformed entry — revise the tier or re-examine the triage.

**Scope**: Only HIGH and MEDIUM surprises generate rules. LOW surprises are informative
but too peripheral to anchor a rule.

**Traceability check**: After writing all rules, verify end-to-end: does the tier in each
rule match the tier header of the surprise entry it names? A yes on all rules closes the
full chain: signal artifact → typed-route prediction sort (with named destinations) →
typed-gate verdict (with falsifiable "We believed:" field) → ranked named surprise (with
tier) → impact-annotated rule (with matching tier). The Institutional Archaeologist can
confirm: each link in this chain is independently auditable by a future reader arriving
with no context.

Label the section **"Rules of Thumb"**.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 5-8. Steps 1-4 are execution scaffolding.
