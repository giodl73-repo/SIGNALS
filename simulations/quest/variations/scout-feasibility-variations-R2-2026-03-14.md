**scout-feasibility-variations-R2-2026-03-14.md** written. Here's what each variation does and why it differs from Round 1:

---

## Round 2 Variations

| V | Axis | Core move |
|---|------|-----------|
| **V-01** FINDINGS-mirror | Output format | Numbered FINDINGS 0-9 aligned to rubric criteria — each criterion is a named required slot, not an emergent property of good execution |
| **V-02** Sum-first | Lifecycle emphasis | Hour enumeration is the *only* act in Phase 3 (no ratings) — the budget chain must close in Phase 4 before any traffic light can appear in Phase 5 |
| **V-03** Prohibitive | Phrasing register | "PROHIBITED until" replaces "do not proceed until" — frames constraints as output properties rather than workflow instructions |
| **V-04** Interrogative + sum-first | Phrasing + lifecycle | R1 V-04 scored 95 but failed C-09 because Q2 had available hours and Q3 had ratings but no per-component estimates between them. R2 inserts a dedicated Q3 (hour enumeration) + Q4 (chain closure) before Q5 (ratings) — minimal surgery on a known-strong frame |
| **V-05** Golden synthesis | Format + register + lifecycle | Combines R1 scorecard synthesis targets: FINDINGS-mirror structure, PM-first ordering, prohibitive language for C-12, explicit four-element chain instruction, V-05 R1's score-delta amendment format |

---

### Key design decision

Every R2 variation enforces C-09, C-11, and C-12 — the three criteria that failed in 4/5 R1 variations. The variation is *how* the constraints are enforced. Round 2 should determine whether **output-format enforcement** (V-01), **lifecycle separation** (V-02), **prohibitive language** (V-03), or **question-sequence ordering** (V-04) produces the most reliable execution — and whether V-05's synthesis beats them all.
ood execution.
R1 V-02 excellence signal: "FINDINGS section mirrors rubric structure." This variation makes
it the organizing principle rather than a secondary benefit.

```
You are running /scout-feasibility. Produce the findings below in sequence.
Each FINDING is a required output slot -- write its header before its content.

SETUP -- STACK SCAN:
Scan for: package.json, tsconfig.json, Cargo.toml.
If none found: write one sentence naming the fallback source and what was inferred.
This is FINDING 0 and is required before any other finding.

FINDING 1 -- INFERENCE BLOCK:
Write as a contiguous block. Do not write FINDING 2 until all three appear here:
  Feature:   [one sentence describing what is being assessed]
  Team:      [N engineers -- source: ___]
  Timeline:  [N sprints/weeks -- source: ___]

FINDING 2 -- BUDGET CHAIN:
Required before FINDING 3. Compute and write all four elements as a linked chain:
  Available hours = [team] x [hrs/sprint] x [sprints] = [N] hrs
  Component hour estimates:
  | Component | Estimated Hours |
  | Total     | [N]             |
  Estimated: [N] | Available: [N] | Delta: [+-N] | OVER-BUDGET / UNDER-BUDGET / ON-BUDGET

FINDING 3 -- COMPONENT RATINGS:
| Component | GREEN / YELLOW / RED | Rationale | Hours (from F2) |

FINDING 4 -- COMPOSITE VERDICT:
Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE.

FINDING 5 -- RED BLOCKERS:
Required for every RED component from F3:
  [Component]: [Why it is blocked] -- [Lift condition: what changes the rating]
Omit this finding only if no component is RED.

FINDING 6 -- BUILD VS BUY:
| Component | Build / Buy / Use existing | Strategic rationale |
Required for at least 50% of components.

FINDING 7 -- SCOPED ALTERNATIVE:
Required when score < 50 (NOT FEASIBLE):
  "Scoped to [specific constraint]: [N]/100."
Omit if score >= 50.

FINDING 8 -- PREREQUISITES:
Required when label is FEASIBLE WITH CAVEATS:
Numbered list. Every RED-rated component from F3 must appear.
Omit if label is not FEASIBLE WITH CAVEATS.

FINDING 9 -- AMENDMENTS:
Numbered actions converting RED and YELLOW findings to next steps.
Each action must:
  - Name the specific component it addresses
  - State what changes in the feasibility score if the action is completed
    (e.g., "Completing this moves [Component] from RED to YELLOW, raising score ~10 pts")

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated.
```

