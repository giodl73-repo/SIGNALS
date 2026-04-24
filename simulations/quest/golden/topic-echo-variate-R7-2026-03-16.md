---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 7
rubric: v7
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v7-2026-03-16.md
---

# Variations: `topic:echo` — Round 7 (2026-03-16)

**Rubric:** v7 (2026-03-16) | **Criteria count:** 22 (4 essential / 3 recommended / 15 aspirational)

---

## Design Context

Two new aspirational criteria were added to the v7 rubric on 2026-03-16:

**C-21 | Enforcement Pipeline Staging** — enforcement mechanisms at ≥2 distinct pipeline
positions from {pre-gate, entry-gate, post-gate, synthesis-phase}, each naming a failure
class detectable *only* at its position. Pre-gate catches collection-level failures invisible
per-entry (e.g., namespace monoculture across the full candidate set). Post-gate catches
cross-entry relational failures invisible within a single entry (e.g., degree-variant pairs
that each pass individual validation). C-21 is orthogonal to C-20: two structural-scope
mechanisms at different pipeline positions are additive under C-21 even if C-20 calls them
scope-redundant.

**C-22 | Synthesis Verdict Commitment** — every verdict-bearing synthesis section commits
to exactly two valid terminal states; hedged-language forms are explicitly named as FAIL
conditions; no-verdict (field absent or empty) is itself a FAIL. The commitment contract
turns a synthesis section into an integration-ready judgment rather than a reader-burdening
narrative. Cross-reference: C-22 FAIL → C-13 cannot exceed PARTIAL.

**Strategy for R7 variations:**
- V-01: Single-axis — C-21 (enforcement pipeline staging)
- V-02: Single-axis — C-22 (synthesis verdict commitment)
- V-03: Single-axis — phrasing register (embedded directive vs. formal declaration blocks)
- V-04: Combination — C-21 + C-22
- V-05: Full combination — C-21 + C-22 + inertia framing (pre-investigation assumption as
  named competitor)

All variations build on the R6 best state: two roles with function declaration, typed
routing, three-stage epistemic gate with anti-pattern catalog, comparative triage, naming
scaffold, co-validation gate, echo entries, cross-signal synthesis, forward handover, rules
of thumb.

---

## V-01 — Pipeline Staging Axis (C-21)

**Variation axis**: Lifecycle emphasis — enforcement mechanisms placed at three distinct
pipeline positions (pre-gate, entry-gate, post-gate), each naming the failure class visible
only at that position.

**Hypothesis**: A multi-stage epistemic gate (entry-gate) screens each candidate in
isolation. It cannot detect collection-level failure (namespace monoculture across all
candidates) or cross-entry relational failure (degree-variant pairs that each pass
individually). Placing a pre-gate check before entry-gate validation and a post-gate check
after all entries have cleared individual validation closes both failure classes. The model
executing this prompt has a structural map of which pipeline position runs which check and
why no other position could catch the same failure.

**Builds on**: R6 best state — all C-01..C-20 mechanisms active (two roles with function
declaration, typed routing, three-stage gate, comparative triage, naming scaffold,
co-validation gate, echo entries, synthesis, handover, rules of thumb).

**New elements targeting C-21**: Step 1b (PRE-GATE position) and Step 6b (POST-GATE
position), each with explicit pipeline position label and per-position failure class.

---

You are running `/topic:echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface what those signals revealed that no
competent practitioner would have predicted before the investigation began.

Not a summary. Not a survey of discoveries. An echo: the signal that comes back that you
did not send, visible only in retrospect from cross-signal tension.

---

### Roles

**Institutional Archaeologist (IA)** — active Steps 2, 5, 7, 8, 9.
Recovers false assumptions embedded in existing materials — what a future team would carry
as truth without knowing otherwise. Frames every surprise as a correction to a false
assumption, not as a description of a discovery. The IA's orienting question: "What would
the next team build wrong because they did not know what you now know?"

**Gatekeeper** — first invoked Step 3.

```
GATEKEEPER — FUNCTION DECLARATION
──────────────────────────────────────────────────────────────────
Function:     Adversarial rejection. Tests each gate-pipeline candidate
              against two criteria: (1) Could a competent practitioner
              have predicted it from first principles before any signal
              gathering? (2) Does it emerge from cross-signal reading, or
              from a single artifact in isolation? Fails either → rejected.

Not-function: Future-reader framing. The Gatekeeper does not ask what a
              future team would get wrong — that is the IA's domain. The
              IA's perspective is not consulted during gate evaluation.

Not-function: Thematic synthesis or cross-item grouping. The Gatekeeper
              evaluates each candidate independently, not relationally.

Role boundary: Gate rejections are final. The IA cannot reverse a gate
               rejection. One role tests plausibility; the other frames
               implication. They do not overlap.
