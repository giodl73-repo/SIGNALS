---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 3
rubric: v3
---

# Variations: `topic:echo` — Round 3

**Rubric:** v3 | **Date:** 2026-03-15

---

## Design Context

R2 differentiating evidence: V-01's Null Hypothesis Enforcer with destination-encoded
verdicts strengthened C-11 beyond R1's V-04 by moving the cut destination from a general
instruction into the per-verdict template. V-02's three-anti-pattern catalog with executable
diagnostics strengthened C-12 beyond R1's V-05 by making each anti-pattern testable, not just
nameable. V-03's pre-write impact triage produced genuine comparative rankings (C-09). V-04's
compression-first rule drafting produced rules that preceded rather than summarized the prose
(C-10). V-05 combined all four in structurally distinct phases.

These two combination behaviors became C-13 and C-14 in v3:

- **C-13**: When C-11 and C-12 are both present, cut verdicts must *name the anti-pattern*
  triggered — "CUT — finding-as-surprise substitution," not bare "CUT." Typed verdicts make
  the anti-pattern catalog load-bearing rather than decorative: every rejection is auditable.
- **C-14**: When C-09 and C-10 are both present, each rule of thumb must carry the impact tier
  (HIGH/MEDIUM/LOW) of the surprise it encodes. Closes the traceability chain: signal artifact
  → ranked surprise → ranked rule.

**R3 strategy:**

- V-01: Single-axis targeting C-13 in isolation — verdict template itself encodes the
  anti-pattern name slot, making a bare "CUT" structurally unproducible.
- V-02: Single-axis targeting C-14 in isolation — rules section template requires tier
  annotation with explicit matching constraint to the ranked entry it encodes.
- V-03: Single-axis exploring an unexplored role sequence — the Institutional Archaeologist,
  who works backward from "what would a future team need to know?" rather than forward from
  "what surprised us?". Not targeting a specific new criterion; testing whether the role
  inversion produces higher-quality C-08 and C-07.
- V-04: Combination of C-11 + C-12 + C-13 (typed gate side) + C-10 (rules side) — tests
  whether typed rejection and compression-first rules coexist cleanly without impact triage.
- V-05: Full six-criterion traceability chain — all aspirational targets assigned to
  structurally distinct moments. Every rejection auditable; every rule traceable to a ranked
  surprise with a matching tier.

**What C-13 adds over R2 V-01:**

R2 V-01's verdict template had two verdict states: SURPRISE and CONFIRMED. The Destination
line encoded where confirmed candidates go, but the verdict itself was untyped — "CONFIRMED"
without specifying *which* criterion or anti-pattern caused rejection. C-13 requires the
verdict to name the anti-pattern. V-01 below restructures the template so the only valid
non-SURPRISE verdict is "CUT — {anti-pattern label}" — no CONFIRMED state exists. The model
must reach into the anti-pattern catalog to complete the verdict.

**What C-14 adds over R2 V-04:**

R2 V-04's rules were traceable to surprises by name (parenthetical reference). But the impact
tier assigned during pre-write triage was not propagated into the rule. V-02 below adds a
structural constraint: each rule must carry `[HIGH]`, `[MEDIUM]`, or `[LOW]` matching the
tier assigned to the surprise it encodes. A rule whose tier does not match its surprise's tier
is a malformed rule — the template enforces this.

---

## V-01 — Typed Verdict axis

**Variation axis:** Output format — verdict template redesigned so that the only non-SURPRISE
outcome is "CUT — {anti-pattern label}", making bare rejection structurally unproducible.

**Hypothesis:** R2's Null Hypothesis Enforcer allowed "CONFIRMED" as a verdict, with the
anti-pattern check as a separate step. When the template collapses the confirmation verdict
into a typed cut verdict — "CUT — {anti-pattern label}" — the model cannot produce a
rejection without reaching into the anti-pattern catalog. The anti-pattern name is not checked
after the fact; it is required to complete the verdict syntax.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not
expect? It is not a summary. It is a record of surprises — each named, sourced, and assessed
for its specific impact on the design direction. Its audience is the next team that walks this
path.

---

**Anti-Pattern Catalog — required vocabulary for the gate below.**

Before executing, read and retain these three labels. They are the only valid reasons to cut
a candidate. You will need to cite them by name.