---

## V-02: Sum-first lifecycle

**Axis:** Lifecycle emphasis -- hour enumeration is the first substantive act; no rating appears
until the budget chain is closed
**Hypothesis:** Separating enumeration (hours only, no ratings) from evaluation (ratings, using
the closed chain) makes C-12 structurally necessary. In R1, even V-02 computed hours and ratings
in the same phase (PHASE 2). Sum-first creates a hard checkpoint that cannot collapse even under
length pressure.

```
You are running /scout-feasibility. Lifecycle order: enumerate hours first,
close the budget chain, then rate. No traffic light may appear before the chain closes.

PHASE 1 -- STACK:
Scan: package.json, tsconfig.json, Cargo.toml.
If absent: name the fallback source and state what was inferred. Required.

PHASE 2 -- INFERENCE GATE:
Write as a contiguous block. Do not continue until all three are visible:
  Feature:   [one sentence]
  Team:      [N engineers -- source: ___]
  Timeline:  [N sprints/weeks -- source: ___]

PHASE 3 -- HOUR ENUMERATION (no ratings in this phase):
List all feature components and estimate hours for each. No traffic lights yet.
| Component | Description          | Estimated Hours |
| Total     |                      | [N]             |

PHASE 4 -- BUDGET CHAIN (required before Phase 5):
Available hours = [team] x [hrs/sprint] x [sprints] = [N] hrs
  Estimated:  [N hrs -- from Phase 3 total]
  Available:  [N hrs]
  Delta:      [+-N]
  Flag:       OVER-BUDGET / UNDER-BUDGET / ON-BUDGET

PHASE 5 -- TRAFFIC LIGHTS:
The budget chain is now closed. Rate each component using the Phase 4 flag.
YELLOW means stack-fit but tight; RED means stack gap or budget cannot absorb without
mitigation. A component that pushes an already-over-budget team is not YELLOW.
| Component | Rating | Rationale | Hours |
Blockers (required for every RED component):
  [Component]: [Why blocked] -- [Lift condition]

PHASE 6 -- STRATEGY:
| Component | Build / Buy / Use existing | Rationale |

PHASE 7 -- VERDICT:
Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE.
If score < 50: "Scoped to [constraint]: [N]/100." Required.
If FEASIBLE WITH CAVEATS: numbered prerequisites, all RED items represented.

PHASE 8 -- AMENDMENTS:
Numbered actions. Each must name the specific RED or YELLOW component and state
what changes in the feasibility score if the action is completed.

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated.
```

---

## V-03: Prohibitive register

