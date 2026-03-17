Written to `simulations/quest/variations/program-plan-variations-R4-2026-03-14.md`.

---

## program-plan R4 — Summary

**Gap from R3:** R3 V-03/V-04 retroactively score 140/145 under v4. C-18 is already passed (displacement-framing was in the parenthetical). The single gap is **C-19** — multi-hop downstream consequence cascade (2+ ordered consequences using → notation, crossing arc-layer boundaries).

**Five variation axes:**

| ID | Axis | C-19 Mechanism | Predicted |
|----|------|----------------|-----------|
| **V-01** | Cascade requirement embedded in column header | Header instruction fires at every row (same pattern as C-18 taught us) | 145/145 |
| **V-02** | Post-table cascade gate with example format | Checkpoint + template after table; model must verify before proceeding | 145/145 |
| **V-03** | C-18 strong + C-19 minimal form (both) | Single "expand one entry" constraint after table | 145/145 |
| **V-04** | Cascade contrast opener only (no explicit table instruction) | Opener models the arc cascade pattern — tests if priming alone is sufficient | 140–145/145 |
| **V-05** | Full synthesis — cascade from opener + header + archetype + check + Step 8 | Maximum redundancy from all angles | 145/145 |

**Key hypotheses:**
- **R4-H01/H02**: Header instruction vs. post-table gate — which mechanism drives C-19 more reliably?
- **R4-H03**: V-04 is the pivot — if cascade opener priming alone passes C-19, explicit table instruction is redundant. If it fails, a direct instruction is required.
- **R4-H04**: Does V-05's max-redundancy produce richer cascades than V-03's minimal form, or does C-19 pass at the same minimum depth regardless?

The new **C-18** pass condition is secured in all variations by upgrading the column header from parenthetical displacement framing to primary framing ("Why this actor cannot run earlier — [cascade/consequence]").
-impossibility header)** — R3 showed that parenthetical framing
("Why this position (what breaks if moved earlier)") passes, but the primary label
("Why this position") is still positive-belonging. R4 variations make the displacement
framing the *primary* label, not a parenthetical. V-04's R3 header ("Why this actor
cannot run earlier") is the canonical passing form.

**C-19 (multi-hop downstream consequence cascade)** — R3 V-05's PM entry is the archetype:
"Moved later: design is anchored in the author's assumptions → review critiques a design
targeting the wrong problem → prove investigates a hypothesis without market grounding."
Three elements: (1) explicit sequencing notation (→), (2) two or more ordered consequences,
(3) crossing arc-layer boundaries (breadth failure → design failure → validation failure).
R4 explores five mechanisms to elicit this reliably: header instruction, post-table gate,
combined minimal, opener priming, and full integration.

**Four hypotheses to resolve in scoring:**

- **R4-H01**: Does embedding the cascade requirement in the column header (V-01) reliably
  drive multi-hop entries, or do models treat it as a formatting hint and satisfy it with
  two short clauses?
- **R4-H02**: Does a post-table cascade gate with example format (V-02) produce more reliable
  cascades than a header instruction (V-01)? Or does the post-table position make it easier
  to satisfy minimally?
- **R4-H03**: Can the cascade contrast opener (V-04) prime the model to produce cascades
  in the actor table without any explicit cascade instruction? If V-04 passes C-19, opener
  framing is sufficient. If it fails, explicit table-level instruction is required.
- **R4-H04**: Does combining header + opener + example + step (V-05) produce richer cascades
  than single-mechanism variations, or does C-19 pass at the same minimum depth regardless
  of instruction density?

---

## V-01 — Header-Embedded Cascade Requirement (C-19 via column header)

**Axis**: C-19 single axis — the displacement-impossibility header is upgraded to explicitly
require cascade notation. Column becomes: "Why this actor cannot run earlier — and what
cascade breaks downstream (use → arrows, 2+ ordered consequences, crossing arc-layer
boundaries)." No other changes from R3 V-03 baseline.
**Hypothesis**: The column header is load-bearing (the C-18 finding showed header framing
drives per-row reasoning). Embedding the cascade requirement directly in the header keeps
the instruction visible at every row and drives the model to trace 2+ consequences per
actor — the same mechanism that made displacement-impossibility framing reliable for C-15.
**Predicted**: All 19 PASS → **145/145, GOLDEN**