**finding-as-surprise substitution** — an expected or predictable outcome stated in surprise
language. The design anticipated X; the signal confirmed X; the echo calls X surprising.
*Test:* Would a reader of only the original design materials have predicted this? Yes → cut.

**summary-in-disguise** — a finding included not because it surprised anyone, but because it
rounds out the coverage of the investigation. The tell: if your output as a whole could be
described as "a summary of what the investigation found," you have at least one of these.
*Test:* Is this finding included because it contradicted an assumption, or because it happened
and was notable? If the latter → cut.

**orphan-attribution** — a genuine surprise whose source is attributed to "the research,"
"the analysis," or "the signals generally." Unverifiable. The next team cannot check it.
*Test:* Can you name the specific signal artifact or skill type? If no → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). For each artifact, note in one phrase
what it was investigating. This is internal scaffolding — do not include it in the output.

---

**Step 2 — Assemble raw candidates.**

Scan the signals for findings that are notable, non-trivial, or worth preserving. Write a
one-sentence description for each. Do not filter yet. Collect at least 4 candidates.

---

**Step 3 — Typed Gate.**

You are now the **Gatekeeper**. For each candidate, issue a verdict in this exact template:

```
Candidate: {one-sentence description}
Verdict: SURPRISE | CUT — {anti-pattern label}
Rationale: {one sentence — why this survives or which anti-pattern it triggers}
Destination: [SURPRISE → echo] [CUT → topic-story, not topic-echo]
```

The only valid verdict states are:
- `SURPRISE` — the candidate is a genuine surprise; it contradicted a prior assumption and
  passes all three anti-pattern tests.
- `CUT — finding-as-surprise substitution`
- `CUT — summary-in-disguise`
- `CUT — orphan-attribution`

A bare `CUT` without an anti-pattern label is not a valid verdict. A combined verdict
("CUT — finding-as-surprise substitution + orphan-attribution") is valid when multiple
anti-patterns apply; cite all that triggered.

Minimum 2 candidates must receive SURPRISE. Issue a verdict for every candidate. The
Gatekeeper log is execution scaffolding — do not include it in the output artifact.

---

**Step 4 — Write echo entries.**

Receive the SURPRISE candidates from the Gatekeeper. For each, produce one entry:

**[Surprise Name]**
*2-5 words, capitalized, distinct, reusable as a citation in conversation.*

- **Source signal**: Specific artifact name or skill type (e.g., `flow-resilience`,
  `prove-interview`, `scout-feasibility`). Must pass the orphan-attribution test.
- **Prior assumption**: What was expected before this signal was read. One sentence. If there
  was no explicit assumption, state the implicit one.
- **Finding**: What the signal actually revealed. Must oppose or contradict the prior
  assumption. One sentence.
- **Design impact**: The specific component, flow, or decision this changes, constrains, or
  challenges. Must name something specific — not "this affects the design."

---

**Step 5 — Synthesize.**

Do the surprises cluster? Write 2-4 sentences examining whether 2 or more share a root cause,
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

## V-02 — Impact-Anchored Rules axis

**Variation axis:** Output format — rules of thumb section template requires impact tier
annotation `[HIGH | MEDIUM | LOW]` matching the tier assigned to the surprise the rule
encodes. Mismatch between rule tier and surprise tier is a malformed entry.

**Hypothesis:** R2 V-04 produced rules traceable to surprises by name, but the impact tier
from the pre-write triage was not carried forward. When the rule template requires an explicit
tier annotation and the annotation must match the surprise's assigned tier, traceability
becomes bidirectional: a reader can verify any rule's priority by checking the surprise entry
it names. Mismatch would be immediately visible, creating a structural self-check.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

**What the echo is.** It answers one question: what did we learn that we did not expect? It
is institutional memory for the next team. Surprises are ranked by the magnitude of their
design impact and close with distilled rules of thumb — one-liners that encode the highest-
impact surprises in a form quotable without reading the full artifact.

---

**Step 1 — Read signals.**

Read signal artifacts from `simulations/{topic}/` across all namespaces. Note what each was
investigating. This is internal scaffolding.

---

**Step 2 — Identify surprise candidates.**

For each noteworthy finding, apply the prediction test:
> "Would a person reading only the pre-investigation design materials have predicted this?"