**Axis:** Phrasing register -- "PROHIBITED until" output rules replace "do not proceed until"
phase gates
**Hypothesis:** Framing constraints as hard output rules ("Rating a component is PROHIBITED
until X") is structurally distinct from sequencing instructions ("do not proceed to Phase N
until X"). Rules-of-output frame the constraint as a property of the artifact, not a workflow
instruction, which may be harder for the model to override under compression or length pressure.

```
You are running /scout-feasibility. The following output rules are hard constraints.
Violations produce an invalid artifact.

RULE 1 -- TRAFFIC LIGHT FORMAT:
Every component MUST receive an explicit GREEN / YELLOW / RED label as a distinct field
in a table row. Labels embedded in prose are PROHIBITED.

RULE 2 -- INFERENCE GATE:
Scoring any component is PROHIBITED until the following block appears as a unit:
  (a) Feature description -- one sentence
  (b) Inferred team size -- with source
  (c) Inferred timeline -- with source
The block must be contiguous. Scattered values do not satisfy RULE 2.

RULE 3 -- BUDGET BEFORE RATINGS:
Traffic-light ratings are PROHIBITED until the budget chain appears and is closed.
The budget chain MUST contain all four elements:
  (a) Sum of per-component estimated hours
  (b) Available hours (team x hrs/sprint x sprints)
  (c) Delta
  (d) OVER-BUDGET / UNDER-BUDGET / ON-BUDGET flag

RULE 4 -- RED BLOCKERS:
Every RED component MUST have a blocker entry: why it is blocked, and what specific
change lifts the rating. Omitting a blocker for any RED component is PROHIBITED.

RULE 5 -- BUILD VS BUY:
At least 50% of components MUST carry a Build / Buy / Use existing label.

RULE 6 -- VERDICT:
The output MUST close with a numeric score (0-100) and one of: NOT FEASIBLE /
FEASIBLE WITH CAVEATS / FEASIBLE, as a dedicated section.

Run the assessment in this order (RULES 2 and 3 enforce the ordering):
1. Stack scan: find package.json, tsconfig.json, Cargo.toml. If absent, name the
   fallback source and state what was inferred. Required before step 2.
2. Write the RULE 2 inference block (all three required values, contiguous).
3. Enumerate components and estimate hours per component (satisfies RULE 3 part a).
4. Compute available hours and close the budget chain (satisfies RULE 3 parts b-d).
   RULE 3 now unblocked: traffic-light ratings may begin.
5. Write component ratings table (RULE 1).
6. Write RED blocker entries (RULE 4).
7. Write Build / Buy / Use existing table (RULE 5).
8. Write verdict score and label (RULE 6). Add scoped alternative if score < 50.
   Add prerequisites if FEASIBLE WITH CAVEATS.
9. Write numbered amendment actions, each traceable to a RED or YELLOW component.
   Each action must state what changes in the feasibility score if completed.

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated.
```

---

## V-04: Interrogative + sum-first

**Axes:** Phrasing register (interrogative Q&A) + lifecycle emphasis (hour sum before ratings)
**Hypothesis:** R1 V-04 scored 95 but failed C-09 because Q2 collected available hours but
Q3 had no per-component hour estimates -- the inputs never met. Adding a dedicated hour-sum
question (Q3) before the ratings question (Q4) closes the chain without disrupting the Q&A frame
that produced clean C-03/C-04 compliance in R1. This is a minimal surgical extension of the
R1 V-04 pattern.

```
You are running /scout-feasibility. Answer each question in sequence.
Each answer is a named finding. Questions run in fixed order.

Q1. What is the stack?
Scan: package.json, tsconfig.json, Cargo.toml. List detected signals.
If canonical files absent: write one sentence naming the fallback file and what was inferred.
Required before Q2.

Q2. Who is building this, and when?
Write as a contiguous block. Do not proceed to Q3 without all three values:
  Feature:   [one sentence describing what is being assessed]
  Team:      [N engineers -- source: ___]
  Timeline:  [N sprints/weeks -- source: ___]

Q3. What will it cost in hours?
Enumerate all components and estimate hours for each. No ratings yet.
| Component | Estimated Hours |
| Total     | [N]             |

Q4. Does the budget cover the estimate?
Available hours = [team] x [hrs/sprint] x [sprints] = [N] hrs
Write the chain as a single linked statement:
  Estimated [N from Q3] | Available [N] | Delta [+-N] | OVER / UNDER / ON-BUDGET
All four elements required. Do not proceed to Q5 without the flag.

Q5. What is the traffic-light rating for each component?
The budget flag from Q4 is visible. Use it -- RED means stack gap or over-budget
without mitigation. Do not rate components without the Q4 chain on the page above.
| Component | Rating | Rationale | Hours |
For every RED component: why is it blocked? What would lift it?

Q6. Should each component be built, bought, or reused?
| Component | Build / Buy / Use existing | Reasoning |
Required for at least 50% of components.

Q7. What is the verdict?
Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE.
If score < 50: "Scoped to [constraint]: [N]/100." Required.
If FEASIBLE WITH CAVEATS: numbered prerequisite list, all RED items included.

Q8. What should the team do next?
Numbered actions. Each must:
  - Name the specific RED or YELLOW component it addresses
  - State what changes in the feasibility score if the action is completed

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated.
```

---

## V-05: Golden synthesis

**Axes:** Output format (FINDINGS-mirror) + phrasing register (prohibitive) + lifecycle emphasis
(PM-first) + score-delta amendment format
**Hypothesis:** Combines the four winning patterns from R1 scorecard synthesis: (1) FINDINGS
structure mirrors rubric criteria, (2) PM-first role ordering makes C-12 structurally unavoidable,
(3) explicit chain instruction closes C-09, (4) V-05's score-delta amendment format (strongest
C-10 formulation). This is the synthesis target identified in the R1 scorecard.

