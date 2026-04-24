Reading the scorecard carefully to extract the new excellence patterns before writing v3.

**New patterns visible in Round 2:**

1. **V-03 C-06 PASS / C-12 PARTIAL** — V-03's collective brief *leads* the artifact structurally. V-01 and V-02 both get C-12 PARTIAL because "no first-draft-before-entries constraint; no non-derivability test." The mechanism is distinct from C-12 (which requires the block to exist): C-13 requires the block to precede entries, making post-hoc summarization impossible.

2. **V-01 C-10 PASS** — The Archaeologist writes the belief ledger *before* signals are read. This is structurally different from C-10 (which requires the delta to appear in the entry): C-14 requires a pre-investigation lock that makes the prior assumption independently verifiable, not reconstructed. The "do not omit the third clause" enforcement in V-01 is the output signal; the ledger-before-reading is the mechanism.

Both V-01 and V-02 PARTIAL on C-12 because of no pre-write constraint. V-02 PARTIAL on C-10 because "no required delta sentence structure." These are the two gaps that become C-13 and C-14.

---

```markdown
# topic-echo-rubric-v3-2026-03-15.md

## Rubric: `topic-echo` — v3

**Skill**: `topic:echo`
**Version**: v3
**Date**: 2026-03-15
**Criteria count**: 14 (4 essential / 3 recommended / 7 aspirational)

**Formula**:
`(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/7 × 10)`

PARTIAL = 0.5. Max composite = 100. Aspirational tier is a ceiling bonus,
not a score driver. Each full aspirational pass ≈ 1.43 pts.

**Band thresholds**: Gold ≥ 85 + all_essential_pass | Silver ≥ 70 +
all_essential_pass | Bronze ≥ 55 + all_essential_pass | Miss < 55 or any
essential FAIL

---

## Essential Criteria (60 pts — output fails without these)

### C-01 | Surprise Orientation
- **Weight**: essential
- **Category**: correctness
- **Text**: The output contains only genuine surprises — findings that
  contradict, reverse, or significantly complicate what was believed or
  designed before the signals arrived. Confirmations (findings that match
  prior expectations) are excluded from the surprise entries.
- **Pass condition**: Every entry in the output names something that was
  not predictable from pre-investigation design materials. An entry that
  restates what the spec already said fails. An entry framed as "this
  confirmed X" fails. PARTIAL if one entry is borderline but the
  remainder are genuine surprises.

### C-02 | Source Signal Tracing
- **Weight**: essential
- **Category**: correctness
- **Text**: Each surprise names the specific signal artifact or skill type
  that produced it. Vague attribution ("the research", "the signals",
  "investigation") is not acceptable. Tracing must be specific enough
  that a reviewer could locate the source artifact.
- **Pass condition**: Every surprise entry names a specific artifact (e.g.,
  `prove-interview-variate-R3`, `flow-resilience`) or skill type with
  enough precision to locate the source. "The signals" or "our research"
  fails. PARTIAL if one entry has weak attribution but the rest are
  specific.

### C-03 | Design Impact Assessment
- **Weight**: essential
- **Category**: depth
- **Text**: Each surprise states its consequence for design: what component,
  flow, constraint, or decision must change as a result. An entry that
  merely reports an interesting finding without naming what changes is
  incomplete.
- **Pass condition**: Every surprise entry contains a design impact clause
  that names a specific artifact, component, or decision. "This is
  interesting" or "worth noting" fails. PARTIAL if one entry has a weak
  impact clause but the rest are specific.

### C-04 | Named and Countable Surprises
- **Weight**: essential
- **Category**: format
- **Text**: Each surprise is a discrete, titled item. The output contains
  at least 2 surprises. A single observation is not a synthesis.
- **Pass condition**: Output has ≥ 2 surprises, each with a distinct name
  or title that can be referenced independently. An undifferentiated
  paragraph fails even if it contains multiple ideas.

---

## Recommended Criteria (30 pts — output better with these)

### C-05 | Surprise Diversity
- **Weight**: recommended
- **Category**: coverage
- **Text**: The surprises span meaningfully different dimensions — not
  three variations on the same theme. Diversity might be across namespace
  (e.g., one from flow, one from prove, one from scout), or across concern
  type (behavioral, structural, adoption, constraint).
- **Pass condition**: No two surprises are drawn from the same root cause
  or the same signal cluster. A reviewer should not be able to collapse
  any two surprises into one without loss of information.

### C-06 | Future-Team Framing
- **Weight**: recommended
- **Category**: behavior
- **Text**: The document reads as institutional memory written *for* the
  next team, not as a personal reflection. Language is durable: it does
  not assume the current team's context and frames surprises as
  transferable lessons.
- **Pass condition**: A reader with no prior context on this topic can
  understand each surprise, its source, and its design implication without
  asking a follow-up question.

### C-07 | Impact Specificity
- **Weight**: recommended
- **Category**: depth
- **Text**: Design impact statements are concrete and falsifiable. "Changes
  how throttle decisions are sequenced" passes. "Might affect design" or
  "worth noting" fails.
- **Pass condition**: Each impact clause names a specific artifact,
  decision, constraint, or behavior that changes as a result of the
  surprise. Vague consequences do not pass.

---

## Aspirational Criteria (10 pts — raise the bar)

### C-08 | Cross-Signal Synthesis
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one surprise synthesizes a pattern visible only across
  *multiple* signals — something no single signal would have revealed
  alone. This is the highest form of the echo: emergent insight from
  signal convergence.
- **Pass condition**: At least one surprise explicitly cites 2+ source
  signals and articulates why the surprise requires both to be visible.
  Single-source surprises, however well-written, do not satisfy this
  criterion.

### C-09 | Counterfactual Awareness
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one surprise includes a counterfactual: what decision
  would have been made, or what design would have been built, had this
  surprise not been discovered.
- **Pass condition**: At least one surprise contains an explicit "without
  this signal, we would have..." or equivalent clause that names a
  specific wrong turn that was avoided or a better path that was revealed.

### C-10 | Epistemic Delta Tracing
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one surprise makes the belief-before-signal explicit.
  Not just "the signal showed X" but "we assumed Y before this signal;
  the signal showed X; this changes Z." The prior assumption is named,
  not implied. All three clauses are required; omitting the third ("this
  changes Z") fails even if the first two are present.
- **Pass condition**: At least one surprise entry contains an explicit
  prior assumption ("we believed...", "the design assumed...", "prior to
  this signal, the expectation was..."), the finding that overturned it,
  *and* the design consequence. Entries that state the finding alone — even
  with strong source tracing (C-02) — do not satisfy this criterion.
- **Source**: V-04 R1 excellence. V-01 R2 enforcement: "Do not omit the
  third clause" made the full delta structure a hard requirement, not a
  style suggestion.

### C-11 | Confirmation Accounting
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The output explicitly records at least one finding that was
  reviewed and rejected as a confirmation — not just excluded, but named
  and classified. The ledger entry states the finding, classifies it as a
  confirmation (i.e., matched prior expectation), and names its
  destination (e.g., routed to topic-story). This makes gate execution
  verifiable: a future reader can confirm the gate ran and was not skipped.
- **Pass condition**: Output contains a confirmation ledger section (or
  equivalent) with at least one named entry classified as a confirmation.
  The section appears in the output artifact, not only in scaffolding.
  Omitting confirmed findings entirely fails even if all surprise entries
  are genuine.
- **Source**: V-03 R1 excellence. V-02 R2 mechanism: Phase 3 Confirmation
  Ledger as required output section with the explicit statement "a future
  reader can verify that the gate ran."

### C-12 | Collective Next-Team Signal
- **Weight**: aspirational
- **Category**: behavior
- **Text**: A dedicated synthesis block states what the surprises say
  *collectively* — a pattern, orientation, or implication non-derivable
  from reading the individual entries in sequence. The next team should
  be able to read only the collective block and have an accurate
  orientation to the topic's signal landscape.
- **Pass condition**: A synthesis block exists whose content cannot be
  reconstructed by concatenating or summarizing the individual surprise
  entries. If the block merely re-lists the surprises, it fails. PARTIAL
  if a synthesis block exists but is derivable from entries or omits the
  collective implication.
- **Source**: V-04 R1 excellence. The "what do the surprises tell the next
  team *collectively*?" question produced output distinct from both C-06
  (individual framing) and C-08 (cross-signal mechanics).

### C-13 | Collective Brief First-Position Ordering
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The collective orientation block (C-12) leads the output
  artifact — it appears as the first substantive section, before any
  individual surprise entries. This structural ordering guarantees the
  next team encounters the collective pattern before detail, regardless
  of whether they read the full document. Durability is structural, not
  behavioral.
- **Pass condition**: The collective orientation block is the first
  substantive section of the artifact. Individual surprise entries follow
  it. An orientation block that appears after entries — however well
  written — does not satisfy this criterion. PARTIAL is not available:
  ordering is binary.
- **Source**: V-03 R2 excellence. V-01 and V-02 both received PARTIAL on
  C-12 because their synthesis was written after entries, permitting
  derivation. V-03's mechanism — brief drafted before entries, leading
  the artifact — is what distinguishes structural non-derivability from
  coincidental non-derivability.

### C-14 | Pre-Signal Belief Locking
- **Weight**: aspirational
- **Category**: depth
- **Text**: Prior beliefs about the topic are recorded and locked *before*
  signals are read — not reconstructed post-hoc. The pre-investigation
  belief record is referenced in the output, making C-10 (Epistemic Delta
  Tracing) independently verifiable: a scorer can confirm the prior
  assumption in an entry was held before investigation, not invented to
  fit the finding.
- **Pass condition**: The output references a pre-investigation belief
  record or ledger that predates signal reading. Entries that cite prior
  assumptions without this pre-lock record do not satisfy C-14, even if
  they fully satisfy C-10. PARTIAL if the pre-lock is referenced but its
  pre-investigation status is ambiguous.
- **Source**: V-01 R2 excellence. The Archaeologist/Chronicler split
  requires beliefs to be written and locked before any signal is read.
  This makes the epistemic delta in C-10 entries falsifiable — the prior
  is a datable artifact, not a recalled assumption.

---

## What Changed from v2 to v3

**Two new aspirational criteria extracted from Round 2 excellence
signals:**

### C-13 | Collective Brief First-Position Ordering
*Source: V-03 R2*

V-03 was the only variation that made the collective orientation brief
structurally lead the artifact. V-01 and V-02 received C-12 PARTIAL
because "no first-draft-before-entries constraint; no non-derivability
test" — their synthesis blocks were appended after entries and could be
derived from them. V-03's mechanism eliminates this ambiguity: the brief
is drafted first and precedes entries in the artifact. C-12 asks whether
the collective block is non-derivable; C-13 asks whether it structurally
precedes entries, making post-hoc derivation impossible by construction.

### C-14 | Pre-Signal Belief Locking
*Source: V-01 R2*

V-01's full PASS on C-10 was driven by the Archaeologist role writing
the belief ledger *before* any signals were read. V-02 received C-10
PARTIAL because a "prior assumption" field existed but with no required
delta sentence structure and no pre-lock mechanism. The distinction: C-10
requires the delta to appear in the entry; C-14 requires the prior
assumption to have been recorded before investigation, making the delta
independently verifiable rather than reconstructed. Without C-14, a
strong C-10 entry is unfalsifiable — we cannot know if the prior
assumption was held before or invented to fit the finding.

**Formula update:** aspirational denominator changes from `/ 5` to
`/ 7`. Max composite remains 100. Each full aspirational pass ≈ 1.43 pts
(vs. 2 pts in v2). The tier stays a ceiling bonus, not a score driver.
PARTIAL = 0.5 aspirational passes.
```

---

Two new criteria, both sourced from mechanisms the scorecard explicitly flagged as absent or partial in Round 2. C-13 closes the C-12 PARTIAL gap (brief-after-entries makes non-derivability coincidental, not structural). C-14 closes the C-10 PARTIAL gap in V-02 (prior assumption field without pre-lock makes the delta unverifiable).