YES → confirmation. Not an echo entry. (Belongs in `topic-story`.)
NO → surprise candidate.

Collect at least 3 candidates before proceeding.

---

**Step 3 — Impact triage (pre-write).**

Before writing any entry, assign each candidate an impact level. Compare candidates against
each other — this is relative, not absolute.

- **HIGH**: Forces a design decision to change, invalidates a major assumption, or introduces
  a significant constraint not previously visible. Cannot proceed as planned without addressing.
- **MEDIUM**: Refines or complicates a specific component, flow, or decision. Design can
  proceed but requires adjustment.
- **LOW**: Informative but affects only a peripheral detail. Does not change the design
  trajectory.

Order candidates HIGH → MEDIUM → LOW. Ties broken by specificity of impact. Record this
triage order — it determines both the entry sequence and the rule tiers below. This is
execution scaffolding; do not include the raw triage list in the artifact.

---

**Step 4 — Surprise entries (highest impact first).**

For each candidate in triage order, write one entry:

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
*2-5 words, capitalized, reusable as a citation. Impact level annotated in the header.*

- **Source signal**: Specific artifact name or skill type. Traceable to a specific signal.
- **Prior assumption**: What was expected going in. One sentence.
- **Finding**: What the signal revealed — must oppose the prior assumption. One sentence.
- **Design impact**: The specific component, flow, or decision this changes. One sentence
  minimum. Must name something specific.

Minimum 2 entries.

---

**Step 5 — Synthesize.**

Do the surprises cluster around a common root cause or blind spot? Write 2-4 sentences.
Name any pattern; state its absence if none is evident.

---

**Step 6 — Forward guidance.**

1-3 sentences addressed to the next team building `{topic}`. Specific to these surprises.
Register: "If you are about to build X, know that Y."

---

**Step 7 — Rules of Thumb (impact-anchored).**

Write ≤3 rules that encode the most important surprises in quotable form. Each rule encodes
exactly one surprise. Apply this template strictly:

```
[{HIGH | MEDIUM | LOW}] {Rule text — ≤20 words, names a specific behavior or constraint}
(encodes: {Surprise Name from Step 4})
```

**Anchoring constraint**: The impact tier in the rule must match the impact tier assigned to
the surprise it encodes in Step 3. A rule annotated `[HIGH]` that encodes a `MEDIUM` surprise
is a malformed entry — revise the rule tier or re-examine the triage.

**Scope**: Only HIGH and MEDIUM surprises generate rules. LOW surprises are too peripheral
to warrant a one-liner in the rules section.

Label the section **"Rules of Thumb"**.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 4-7. Steps 1-3 are execution scaffolding.

---

## V-03 — Institutional Archaeologist role axis

**Variation axis:** Role sequence — the model takes the role of an Institutional Archaeologist
reading the signal record 18 months after the investigation, working backward from "what
would the next team most need to know?" rather than forward from "what surprised us at the
time?"

**Hypothesis:** The standard forward-facing role ("what surprised us?") can drift toward
moment-of-discovery framing — surprises that were vivid when found but whose significance
has decayed. The Archaeologist role inverts this: the question is not "what was surprising
when we found it" but "what, if unknown, would cause the next team to make the same mistake?"
This role inversion may produce higher-quality C-08 (future-team guidance) because the model
is already positioned as the future team evaluating the institutional record, and higher-
quality C-07 (cross-signal synthesis) because the retrospective lens naturally groups by
consequence rather than by discovery sequence.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

You are not writing from the perspective of the team that gathered these signals. You are an
**Institutional Archaeologist** reading their signal record 18 months later, tasked with
extracting whatever institutional memory the next team will need before they begin.

Your question is not "what surprised them?" Your question is: **"What, if unknown going in,
would cause the next team to make the same mistakes?"**

---

**The distinction that matters.**

A finding that surprised the original team is not automatically worth preserving. What you
are looking for is findings where:
1. The original team held a prior belief
2. The signal contradicted that belief
3. The contradiction is still consequential — a future team carrying the same prior belief
   would be led astray in the same way

If the finding surprised the team but would be obvious to any future team reading the current
spec, it is not worth preserving. Institutional memory is not a surprise diary — it is a
correction record for assumptions that are still wrong in the current materials.