──────────────────────────────────────────────────────────────────
```

---

### Step 1 — Read Signal Record *(C-10, C-12)*

Read all signal artifacts across all namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record:
- Namespaces covered (list each; ≥3 required)
- Date range of artifacts (earliest → latest)

---

### Step 1b — PRE-GATE: Namespace Diversity Check *(C-21; pipeline position: pre-gate)*

**Pipeline position**: pre-gate — runs before any per-entry validation. This is the only
position that can see collection-level properties across all candidates simultaneously.

**Failure class detectable here only**: *Collection-level namespace monoculture* — all
gate-pipeline candidates originating from a single namespace. Each candidate's namespace
assignment is individually valid; no per-entry check can detect that the full candidate set
lacks namespace diversity. This failure only manifests when counting distinct namespace
segments across the complete candidate pool.

Action: From Step 1, count distinct namespaces represented in the full candidate pool.

If < 2 distinct namespaces: **PRE-GATE BLOCK**. The candidate pool lacks namespace
diversity. Do not proceed to Step 2 or Step 3. Return: "Echo blocked: all candidates from
a single namespace. Broaden signal coverage before running topic:echo."

If ≥ 2 distinct namespaces: **PRE-GATE CLEAR**. Record the namespace count and proceed.

---

### Step 2 — Pre-Write Prediction Sort *(IA; C-16, C-11)*

Assign a typed route to every finding before any gate evaluation:

- `topic-story` — confirms a working hypothesis; routes downstream to topic narrative
- `topic-report` — restates a known constraint; routes to report
- `gate-pipeline` — candidate surprise; not present in pre-investigation frame; proceeds
  to Step 3

Anti-hypothesis guard *(C-11)*: explicitly check — "Does this confirm what we set out to
prove?" Confirmed hypotheses route to `topic-story` regardless of apparent novelty.

*(IA)* Co-validation per `gate-pipeline` item: "A new team approaching from the spec alone
would not have encountered this finding."

Discard log *(C-09)*: record every finding routed to `topic-story` or `topic-report` with
its route reason and typed downstream destination. A non-empty discard log is a
prerequisite; an empty log indicates the filter was not applied.

---

### Step 3 — ENTRY-GATE: Multi-Stage Epistemic Gate *(Gatekeeper; C-13; pipeline position: entry-gate)*

**Pipeline position**: entry-gate — validates each candidate independently. Catches
per-entry structural failures: predictable findings, restatements, isolated single-artifact
items. Cannot detect collection-level properties (pre-gate territory) or cross-entry
relationships (post-gate territory).

**Anti-Pattern Catalog** — Gatekeeper applies per candidate:
- CONFIRMATION: confirms original hypothesis → PREDICTABLE regardless of stage
- RESTATEMENT: restates a known constraint → route to `topic-report`
- ISOLATED-FINDING: exists in one artifact only → route to `topic-report` at Stage 3

Three sequential stages. Write each stage verdict before proceeding to the next. Do not
collapse stages into a combined verdict — collapse prohibition applies absolutely.

**Stage 1 — Prediction Test** *(Gatekeeper)*
Gate question: "Would a competent practitioner have predicted this from first principles,
prior to any signal gathering?"
`PREDICTABLE` → discard; log in discard log
`UNPREDICTABLE` → proceed to Stage 2
Commit: `Stage 1: [{item}] → [PREDICTABLE | UNPREDICTABLE]`

**Stage 2 — Contradiction Test** *(Gatekeeper)*
Gate question: "Does this item contradict, complicate, or qualify an assumption from the
pre-investigation frame?"
We believed: `{falsifiable pre-investigation assumption}`
VALID: `{case that genuinely falsifies the belief — names the specific assumption contradicted}`
INVALID (absence-of-consideration): `{notes absence of something, not falsification of a held belief}`
INVALID (sentiment-reaction): `{expresses surprise without naming the contradicted assumption}`
INVALID (hedge-uncertainty): `{hedges on whether the belief was ever actually held}`
`NO CONTRADICTION` → discard | `CONTRADICTION FOUND` → Stage 3
Commit: `Stage 2: [{item}] → [NO CONTRADICTION | CONTRADICTION FOUND]`

**Stage 3 — Attribution Test** *(Gatekeeper)*
Gate question: "Does this finding emerge from cross-signal reading, or from one artifact alone?"
`SINGLE-ARTIFACT` → discard | `CROSS-SIGNAL (cite ≥2 artifacts)` → verdict SURPRISE
Commit: `Stage 3: [{item}] → [SINGLE-ARTIFACT | CROSS-SIGNAL] — sources: [{artifact1 (ns/skill)}, {artifact2 (ns/skill)}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23)*

Assign HIGH/MEDIUM/LOW comparatively — compare all SURPRISE candidates against each other
before assigning any tier. No tier is assigned in isolation.

- **HIGH**: Forces revision to a core design decision, assumption, or scope boundary
- **MEDIUM**: Qualifies a design principle or adds a constraint to an existing decision
- **LOW**: Notable but no clear design consequence at present

Record triage assignments. Write entries HIGH → MEDIUM → LOW.

---

### Step 5 — Naming Scaffold *(C-17)*

For each SURPRISE candidate, derive the name before writing any entry:

1. State the old belief: "The team carried the assumption that ___."
2. State the correction: "The signals revealed instead that ___."
3. Derive the domain: "This affects the ___ area of the design."
4. Form the label: `The {Corrected Belief}: {Domain}`

VALID: "The Silent Veto: Adoption Workflow"
INVALID: "Surprising Finding About Adoption" — discovery register, not correction register

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20)*

Before expanding any entry, co-validate two fields simultaneously:

- **Name form** *(C-17)*: does the label follow `The {Corrected Belief}: {Domain}`?
- **Failure field** *(C-18)*: does the failure read as "If the next team carries the old
  assumption, {specific concrete failure — a named mis-design, not a change-list}"?

Both must be VALID. If either fails, revise before expanding. A failed co-validation blocks
entry expansion; do not skip.

---

### Step 6b — POST-GATE: Pairwise Redundancy Check *(C-21; pipeline position: post-gate)*

**Pipeline position**: post-gate — runs after all entries have cleared entry-gate
validation. This is the only position that can see cross-entry relationships. A per-entry
check cannot detect that two entries name variants of the same underlying correction.

**Failure class detectable here only**: *Degree-variant pairs* — two entries that each
pass all three entry-gate stages (both unpredictable, both contradictions, both
cross-signal) but name the same underlying correction at different granularities or
framings. Each entry is individually valid; the pair is collectively redundant. Only
detectable by direct cross-entry comparison after all entries have passed individual
validation.

Action: Run exhaustive N*(N-1)/2 pairwise comparison across all SURPRISE entries that
cleared Step 3.

For each pair:
- Do both entries correct the same pre-investigation assumption, even if framed differently?
- If YES: merge the pair into one entry (selecting the framing that scores highest on
  the naming scaffold) or exclude the weaker entry. State rationale for decision.
- If NO: record "pair [{A}] × [{B}]: distinct corrections — proceed."

If any merges or exclusions occur: update the discard log with reason `post-gate-redundancy`.

**POST-GATE COMPLETE**: record final SURPRISE count after redundancy resolution.

---

### Step 7 — Write Echo Entries *(IA perspective; triage order)*

For each SURPRISE entry (HIGH → MEDIUM → LOW):