---

Naive program plans sort skills by namespace and call that sequencing. Their gates say "ready"
or "complete" — conditions that cannot be verified. Their stage boundaries reflect file
organization, not workflow logic. **This variation defeats that by two mechanisms: actor-layer
assignment that grounds every stage in a workflow transition, and a required
handoff+threshold gate format that forces artifact naming and role transitions simultaneously.**

---

**Actor assignments** — assign skills to arc layer using this table. The column header names
the reasoning depth required for each entry.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier — and what cascade breaks downstream (use → arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; all downstream work requires landscape context. Moved later: design targets an unvalidated problem → review evaluates a design anchored in wrong assumptions → prove tests a hypothesis with no market grounding. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation with no landscape anchor → depth layer has no validated artifact to test against → synthesis draws conclusions from unvalidated design. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact to evaluate. Moved earlier: review critiques a void → prove launches an investigation without a target → synthesis inherits findings with no anchor in a real design decision. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires both a spec and a process model. Moved before draft: simulation runs against an undefined system → outputs cannot be compared against design intent → integration failures surface with no reference to fix against. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate. Moved earlier: feedback simulation produces anecdotes with no expectation model → the team cannot distinguish expected from unexpected findings → listen artifacts are noise, not calibrated signal. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved earlier: narrative has no material → readiness signal is empty → decision is made without a signal foundation. |

**Evidence arc** — each layer produces what the next layer consumes:

1. **Breadth** (scout): Landscape signals. Nothing downstream is productive without them.
2. **Design** (draft): Authored intent anchored in breadth.
3. **Depth** (review, prove, flow, trace): Stress-testing the design.
4. **Synthesis** (listen, topic): Post-signal conclusions.

---

**Complete skill catalog** — no other skill names exist. Any name not in this list is invalid:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

---

**To build the program plan:**

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and existing signal artifacts for
the topic. Identify the decision this investigation must answer.

**Step 2 -- Select skills.** For each actor group, choose only the skills this topic needs.
Select only from the catalog above.

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis).

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format for every non-echo
gate:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules: Name both actors. Name specific artifact types. `>=N` threshold required.
"Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Names reflect arc intent (`discovery`, `design`,
`validation`, `synthesis`), not skill names or `stage1`.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages`, and echo.
Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** Write 2-3 sentences: what this plan prioritizes early,
what it defers, and what happens if any gate is removed.

---

## V-02 — Post-Table Cascade Gate (C-19 via explicit check after table)

**Axis**: C-19 single axis — after the actor table, a dedicated cascade check block requires
the model to verify that at least one entry traces a 2+ hop consequence chain with → notation
crossing arc-layer boundaries, and provides the example format. Column header retains R3 V-03
parenthetical style; the cascade requirement is surfaced at the post-table stage.
**Hypothesis**: A post-table cascade gate with an inline example creates a checkpoint:
the model must review its own table entries against the cascade requirement before proceeding.
The example format ("Moved later: [Layer A failure] → [Layer B failure] → [Layer C failure]")
gives the model a literal template to pattern-match against. Tests whether a checkpoint
instruction after the table is more reliable than embedding the requirement in the header.
**Predicted**: All 19 PASS → **145/145, GOLDEN**

---

Naive program plans sort skills by namespace and call that sequencing. Their gates say "ready"
or "complete" — conditions that cannot be verified. Their stage boundaries reflect file
organization, not workflow logic. **This variation defeats that by two mechanisms: actor-layer
assignment that grounds every stage in a workflow transition, and a required
handoff+threshold gate format that forces artifact naming and role transitions simultaneously.**

---

**Actor assignments** — assign skills to arc layer using this table. The justification column
names why this actor cannot run earlier and what breaks if displaced.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier — what breaks if displaced |
|-------|-----------|-----------|--------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; all downstream work requires landscape context. Moved later: design targets an unvalidated problem. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation with no landscape anchor. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact to evaluate. Moved earlier: review critiques a void; prove investigates an undefined target. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires both a spec and a process model. Moved before draft: simulation runs against an undefined system. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate. Moved earlier: feedback simulation produces anecdotes, not calibrated findings. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved earlier: narrative has no material; readiness signal is empty. |

**Arc cascade check** — before proceeding to skill selection, review the table above. At
least one entry must trace a displacement consequence chain of two or more ordered hops using
→ notation, crossing at least one arc-layer boundary. Format:

  `"Moved later: [Failure in Layer A] → [Failure in Layer B caused by A] → [Failure in Layer C if applicable]"`

Example: `"Moved later: design is anchored in assumptions → review evaluates a design targeting the wrong problem → prove tests a hypothesis without market grounding."` If no entry has this depth, expand one entry before continuing.

**Evidence arc** — each layer produces what the next layer consumes:

1. **Breadth** (scout): Landscape signals. Nothing downstream is productive without them.
2. **Design** (draft): Authored intent anchored in breadth.
3. **Depth** (review, prove, flow, trace): Stress-testing the design.
4. **Synthesis** (listen, topic): Post-signal conclusions.

---

**Complete skill catalog** -- no other skill names exist. Any name not in this list is invalid:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

---

**To build the program plan:**

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and existing signal artifacts for
the topic. Identify the decision this investigation must answer.

**Step 2 -- Select skills.** For each actor group, choose only the skills this topic needs.
Select only from the catalog above.

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis).

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules: Name both actors. Name specific artifact types. `>=N` threshold required.
"Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Names reflect arc intent (`discovery`, `design`,
`validation`, `synthesis`), not skill names or `stage1`.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages`, and echo.
Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** Write 2-3 sentences: what this plan prioritizes early,
what it defers, and what happens if any gate is removed.

