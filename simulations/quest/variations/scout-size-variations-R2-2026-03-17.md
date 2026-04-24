Written to `simulations/quest/variations/scout-size-variations-R2-2026-03-17.md`.

---

## scout-size Variations — Round 2

**Target rubric:** v2 (C-11 ownership scope, C-12 named unknowns, C-13 synthesis)
**Strategy:** R1 already satisfies C-01–C-10 with structural redundancy. R2 varies on the three new aspirational criteria only.

---

### Variation Axes

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Synthesis structure | FORCED-TEMPLATE | default | default | HYPOTHESIS-REVISION | FULL-STACK |
| Unknowns elevation | default | OWN-SECTION | default | default | FULL-STACK |
| Ownership contract | default | default | CONTRACT-TABLE | default | FULL-STACK |
| Base | V-05 R1 | V-02 R1 | V-01 R1 | novel | V-05 R1 |

---

### V-01 — Synthesis-Forcing Template (C-13)

**Axis:** Synthesis structure — single-axis
**Base:** V-05 R1 (inertia-first + table + formal)
**Hypothesis:** A fill-in-the-blank sentence template for Section 6 prevents "form-filling juxtaposition" by structurally requiring the model to name two dimensions before completing the sentence. "[Dimension A] combined with [Dimension B] [argues for / cautions against] [recommendation]" cannot be satisfied by restating sections in sequence.

Adds Section 4 (TEAM OWNERSHIP with `Role:` / `Owns:` sub-structure) and Section 5 with the explicit Unknown-movement format. Section 6 SYNTHESIS is the new structural bet: the anchor sentence template is mandatory, and the prompt explicitly names the failure mode ("Restating each section in sequence is not synthesis — it is juxtaposition").

---

### V-02 — Unknowns-as-Section (C-12)

**Axis:** Unknowns elevation — single-axis
**Base:** V-02 R1 (inertia-first steps)
**Hypothesis:** Splitting STEP 7 (OPEN UNKNOWNS) from STEP 6 (CONFIDENCE BASIS) elevates unknowns to first-class status. When unknowns are a sub-bullet they can be omitted silently; when they are a named section with `Unknown:` / `Impact:` / `Movement:` fields, a missing entry is structurally visible. Also prevents the HIGH-confidence dodge: "No open unknowns — confidence is stable. The following would lower it: [X]" is required as the fallback.

No synthesis section — this variation is deliberately single-axis to isolate C-12 behavior.

---

### V-03 — Ownership-Contract Table (C-11)

**Axis:** Ownership contract format — single-axis
**Base:** V-01 R1 (table-first)
**Hypothesis:** A three-column table (`Role | Owns | Dependency`) makes a missing Owns cell visually detectable the same way a blank table cell is more obviously incomplete than a missing prose sentence. The prompt explicitly names the failure mode: "Owns: backend work" fails; "Owns: event schema + storage migration" passes. Also adds `Unknown → confidence movement` format to the confidence section, giving C-12 partial coverage.

No synthesis section — scope limited to C-11 improvement plus C-12 partial.

---

### V-04 — Synthesis-First with Hypothesis Revision (C-13 + novel lifecycle)

**Axis:** Synthesis structure + lifecycle inversion — combination (novel)
**Base:** New structure, no direct R1 ancestor
**Hypothesis:** An opening hypothesis that names two expected dimensions — before any sizing runs — forces the closing synthesis to be comparative rather than additive. The model must either confirm or revise its opening claim, which requires reasoning across dimensions. A closing that merely sequences sections cannot satisfy "return to the opening hypothesis and confirm or revise it." This is the strongest theoretical forcing function for C-13, but has execution risk: the model may treat the opening as a throw-away rather than a commitment.

Covers C-11 via the TEAM SIGNAL section ("state what they own during the build"), C-12 via the CONFIDENCE section (Unknown movement format). Full-coverage attempt but through conversational structure rather than table structure.

---

### V-05 — Full Aspirational Stack on V-05 R1 Base (C-11 + C-12 + C-13)

**Axis:** All three new criteria — combination
**Base:** V-05 R1 (98/100; highest R1 score)
**Hypothesis:** V-05 R1 already satisfies C-01–C-10 with structural redundancy. Layer all three new criteria onto that foundation:
- C-11 → Section 4 TEAM OWNERSHIP with `Role:` / `Owns:` / `Hands off:` sub-structure
- C-12 → Section 5 CONFIDENCE AND OPEN UNKNOWNS with `Unknown:` / `Affects:` / `Movement:` entries
- C-13 → Section 6 SYNTHESIS with mandatory anchor sentence template and explicit anti-juxtaposition language