---

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})`
*(If multiple sources: list all. Annotate as `[CROSS: {artifact-A} × {artifact-B}]` if C-08)*

Temporal anchor *(C-12)*: `{round or date of earliest source signal}`

We believed: `{falsifiable pre-investigation assumption}`

The surprise: `{what the signals revealed that contradicts or complicates that assumption}`

If the next team carries the old assumption *(C-18)*: `{specific concrete mis-design that
results — name the wrong component built, the wrong decision made, the wrong constraint
ignored}`.

Downstream route *(C-14)*: `→ {topic-story | draft-proposal | trace-component | other skill}`

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA)*

One paragraph, ≤120 words.

Name ≥2 SURPRISE entries by their labels and explain why the pattern they form only emerges
from reading those entries together — it cannot be derived from either entry alone.

*(IA)*: How do the current materials — collectively — create a misleading picture for a
future team arriving without context?

---

### Step 9 — Forward Handover Guidance *(C-06; IA)*

Select register from the following menu. Match the register to the most actionable
downstream route from Step 7.

- T-1 (builder): "If you are about to build {scenario}, know that {constraint} because {source}."
- T-2 (reviewer): "Before approving {decision}, verify {constraint} against {source}."
- T-3 (PM): "Scope the {area} decision against {constraint} found in {source}."
- T-4 (architect): "The {component} design assumes {belief}; {source} shows this is false."

Verify that all slot values are filled from specific artifacts before writing the final
statement. Vague slots ("the signals", "our research") are not permitted.

---

### Step 10 — Rules of Thumb *(C-24)*

≤3 rules. HIGH and MEDIUM surprises only. LOW surprises do not generate rules.

```
[{HIGH | MEDIUM}] {Rule — ≤20 words, quotable as standalone heuristic}
(encodes: {SURPRISE NAME})
```

Traceability check *(C-24)*: for each rule, verify that its impact tier matches the named
surprise's triage tier from Step 4. If mismatch: correct before producing output.

---

**Output**: Steps 7–10 only. Steps 1–6b are execution scaffolding; do not include them in
the final artifact.

Sequence: Echo entries (triage-ordered, POST-GATE count verified) → Cross-signal synthesis
→ Forward handover → Rules of thumb.

If the PRE-GATE blocked in Step 1b, the output is the block notice only.

---

---

## V-02 — Synthesis Verdict Commitment Axis (C-22)

**Variation axis**: Output format — every verdict-bearing synthesis section commits to
exactly two valid terminal states; hedged-language forms are explicitly listed as FAIL
conditions; no-verdict is itself a FAIL.

**Hypothesis**: A synthesis section that ends with "the echo appears complete" or "coverage
is generally sufficient" transfers the integration decision to the reader. Making binary
commitment the only valid terminal state — with hedged forms explicitly named as FAIL
conditions and no-verdict treated as equivalent to a hedged verdict — creates a commitment
contract. The model executing this prompt cannot produce a compliant output without
resolving each synthesis section to a binary state unconditionally.

**Builds on**: R6 best state — all C-01..C-20 mechanisms active.

**New elements targeting C-22**: Verdict commitment blocks added to Step 8 (Cross-Signal
Synthesis) and Step 1c (Signal Coverage Meta-Reflection). Each block: declares two valid
terminal states, lists ≥2 hedged-language forms as FAIL conditions, names no-verdict as FAIL.

---

You are running `/topic:echo` for the topic: {topic}.

All essential signals are in hand. Surface what those signals revealed that no competent
practitioner would have predicted before the investigation began.

Not a summary. An echo: the signal that comes back that you did not send.

---

### Roles

**Institutional Archaeologist (IA)** — active Steps 1c, 2, 5, 7, 8, 9.
Holds the perspective of a future team arriving at this topic without the context earned
through investigation. Recovers false assumptions; frames every surprise as a correction.

**Gatekeeper** — active Step 3.

```
GATEKEEPER — FUNCTION DECLARATION
──────────────────────────────────────────────────────────────────
Function:     Adversarial rejection. Tests predictability from first
              principles (Stage 1) and cross-signal emergence vs.
              single-artifact isolation (Stage 3).

Not-function: Future-reader framing (IA domain).
Not-function: Thematic synthesis or cross-item grouping (IA domain).

Role boundary: Gate rejections are final. IA cannot override.
──────────────────────────────────────────────────────────────────
```

---

### Step 1 — Read Signal Record *(C-10, C-12)*

Read all signal artifacts across all namespaces. Record: namespaces covered (list each;
≥3 required), date range (earliest → latest).

---

### Step 1c — Signal Coverage Meta-Reflection *(C-13; C-22 verdict)*

Assess signal coverage before proceeding:
- List each namespace reached and count artifacts per namespace
- Name any namespace in scope (scout, draft, review, flow, trace, prove, listen, program,
  topic) that contributed zero artifacts
- State whether uncovered namespaces represent material gaps or acceptable scope limits

**Verdict commitment** *(C-22)*:

Declare one of exactly two valid terminal states:
```
COVERAGE VERDICT: COMPLETE
  — all in-scope namespaces have contributed at least one artifact; no material gaps
COVERAGE VERDICT: INCOMPLETE
  — [name specific namespace(s)] contributed zero artifacts; signals in those
    namespaces could contain surprises not visible in the current candidate pool
```

FAIL forms — the following are not valid verdicts and must not appear as terminal states:
- "coverage appears sufficient"
- "most namespaces are represented"
- "generally covered"
- "coverage seems adequate"
- Any graduated or probabilistic statement ("80% coverage", "largely complete")
- No verdict (verdict field absent or empty) — treated as INCOMPLETE by default; state
  explicitly if that is the intent

If INCOMPLETE: note the gap. Continue — an incomplete signal set can still yield an echo;
the incompleteness must be surfaced, not silently accepted.

---

### Step 2 — Pre-Write Prediction Sort *(IA; C-16, C-11)*

Typed route per finding:
- `topic-story` — confirms hypothesis
- `topic-report` — restates known constraint
- `gate-pipeline` — candidate surprise; not in pre-investigation frame

Anti-hypothesis guard *(C-11)*: "Does this confirm what we set out to prove?" → `topic-story`.
*(IA)* co-validation: "A new team from the spec alone would not have encountered this."

Discard log *(C-09)*: record all routed items with typed route reason.

---

### Step 3 — Multi-Stage Epistemic Gate *(Gatekeeper; C-13)*

Anti-Pattern Catalog: CONFIRMATION / RESTATEMENT / ISOLATED-FINDING.
Three stages. Per-stage commits. Collapse prohibition.

**Stage 1 — Prediction Test** *(Gatekeeper)*
"Would a competent practitioner have predicted this?"
`PREDICTABLE` → discard | `UNPREDICTABLE` → Stage 2
Commit: `Stage 1: [{item}] → [{verdict}]`

**Stage 2 — Contradiction Test** *(Gatekeeper)*
"Does this contradict the pre-investigation frame?"
We believed: `{falsifiable assumption}`
VALID: `{genuine falsification}` | INVALID (absence-of-consideration / sentiment-reaction /
hedge-uncertainty): `{describe type}`
`NO CONTRADICTION` → discard | `CONTRADICTION FOUND` → Stage 3
Commit: `Stage 2: [{item}] → [{verdict}]`

**Stage 3 — Attribution Test** *(Gatekeeper)*
"Cross-signal or single-artifact?"
`SINGLE-ARTIFACT` → discard | `CROSS-SIGNAL (cite ≥2)` → SURPRISE
Commit: `Stage 3: [{item}] → [{verdict}] — sources: [{artifact1 (ns/skill)}, {artifact2 (ns/skill)}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23)*

HIGH / MEDIUM / LOW comparatively across all SURPRISE candidates before any expansion.
- HIGH: forces revision to core design decision, assumption, or scope boundary
- MEDIUM: qualifies principle or adds constraint to existing decision
- LOW: notable; no current design consequence

Write entries HIGH → MEDIUM → LOW.

---

### Step 5 — Naming Scaffold *(C-17)*

For each candidate:
1. Old belief: "The team carried the assumption that ___."
2. Correction: "The signals revealed instead that ___."
3. Domain: "This affects the ___ area."
4. Label: `The {Corrected Belief}: {Domain}`

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20)*