---

## V-03 — C-18 Strong + C-19 Minimal Form (both, minimum sufficient)

**Axes**: C-18 and C-19 both addressed at minimum sufficient form. Column header uses primary
displacement-impossibility framing (not parenthetical). C-19 is addressed by a single
post-table constraint sentence naming the → notation requirement and boundary condition.
**Hypothesis**: Both criteria pass at their minimum implementation, confirming the rubric
rewards structural signal (displacement-impossibility header present + cascade chain present)
rather than instruction elaboration. If V-03 scores 145, minimum form is the efficient
frontier for R4 as V-03 was for R3. If V-03 scores 140 while V-05 scores 145, instruction
depth matters for reliable cascade elicitation.
**Predicted**: All 19 PASS → **145/145, GOLDEN**

---

Naive program plans sort skills by namespace and call that sequencing. Their gates say "ready"
or "complete" — conditions that cannot be verified. Their stage boundaries reflect file
organization, not workflow logic. **This variation defeats that by two mechanisms: actor-layer
assignment that grounds every stage in a workflow transition, and a required
handoff+threshold gate format that forces artifact naming and role transitions simultaneously.**

---

**Actor assignments** — assign skills to arc layer using this table. Each entry must name
why this actor cannot run earlier and what breaks if displaced.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier — and what breaks if displaced |
|-------|-----------|-----------|------------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; all downstream work requires landscape context. Moved later: design targets an unvalidated problem. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation with no landscape anchor. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact to evaluate. Moved earlier: review critiques a void; prove investigates an undefined target. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires both a spec and a process model. Moved before draft: simulation runs against an undefined system. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate. Moved earlier: feedback simulation produces anecdotes, not calibrated findings. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved earlier: narrative has no material; readiness signal is empty. |

**Cascade requirement** — at least one table entry above must trace a chain of 2+ ordered
displacement consequences using → notation, crossing arc-layer boundaries (e.g., a failure
in breadth that causes a failure in design that causes a failure in validation). Expand one
entry now if no chain is present.

**Evidence arc** -- each layer produces what the next layer consumes:

1. **Breadth** (scout): Landscape signals. Nothing downstream is productive without them.
2. **Design** (draft): Authored intent anchored in breadth.
3. **Depth** (review, prove, flow, trace): Stress-testing the design.
4. **Synthesis** (listen, topic): Post-signal conclusions.

---

**Complete skill catalog** -- no other skill names exist. Any name not in this list is invalid:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

---

**To build the program plan:**

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and existing signal artifacts for
the topic. Identify the decision this investigation must answer.