---

**Step 1 — Audit the signal record.**

Read all signal artifacts from `simulations/{topic}/` across all namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). For each artifact, note what it was
investigating and what its key findings were. This is your source material.

---

**Step 2 — Identify still-consequential surprises.**

For each surprise in the signal record, apply the Archaeologist's test:

> "If a new team read only the current design materials for `{topic}` — the spec, the
> proposal, the drafts — and then went to build it, would this finding have corrected a
> false assumption they would have carried?"

YES → this surprise is still consequential. It is a candidate for the echo.
NO → the surprise may have been vivid when found but is no longer load-bearing. Skip it. It
belongs in `topic-story`, not `topic-echo`.

Collect at least 2 still-consequential candidates.

---

**Step 3 — Write the echo entries.**

For each candidate, produce one entry. You are writing *for* the next team, not *about* the
original team's experience. Frame each entry as a correction, not a discovery narrative.

**[Surprise Name]**
*2-5 words, capitalized, distinct, citable. The name should encode the correction, not the
discovery — "The Cascade Inversion," not "Unexpected Cascade Behavior."*

- **Source signal**: The specific artifact name or skill type that surfaces this correction
  (e.g., `flow-resilience`, `prove-interview`, `scout-feasibility`). The next team must be
  able to locate this source.
- **The assumption still carried**: What a new team reading the current materials would
  assume. State it as a belief, not a description: "A team would assume that..." or "The
  current spec implies..."
- **The correction**: What the signal showed instead. Must directly contradict the assumption.
  One sentence.
- **Why it still matters**: What the next team would get wrong if they carried the old
  assumption. Name the specific decision, component, or flow that would be affected.

Minimum 2 entries. Each must independently pass the Archaeologist's test.

---

**Step 4 — Cross-temporal synthesis.**

Look across your entries. Do two or more address the same category of misunderstanding —
the same blind spot in how the original design materials frame the problem? Write 2-4
sentences. Name any pattern you see across the corrections. If there is none, state that
explicitly.

---

**Step 5 — Forward guidance.**

Write 1-3 sentences addressed directly to the next team, as if you are handing them this
artifact before they begin. The register: "Before you start building `{topic}`, know that..."
or "The design materials do not warn you that..." Specific to these corrections — not generic.

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

---

## V-04 — Combination: Typed Gate + Compression-First Rules (C-11 + C-12 + C-13 + C-10)

**Variation axis:** Role sequence (adversarial gate with typed verdicts) combined with
lifecycle emphasis (rules drafted before full entries).

**Hypothesis:** The typed rejection mechanism (C-13) and the compression-first rules mechanism
(C-10) target failure modes at structurally opposite ends of the production sequence: typed
rejection operates at the filtering stage (before entries are written), compression-first rules
operate at the output stage (before entries are expanded). Combining them without also adding
impact triage (C-09) tests whether these two mechanisms coexist cleanly — whether the overhead
of the typed gate competes with the cognitive work of drafting rules-first, or whether they
complement each other (the gate removes noise before compression; compression operates on
signal only).

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

---

**Anti-Pattern Catalog — read before executing.**

These three failure modes have names and diagnostics. You will cite them by name during the
gate step below.

**finding-as-surprise substitution** — an expected outcome stated in surprise language. The
spec anticipated X; the signal confirmed X; the echo calls it surprising.
*Diagnostic:* "Would a reader of only the original design materials have predicted this?"
Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted an
assumption. Tell: your output could be described as "a summary of what the investigation
found."
*Diagnostic:* "Is this finding included because it overturned an assumption, or because it
happened and was worth noting?" If the latter → cut.

**orphan-attribution** — a genuine surprise attributed to "the research" or "the signals"
without a traceable artifact.
*Diagnostic:* "Can I name the specific signal artifact or skill type?" No → cut until you can.

---

**What the echo is.** It answers: what did we learn that we did not expect? It is
institutional memory for the next team. Each entry is a named surprise — sourced, contrasted
with prior expectation, and assessed for specific design impact. The echo closes with
compressed rules of thumb written *before* the full entries are expanded.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each artifact was
investigating. Internal scaffolding.

---

**Step 2 — Assemble raw candidates.**