Before expanding any entry, co-validate simultaneously:
- Name form passes `The {Corrected Belief}: {Domain}` *(C-17)* → VALID / INVALID
- Failure field reads as "If the next team carries the old assumption, {specific mis-design}"
  *(C-18)* → VALID / INVALID

Both VALID to proceed. Either fails → revise before expanding.

---

### Step 7 — Write Echo Entries *(IA; triage order)*

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} × {artifact-B}]` *(if C-08)*
Temporal anchor *(C-12)*: `{round or date}`
We believed: `{falsifiable pre-investigation assumption}`
The surprise: `{what signals revealed}`
If the next team carries the old assumption *(C-18)*: `{specific concrete mis-design}`.
Downstream route *(C-14)*: `→ {skill or namespace}`

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA)*

One paragraph, ≤120 words.

Name ≥2 SURPRISE entries by their labels. Explain why the pattern they form only emerges
from reading them together — not derivable from either entry alone.

*(IA)*: How do the current materials collectively create a misleading picture for a future
team?

**Verdict commitment** *(C-22)*:

Declare one of exactly two valid terminal states:
```
ECHO VERDICT: ECHOES PRESENT
  — ≥2 entries with distinct corrections; cross-signal pattern named; surprise synthesis
    is complete and integration-ready
ECHO VERDICT: ECHOES ABSENT
  — fewer than 2 entries cleared all gate stages; or all entries trace to a single artifact;
    cross-signal synthesis cannot proceed; output is a finding record, not an echo
```

FAIL forms — the following are not valid verdicts:
- "the echo appears complete"
- "surprises are generally sufficient"
- "seems like a strong synthesis"
- Any graduated verdict ("partial echo", "mostly complete")
- No verdict (verdict field absent or empty)

---

### Step 9 — Forward Handover Guidance *(C-06; IA)*

Register menu: T-1 (builder) / T-2 (reviewer) / T-3 (PM) / T-4 (architect).
Select register matching most actionable downstream route. Fill all slots from specific
artifacts before writing.

---

### Step 10 — Rules of Thumb *(C-24)*

≤3 rules. HIGH and MEDIUM surprises only.

```
[{HIGH | MEDIUM}] {Rule — ≤20 words}
(encodes: {SURPRISE NAME})
```

Traceability check: each rule's tier must match its named surprise's triage tier from
Step 4. Correct mismatches before output.

---

**Output**: Steps 1c verdict + Steps 7–10. Steps 2–6 are execution scaffolding.

Sequence: Signal coverage verdict → Echo entries (triage-ordered) → Cross-signal synthesis
with echo verdict → Forward handover → Rules of thumb.

---

---

## V-03 — Phrasing Register Axis (embedded directive)

**Variation axis**: Phrasing register — formal declaration blocks (FUNCTION DECLARATION,
labeled header boxes) replaced by inline directive language; structural constraints
embedded in step instructions rather than announced in separate labeled sections.

**Hypothesis**: The formal FUNCTION DECLARATION block is a clear structural signal, but
adds visual overhead and may train the model to treat "declared sections" as the only
constraint-bearing elements. Testing whether embedding the same structural constraints as
direct imperatives ("Do X. Do not Y. The boundary: Z.") achieves equivalent role clarity
and pipeline staging, while also producing a more scannable, execution-dense prompt.

**Builds on**: R6 best state. Adds C-21 (pipeline staging via inline position callouts)
without formal block declarations.

**New element targeting C-21**: Inline `[PRE-GATE]` and `[POST-GATE]` position markers
embedded directly in step instructions, each with an inline failure-class clause.

---

You are running `/topic:echo` for the topic: {topic}.

All essential signals are in hand. One question: what did the signals reveal that no
competent practitioner would have predicted before gathering them?

Not a summary. An echo: what only becomes visible in retrospect.

---

Two roles operate throughout:

**Institutional Archaeologist (IA)**: active in Steps 2, 5, 7, 8, 9. Recover false
assumptions. Frame every surprise as a correction to a false belief, not as a description
of a new discovery. Default question: "What would the next team build wrong?"

**Gatekeeper**: active in Step 3 only. Reject on predictability and single-artifact
grounds. Do not frame for future teams — that is IA's job. Do not synthesize across
items — evaluate each candidate independently. Rejections are final; IA cannot override.

---

**Step 1.** Read all signal artifacts across all namespaces. List namespaces reached and
date range. This is your signal inventory.

**Step 1b. [PRE-GATE — run before any per-entry validation]** Count distinct namespace
segments across all candidates. If all candidates come from a single namespace, stop here:
"Echo blocked: namespace monoculture. Broaden signal coverage before proceeding." Why this
check must run here: per-entry validation cannot see the collection-level namespace count —
each candidate's namespace is valid in isolation; the monoculture only manifests across the
full set.

---

**Step 2. [IA]** Route every finding before gate evaluation. Three routes only:
`topic-story` (confirms hypothesis → downstream to narrative), `topic-report` (known
constraint → downstream to report), `gate-pipeline` (not in pre-investigation frame →
proceeds to Step 3).

Anti-hypothesis guard: ask "Does this confirm what we set out to prove?" before routing
any item. Confirmed hypotheses go to `topic-story` regardless of how surprising they seem.

Co-validate each `gate-pipeline` item: "A new team from the spec alone would not have
encountered this." Items that fail this test route to `topic-report`.

Record all routed items in a discard log with route reason and typed downstream destination.
An empty discard log is a process failure, not a clean result.

---

**Step 3. [ENTRY-GATE — per-entry validation; runs one candidate at a time]**

Gatekeeper runs three stages per candidate. Write each verdict before moving to the next
stage. Do not combine stages into one verdict.

Anti-pattern catalog (Gatekeeper applies to each candidate): CONFIRMATION (confirms
hypothesis → reject regardless of stage); RESTATEMENT (restates known constraint →
`topic-report`); ISOLATED-FINDING (one artifact only → reject at Stage 3).

*Stage 1 — Prediction Test.* "Would a competent practitioner have predicted this?" PREDICTABLE → discard and log. UNPREDICTABLE → Stage 2. Write: `Stage 1: [{item}] → [{verdict}]`.

*Stage 2 — Contradiction Test.* "Does this contradict or complicate the pre-investigation
frame?" State the belief being tested: `We believed: {falsifiable assumption}`. Mark VALID
only if a held belief is genuinely falsified — not if something was merely absent from
consideration, not if the item only expresses surprise without naming the assumption. NO
CONTRADICTION → discard and log. CONTRADICTION FOUND → Stage 3. Write: `Stage 2: [{item}] → [{verdict}]`.

*Stage 3 — Attribution Test.* "Cross-signal emergence or single artifact?" SINGLE-ARTIFACT
→ discard and log. CROSS-SIGNAL (cite ≥2 artifacts) → SURPRISE. Write: `Stage 3: [{item}] → [{verdict}] — sources: [{artifact1 (ns/skill)}, {artifact2}]`.

Why entry-gate cannot see everything: it validates each candidate independently. It cannot
detect that two candidates that each pass all three stages name variants of the same
underlying correction. That is post-gate territory.

---

**Step 4.** Assign HIGH / MEDIUM / LOW to all SURPRISE candidates comparatively — compare
all against each other before assigning any tier, not one at a time. HIGH: forces revision
to a core design decision. MEDIUM: qualifies a principle or adds a constraint. LOW: notable,
no current design consequence. Write entries HIGH → MEDIUM → LOW.

---

**Step 5. [IA]** Derive each name before writing any entry:
1. Old belief: "The team carried the assumption that ___."
2. Correction: "The signals revealed instead that ___."
3. Domain: "This affects the ___ area."
4. Label: `The {Corrected Belief}: {Domain}`.
INVALID: "Surprising Finding About X" — that is discovery register, not correction register.

---

**Step 6.** Before expanding any entry, check two things simultaneously: (a) does the
label follow `The {Corrected Belief}: {Domain}`? (b) does the failure clause read as a
specific concrete mis-design, not a general recommendation? Both must pass. If either
fails, revise first. Do not skip this check to save time.

---

**Step 6b. [POST-GATE — cross-entry check; runs after all entries pass Step 6]** Compare
every pair of SURPRISE entries. For each pair: do both entries correct the same underlying
pre-investigation assumption, even if framed differently? If yes: merge into one entry
(keep the framing that better satisfies the naming scaffold) or exclude the weaker one with
stated rationale. Log any merges or exclusions as `post-gate-redundancy`. Why this check
must run here: per-entry validation cannot see that two valid entries are degree-variants
of each other — the redundancy only becomes visible when comparing entries side by side
after all have cleared individual validation.

---

**Step 7. [IA]** Write echo entries in triage order (HIGH → MEDIUM → LOW). For each:

`The {Corrected Belief}: {Domain}` — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})` — `[CROSS: {A} × {B}]` if cross-signal.
Temporal anchor: `{round or date}`.
We believed: `{falsifiable pre-investigation assumption}`.
The surprise: `{what the signals revealed}`.
If the next team carries the old assumption: `{specific concrete mis-design}`.
Downstream route: `→ {skill or namespace}`.

