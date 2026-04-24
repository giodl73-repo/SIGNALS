---

# scout-size — Prompt Variations (Round 1)

**Skill:** `scout-size` — Feature sizing and effort estimation signal
**Rubric:** v1 (10 criteria, 5 essential)
**Variation round:** R1

---

## Variation Axes Selected

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Output format | TABLE-FIRST | default | default | default | TABLE-FIRST |
| Inertia framing | default | INERTIA-FIRST | default | default | INERTIA-FIRST |
| Role sequence | default | default | ARCH-FIRST | default | default |
| Phrasing register | default | default | default | CONVERSATIONAL | FORMAL |
| Lifecycle emphasis | default | default | default | EXPLICIT-PHASES | default |

Single-axis: V-01 (format), V-02 (inertia), V-03 (role sequence)
Combination: V-04 (register + lifecycle), V-05 (inertia + format + register)

---

## V-01 — Table-First Output Format

**Axis:** Output format
**Hypothesis:** Mandating a structured summary table for all 5 sizing dimensions makes omission structurally impossible — each row is a required cell.

```
Produce a sizing signal for the feature described below. The output is consumed
by program-plan; it is NOT a project plan.

REQUIRED: Begin with a sizing summary table before any prose. The table must
have exactly these rows. Leave no cell empty.

| Dimension        | Value                    | Notes                         |
|------------------|--------------------------|-------------------------------|
| Complexity       | LOW / MEDIUM / HIGH / XL | Primary driver (1 sentence)   |
| Timeline         | N-M sprints              | Range required, not a point   |
| Surface Area     | N integration points     | Named list below the table    |
| Team Signal      | Role A + Role B + ...    | Specializations, not headcount|
| Confidence       | LOW / MED / HIGH (N%)    | Basis (1 sentence)            |

After the table, expand each row:

SURFACE AREA — enumerate every integration point by name (APIs, hooks, stores,
UI surfaces, external systems). If fewer than 2, explain why.

COMPLEXITY DRIVER — one sentence naming what pushed the complexity to that tier.
"HIGH because X", "LOW because Y". This must appear.

TEAM SIGNAL — for each role, state what they own during implementation, not just
their title.

CONFIDENCE BASIS — state what is known vs unknown. If confidence is LOW or MED,
name the specific unknowns driving it down.

INERTIA CHECK — this section is mandatory and appears last before the scope note.
Name what teams currently do without this feature (the workaround). State at
least one cost dimension (time lost, error rate, manual steps, capability gap).
Then state a break-even signal: at what adoption level or frequency does building
this feature pay off relative to continuing the workaround? If break-even cannot
be assessed, say why.

SCOPE — one bullet list of what this sizing does NOT cover (out-of-scope
sub-systems, deferred complexity, assumptions made).

AMEND support: if an AMEND directive is present, modify the affected table cell
and the corresponding expansion section. The table must reflect the amendment --
do not acknowledge it without changing the output.

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Inertia-First Framing

**Axis:** Inertia framing
**Hypothesis:** Opening with the current workaround as the primary frame causes the inertia check to be substantive (not an afterthought) and naturally surfaces break-even because all sizing is anchored against the cost of not building.

```
Before estimating anything, name the competition.

STEP 1 — INERTIA CHECK (run this before sizing)
What do teams currently do without this feature? Name the workaround precisely.
State its cost on at least one dimension: time per use, error rate, manual steps,
or missing capability. Then estimate a break-even signal: at roughly what usage
level or frequency does building this feature recover its implementation cost
relative to the ongoing workaround cost? If you cannot assess break-even, explain
the blocker. The inertia check is the most important section -- a sizing signal
that skips it is indistinguishable from a raw effort guess.

STEP 2 — SURFACE AREA
Count and name the integration points: APIs, hooks, namespaces, data stores, UI
surfaces, external systems. List them. If the count is 0-1, explain why.

STEP 3 — COMPLEXITY
Rate complexity: LOW / MEDIUM / HIGH / XL. State the primary driver in one
sentence immediately after the rating. The driver is what pushed the tier up or
kept it down.

STEP 4 — TIMELINE SIGNAL
State a sprint range with both bounds (e.g., 2-4 sprints). A single number fails
because point estimates imply false precision. Calendar dates fail. The range
must be defensible from the surface area and complexity above.

STEP 5 — TEAM SIGNAL
Name the specializations required, not just headcount. "1 backend + 1 infra" not
"2 engineers". For each specialization, note what they own during the build.

STEP 6 — CONFIDENCE
State a confidence level (LOW / MED / HIGH or a percentage). Then give the
primary reason. If confidence is below HIGH, name the specific unknowns.

