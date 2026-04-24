**R5 variations written** (`simulations/quest/variations/program-plan-variations-R5-2026-03-14.md`).

---

## Summary

All 5 variations target **155/155** (the v5 ceiling). The gap from R4 (C-20 + C-21) is addressed in every variation. Axis breakdown:

| ID | Axis | Key Structure |
|----|------|---------------|
| **V-01** | Confirmed full-replication baseline | Direct R4-V-01 replication — all 6 rows 3-hop, header embeds C-20 spec. Ceiling confirmation. |
| **V-02** | Two-column cascade table | Cascade is its own column; cascade column header carries C-20 spec. Structural isolation as C-21 mechanism. |
| **V-03** | Minimum-density 155/155 form | C-20 header + all 6 rows at minimum 2-hop cascades, no redundancy. Tests whether 2-hop satisfies C-21. |
| **V-04** | Gate-integrated cascade | Gate template embeds `— removing this gate: [cascade chain]`, structurally enforcing C-17 at every gate. |
| **V-05** | Cascade-first structure | Actor cascade table appears before the naive-competitor opener — tests whether leading with the table drives deeper cascade internalization. |

**Key open question for R5 scoring:** V-03 tests whether 2-hop depth per row satisfies C-21, or whether the R4-V-01/V-05 archetypes (3-hop) set a de facto scorer expectation. V-02 tests whether a dedicated cascade column can carry C-20 vs. whether C-20 requires a single combined column.
| Frame priming does not substitute for structural cascade instruction |

**R5 variation axes** — all five target 155/155 but explore different structural mechanisms
for achieving reliable full-table cascade coverage (C-21) and header cascade spec (C-20):

| ID | Axis | C-21 Mechanism | New Hypothesis |
|----|------|----------------|----------------|
| **V-01** | Confirmed full-replication baseline | All 6 rows pre-filled with 3-hop → chains; header embeds C-20 spec | Can R4-V-01 be precisely replicated for ceiling confirmation? |
| **V-02** | Two-column cascade table | Structural isolation: cascade chain is its own column, header carries C-20 spec | Does separating cascade into a dedicated column guarantee C-21 more reliably than a combined column? |
| **V-03** | Minimum-density 155/155 form | Header C-20 spec; all 6 rows have minimum 2-hop cascades; no pre-fill, no post-check | What is the minimum sufficient instruction density to achieve C-21? Is 2-hop sufficient? |
| **V-04** | Gate-integrated cascade | Actor table + C-20 header; gate template embeds cascade consequence statement | Does gate-level cascade reasoning (C-17 structurally embedded) strengthen arc strategy output? |
| **V-05** | Cascade-first structure | Actor cascade table appears first (before opener); C-20 header; all entries 3-hop | Does leading with the cascade table drive deeper internalization than mid-prompt placement? |

**R5 hypotheses:**

- **R5-H01**: Does precisely replicating R4-V-01 produce a stable 155/155 or was the R4
  result a one-time ceiling hit?
- **R5-H02**: Does structural column isolation (cascade as own column, V-02) produce more
  reliable C-21 coverage than a combined column with C-20 header (V-01)?
- **R5-H03**: Does minimum 2-hop depth per entry (V-03) pass C-21, or does the criterion
  require 3-hop chains across all entries?
- **R5-H04**: Does gate-embedded cascade (V-04) produce a more grounded arc strategy
  statement than actor-table-only cascade (V-01)?
- **R5-H05**: Does cascade-first structure (V-05) improve cascade depth in model output
  by front-loading the cascade table before the task framing?

---

## V-01 — Confirmed Full-Replication Baseline

**Axis**: Structural confirmation — all 6 actor rows pre-filled with 3-hop → cascades;
column header embeds C-20 spec. Direct replication of the R4-V-01 pattern confirmed at
155/155 retroactively under v5.
**Hypothesis**: The R4-V-01 structural pattern (header-embedded cascade requirement +
full-table cascade coverage as pre-filled archetypes) is the confirmed 155/155 mechanism.
Re-running it as a clean R5 baseline tests whether the ceiling score is stable.
**Predicted**: All 21 PASS → **155/155, GOLDEN**

---