---

**Step 8. [IA]** Cross-signal synthesis, ≤120 words. Name ≥2 SURPRISE entries by label.
Explain why the pattern they form only emerges from reading them together. Ask: how do the
current materials collectively mislead a future team?

---

**Step 9. [IA]** Forward handover. Pick a register: T-1 (builder: "If you are about to
build {X}, know that {constraint} because {source}"), T-2 (reviewer: "Before approving
{X}, verify {constraint} against {source}"), T-3 (PM: "Scope {area} against {constraint}
found in {source}"), T-4 (architect: "{Component} assumes {belief}; {source} shows this is
false"). Fill all slots from specific artifacts.

---

**Step 10.** Rules of thumb: ≤3 rules, HIGH and MEDIUM surprises only. Format: `[{tier}]
{Rule — ≤20 words} (encodes: {SURPRISE NAME})`. Before writing each rule, confirm the
tier in brackets matches the triage tier assigned in Step 4. Correct any mismatch first.

---

**Output**: Steps 7–10 only. Include the POST-GATE entry count from Step 6b as a one-line
header before the entries.

---

---

## V-04 — Combination: C-21 + C-22

**Variation axis**: Combination — lifecycle emphasis (pipeline staging) + output format
(verdict commitment).

**Hypothesis**: C-21 and C-22 address orthogonal dimensions: C-21 governs *when* in the
pipeline enforcement checks run; C-22 governs *what form* synthesis verdicts take. They
share no mechanism and cannot interfere. A variation that satisfies both simultaneously
should score additively on both criteria. The combined prompt adds a pre-gate namespace
check, a post-gate redundancy check (C-21), and binary verdict blocks in the signal
coverage meta-reflection and cross-signal synthesis sections (C-22).

**Builds on**: R6 best state — all C-01..C-20 active.

**New elements**: Step 1b (PRE-GATE, C-21), Step 6b (POST-GATE, C-21), Step 1c verdict
block (C-22), Step 8 verdict block (C-22).

---

You are running `/topic:echo` for the topic: {topic}.

All essential signals are in hand. Your task: surface what those signals revealed that no
competent practitioner would have predicted before the investigation began.

Not a summary. Not a survey. An echo — the signal that comes back that you did not send.

---

### Roles

**Institutional Archaeologist (IA)** — active Steps 1c, 2, 5, 7, 8, 9.
Recovers false assumptions embedded in existing materials. Frames every surprise as a
correction to a false assumption held before the investigation, not as a description of a
discovery made during it. Orienting question: "What would the next team build wrong without
this knowledge?"

**Gatekeeper** — first invoked Step 3.

```
GATEKEEPER — FUNCTION DECLARATION
──────────────────────────────────────────────────────────────────
Function:     Adversarial rejection. Tests predictability (Stage 1),
              genuine contradiction of a held belief (Stage 2), and
              cross-signal emergence vs. single-artifact isolation (Stage 3).

Not-function: Future-reader framing (IA domain — not Gatekeeper domain).
Not-function: Synthesis or cross-item grouping (IA domain).

Role boundary: Gate rejections are final. IA cannot reverse.
              Entry-gate evaluates candidates independently; collection-
              level and cross-entry failures are handled at other pipeline
              positions, not here.
──────────────────────────────────────────────────────────────────
```

---

### Step 1 — Read Signal Record *(C-10, C-12)*

Read all signal artifacts across all namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic). Record:
- Namespaces covered (list each; ≥3 required)
- Date range (earliest → latest)
- Total artifact count per namespace

---

### Step 1b — PRE-GATE: Namespace Diversity Check *(C-21)*

**Pipeline position: pre-gate** — before any per-entry validation.
**Failure class unique to this position**: collection-level namespace monoculture. All
candidates from a single namespace; each entry's namespace is individually valid, so the
monoculture is invisible to per-entry checks.

Count distinct namespace segments in the full candidate pool.

- < 2 distinct namespaces: **PRE-GATE BLOCK**. Echo blocked: namespace monoculture.
  Broaden signal coverage before running topic:echo.
- ≥ 2 distinct namespaces: **PRE-GATE CLEAR**. Record count and proceed.

---

### Step 1c — Signal Coverage Meta-Reflection *(C-13; C-22 verdict)* *(IA)*

Assess which namespaces contributed candidates and which did not. Name any namespace with
zero contribution. State whether gaps represent material blind spots or acceptable scope
limits.

**Verdict commitment** *(C-22)*: Declare exactly one of two valid terminal states —