STEP 7 — SCOPE NOTE
List what this sizing does NOT cover: out-of-scope sub-systems, deferred work,
assumptions that could invalidate the estimate if wrong.

AMEND: if an AMEND directive is present (adjust confidence thresholds, focus on
a specific complexity dimension), apply it -- update the relevant step's content.
Do not only acknowledge the amendment; change the output.

Stock roles: Inertia Analyst (Step 1), Architect (Steps 2-3), PM (Steps 4-5),
Risk (Step 6).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Architect-First Role Sequence

**Axis:** Role sequence
**Hypothesis:** Running Architect (surface area + complexity) before PM (timeline) before Inertia Analyst ensures the complexity driver is established before the timeline is estimated, producing better-justified tier labels and tighter sprint ranges.

```
Produce a feature sizing signal. Run stock roles in this order -- each role
reads the previous role's output before producing its own.

ARCHITECT (runs first)
Enumerate integration points: APIs, hooks, namespaces, data stores, UI surfaces,
external systems. Name each one. Count them. Then assign a complexity tier:
LOW / MEDIUM / HIGH / XL. State the single driver that determined the tier.
"HIGH because distributed transaction boundary crosses service X and Y."
"LOW because isolated namespace, no shared state." The tier label and the driver
sentence must both appear.

PM (runs second, reads Architect output)
Translate the surface area and complexity into a timeline signal: a sprint range
with both lower and upper bound. Reason from the Architect's integration point
count and tier. State a team-size signal with specializations named -- "1 backend
+ 1 infra", not "2 engineers". For each role, note what they own.

INERTIA ANALYST (runs third, reads both)
Name what teams currently do without this feature. State at least one cost
dimension (time, error rate, manual effort, missing capability). Then provide a
break-even signal: at what adoption level or frequency does building this feature
pay off against continuing the workaround? If break-even cannot be assessed,
explain why. This is mandatory -- do not skip or abbreviate.

RISK (runs fourth, reads all)
State a confidence level (LOW / MED / HIGH). Give the primary basis. Name any
unknowns that would move confidence down. If the surface area or inertia check
revealed open questions, reference them.

SYNTHESIS
Produce a final artifact combining all four role outputs. Add a SCOPE section
listing what this sizing does NOT cover (out-of-scope systems, deferred
complexity, assumptions).

AMEND: if an AMEND directive is present, re-run the affected role and update
the synthesis. The amendment must produce a change in the artifact, not just
an acknowledgment.

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Conversational Register with Explicit Lifecycle Phases

**Axis:** Phrasing register (conversational) + lifecycle emphasis (explicit phases)
**Hypothesis:** Walking through 5 named phases in plain working language (rather than field-by-field instruction) produces fuller outputs because it matches how engineers actually talk through a sizing exercise, reducing mechanical compliance in favor of genuine reasoning.

```
Walk through a feature sizing in five phases. Each phase is a conversation
between roles -- keep the reasoning visible.

--- PHASE 1: WHAT ARE WE TOUCHING? ---
Look at the feature and ask: what parts of the system have to change or connect
for this to work? List every integration point you find -- APIs, hooks, data
stores, UI surfaces, external systems. Be specific; "the backend" does not count.
Count the total. This is your surface area.

--- PHASE 2: HOW HARD IS IT REALLY? ---
Given the surface area from Phase 1, pick one: LOW / MEDIUM / HIGH / XL.
Then say out loud what made you pick that tier. Is it the number of integration
points? A tricky transaction boundary? Shared state across services? Unknown
territory? One honest sentence is enough. If you cannot name the driver, lower
your confidence in Phase 5.

--- PHASE 3: HOW LONG AND WHO? ---
Turn the complexity into a timeline signal: a sprint range. Give a low end and
a high end -- not a single number, because a single number implies you are more
certain than you are. Then name who needs to be on the team by specialization,
not by headcount. What does each person own?

--- PHASE 4: IS IT WORTH BUILDING? ---
Before committing to the estimate, ask: what do people do today without this?
Describe the workaround. What does it cost them -- time, errors, manual steps,
a capability they simply do not have? Then ask the harder question: at what
point does building this actually pay off relative to living with the workaround?
Even a rough answer ("break-even at ~5 uses per week across 3 teams") is more
useful than skipping it. If you truly cannot assess break-even, say why.

--- PHASE 5: HOW SURE ARE WE? ---
State a confidence level: LOW, MED, or HIGH (or a percentage if you prefer).
Tell the reader why. What do you know well? What is still fuzzy? If confidence
is anything less than HIGH, name the specific unknowns pulling it down.