Naive program plans sort skills by namespace and call that sequencing. Their gates say
"ready" or "complete" — conditions that cannot be verified. Their stage boundaries reflect
file organization, not workflow logic. **This variation defeats that by two structural
choices enforced before any skill is placed**: (1) an actor-layer assignment table where
every row traces the cascade of failures that follow displacement (keeping arc boundaries
visible at every row via the column header), and (2) a required handoff+threshold gate
template that exposes the delivering actor, receiving actor, minimum threshold, and artifact
type at every stage boundary.

---

**Actor assignments** — read this table before placing any skill. Every row below
demonstrates the required cascade depth: each entry names why this actor cannot run earlier
and traces the cascade of failures downstream using → arrows. When you construct your own
actor table for a new topic, match this depth in every row.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier — and what cascade breaks downstream (use → arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; every downstream layer depends on landscape signals. Moved later: design is anchored in the author's assumptions → review evaluates a design targeting the wrong problem → prove tests a hypothesis without market grounding. Scout gates protect all downstream layers simultaneously. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation with no landscape anchor → depth layer evaluates a design built on wrong assumptions → synthesis draws conclusions from a corrupted evidence arc. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact to evaluate. Moved before draft: review critiques a void with no anchor → prove investigates an undefined target → synthesis inherits ungrounded findings as if they were valid. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires a spec and a process model. Moved before draft: simulation runs against an undefined system → outputs cannot be compared against design intent → integration failures surface with no reference point for resolution. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate expectations. Moved before depth: feedback produces anecdotes with no expectation baseline → team cannot distinguish expected from unexpected findings → listen artifacts are noise rather than calibrated signal. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved earlier: narrative has no material → topic:status is a placeholder not a decision input → team makes a go/no-go without a signal foundation. |

**Evidence arc** — each layer produces what the next layer consumes:

1. **Breadth** (scout): Landscape signals. Nothing downstream is productive without them.
2. **Design** (draft): Authored intent anchored in breadth.
3. **Depth** (review, prove, flow, trace): Stress-testing the design.
4. **Synthesis** (listen, topic): Post-signal conclusions.

---

**Complete skill catalog** — no other skill names exist. Any name not in this list is
invalid:

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
Not every skill applies to every topic. Select only from the catalog above.

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth → Design → Depth → Synthesis).

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format for every non-echo
gate — all three elements must appear together:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules: Name both actors. Name specific artifact types (`scout-feasibility`, `draft-spec`).
`>=N` threshold required. "Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Names reflect arc intent (`discovery`, `design`,
`validation`, `synthesis`), not skill names or `stage1`.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages`, and echo.
Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** Write 2-3 sentences: what this plan prioritizes early,
what it defers, and what happens if any gate is removed.

---

## V-02 — Two-Column Cascade Table

**Axis**: Table structure — split the actor table justification into two columns: (1)
position rationale (prerequisites), and (2) cascade chain if displaced. The cascade column
header carries the C-20 spec (→ arrows, 2+ ordered consequences, crossing arc-layer
boundaries). Structural separation forces cascade completeness: every row must have a value
in the cascade column, making missing chains visible at construction time.
**Hypothesis**: A dedicated cascade column with a C-20 spec header produces C-21 more
reliably than a combined column because omission is structurally visible (a blank cell) rather
than hidden inside a single-consequence sentence. Tests whether column isolation is a stronger
C-21 mechanism than header instruction on a combined column.
**Predicted**: All 21 PASS → **155/155, GOLDEN**

---

Naive program plans group skills by namespace and stop there. Their gates say "done" or
"ready" — conditions without artifact names, thresholds, or actor transitions. Their stage
boundaries express file organization, not workflow logic. **This variation defeats flat-list
sequencing and abstract gates by requiring two things no flat plan can provide: (1) a
two-part actor justification that separates prerequisite reasoning from downstream cascade
consequence, forcing both rationale and displacement cost into every row, and (2) a
handoff+threshold gate template that names the delivering actor, receiving actor, artifact
type, and minimum count in one required format string.**

---

**Actor assignments** — the table uses two justification columns. Fill both for every actor
row. The cascade column is required: entries that name only a single consequence must be
expanded before proceeding.

| Actor | Namespaces | Arc layer | Why this position (prerequisites) | Cascade if displaced — use → arrows, 2+ ordered consequences, crossing arc-layer boundaries |
|-------|-----------|-----------|------------------------------------|---------------------------------------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; landscape context is required by every downstream layer. | Moved later: design is anchored in the author's assumptions → review evaluates a design targeting the wrong problem → prove tests a hypothesis without market grounding. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact; design without landscape context is unconstrained. | Moved earlier: design produces unconstrained speculation → depth layer evaluates a design built on wrong assumptions → synthesis draws conclusions from a corrupted arc. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact; evaluating or proving against a void produces no signal. | Moved before draft: review critiques a void with no anchor → prove investigates an undefined target → synthesis inherits ungrounded findings as if valid. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires spec and process model; simulation without both is structurally undefined. | Moved before draft: simulation runs against an undefined system → outputs cannot be compared to design intent → integration failures surface with no reference point for resolution. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate expectations; feedback without prior findings is noise. | Moved before depth: feedback produces anecdotes with no expectation model → team cannot distinguish expected from unexpected findings → listen artifacts become noise rather than calibrated signal. |
| Anyone | `topic` | Synthesis | Requires all prior signals; narrative without material is empty. | Moved earlier: topic:status has no material → readiness signal is a placeholder not a decision input → team makes a go/no-go without a signal foundation. |

**Evidence arc** — each layer produces what the next layer consumes:

1. **Breadth** (scout): Landscape signals that define what is worth building.
2. **Design** (draft): Authored intent anchored in breadth.
3. **Depth** (review, prove, flow, trace): Stress-testing the design.
4. **Synthesis** (listen, topic): Post-signal conclusions.

---

**Complete skill catalog** — no other skill names exist. Any name not in this list is
invalid:

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
(Breadth → Design → Depth → Synthesis). The arc-layer mapping determines stage grouping
and gate positions.

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format for every non-echo
gate — all three elements must appear together:

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

## V-03 — Minimum-Density 155/155 Form

**Axis**: Instruction density — minimum text sufficient for 155/155. Column header embeds
C-20 spec. All 6 actor rows have minimum 2-hop → cascades (no 3rd hop). No archetype
pre-fill preamble. No post-table cascade verification step. No cascade reference in gates.
**Hypothesis**: C-21 requires every entry to demonstrate "2+ ordered consequences crossing
arc-layer boundaries" — the minimum is 2 hops, not 3. This variation tests whether 2-hop
cascades per row satisfy C-21 scoring, or whether the R4-V-01 and V-05 archetypes (3-hop)
set a de facto depth expectation. If 2-hop passes, V-03 is the efficient frontier at lower
instruction density than V-01.
**Predicted**: All 21 PASS → **155/155, GOLDEN**

---

Naive program plans produce flat skill lists with abstract gates. Their gates say "complete"
or "proceed" — neither names an artifact, a threshold, nor an actor. **This variation
defeats flat-list planning and abstract gates by requiring every stage boundary to expose
a workflow handoff: the delivering actor, the receiving actor, the minimum artifact count,
and the specific artifact type — all in a single required gate format string.**

---

**Actor assignments** — each entry must name why this actor cannot run earlier and trace
the cascade of failures if displaced. Use → arrows. Every row requires 2+ ordered
consequences crossing arc-layer boundaries.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier — cascade if displaced (use → arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; all downstream work requires landscape context. Moved later: design targets an unvalidated problem → depth layer evaluates a design anchored in wrong assumptions. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation with no anchor → depth layer receives a design built on unvalidated assumptions. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact. Moved before draft: review critiques a void → synthesis inherits ungrounded findings as if they were valid signal. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires spec and process model. Moved before draft: simulation runs against an undefined system → outputs cannot be compared against design intent. |
| Team | `listen` | Synthesis | Requires depth signals. Moved before depth: feedback produces anecdotes with no expectation model → listen artifacts cannot calibrate against validated findings. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved earlier: topic:status has no material → readiness signal is a placeholder not a decision input. |

**Evidence arc** — each layer produces what the next layer consumes:

1. **Breadth** (scout): Landscape signals. Nothing downstream is productive without them.
2. **Design** (draft): Authored intent anchored in breadth.
3. **Depth** (review, prove, flow, trace): Stress-testing the design.
4. **Synthesis** (listen, topic): Post-signal conclusions.

---

**Complete skill catalog** — no other skill names exist. Any name not in this list is
invalid:

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
(Breadth → Design → Depth → Synthesis).

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format for every non-echo
gate — all three elements must appear together:

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

## V-04 — Gate-Integrated Cascade

**Axis**: Cascade in gate format — the gate template embeds a cascade consequence statement
directly inside the gate string. The unified gate template becomes:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type — removing this gate: [cascade consequence chain]"`