```
COVERAGE VERDICT: COMPLETE
  — all in-scope namespaces contributed ≥1 candidate; no material blind spots
COVERAGE VERDICT: INCOMPLETE
  — [list namespace(s)] contributed zero candidates; blind spots named above
```

FAIL — these are not valid verdicts:
- "coverage appears sufficient" / "most areas are covered" / "largely complete"
- Any graduated or probabilistic statement
- No verdict (verdict field absent = treated as INCOMPLETE; state explicitly)

---

### Step 2 — Pre-Write Prediction Sort *(IA; C-16, C-11)*

Typed route per finding:
- `topic-story` — confirms hypothesis
- `topic-report` — restates known constraint
- `gate-pipeline` — candidate surprise; not in pre-investigation frame

Anti-hypothesis guard *(C-11)*: "Does this confirm what we set out to prove?" → `topic-story`.
*(IA)* co-validation: "A new team from the spec alone would not have encountered this."

Discard log *(C-09)*: record all routed items with typed route reason and downstream
destination. Non-empty log is a prerequisite.

---

### Step 3 — ENTRY-GATE: Multi-Stage Epistemic Gate *(Gatekeeper; C-13)*

**Pipeline position: entry-gate** — per-candidate validation. Cannot see collection-level
properties (pre-gate) or cross-entry relationships (post-gate).

Anti-Pattern Catalog: CONFIRMATION / RESTATEMENT / ISOLATED-FINDING — Gatekeeper applies per candidate.

Three stages. Per-stage commit. Collapse prohibition absolute.

**Stage 1 — Prediction Test** *(Gatekeeper)*
"Would a competent practitioner have predicted this?"
`PREDICTABLE` → discard | `UNPREDICTABLE` → Stage 2
Commit: `Stage 1: [{item}] → [{verdict}]`

**Stage 2 — Contradiction Test** *(Gatekeeper)*
"Does this contradict or complicate the pre-investigation frame?"
We believed: `{falsifiable assumption}`
VALID: `{genuine falsification}`
INVALID (absence-of-consideration): `{names absence, not falsified belief}`
INVALID (sentiment-reaction): `{surprise without named assumption}`
INVALID (hedge-uncertainty): `{hedges on whether belief was held}`
`NO CONTRADICTION` → discard | `CONTRADICTION FOUND` → Stage 3
Commit: `Stage 2: [{item}] → [{verdict}]`

**Stage 3 — Attribution Test** *(Gatekeeper)*
"Cross-signal emergence or single artifact?"
`SINGLE-ARTIFACT` → discard | `CROSS-SIGNAL (cite ≥2)` → SURPRISE
Commit: `Stage 3: [{item}] → [{verdict}] — sources: [{artifact1 (ns/skill)}, {artifact2}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23)*

HIGH / MEDIUM / LOW comparatively across all SURPRISE candidates before any expansion.
HIGH → revision to core decision. MEDIUM → qualifies principle or adds constraint. LOW →
notable, no current consequence. Write entries HIGH → MEDIUM → LOW.

---

### Step 5 — Naming Scaffold *(C-17)*

For each candidate:
1. Old belief: "The team carried the assumption that ___."
2. Correction: "The signals revealed instead that ___."
3. Domain: "This affects the ___ area."
4. Label: `The {Corrected Belief}: {Domain}`

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20)*

Simultaneously before expanding any entry:
- Name form passes `The {Corrected Belief}: {Domain}` *(C-17)* → VALID / INVALID
- Failure field reads as "If the next team carries the old assumption, {specific mis-design}"
  *(C-18)* → VALID / INVALID

Both VALID to proceed. Either fails → revise. Do not skip.

---

### Step 6b — POST-GATE: Pairwise Redundancy Check *(C-21)*

**Pipeline position: post-gate** — after all entries have cleared entry-gate.
**Failure class unique to this position**: degree-variant pairs. Two entries that each
pass all three entry-gate stages but name variants of the same underlying correction. Each
entry is individually valid; the pair is collectively redundant. Invisible per-entry;
detectable only by direct cross-entry comparison.

Exhaustive N*(N-1)/2 pairwise comparison across all SURPRISE entries.

For each pair: "Do both entries correct the same underlying pre-investigation assumption,
even if framed at different granularities?"
- YES: merge (keep the stronger framing) or exclude weaker with stated rationale. Log as
  `post-gate-redundancy`.
- NO: record "pair [{A}] × [{B}]: distinct corrections — proceed."

Record final SURPRISE count after redundancy resolution.

---

### Step 7 — Write Echo Entries *(IA; triage order)*

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} × {artifact-B}]` *(C-08 if cross-signal)*
Temporal anchor *(C-12)*: `{round or date}`
We believed: `{falsifiable pre-investigation assumption}`
The surprise: `{what signals revealed}`
If the next team carries the old assumption *(C-18)*: `{specific concrete mis-design}`.
Downstream route *(C-14)*: `→ {skill or namespace}`

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA)*

≤120 words. Name ≥2 SURPRISE entries by label. Explain why the pattern only emerges from
reading them together — not derivable from either entry alone.

*(IA)*: How do the current materials collectively mislead a future team?

**Verdict commitment** *(C-22)*: Declare exactly one of two valid terminal states —

```
ECHO VERDICT: ECHOES PRESENT
  — ≥2 entries with distinct corrections; cross-signal pattern is named and
    integration-ready; synthesis is complete
ECHO VERDICT: ECHOES ABSENT
  — fewer than 2 entries cleared all gate stages; or all entries trace to one
    artifact; cannot produce echo synthesis; output is a finding record only
```

FAIL — these are not valid verdicts:
- "the echo appears complete" / "synthesis seems sufficient" / "generally echoes present"
- Any graduated or hedged form
- No verdict (absent verdict = ECHOES ABSENT by default; state explicitly)

---

### Step 9 — Forward Handover Guidance *(C-06; IA)*

Register menu: T-1 (builder) / T-2 (reviewer) / T-3 (PM) / T-4 (architect).
Select register matching most actionable downstream route. All slots must be filled from
specific artifacts before writing final statement.

---

### Step 10 — Rules of Thumb *(C-24)*

≤3 rules. HIGH and MEDIUM surprises only.

```
[{HIGH | MEDIUM}] {Rule — ≤20 words}
(encodes: {SURPRISE NAME})
```

Traceability check: each rule's tier must match its named surprise's triage tier from
Step 4. Correct any mismatch before output.

---

**Output**: Steps 1c verdict + Steps 7–10.

Sequence: Signal coverage verdict (COMPLETE | INCOMPLETE) → Echo entries (triage-ordered;
post-gate count noted) → Cross-signal synthesis with echo verdict (ECHOES PRESENT | ECHOES
ABSENT) → Forward handover → Rules of thumb.

---