```
You are running /scout-feasibility. PM runs first. Every gate must fire.
FINDINGS mirror rubric criteria. This is the structured synthesis run.

SETUP -- STACK SCAN:
Scan: package.json, tsconfig.json, Cargo.toml.
If absent: write one sentence naming the fallback file and what was inferred.
Required before the inference gate.

INFERENCE GATE -- write as a contiguous block before any component appears:
  Feature:   [one sentence]
  Team:      [N engineers -- source: ___]
  Timeline:  [N sprints/weeks -- source: ___]
Do not proceed until all three are visible.

PHASE 1 -- PM: BUDGET (runs before Architect complexity scoring):
From the inference gate values:
  Available hours = [team] x [hrs/sprint] x [sprints] = [N] hrs
Enumerate all components and estimate hours:
| Component | Estimated Hours |
| Total     | [N]             |
Close the budget chain -- all four elements required before Phase 2:
  Estimated: [N] | Available: [N] | Delta: [+-N] | OVER-BUDGET / UNDER-BUDGET / ON-BUDGET

PHASE 2 -- ARCHITECT: COMPLEXITY (budget is now visible):
Rate each component using the closed budget chain from Phase 1.
Traffic-light ratings are PROHIBITED before the Phase 1 chain is closed.
| Component | Rating | Rationale | Hours (from Phase 1) |
Blockers (required for every RED component):
  [Component]: [Why blocked] -- [Lift condition: what specifically changes the rating]

PHASE 3 -- STRATEGY: BUILD VS BUY:
| Component | Build / Buy / Use existing | Strategic rationale |
Required for at least 50% of components.

FINDINGS:
F1. Composite score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE.
F2. Budget summary: estimated [N] vs available [N] -- flag: [OVER/UNDER/ON]-BUDGET.
F3. [IF NOT FEASIBLE] Scoped alternative: "Scoped to [constraint]: [N]/100.
    This scope removes [RED items] from the build."
F4. [IF FEASIBLE WITH CAVEATS] Prerequisites: numbered list, all RED items represented.
F5. Amendments: numbered actions -- each must name the specific RED or YELLOW component
    and state what changes in the feasibility score if the action is completed.
    Example format: "Completing this moves [Component] from RED to YELLOW, raising
    score by approximately [N] pts."

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated.
```

---

## Round 2 Design Notes

### What changed from Round 1

R1 identified three structural gaps missing from 4/5 variations:
- **C-09 gap**: hours collected in two phases but chain never closed (R1-01)
- **C-11 gap**: inference disclosure scattered or post-scoring (R1-02)
- **C-12 gap**: budget computed after complexity scoring (R1-03)

All five R2 variations are designed to satisfy all three. The axes vary *how* the constraints
are enforced, not whether they exist.

### Predicted differentiation

| Criterion | Most at risk | Why |
|-----------|-------------|-----|
| C-09 | V-01 | FINDINGS-mirror makes the chain a named slot, but slot-filling pressure may truncate the flag |
| C-11 | V-03 | Prohibitive RULE 2 is strong but the model must apply the rule to its own output ordering |
| C-12 | V-04 | Q-sequence enforces ordering, but Q3/Q4 separation requires no rating answer to bleed into Q3 |

### V-golden candidate

V-05 is the direct synthesis target from R1. If it achieves 100, the next question is
whether one of V-01/V-02/V-03/V-04 matches it -- and whether any variation shows a
qualitative difference in the reasoning depth of RED blocker rationale or amendment specificity.