**Step 2 -- Select skills.** For each actor group, choose only the skills this topic needs.
Select only from the catalog above.

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis).

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules: Name both actors. Name specific artifact types. `>=N` threshold required.
"Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Names reflect arc intent (`discovery`, `design`,
`validation`, `synthesis`), not skill names or `stage1`.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages`, and echo.
Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** Write 2-3 sentences: what this plan prioritizes early,
what it defers, and what happens if any gate is removed.

---

## V-04 — Cascade Contrast Opener (C-19 via opener priming, no explicit table instruction)

**Axes**: C-19 via cascade contrast opener only. The naive-competitor framing is extended to
describe arc-layer cascade failure — breadth → design → validation propagation — as the
specific failure mode being defeated. No explicit cascade instruction appears in the table
or steps. C-18 uses strong displacement-impossibility header. Tests whether framing the
opener in cascading-failure terms primes the model to reproduce cascade patterns in table
entries without explicit instruction.
**Hypothesis**: Naming the failure mode as a cascade ("breadth failure propagates to design,
then to validation, then to synthesis") teaches the model what a cascade looks like before
it reaches the table. If this priming is sufficient, C-19 will pass without any explicit
cascade instruction. If it fails, explicit table-level instruction (V-01/V-02/V-03) is
required and opener-only priming cannot substitute for direct instruction.
**Predicted**: C-18 PASS, C-19 uncertain (hypothesis: PASS from priming) → **140-145/145**

---

The failure mode this variation defeats is arc-layer cascade failure. When breadth-layer
actors are displaced, the design layer has no validated anchor — it builds on the author's
assumptions. Because design is now anchored in assumptions, the depth layer is evaluating
a design that targets the wrong problem. Because the depth layer is producing findings
against a corrupted design, the synthesis layer draws conclusions from compounded errors.
The failure is not local to one stage: it propagates through every downstream arc layer,
each one inheriting the corruption of the previous.

**This variation defeats arc-layer cascade failure by two structural choices: actor-layer
assignment that anchors every namespace to its validated prerequisite layer (preventing
displacement at the source), and a gate format that exposes handoffs between arc layers
(making cascade boundaries visible at every stage boundary). A flat skill list cannot
prevent a cascade because it has no arc boundaries to protect.**

---

**Actor assignments** — before placing any skill, understand why each actor is at this
arc position. Each entry names why this actor cannot run earlier and what breaks if displaced.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier — what breaks if displaced |
|-------|-----------|-----------|--------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; every downstream layer depends on landscape signals. Moved later: design is anchored in the author's assumptions with no validated market context; the cascade begins here. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation — the design layer inherits the assumption problem that should have been resolved in breadth. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact to evaluate. Moved earlier: review produces open-ended critique without an anchor; prove launches an investigation without a target hypothesis grounded in a real design decision. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires a spec and a process model. Can run in parallel with review/prove within Depth, but not before draft. Moved before draft: simulation runs against an undefined system; outputs cannot be compared against design intent. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate expectations. Moved before depth: feedback simulation produces anecdotes with no expectation baseline; the team has no validated findings to compare against. |
| Anyone | `topic` | Synthesis | Requires all prior signals to be meaningful. Moved before synthesis: narrative has no material; topic:status with no artifacts is a placeholder, not a readiness signal. |

**Evidence arc** — each layer produces exactly what the next layer consumes:

1. **Breadth** (scout): Landscape signals that define what is worth building.
2. **Design** (draft): Testable artifacts anchored in breadth signals.
3. **Depth** (review, prove, flow, trace): Validation signals against the design.
4. **Synthesis** (listen, topic): Conclusions drawn from the full signal set.

---

**Complete skill catalog** -- no other skill names exist. Any name not in this list is invalid:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

---

**To build the program plan:**

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and existing signal artifacts for
the topic. Identify the decision this investigation must answer before the team can commit.

**Step 2 -- Select skills.** For each actor group, choose only the Signal skills this topic
needs. Select only from the catalog above.

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis). This mapping determines stage grouping and gate
positions.

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format for every non-echo
gate -- all three elements must appear together:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules:
- Name both actors. Name specific artifact types (`scout-feasibility`, `draft-spec`).
- The `>=N` threshold is required.
- "Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Stage names communicate arc intent:
`discovery`, `design`, `validation`, `synthesis` -- not generic (`stage1`), not skill names.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages` (name, skills,
gate), and the echo final stage. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** After the YAML, write 2-3 sentences: what the plan
prioritizes early, what it defers, and what the gates are protecting against -- specifically,
what happens if any gate is removed.