---

## V-05 — Full Combination with Inertia Framing

**Variation axis**: Combination — C-21 (pipeline staging) + C-22 (verdict commitment) +
inertia framing (the pre-investigation assumption as a named competitor that each surprise
must definitively defeat).

**Hypothesis**: C-21 and C-22 create structural enforcement and verdict commitment. The
inertia framing axis adds a third dimension: naming the weight of pre-investigation belief
explicitly as "the competitor" — the set of assumptions that existed before signals arrived
and that each surprise must defeat to earn its place in the echo. This framing reinforces
C-21 (the PRE-GATE becomes a Belief Inventory — enumerating the competitor set before any
candidate enters the gate) and C-22 (the verdict commitment becomes COMPETITOR DEFEATED /
COMPETITOR SURVIVES — was the pre-investigation assumption definitively overturned?).
Inertia framing also strengthens C-10 (epistemic delta: old belief named as the competitor
the surprise defeats) and C-15 (structural counterfactual induction: the Competitor
Belief field makes future-team framing the default register for every entry).

**Builds on**: V-04 structure (C-21 + C-22) with inertia framing added throughout.

**New element**: Belief Inventory (Step 1d), Competitor Belief field in echo entries
(Step 7), COMPETITOR DEFEATED/SURVIVES verdict replacing ECHOES PRESENT/ABSENT in Step 8
verdict.

---

You are running `/topic:echo` for the topic: {topic}.

All essential signals are in hand. One question: what did they reveal that the team's
pre-investigation beliefs did not predict?

Every surprise must defeat a belief that existed before the signals arrived. A finding
that confirms what the team already believed is not a surprise — it is the competitor
winning. A finding that no one believed possible, that emerges only from cross-signal
tension, is an echo.

---

### Roles

**Institutional Archaeologist (IA)** — active Steps 1d, 2, 5, 7, 8, 9.
Holds the Competitor Belief Set (Step 1d). For every surprise, the IA verifies that it
defeats a named entry in the Competitor Set. The IA's output register: corrections, not
discoveries. Orienting question for every entry: "Which competitor belief does this
surprise defeat, and what would the next team build wrong if they still carried it?"

**Gatekeeper** — active Step 3.

```
GATEKEEPER — FUNCTION DECLARATION
──────────────────────────────────────────────────────────────────
Function:     Adversarial rejection against the Competitor Set. Tests
              each gate-pipeline candidate: (1) Was this predictable
              from the Competitor Set without any signal gathering?
              (2) Does it emerge from cross-signal reading, or from
              one artifact in isolation?

Not-function: Defining the Competitor Set (IA's domain; built in
              Step 1d before the Gatekeeper is invoked).
Not-function: Future-reader framing or mis-design consequence
              assessment (IA domain).

Role boundary: Gate rejections are final. IA cannot override.
              The Gatekeeper tests against the Competitor Set; it
              does not augment it.
──────────────────────────────────────────────────────────────────
```

---

### Step 1 — Read Signal Record *(C-10, C-12)*

Read all signal artifacts across all namespaces. Record namespaces covered (list each;
≥3 required), date range, artifact count per namespace.

---

### Step 1b — PRE-GATE: Namespace Diversity Check *(C-21)*

**Pipeline position: pre-gate** — before any per-entry validation.
**Failure class**: collection-level namespace monoculture — invisible per-entry because
each candidate's namespace is individually valid; only manifests across the full set.

Count distinct namespace segments in the full candidate pool.
- < 2: **PRE-GATE BLOCK**. Echo blocked: namespace monoculture.
- ≥ 2: **PRE-GATE CLEAR**. Proceed.

---

### Step 1c — Signal Coverage Meta-Reflection *(C-13; C-22 verdict)* *(IA)*

List contributing namespaces. Name any with zero contribution. Assess whether gaps are
material.

**Verdict commitment** *(C-22)*:
```
COVERAGE VERDICT: COMPLETE
  — all in-scope namespaces contributed ≥1 candidate
COVERAGE VERDICT: INCOMPLETE
  — [list namespace(s)] contributed zero candidates; named gaps above
```
FAIL forms: "appears sufficient" / "largely covered" / "most areas represented" /
absent verdict. Not valid terminal states.

---

### Step 1d — Belief Inventory: Build the Competitor Set *(IA)*

Before any candidate enters the gate, enumerate what the team believed before signals
arrived. These beliefs are the competitors. Each surprise must defeat one.

For each belief derivable from pre-investigation materials (spec, briefs, prior art,
standing assumptions):

```
COMPETITOR BELIEF [{id}]: {Statement of the belief in falsifiable form}
Source: {document or artifact where this belief was embedded}
Confidence at investigation start: {HIGH | MEDIUM | LOW — how firmly held}
```

Minimum 3 Competitor Beliefs required. If fewer than 3 can be derived from
pre-investigation materials, note: "Competitor Set thin — investigation started with
underdeveloped beliefs; surprises may be hard to distinguish from first discoveries."

The Competitor Set is fixed here. Do not add to it after Step 2 begins.

---

### Step 2 — Pre-Write Prediction Sort *(IA; C-16, C-11)*

Typed route per finding, evaluated against the Competitor Set:

- `topic-story` — confirms a Competitor Belief; Competitor wins this round; routes to narrative
- `topic-report` — restates a known constraint not represented in Competitor Set; routes to report
- `gate-pipeline` — contradicts, complicates, or overturns a Competitor Belief; routes to Step 3

Anti-hypothesis guard *(C-11)*: if a finding confirms what the team set out to prove, it
routes to `topic-story` even if it seemed surprising at first.

*(IA)* co-validation per `gate-pipeline` item: "Which Competitor Belief does this finding
threaten? Can it be found in the Competitor Set?" If no Competitor Belief maps to this
finding, route to `topic-report` with note: "No competitor — not a surprise in the echo
sense."

Discard log *(C-09)*: record all routed items with typed route reason, competitor belief
matched (or "no competitor"), and downstream destination.

---

### Step 3 — ENTRY-GATE: Multi-Stage Epistemic Gate *(Gatekeeper; C-13)*

**Pipeline position: entry-gate** — validates each candidate independently against the
Competitor Set. Cannot see collection-level properties (pre-gate) or cross-entry
relationships (post-gate).

The Gatekeeper evaluates each candidate against the Competitor Set fixed in Step 1d.

Anti-Pattern Catalog: CONFIRMATION (competitor belief confirmed → `topic-story`);
RESTATEMENT (known constraint, no competitor → `topic-report`); ISOLATED-FINDING
(single artifact → reject at Stage 3).

Three stages. Per-stage commit. Collapse prohibition.

**Stage 1 — Prediction Test** *(Gatekeeper)*
"Was this predictable from the Competitor Set before any signal gathering?"
`PREDICTABLE FROM COMPETITOR SET` → discard | `UNPREDICTABLE` → Stage 2
Commit: `Stage 1: [{item}] → [{verdict}] — tested against: Competitor Belief [{id}]`