Actor table retains C-20 header and full 3-hop cascades for C-21. The cascade consequence
clause in the gate format structurally satisfies C-17 (what-happens-if-removed) in every
gate, not just in the arc strategy step.
**Hypothesis**: Embedding gate-removal consequence inside the gate template simultaneously
enforces C-07 (artifact reference), C-10 (quantified threshold), C-12 (actor-role framing),
C-16 (unified template), and C-17 (what-happens-if-removed) with zero instruction overhead.
The arc strategy statement (Step 8) should be richer when every gate already carries its
own cascade reasoning. Tests whether gate-level cascade integration produces stronger C-09
performance than actor-table-only cascade.
**Predicted**: All 21 PASS → **155/155, GOLDEN**

---

Naive program plans sort skills by namespace and stop there. Their gates say "complete" or
"proceed" — no artifacts, no thresholds, no consequence for removal. A gate that names no
consequence can be removed without the plan changing. **This variation defeats consequence-free
gates and flat-list stage ordering by two mechanisms: (1) a required gate template that
names the delivering actor, receiving actor, minimum threshold, artifact type, AND the
cascade that follows if the gate is removed — making every gate carry its own justification,
and (2) an actor-layer table where every entry traces the displacement cascade before any
skill is placed.**

---

**Actor assignments** — each entry must name why this actor cannot run earlier and trace
the cascade of failures downstream using → arrows. Every row requires 2+ ordered consequences
crossing arc-layer boundaries.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier — and what cascade breaks downstream (use → arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; every downstream layer depends on landscape signals. Moved later: design is anchored in the author's assumptions → review evaluates a design targeting the wrong problem → prove tests a hypothesis without market grounding. Scout gates protect all downstream layers simultaneously. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation with no landscape anchor → depth layer evaluates a design built on wrong assumptions → synthesis draws conclusions from a corrupted evidence arc. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact to evaluate. Moved before draft: review critiques a void with no anchor → prove investigates an undefined target → synthesis inherits ungrounded findings as if they were valid. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires a spec and a process model. Moved before draft: simulation runs against an undefined system → outputs cannot be compared against design intent → integration failures surface with no reference point for resolution. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate expectations. Moved before depth: feedback produces anecdotes with no expectation baseline → team cannot distinguish expected from unexpected findings → listen artifacts are noise rather than calibrated signal. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved earlier: narrative has no material → topic:status is a placeholder not a decision input → team makes a go/no-go without a signal foundation. |

**Evidence arc** — each layer produces what the next layer consumes:

1. **Breadth** (scout): Landscape signals. Nothing downstream is productive without them.
2. **Design** (draft): Authored intent anchored in breadth.
3. **Depth** (review, prove, flow, trace): Stress-testing the design.
4. **Synthesis** (listen, topic): Post-signal conclusions.

---

**Complete skill catalog** — no other skill names exist. Any name not in this list is
invalid:

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
(Breadth → Design → Depth → Synthesis).

**Step 4 -- Write handoff gates using the cascade gate format.** Required format for every
non-echo gate — all five elements must appear together:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier] — removing this gate: [cascade consequence chain]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts (scout-requirements, scout-market) present — removing this gate: design is anchored in assumptions → depth evaluates a wrong-problem design → prove tests an ungrounded hypothesis"`
- `"Architect hands off to Team when >=1 draft-spec artifact present — removing this gate: depth layer has no artifact to evaluate → review produces open-ended critique with no anchor → synthesis inherits ungrounded findings"`
- `"Team hands off to Dev when >=2 depth signals (review-design, prove-hypothesis) present — removing this gate: simulation runs against a design that has not been stress-tested → integration failures cannot be traced to validated design decisions"`