Also extends AMEND handling: amendment must now re-evaluate Section 6 and update synthesis if the amended dimension changes the cross-signal conclusion.

**Expected ceiling:** highest composite of R2, inheriting V-05 R1's 98-point base while adding all three new aspirational paths.

---

### Predicted Leaderboard

| Rank | Variation | Structural Bet | Predicted Failure Mode |
|------|-----------|----------------|----------------------|
| 1 | V-05 | Full stack on best base | Verbosity risk on synthesis depth |
| 2 | V-01 | Synthesis template | C-12 still embedded in confidence section |
| 3 | V-04 | Hypothesis revision | Opening hypothesis treated as throw-away |
| 4 | V-02 | Unknowns as section | No synthesis section — C-13 absent |
| 5 | V-03 | Ownership contract table | C-12 partial only; no synthesis |
CLUSIONS
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
PM (table: Timeline + Team Signal rows, Section 4), Risk (Section 5),
Synthesis Lead (Section 6).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Unknowns-as-Section

**Axis:** Unknowns elevation (C-12 target)
**Hypothesis:** Elevating unknowns from a sub-bullet inside the confidence section to its
own named section with explicit "what would move this rating" prompting forces the model to
treat unknowns as first-class sizing artifacts — not as a confidence footnote. This prevents
the pattern where a model states HIGH confidence and never engages with C-12.

```
Before estimating anything, name the competition.

STEP 1 — INERTIA CHECK (run this before sizing)
What do teams currently do without this feature? Name the workaround precisely.
State its cost on at least one dimension: time per use, error rate, manual steps,
or missing capability. Then estimate a break-even signal: at roughly what usage
level or frequency does building this feature recover its implementation cost
relative to the ongoing workaround cost? If you cannot assess break-even, explain
the blocker. The inertia check is the most important section — a sizing signal
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
"2 engineers". For each specialization, state what they own during the build:
what specific artifact, layer, or sub-system is theirs to deliver.

STEP 6 — CONFIDENCE LEVEL AND BASIS
State a confidence level (LOW / MED / HIGH or a percentage). Give the primary
reason — what you know that supports this rating.

STEP 7 — OPEN UNKNOWNS
This is a separate section from Step 6. For each open unknown that affects sizing:

  Unknown: [specific gap]
  Impact: [which dimension(s) it affects: complexity / timeline / surface area]
  Movement: [what resolving it would change — e.g., "would move confidence from
             MED to HIGH", "could shift timeline from 3-5 to 2-3 sprints"]

List at least one unknown. If confidence is HIGH and no unknowns remain, write:
"No open unknowns — confidence is stable. The following would lower it: [X]."
A confidence statement with no engagement with unknowns in either direction is
incomplete.

STEP 8 — SCOPE NOTE
List what this sizing does NOT cover: out-of-scope sub-systems, deferred work,
assumptions that could invalidate the estimate if wrong.

AMEND: if an AMEND directive is present (adjust confidence thresholds, focus on
a specific complexity dimension), apply it — update the relevant step's content.
Do not only acknowledge the amendment; change the output.

Stock roles: Inertia Analyst (Step 1), Architect (Steps 2-3), PM (Steps 4-5),
Risk (Steps 6-7).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Ownership-Contract Table

**Axis:** Ownership contract format (C-11 target)
**Hypothesis:** Replacing the prose team-size section with a mandatory three-column
ownership contract table (Role | Owns | Dependency) makes ownership scope structurally
unskippable — a role entry without an Owns cell is visually incomplete, the same way a
table cell is more obviously missing than a prose sentence.

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

After the table, expand each section:

SURFACE AREA — enumerate every integration point by name (APIs, hooks, stores,
UI surfaces, external systems). If fewer than 2, explain why.

COMPLEXITY DRIVER — one sentence naming what pushed the complexity to that tier.
"HIGH because X", "LOW because Y". This must appear.

TEAM OWNERSHIP TABLE — this replaces a prose team description. For each
specialization in the Team Signal row, produce one entry in this table:

| Role | Owns (during implementation) | Dependency (what they receive/produce) |
|------|------------------------------|----------------------------------------|

  - "Owns" must name a specific artifact, layer, sub-system, or deliverable.
    "Owns: backend work" fails. "Owns: event schema + storage migration" passes.
  - "Dependency" names what this role hands off to others or receives from them.
  - At least one role must appear. Leave no Owns cell empty.

CONFIDENCE BASIS — state what is known vs unknown. Name at least one specific
unknown that, if resolved, would change the confidence rating. Format:
"Unknown: [X] — resolution would move confidence from [level] to [level]."
If confidence is HIGH, state what evidence grounds it and what would lower it.

INERTIA CHECK — this section is mandatory and appears after confidence. Name what
teams currently do without this feature (the workaround). State at least one cost
dimension (time lost, error rate, manual steps, capability gap). Then state a
break-even signal: at what adoption level or frequency does building this feature
pay off relative to continuing the workaround? If break-even cannot be assessed,
say why.

SCOPE — one bullet list of what this sizing does NOT cover (out-of-scope
sub-systems, deferred complexity, assumptions made).

AMEND support: if an AMEND directive is present, modify the affected table cell
and the corresponding expansion section. The table must reflect the amendment —
do not acknowledge it without changing the output.

Stock roles: Architect (sizing table + surface area + complexity driver),
PM (team ownership table + timeline row), Inertia Analyst (inertia check),
Risk (confidence basis + unknowns).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Synthesis-First with Hypothesis Revision

**Axis:** Synthesis structure (C-13) + lifecycle inversion (novel)
**Hypothesis:** Opening with a preliminary synthesis hypothesis — before any sections are
run — and closing by either confirming or explicitly revising that hypothesis forces
cross-dimensional reasoning. The model cannot produce juxtaposition in the closing because
it must actively compare its conclusion to its opening hypothesis, requiring it to reason
across dimensions rather than sequence them.

```
You are producing a sizing signal. Begin by stating a preliminary hypothesis.
Close by confirming or revising it. This structure prevents the output from
being a form filled in sequence — you are reasoning toward a conclusion, not
cataloguing dimensions.