**Stage 2 — Contradiction Test** *(Gatekeeper)*
"Does this item contradict or overturn a Competitor Belief?"
Name the specific Competitor Belief being tested:
Competitor Belief [{id}]: `{belief statement}`
OVERTURN VALID: `{case that genuinely falsifies this belief}`
OVERTURN INVALID (absence-of-consideration): `{notes absence, not falsification}`
OVERTURN INVALID (sentiment-reaction): `{surprise without naming the belief overturned}`
OVERTURN INVALID (hedge-uncertainty): `{hedges on whether the belief was held firmly}`
`NO OVERTURN` → discard | `COMPETITOR BELIEF OVERTURNED` → Stage 3
Commit: `Stage 2: [{item}] → [{verdict}] — defeats: Competitor Belief [{id}]`

**Stage 3 — Attribution Test** *(Gatekeeper)*
"Cross-signal or single artifact?"
`SINGLE-ARTIFACT` → discard | `CROSS-SIGNAL (cite ≥2)` → SURPRISE
Commit: `Stage 3: [{item}] → [{verdict}] — sources: [{artifact1 (ns/skill)}, {artifact2}]`

---

### Step 4 — Pre-Write Impact Triage *(C-23)*

HIGH / MEDIUM / LOW comparatively across all SURPRISE candidates before expansion.
- HIGH: forces revision to a core design decision, assumption, or scope boundary
- MEDIUM: qualifies a principle or adds a constraint
- LOW: notable; no current design consequence

Factor the Competitor Belief confidence from Step 1d: a finding that overturns a
HIGH-confidence belief scores higher triage pressure than one that overturns a LOW-confidence
belief, all else equal.

Write entries HIGH → MEDIUM → LOW.

---

### Step 5 — Naming Scaffold *(C-17)*

For each candidate, derive the name from the Competitor Belief it defeats:
1. Competitor belief: "The team carried the assumption that ___." (cite Competitor Belief [{id}])
2. Correction: "The signals revealed instead that ___."
3. Domain: "This affects the ___ area."
4. Label: `The {Corrected Belief}: {Domain}`

The label encodes the correction; the Competitor Belief field supplies the anchor.

---

### Step 6 — Pre-Expansion Co-Validation Gate *(C-20)*

Simultaneously before expanding any entry:
- Name form passes `The {Corrected Belief}: {Domain}` *(C-17)* → VALID / INVALID
- Failure field reads as "If the next team carries [Competitor Belief {id}], {specific
  mis-design}" *(C-18)* → VALID / INVALID

Both VALID to proceed. Either fails → revise.

---

### Step 6b — POST-GATE: Pairwise Redundancy Check *(C-21)*

**Pipeline position: post-gate** — after all entries clear entry-gate.
**Failure class unique to this position**: two entries each defeat the same Competitor
Belief via differently framed corrections — each passes individually but collectively they
name the same underlying correction. Invisible per-entry; detectable by cross-entry
comparison after all entries have passed.

Check: do any two entries reference the same Competitor Belief [{id}]? If yes: do they
name the same correction at different granularities? If yes → merge or exclude with rationale.
Log as `post-gate-redundancy`.

Record final SURPRISE count after redundancy resolution.

---

### Step 7 — Write Echo Entries *(IA; triage order)*

For each SURPRISE entry (HIGH → MEDIUM → LOW):

---

**[SURPRISE NAME: `The {Corrected Belief}: {Domain}`]** — *{HIGH | MEDIUM | LOW}* *(IA)*

Source signal: `{artifact-name} ({namespace}/{skill})`
`[CROSS: {artifact-A} × {artifact-B}]` *(C-08 if cross-signal)*
Temporal anchor *(C-12)*: `{round or date}`

Competitor belief defeated *(inertia framing)*: `Competitor Belief [{id}] — {belief statement} — held with {HIGH | MEDIUM | LOW} confidence`

We believed: `{same as competitor belief — falsifiable form}`
The surprise: `{what signals revealed that overturns the competitor belief}`
If the next team carries the competitor belief *(C-18)*: `{specific concrete mis-design}`.
Downstream route *(C-14)*: `→ {skill or namespace}`

---

### Step 8 — Cross-Signal Synthesis *(C-05; IA)*

≤120 words. Name ≥2 SURPRISE entries by label. Explain why the pattern they form — the
pattern of which competitor beliefs were defeated and by what signals — only emerges from
reading the entries together.

*(IA)*: What does the Competitor Set look like *after* the echo? Which beliefs were
defeated, which survived, and what does the surviving shape of the Competitor Set tell a
future team about where the remaining risk lives?

**Verdict commitment** *(C-22)*: Declare exactly one of two valid terminal states —

```
ECHO VERDICT: COMPETITOR BELIEFS DEFEATED
  — ≥2 Competitor Beliefs in the Competitor Set have been definitively overturned by
    cross-signal evidence; echo is complete and integration-ready
ECHO VERDICT: COMPETITOR BELIEFS SURVIVE
  — fewer than 2 Competitor Beliefs overturned; or all findings trace to a single artifact;
    the pre-investigation belief set remains substantially intact; output is a finding record
```

FAIL forms:
- "most competitors defeated" / "competitors largely overturned" / "the echo appears complete"
- Any graduated verdict
- No verdict (absent = COMPETITOR BELIEFS SURVIVE by default; state explicitly)

---

### Step 9 — Forward Handover Guidance *(C-06; IA)*

The handover addresses the surviving Competitor Beliefs — what the next team will still
carry as assumptions unless explicitly warned.

Register menu: T-1 (builder) / T-2 (reviewer) / T-3 (PM) / T-4 (architect).
Select register matching the highest-impact surviving risk from Step 8 synthesis.
Fill all slots from specific artifacts before writing.

---

### Step 10 — Rules of Thumb *(C-24)*

≤3 rules. HIGH and MEDIUM surprises only.

```
[{HIGH | MEDIUM}] {Rule — ≤20 words; defeats: Competitor Belief [{id}]}
(encodes: {SURPRISE NAME})
```

Traceability check: each rule's tier must match its named surprise's triage tier from
Step 4. Correct any mismatch. Verify the Competitor Belief id cited is in the Competitor
Set from Step 1d.

---

**Output**: Step 1c verdict + Competitor Set summary (ids, statements, confidence) +
Steps 7–10.

Sequence: Signal coverage verdict → Competitor Set (from Step 1d; fixed before gate) →
Echo entries (triage-ordered; post-gate count; each entry with Competitor Belief id) →
Cross-signal synthesis with COMPETITOR BELIEFS DEFEATED / SURVIVE verdict → Forward
handover → Rules of thumb.

---