---

## V-05 — Full Synthesis Maximum (cascade from every angle)

**Axes**: All 19 criteria at maximum implementation. C-14 opener frames arc-layer cascade
failure (from V-04). Column header embeds the cascade requirement with → syntax (from V-01).
A cascade archetype example is pre-filled in the table introduction, showing the PM entry
as a 3-hop chain. Post-table cascade check verifies at least one chain is present (from
V-02). Step 8 specifically asks for the multi-hop consequence of removing the first gate.
**Hypothesis**: Maximum redundancy from opener + header + example + post-check + step 8
produces reliable C-19 at the highest cascade depth. If V-05 passes C-19 while V-03 fails,
multiple-angle instruction matters. If both pass, V-03 is the efficient frontier for R4.
**Predicted**: All 19 PASS → **145/145, GOLDEN**

---

The failure mode this variation defeats is arc-layer cascade failure. Moving a breadth-layer
actor out of position does not produce one wrong artifact — it propagates: design is anchored
in the author's assumptions → review evaluates a design targeting the wrong problem → prove
tests a hypothesis without market grounding → synthesis draws conclusions from a corrupted
evidence set. Each arc layer inherits the corruption of the previous one.

**This variation defeats arc-layer cascade failure by two structural choices enforced before
any skill is placed**: (1) an actor-layer assignment table with per-actor causal reasoning
that traces the cascade of consequences if the actor is displaced (keeping each arc boundary
visible), and (2) a required handoff+threshold gate template that exposes the delivering
actor, receiving actor, minimum threshold, and artifact type at every stage boundary. A flat
skill list cannot prevent a cascade because it has no arc boundaries to protect.

---

**Actor assignments** — read the justification column before assigning skills. Each entry
names why this actor cannot run earlier and must trace the cascade of failures that follow
displacement using → arrows. At least one entry must trace 2+ ordered consequences crossing
arc-layer boundaries.

**Cascade archetype (PM actor)** — use this depth as the model for your own entries:

> PM | `scout` | Breadth | Cannot run later: scout signals have no prerequisites, and every
> downstream layer depends on them. Moved later: design is anchored in the author's
> assumptions rather than validated landscape signals → review critiques a design targeting
> the wrong problem → prove tests a hypothesis without market grounding. Scout gates protect
> all downstream arc layers simultaneously.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier — cascade of failures if displaced (use →, 2+ hops, cross arc-layer boundaries) |
|-------|-----------|-----------|-------------------------------------------------------------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; every downstream layer depends on landscape signals. Moved later: design is anchored in assumptions → review evaluates a design targeting the wrong problem → prove tests a hypothesis without market grounding. Scout gates protect all downstream layers simultaneously. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier (before scout): design is unconstrained speculation with no landscape anchor → depth layer evaluates a design built on wrong assumptions → synthesis draws conclusions from a corrupted evidence arc. Moved later (after review): team reviews a void, then a design appears to confirm conclusions already reached. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact. Moved before draft: review critiques a void with no anchor → prove investigates an undefined target → synthesis inherits ungrounded findings as if they were valid. Moving review/prove earlier does not accelerate the arc — it breaks the arc. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires a spec and a process model. Can run parallel to review/prove within Depth, but not before draft. Moved before draft: simulation runs against an undefined system → outputs cannot be compared against design intent → integration failures surface with no reference point for resolution. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate expectations. Moved before depth: feedback simulation produces anecdotes with no expectation baseline → the team cannot distinguish expected from unexpected findings → listen artifacts are noise rather than calibrated signal. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved earlier: narrative has no material → topic:status is a placeholder not a decision input → the team makes a go/no-go without a signal foundation. |