--- OPENING HYPOTHESIS ---
Before running any sizing section, write one sentence stating your initial
assessment of this feature. Name at least two dimensions you expect to drive it:
e.g., "This appears MEDIUM complexity with a tight team signal, but inertia may
be low — the break-even case will be the swing factor." You will revisit this
at the end. The hypothesis may be wrong; that is expected. State it anyway.

--- INERTIA CHECK ---
What do teams do today without this feature? Name the workaround. State its cost:
time, errors, manual effort, or a capability they lack. Estimate break-even: at
what adoption level does building this pay off? If you cannot assess break-even,
name the blocking unknown. Do not skip — the workaround is the competition, and
every sizing number exists in relation to it.

--- SURFACE AREA ---
Enumerate integration points: APIs, hooks, namespaces, data stores, UI surfaces,
external systems. Name each one. Count the total. If the count is 0-1, explain.

--- COMPLEXITY ---
Assign a tier: LOW / MEDIUM / HIGH / XL. State the single driver that determined
the tier. "HIGH because X." "LOW because Y." Both the tier and the driver are
required.

--- TIMELINE ---
State a sprint range — lower bound and upper bound. A single number fails; it
implies false precision. Calendar dates fail. Derive the range from the surface
area count and complexity tier above.

--- TEAM SIGNAL ---
Name specializations, not headcount. "1 backend + 1 infra" not "2 engineers".
For each specialization, state what they own during the build — the specific
artifact, layer, or sub-system this role delivers.

--- CONFIDENCE ---
State a confidence level: LOW / MED / HIGH or a percentage. Give the primary
basis. Then name at least one specific unknown that, if resolved, would move
the rating. Format: "Unknown: [X] — would move confidence from [level] to
[level] once resolved." If confidence is HIGH, name what could lower it.

--- SCOPE ---
List what this sizing does NOT cover: out-of-scope sub-systems, deferred
complexity, assumptions that could change the estimate.

--- CLOSING SYNTHESIS ---
Return to the opening hypothesis. Either confirm it or revise it — in either
case, produce one synthesis paragraph that cross-references at least two
signal dimensions by name to support your conclusion. The synthesis must
answer: given what we now know about [dimension A] and [dimension B], what
is the decision-relevant implication?

A closing that merely restates the sections in order is not synthesis — it is
a summary. The synthesis must produce a conclusion that could not be read
directly from any single section.

AMEND: if an AMEND directive is present, reopen the affected section and
revise it, then re-evaluate whether the closing synthesis still holds or needs
updating. The amendment is complete only when both the section and the
synthesis reflect the change.

Stock roles: Hypothesis Lead (opening + closing), Inertia Analyst (inertia),
Architect (surface area + complexity), PM (timeline + team signal), Risk (confidence).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full Aspirational Stack (C-11 + C-12 + C-13 on V-05 R1 Base)

**Axis:** All three new aspirational criteria layered onto the highest-scoring R1 base
**Hypothesis:** V-05 R1 scored 98/100 by combining inertia-first + table-first + formal
register. That base satisfies C-01 through C-10 with structural redundancy. Adding explicit
C-11/C-12/C-13 enforcement — ownership contract, unknowns movement, synthesis template —
on top of that base produces maximum composite without dismantling what already works.

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
reason explicitly — this is unusual and requires justification.