Rules: Name both actors. Name specific artifact types. `>=N` threshold required. Cascade
consequence chain required. "Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Names reflect arc intent (`discovery`, `design`,
`validation`, `synthesis`), not skill names or `stage1`.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages`, and echo.
Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** Write 2-3 sentences: what this plan prioritizes early,
what it defers, and what the gates collectively protect — specifically, what is the
multi-hop consequence cascade if the first gate (scout handoff) is removed.

---

## V-05 — Cascade-First Structure

**Axis**: Structural ordering — the actor cascade table appears first, before the
naive-competitor opener. The opener arrives second and explains why the table is structured
as shown. This inverts the standard order (opener → table) to test whether leading with
a fully-populated cascade table primes cascade internalization more strongly than receiving
it after framing.
**Hypothesis**: When the cascade table appears before any framing, the model encounters the
cascade pattern before instructions tell it what to do. The opener then reinforces a pattern
already demonstrated rather than priming a pattern that appears later. If V-05 produces
richer cascade entries in output than V-01 (same table depth, different position), then
cascade-first placement drives stronger internalization. If both produce equivalent output,
table position does not matter and only table content is load-bearing.
**Predicted**: All 21 PASS → **155/155, GOLDEN**

---

**Actor assignments** — this table defines the arc layer for every Signal namespace actor.
Each row demonstrates the required cascade depth: why this actor cannot run earlier, and the
cascade of failures that propagate if it is displaced. When you construct your own actor
table, match this depth for every row.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier — and what cascade breaks downstream (use → arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; every downstream layer depends on landscape signals. Moved later: design is anchored in the author's assumptions → review evaluates a design targeting the wrong problem → prove tests a hypothesis without market grounding. Scout gates protect all downstream layers simultaneously. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation with no landscape anchor → depth layer evaluates a design built on wrong assumptions → synthesis draws conclusions from a corrupted evidence arc. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact to evaluate. Moved before draft: review critiques a void with no anchor → prove investigates an undefined target → synthesis inherits ungrounded findings as if they were valid. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires a spec and a process model. Moved before draft: simulation runs against an undefined system → outputs cannot be compared against design intent → integration failures surface with no reference point for resolution. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate expectations. Moved before depth: feedback produces anecdotes with no expectation baseline → team cannot distinguish expected from unexpected findings → listen artifacts are noise rather than calibrated signal. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved earlier: narrative has no material → topic:status is a placeholder not a decision input → team makes a go/no-go without a signal foundation. |

---

The table above demonstrates why naive program plans fail. A flat skill list does not
prevent arc-layer cascade failure: when the PM (breadth) is displaced, the design layer
has no validated anchor — it builds on assumptions. Because design is now anchored in
assumptions, the depth layer evaluates a design targeting the wrong problem. Because depth
is producing findings against a corrupted design, synthesis draws conclusions from compounded
errors. The failure is not local to one stage — it propagates through every downstream arc
layer, each one inheriting the corruption of the previous.

**This variation defeats arc-layer cascade failure and abstract gate conditions by two
structural choices visible in the table above**: (1) every actor row traces its displacement
cascade before any skill is placed, keeping the cascade visible at the moment of assignment,
and (2) a required handoff+threshold gate template that names the delivering actor, receiving
actor, minimum threshold, and artifact type at every stage boundary.

**Evidence arc** — each layer produces what the next layer consumes:

1. **Breadth** (scout): Landscape signals that define what is worth building.
2. **Design** (draft): Testable artifacts anchored in breadth signals.
3. **Depth** (review, prove, flow, trace): Validation signals against the design.
4. **Synthesis** (listen, topic): Conclusions drawn from the full signal set.

---

**Complete skill catalog** — no other skill names exist. Any name not in this list is
invalid:

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
(Breadth → Design → Depth → Synthesis). The actor cascade table above defines which
namespaces belong to each layer.

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format for every non-echo
gate — all three elements must appear together:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules: Name both actors. Name specific artifact types (`scout-feasibility`, `draft-spec`).
`>=N` threshold required. "Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Stage names communicate arc intent:
`discovery`, `design`, `validation`, `synthesis` — not generic (`stage1`), not skill names.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
The echo surfaces what the signals revealed that was not in the original plan. No other stage
may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages` (name, skills,
gate), and the echo final stage. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** After the YAML, write 2-3 sentences: what the plan
prioritizes early, what it defers, and what happens if any gate is removed — specifically,
what is the multi-hop consequence cascade if the first gate (scout handoff) is removed.