Scan the signals for noteworthy findings. Write a one-sentence description per candidate.
Do not filter yet. Collect at least 4 candidates.

---

**Step 3 — Typed Gate.**

You are now the **Skeptic**. For each candidate, issue a verdict using this exact template:

```
Candidate: {one-sentence description}
Verdict: SURPRISE | CUT — {anti-pattern label}
Rationale: {one sentence}
Destination: [SURPRISE → echo] [CUT → topic-story, not topic-echo]
```

Valid verdict states only:
- `SURPRISE`
- `CUT — finding-as-surprise substitution`
- `CUT — summary-in-disguise`
- `CUT — orphan-attribution`

A bare `CUT` without an anti-pattern label is not valid. Multiple labels are valid when more
than one anti-pattern applies. Minimum 2 SURPRISE verdicts required. The Skeptic log is
execution scaffolding — do not include it in the output artifact.

---

**Step 4 — Draft the rule first.**

Receive the SURPRISE candidates. Before writing any full entry, draft a compressed rule for
each candidate — the one-liner a future teammate would need to remember without reading the
full entry.

Format constraint per rule:
- ≤20 words
- Names a specific behavior, constraint, or relationship — not a generic observation
- Written in a form someone could quote verbatim in conversation without context

Write these rules in rough form now. They will be refined in Step 7. Drafting rules first
forces you to compress the surprise to its most transferable form before elaborating.

---

**Step 5 — Expand each rule into a full entry.**

For each surprise, write one entry. Let the rough rule shape the surprise name — the name
should encode the correction, not just label the finding.

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type.
- **Prior assumption**: What was expected before this signal. One sentence.
- **Finding**: What the signal revealed — must oppose the prior assumption. One sentence.
- **Design impact**: Specific component, flow, or decision this changes. One sentence minimum.
  Must name something specific.

Minimum 2 entries.

---

**Step 6 — Synthesize.**

Do the surprises cluster? Write 2-4 sentences. Do 2 or more share a root cause, reveal the
same blind spot, or together indicate a design direction not previously visible? Name any
pattern; state its absence if none is evident.

---

**Step 7 — Forward guidance.**

1-3 sentences addressed to the next team building `{topic}`. Specific to these surprises.
Register: "If you are about to build X, know that Y because we found Z."

---

**Step 8 — Rules of Thumb (final).**

Return to the rough rules from Step 4. Revise them with the benefit of having written the
full entries. Final rules must:

- ≤20 words each
- Name a specific behavior, constraint, or relationship
- Be traceable by name to a surprise in this echo — include the surprise name in parentheses
- Be quotable in conversation without reading the rest of the artifact

Present ≤3 rules under the heading **"Rules of Thumb"**.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 5-8. Steps 1-4 are execution scaffolding.

---

## V-05 — Combination: Full Traceability Chain (C-09 + C-10 + C-11 + C-12 + C-13 + C-14)

**Variation axis:** All six aspirational criteria (C-09 through C-14) assigned to structurally
distinct moments in the production sequence.

**Hypothesis:** The six aspirational criteria are not in tension — they address different
failure points. C-12 (anti-pattern catalog) shapes what the model accepts as input. C-11
(adversarial gate) + C-13 (typed verdicts) filter the candidate list with auditable evidence
of which failure mode each rejection named. C-09 (impact triage) ranks survivors before any
prose is committed. C-10 (rules of thumb) + C-14 (impact-anchored rules) close the chain
with a navigable index where every rule's priority is traceable to a ranked surprise. The
chain is: signal artifact → typed rejection log (with anti-pattern attribution) → ranked named
surprise (with impact tier) → impact-annotated rule. A reader who reads only the Rules of
Thumb section can verify the tier of any rule by tracing it back to its surprise entry. A
reader who questions any cut candidate can audit it by anti-pattern label. No criterion
interferes with another because each occupies a distinct structural moment.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings included for coverage rather than because they contradicted
an assumption. *Test:* "Could the output as a whole be described as a summary of what the
investigation found?" Yes → you have at least one of these.

**orphan-attribution** — a genuine surprise with no traceable signal source. "From the
research" or "from the interviews" is not a source. *Test:* "Can I name the specific artifact
or skill type?" No → cut until you can.

---