Section 4 — TEAM OWNERSHIP
For each specialization named in the Team Signal table row, produce an entry:

  Role: [specialization]
  Owns: [specific artifact, layer, or sub-system delivered during implementation]
  Hands off: [what this role produces for the next role or integration point]

Rules:
  - "Owns: implementation" is not acceptable. Name the specific thing.
  - "Owns: event schema design and storage migration scripts" passes.
  - Do not list a role without an Owns line.
  - At least one role must have both Owns and Hands off populated.

Section 5 — CONFIDENCE AND OPEN UNKNOWNS
(a) State the confidence level again: LOW / MED / HIGH or a percentage.
(b) Give the primary basis — what knowledge supports this rating.
(c) For each open unknown, produce one entry:

    Unknown: [specific gap]
    Affects: [complexity / timeline / surface area / inertia — pick one or more]
    Movement: [resolving this would move confidence from X to Y]

    At minimum, one unknown must appear. If confidence is HIGH and no unknowns
    remain, write: "No remaining unknowns. The following would lower confidence:
    [X]." Stating confidence without any engagement with unknowns is incomplete.

Section 6 — SYNTHESIS
Write one synthesis paragraph. Requirements:
  - Cross-reference at least two sizing dimensions by name (e.g., complexity
    and confidence, surface area and timeline, inertia cost and team signal).
  - Produce a directional recommendation or decision-relevant conclusion.
  - Use this anchor structure: "[Dimension A] combined with [Dimension B]
    [argues for / supports / cautions against] [recommendation]."
  - Do not restate each section in sequence — that is juxtaposition, not
    synthesis. The conclusion must be derivable only by reasoning across
    dimensions, not from reading any single section in isolation.

Section 7 — SCOPE EXCLUSIONS
State what this sizing does NOT cover. Include: out-of-scope sub-systems,
complexity deferred to later milestones, and assumptions whose violation would
materially change the estimate. At least one exclusion is required.

AMEND HANDLING
If an AMEND directive is present (adjust confidence thresholds; focus analysis
on a specific complexity dimension), apply the amendment by:
  1. Revising the relevant table cell and its corresponding section.
  2. Re-evaluating whether the synthesis still holds; update Section 6 if
     the amended dimension changes the cross-signal conclusion.
The amended artifact must differ in content from the pre-amendment version.
Acknowledgment without content change does not satisfy the AMEND contract.

Stock roles: Inertia Analyst (Section 1), Architect (Sections 2-3),
PM (table: Timeline + Team Signal rows, Section 4), Risk (Section 5),
Synthesis Lead (Section 6).

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| Variation | Primary Axis | New Criteria Targeted | Base | Structural Bet |
|-----------|-------------|----------------------|------|----------------|
| V-01 | Synthesis-forcing template | C-13 | V-05 R1 | Fill-in sentence template makes juxtaposition structurally incomplete |
| V-02 | Unknowns as own section | C-12 | V-02 R1 | Separating unknowns from confidence forces first-class treatment |
| V-03 | Ownership contract table | C-11 | V-01 R1 | Three-column table makes missing Owns cell visually detectable |
| V-04 | Synthesis-first + hypothesis revision | C-13 + lifecycle | novel | Opening hypothesis forces closing to reason across dimensions, not sequence |
| V-05 | Full aspirational stack | C-11 + C-12 + C-13 | V-05 R1 | Best base + explicit new criteria = maximum composite coverage |

**Expected leaderboard hypothesis:** V-05 > V-01 > V-04 > V-02 > V-03 on composite.
V-05 inherits V-05 R1's structural redundancy plus all three new criteria. V-01 adds
synthesis forcing to the same base but leaves C-11/C-12 unchanged from R1 levels. V-04
is the most novel — the hypothesis-revision pattern is the strongest theoretical forcing
for C-13 but introduces the most execution risk (model may collapse both hypothesis and
synthesis into a single pass, defeating the mechanism). V-02 and V-03 are single-axis
and likely strong on their target criterion but weaker on the other two new criteria.

**Predicted failure modes:**
- V-01: C-12 still embedded in confidence section — unknowns movement may not surface
- V-02: C-13 absent — no cross-signal requirement; no synthesis section
- V-03: C-12 and C-13 absent — scope limited to C-11 improvement only
- V-04: C-11 execution risk — ownership may be omitted in the conversational flow
- V-05: Verbosity risk — four new requirements on top of existing structure may produce
  mechanical compliance rather than substantive reasoning depth in synthesis