---

## Predicted Score Summary

| ID | Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | Total | Golden |
|----|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | Full-replication baseline | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **P** | **P** | **155** | YES |
| V-02 | Two-column cascade table | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **P** | **P** | **155** | YES |
| V-03 | Minimum-density form | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **P** | **P** | **155** | YES |
| V-04 | Gate-integrated cascade | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **P** | **P** | **P** | **155** | YES |
| V-05 | Cascade-first structure | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | **P** | **P** | **155** | YES |

Points: Essential 12 pts x 5 = 60 | Recommended 10 pts x 3 = 30 | Aspirational 5 pts x 13 = 65
Max 155 | Golden = all essential pass AND composite >= 124.

C-20 and C-21 risk assessment per variation:

| ID | C-20 location | C-21 coverage | Risk |
|----|---------------|---------------|------|
| V-01 | Combined header: "cannot run earlier — and what cascade breaks downstream (use → arrows, 2+ ordered consequences, crossing arc-layer boundaries)" | All 6 rows: 3-hop → chains | Low — confirmed R4-V-01 pattern |
| V-02 | Cascade column header: "Cascade if displaced — use → arrows, 2+ ordered consequences, crossing arc-layer boundaries" | All 6 rows: 3-hop → chains in cascade column | Low — header isolation, but scorer may interpret C-20 as applying to combined column only |
| V-03 | Combined header: same C-20 spec as V-01 | All 6 rows: 2-hop → chains | Medium — 2-hop meets C-21 letter (2+ required); 3-hop may be scorer expectation from R4 archetypes |
| V-04 | Combined header: same C-20 spec as V-01 | All 6 rows: 3-hop → chains | Low — same table structure as V-01, gate format adds no risk |
| V-05 | Combined header: same C-20 spec as V-01 | All 6 rows: 3-hop → chains | Low — same table structure as V-01, position swap adds no risk |