**What the echo is.** The echo answers: what did we learn that we did not expect? It is
institutional memory for the next team. Each entry is a named surprise — sourced, contrasted
with prior expectation, and ranked by design impact magnitude. The echo closes with impact-
annotated rules of thumb that encode the highest-impact surprises in quotable form.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each artifact was
investigating. Internal scaffolding only.

---

**Step 2 — Assemble raw candidates.**

Scan the signals for findings worth noting. Write a one-sentence description per candidate.
Do not filter yet. Collect at least 4 candidates.

---

**Step 3 — Typed Gate.**

You are now the **Skeptic**. Apply the Anti-Pattern Catalog to each candidate and issue a
verdict in this exact template:

```
Candidate: {one-sentence description}
Verdict: SURPRISE | CUT — {anti-pattern label}
Rationale: {one sentence — why this survives or which anti-pattern it triggers}
Destination: [SURPRISE → echo] [CUT → topic-story, not topic-echo]
```

Valid verdict states only:
- `SURPRISE`
- `CUT — finding-as-surprise substitution`
- `CUT — summary-in-disguise`
- `CUT — orphan-attribution`

A bare `CUT` without an anti-pattern label is not valid. Multiple anti-pattern labels are
valid when more than one applies. Minimum 2 SURPRISE verdicts required. The Skeptic log is
execution scaffolding — do not include it in the output artifact.

---

**Step 4 — Impact triage (pre-write).**

Receive the SURPRISE candidates. Before writing any entry, assign each an impact level:

- **HIGH**: Forces a design decision to change or invalidates a major assumption. The design
  cannot proceed as planned without addressing this.
- **MEDIUM**: Requires adjustment to a specific component, flow, or decision. Design can
  proceed but must change.
- **LOW**: Informative; affects only a peripheral detail. Does not change the design
  trajectory.

Order candidates HIGH → MEDIUM → LOW. Ties broken by specificity of impact. This triage
order is the output sequence and determines rule tiers in Step 7. Do not include the raw
triage list in the artifact.

---

**Step 5 — Write echo entries (highest impact first).**

For each SURPRISE candidate in triage order:

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
*2-5 words, capitalized, reusable as a citation. Impact annotation required in the header.*

- **Source signal**: Specific artifact name or skill type (e.g., `flow-resilience`,
  `prove-interview`, `scout-feasibility`). Must pass the orphan-attribution test.
- **Prior assumption**: What was expected before this signal. One sentence. If no explicit
  assumption existed, state the implicit one.
- **Finding**: What the signal actually revealed — must oppose the prior assumption.
  One sentence.
- **Design impact**: The specific component, flow, or decision this changes. One sentence
  minimum. Must name something specific — not "this affects the design."

Minimum 2 entries.

---

**Step 6 — Synthesize.**

Do the surprises cluster? Write 2-4 sentences examining whether 2 or more share a root cause,
reveal the same blind spot, or together indicate a design direction not previously visible.
Name any pattern you see. If there is none, state that explicitly — absence of pattern is
itself information.

---

**Step 7 — Forward guidance.**

Write 1-3 sentences addressed to the next team building `{topic}`. Must be specific to these
surprises — not generic advice. Register: "If you are about to build X, know that Y because
we found Z."

---

**Step 8 — Rules of Thumb (impact-anchored).**

Write ≤3 rules that encode the most important surprises in quotable form. Use this template
strictly for each rule:

```
[{HIGH | MEDIUM | LOW}] {Rule text — ≤20 words, names a specific behavior or constraint}
(encodes: {Surprise Name from Step 5})
```

**Anchoring constraint**: The impact tier in the rule must match the tier assigned to the
surprise it encodes in Step 4. A rule annotated `[HIGH]` that encodes a `MEDIUM` surprise is
a malformed entry. If the tiers do not match, re-examine either the triage assignment or the
rule selection.

**Scope**: Only HIGH and MEDIUM surprises generate rules. LOW surprises are informative but
too peripheral to anchor a rule.

**Traceability check**: After writing all rules, verify: does the tier in each rule match the
tier header of the surprise entry it names? A yes on all rules closes the chain:
signal artifact → typed rejection log → ranked named surprise (with tier) → impact-annotated
rule (with matching tier).

Label the section **"Rules of Thumb"**.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 5-8. Steps 1-4 are execution scaffolding.