**Cascade check** — verify before proceeding: at least one entry above traces 2+ ordered
consequences using → notation, crossing from one arc layer to another. The PM and
Architect/PM entries are filled above as archetypes; match this depth for each actor's
entry. If any entry contains only a single consequence, expand it before continuing.

**Evidence arc** -- each layer produces exactly what the next layer consumes:

1. **Breadth** (scout): Landscape signals that define what is worth building.
2. **Design** (draft): Testable artifacts anchored in breadth signals.
3. **Depth** (review, prove, flow, trace): Validation signals against the design.
4. **Synthesis** (listen, topic): Conclusions drawn from the full signal set.

---

**Complete skill catalog** -- no other skill names exist. Any name not in this list is invalid:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

---

**To build the program plan:**

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and existing signal artifacts for
the topic. Identify the decision this investigation must answer before the team can commit.

**Step 2 -- Select skills.** For each actor group, choose only the Signal skills this topic
needs. Not every skill applies to every topic. Select only from the catalog above.

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis). This mapping determines stage grouping and gate
positions.

**Step 4 -- Write handoff gates using `>=N` syntax.** For each non-echo stage, write the
gate in this required format -- all three elements must appear together:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules:
- Name the delivering actor and the receiving actor -- both required.
- Name specific artifact types: `scout-feasibility`, `draft-spec` -- not "signal" in the abstract.
- The `>=N` threshold is required in every gate where a count is meaningful.
- "Done", "ready", "complete" are not gates -- replace with threshold and artifact name.

**Step 5 -- Group into 3-6 named stages.** Stage names communicate arc layer intent:
`discovery`, `design`, `validation`, `synthesis` -- not generic (`stage1`), not skill names.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
The echo surfaces what the signals revealed that was not in the original plan. No other stage
may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages` (name, skills,
gate), and the echo final stage. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** After the YAML, write 2-3 sentences: what the plan
prioritizes early, what it defers, and what the gates are protecting against -- specifically,
what is the multi-hop consequence cascade if the first gate (scout handoff) is removed.

---

## Predicted Score Summary

| ID | Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Total | Golden |
|----|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | Cascade in header | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **145** | YES |
| V-02 | Post-table cascade gate | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **145** | YES |
| V-03 | C-18 strong + C-19 minimal | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **145** | YES |
| V-04 | Cascade contrast opener | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | ? | **140-145** | YES |
| V-05 | Full synthesis maximum | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **145** | YES |

Points: Essential 12 pts x 5 = 60 | Recommended 10 pts x 3 = 30 | Aspirational 5 pts x 11 = 55
Max 145 | Golden = all essential pass AND composite >= 116.

---

## R4 Hypotheses to Resolve

**R4-H01: Does embedding the cascade requirement in the column header drive reliable 2+ hop
entries?**
V-01 puts the cascade requirement ("use → arrows, 2+ ordered consequences, crossing
arc-layer boundaries") directly in the column header. If this passes C-19 reliably, the
header-embedding pattern (validated for C-18) generalizes to cascade requirements. V-01 is
the cleanest single-mechanism test.

**R4-H02: Is a post-table cascade gate (V-02) more or less reliable than a header instruction
(V-01)?**
V-02 uses a post-table check with an inline example. If V-02 passes and V-01 fails, the
checkpoint+example format is required. If both pass, the header-only mechanism is sufficient
and V-03 is the efficient frontier.

**R4-H03: Can cascade contrast opener alone (V-04) prime the model to produce multi-hop
chains without explicit instruction?**
V-04 names the failure mode as a cascade, models the cascade pattern in the opener, but
provides no explicit "use → notation" instruction in the table. If V-04 passes C-19,
opener-level priming is sufficient and cascade instructions are redundant. If V-04 fails
C-19, the opener primes the frame but the model needs explicit notation requirements to
produce the chain in the table. V-04 is the riskiest variation and the most informative.

**R4-H04: Does V-05's maximum-redundancy approach (cascade from opener + header + example +
check + step 8) produce richer cascades than minimal-instruction V-03?**
C-19 passes at minimum when one entry has a 2+ hop chain. If V-05 and V-03 both pass C-19,
the criterion passes regardless of instruction density. The remaining question is whether
V-05 produces more reliable cascades in practice (relevant if these variations are used in
production settings where model behavior is stochastic).