---

## R5 Hypotheses to Resolve in Scoring

**R5-H01: Is the R4-V-01 155/155 score stable?**
V-01 is a direct replication. If it scores 155/155, the R4 ceiling is stable. If it scores
lower, the R4 result was stochastic (unlikely given rubric is evaluated on variation text,
not output).

**R5-H02: Does column isolation (V-02 two-column table) score C-20 and C-21?**
C-20 requires the column header to embed cascade notation. V-02's cascade column header
does embed this. The risk is whether the scorer treats C-20 as requiring a SINGLE combined
column or accepts a dedicated cascade column as the relevant header. If V-02 passes C-20,
column isolation is a valid alternative C-21 mechanism. If V-02 fails C-20, the criterion
requires a single combined justification column.

**R5-H03: Does 2-hop depth (V-03) pass C-21?**
C-21 says "2+ ordered consequences." V-03 rows are minimum 2-hop. If V-03 passes C-21,
the 3-hop depth in V-01/V-04/V-05 is above the minimum. If V-03 fails C-21, the criterion
requires 3-hop chains despite saying "2+" — or the scorer considers R4-V-01/V-05 archetypes
(3-hop) as the de facto standard. This is the key efficiency question for R5.

**R5-H04: Does gate-integrated cascade (V-04) produce a richer arc strategy in Step 8?**
V-04's gate format embeds "removing this gate: [cascade]" in every gate. Step 8 asks for
the multi-hop consequence of removing the first gate — which has already been stated in the
gate itself. This tests whether the gate format pre-populates Step 8 reasoning or whether
redundancy produces lower-quality arc strategy statements (model restates the gate rather
than synthesizing across all gates).

**R5-H05: Does cascade-first placement (V-05) produce deeper cascade entries in output?**
V-05 leads with the cascade table before the opener. If model output for V-05 topics has
richer cascade entries in their actor tables than V-01 output (controlled for topic), then
position is load-bearing. If output quality is equivalent, only table content matters.
This hypothesis can only be resolved through production execution across multiple topics.