--- SCOPE NOTE ---
Before finishing, note what this sizing does NOT cover. Out-of-scope sub-systems,
work deferred to a future iteration, assumptions that could change the estimate.
One bulleted list is fine.

AMEND: if an AMEND directive arrives after the initial sizing (adjust confidence
thresholds, dig deeper on one dimension), reopen the affected phase and revise
it. Update the artifact with the change -- the amendment is not complete until
the output is different.

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Combination: Inertia-First + Table + Formal Register

**Axis:** Inertia framing + output format + phrasing register (combination)
**Hypothesis:** Combining inertia-first framing with a mandatory summary table and strict formal terminology satisfies all rubric criteria systematically: the table enforces structural completeness, inertia-first prevents the break-even signal from being omitted as an afterthought, and formal register ensures canonical label usage (LOW/MEDIUM/HIGH/XL, sprint ranges).

```
You are producing a sizing signal artifact. The artifact feeds program-plan.
It is a signal, not a plan. Precision beyond what the evidence supports is
an error.

PROTOCOL

Section 1 — INERTIA CHECK (mandatory, runs before all sizing)
Identify the current workaround: the behavior teams use today in the absence of
this feature. State it specifically. Characterize its cost on at least one
dimension:
  - time cost (per-use or per-week)
  - error or quality cost
  - manual effort overhead
  - capability gap (something teams simply cannot do)
Then state a break-even signal: the adoption level, usage frequency, or team
count at which implementing this feature becomes net-positive relative to
perpetuating the workaround. Express as a threshold, not a guarantee. If
break-even assessment is blocked by insufficient data, state the blocking
condition explicitly.

Section 2 — SIZING SUMMARY TABLE
Present the following table. All cells are required. No cell may contain a
narrative substitute for the canonical value.

| Dimension    | Value                     | Basis / Driver                   |
|--------------|---------------------------|----------------------------------|
| Complexity   | LOW / MEDIUM / HIGH / XL  | One sentence naming the driver   |
| Timeline     | N-M sprints               | Derived from complexity + surface|
| Surface Area | N points (list follows)   | Count of named integration points|
| Team Signal  | Role + Role + ...         | Specializations, not headcount   |
| Confidence   | LOW / MED / HIGH          | One sentence naming the basis    |

Section 3 — SURFACE AREA DETAIL
Enumerate each integration point by name: APIs, hooks, event subscriptions,
data stores, UI surfaces, external systems. If the count is 0 or 1, state the
reason explicitly -- this is unusual and requires justification.

Section 4 — CONFIDENCE DETAIL
Expand the confidence basis from the table. If confidence is LOW or MED,
enumerate the specific unknowns. Reference the inertia check where relevant:
a poorly understood workaround reduces confidence in the break-even signal and
should be noted.

Section 5 — SCOPE EXCLUSIONS
State what this sizing does NOT cover. Include: out-of-scope sub-systems,
complexity deferred to later milestones, and assumptions whose violation would
materially change the estimate. At least one exclusion is required.

AMEND HANDLING
If an AMEND directive is present (adjust confidence thresholds; focus analysis
on a specific complexity dimension), apply the amendment by revising the
relevant table cell and its corresponding section. The amended artifact must
differ in content from the pre-amendment version. Acknowledgment without
content change does not satisfy the AMEND contract.

Stock roles: Inertia Analyst (Section 1), Architect (Sections 2-3),
Risk (Section 4), PM (table: Timeline + Team Signal rows).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| Variation | Primary Axis | Structural Bet | Predicted Strength | Predicted Risk |
|-----------|-------------|----------------|--------------------|----------------|
| V-01 | Table-first format | Table enforces completeness | C-01/02/03/06 pass rate | C-04 (inertia) may be thin |
| V-02 | Inertia-first | All sizing anchored to workaround cost | C-04/C-10 pass rate | C-01/02 label discipline |
| V-03 | Architect-first roles | Complexity grounded before timeline | C-07 driver quality | C-04 comes last, may compress |
| V-04 | Conversational phases | Phase names match engineer intuition | C-07/C-05 reasoning depth | C-01/02 label discipline without explicit constraints |
| V-05 | Inertia + Table + Formal | Multi-axis: structural + order + register | Highest composite, all 10 | Verbosity; AMEND section may be ignored |

**Expected leaderboard hypothesis:** V-05 > V-01 > V-02 > V-03 > V-04 on essential pass rate. V-04 likely highest on depth reasoning (C-07, C-05) if the model engages with the conversational invitation. V-03 most likely to fail C-04 (inertia comes last and compresses under context pressure).
