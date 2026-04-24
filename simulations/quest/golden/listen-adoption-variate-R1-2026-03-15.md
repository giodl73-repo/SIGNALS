# Variations: listen-adoption — Round 1

**Rubric:** v1 | **Criteria:** C-01 through C-10 | **Max composite:** 100 | **Golden threshold (80%):** all 5 essential pass + composite >= 80

---

## Variation Axes

| Axis | R1 Target | Description |
|------|-----------|-------------|
| Output format | Table-primary | Replace prose-heavy output with mandatory tables for mapping, simulation, and interventions |
| Lifecycle emphasis | Explicit month headers | Each simulation month gets a named fill-contract block; phase boundaries are structural, not implied |
| Inertia framing | Incumbent named + tracked | Status-quo workflow/tool named at top, re-cited in chasm and interventions |

**Single-axis (V-01, V-02, V-03):** Output format · Lifecycle emphasis · Inertia framing
**Combined (V-04):** Lifecycle emphasis + Output format
**Full (V-05):** Lifecycle emphasis + Output format + Inertia framing

---

## V-01 — Single Axis: Output Format (Table-Primary)

**Variation axis:** Output format — All structural outputs (archetype mapping, simulation timeline,
chasm summary, intervention list, churn register) are delivered as labeled tables with required
columns. Prose is confined to analysis sections where tables cannot capture causal reasoning.

**Hypothesis:** Prose-first prompts produce well-written narratives that omit roles silently
(failing C-08) and state interventions without a consistent delta column (failing C-04 ordering).
Mandatory table structure forces complete 16-role coverage into C-01 and C-08 by making each
row a named slot, and forces adoption delta into a required column so C-04 ranking is
mechanical rather than discretionary.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles.

Deliver the sections below in the order shown. Every table has required columns — complete all
columns for every row before proceeding.

---

### SECTION 1 — Archetype Mapping

Produce a table with all 16 stock roles. No role may be omitted.

| Role | Rogers Archetype | Primary adoption driver |
|------|-----------------|------------------------|
| PM | | |
| UX | | |
| C-01 | | |
| C-02 | | |
| C-03 | | |
| C-04 | | |
| C-05 | | |
| C-06 | | |
| C-07 | | |
| C-08 | | |
| C-09 | | |
| C-10 | | |
| C-11 | | |
| C-12 | | |
| Support | | |
| SRE | | |

Rogers archetypes (use exactly): Innovator / Early Adopter / Early Majority / Late Majority / Laggard

---

### SECTION 2 — Month-by-Month Simulation

Produce a timeline table for at least 6 months. For each month, list the roles that newly adopt,
the archetype cohort they belong to, the adoption mechanism, and the running cumulative count.

| Month | Newly adopting roles | Archetype cohort | Adoption mechanism | Cumulative adopters (of 16) |
|-------|---------------------|-----------------|-------------------|----------------------------|
| M1 | | | | |
| M2 | | | | |
| M3 | | | | |
| M4 | | | | |
| M5 | | | | |
| M6 | | | | |

After the table: write 1-2 sentences explaining any month where adoption stalled (zero new roles).

Cumulative count in the final row must be consistent with 16-role total. Every role named in
SECTION 1 must appear in at least one row of this table.

---

### SECTION 3 — Chasm Analysis

The chasm is the gap between early-adopter exit and early-majority entry. Fill each field.

**Gap location:** Between [early-adopter roles] and [early-majority roles] — state specific roles.

**Cause:** Why does the gap exist for {{topic}} specifically? Name the mechanism (trust gap,
workflow friction, missing social proof, tool complexity, etc.).

**Risk if not bridged:** What stalls, regresses, or never completes if the chasm is not crossed?
Name which roles plateau and what feature value goes uncaptured.

---

### SECTION 4 — Champion Network

Produce a table of roles that bridge the chasm. At least 2 champions required.

| Champion role | Bridges from | Bridges to | Bridging mechanism |
|--------------|-------------|------------|-------------------|
| | | | |
| | | | |

**Influence pathway:** For each champion, describe in one sentence how their advocacy converts
a late-cohort role from aware to trying. Distinguish active sponsorship from passive diffusion.

---

### SECTION 5 — Intervention Recommendations

Produce a table sorted by adoption delta, highest first. At least 3 interventions required.

| Rank | Intervention | Targets | Adoption delta | Earliest effective month |
|------|-------------|---------|---------------|------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

Adoption delta must be a concrete statement: "+N roles by month M" or "+X% coverage by [date]".
Earliest effective month pins each intervention to the simulation timeline (satisfies C-10).

---

### SECTION 6 — Churn Risk Register

Produce a table of roles at risk of disengaging before full adoption. At least 2 entries required.

| Role | Archetype | Churn trigger | Why this role is at risk |
|------|-----------|--------------|--------------------------|
| | | | |
| | | | |

---

### SECTION 7 — S-Curve Summary

Summarize the adoption trajectory in numeric terms consistent with the 16-role cast.

| Phase | Month range | Adopters at start | Adopters at end | % of cast |
|-------|------------|-------------------|-----------------|-----------|
| Innovator ignition | | | | |
| Early-adopter spread | | | | |
| Chasm | | | | |
| Early-majority uptake | | | | |
| Late-majority close | | | | |

---

## V-02 — Single Axis: Lifecycle Emphasis (Explicit Month Headers)

**Variation axis:** Lifecycle emphasis — Each simulation month is a named structural block with
required fill-contract fields. Phase boundaries (innovator ignition, early-adopter spread, chasm,
early-majority uptake, late-majority close) are explicit section headers, not implied by prose
flow. Each month block must complete all fields before the next month begins.

**Hypothesis:** When months are implicit in a timeline table, the model telescopes adjacent months,
collapses mechanisms, and leaves early-majority arrival underdescribed. Explicit month blocks
force each time step to independently answer "who, why, how many" — satisfying C-02 fully and
making C-10 (interventions pinned to months) structural. The lifecycle boundary headers also
make the chasm (Phase 3) a mandatory named stop, ensuring C-03 is not absorbed into narrative.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles (PM, UX, C-01 through
C-12, Support, SRE).

Produce the output in five phases, each subdivided by month. Every field in every block is a
fill contract — complete it before proceeding to the next block.

---

### PHASE 0 — Archetype Map

Assign each stock role to exactly one Rogers archetype. No role omitted.

```
PM:       [Innovator / Early Adopter / Early Majority / Late Majority / Laggard]
UX:       [...]
C-01:     [...]
C-02:     [...]
C-03:     [...]
C-04:     [...]
C-05:     [...]
C-06:     [...]
C-07:     [...]
C-08:     [...]
C-09:     [...]
C-10:     [...]
C-11:     [...]
C-12:     [...]
Support:  [...]
SRE:      [...]
```

---

### PHASE 1 — Innovator Ignition

**Entry state:** No roles have adopted {{topic}}. THE INCUMBENT workflow is fully in place.

#### Month 1

```
Roles newly adopting:      [list]
Archetype cohort:          Innovator
Mechanism:                 [what triggers first contact — curiosity, internal demo, side project]
Cumulative adopters:       [N] of 16
Signal visible to others?: [yes/no — why]
```

#### Month 2 (if applicable — skip if innovators complete in M1)

```
Roles newly adopting:      [list or "none — innovator phase complete"]
Cumulative adopters:       [N] of 16
Phase-close note:          [what the innovator cohort leaves behind — artifacts, reputation, demo]
```

**PHASE 1 CLOSE**
```
Innovator-cohort exit state:   [which roles have adopted, total count]
Signal to early adopters:      [what evidence exists that {{topic}} works]
```

---

### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE exit state verbatim.

#### Month 3

```
Roles newly adopting:      [list]
Archetype cohort:          Early Adopter
Mechanism:                 [demo culture, pairing, visible wins, peer referral]
Cumulative adopters:       [N] of 16
Champion emerging?:        [name role if yes; mechanism of emerging influence]
```

#### Month 4

```
Roles newly adopting:      [list]
Mechanism:                 [...]
Cumulative adopters:       [N] of 16
Champion network forming?: [describe or "not yet"]
```

**PHASE 2 CLOSE**
```
Early-adopter exit state:      [roles adopted, total count]
Champion network status:       [roles, bridging mechanisms]
Gap to early majority:         [what is missing for early-majority entry]
```

---

### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE exit state verbatim.

#### CHASM-A — Gap Definition

```
Gap:    The space between [early-adopter roles] and [early-majority roles].
Cause:  [Why does early majority not follow automatically for {{topic}}?
         Name the specific friction: trust deficit, workflow disruption, unclear ROI, etc.]
```

#### CHASM-B — Risk Assessment

```
At risk if not bridged:  [which roles plateau; what feature value goes uncaptured]
Stall duration estimate: [months or indefinite — with reasoning]
```

#### CHASM-C — Bridge Conditions

```
What early majority needs to cross:  [evidence type, champion endorsement, tool polish, mandate]
Which champion roles can provide it: [name roles; mechanism]
```

**PHASE 3 CLOSE**
```
Chasm bridging condition:  [what must be true for PHASE 4 to begin]
```

---

### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE exit state verbatim.

#### Month 5

```
Roles newly adopting:      [list]
Archetype cohort:          Early Majority
Mechanism:                 [what bridged them — champion demo, team mandate, visible peer success]
Cumulative adopters:       [N] of 16
Churn risk activating?:    [name role and trigger if yes]
```

#### Month 6

```
Roles newly adopting:      [list]
Mechanism:                 [...]
Cumulative adopters:       [N] of 16
```

**PHASE 4 CLOSE**
```
Early-majority exit state: [roles adopted, total count, % of 16-role cast]
```

---

### PHASE 5 — Late-Majority Close and Laggard Handling

**Entry state:** Re-cite PHASE 4 CLOSE exit state verbatim.

#### Month 7–9 (compress if uniform)

```
Roles newly adopting:      [list]
Archetype cohort:          Late Majority / Laggard
Mechanism:                 [social pressure, mandate, removal of alternative]
Cumulative adopters:       [N] of 16
Remaining holdouts:        [roles; churn risk or permanent non-adoption?]
```

**PHASE 5 CLOSE**
```
Final adoption count:      [N] of 16 ([%])
Non-adopters (if any):     [roles; reason adoption fails to complete]
```

---

### PART A — Churn Risk Register

For each role at risk of disengaging before full adoption: name the role, the trigger, and the
reason. Minimum 2 entries.

```
[Role] — Trigger: [...] — Why at risk: [...]
[Role] — Trigger: [...] — Why at risk: [...]
```

---

### PART B — Champion Network

For each champion role: name who they bridge from and to, and the exact mechanism.

```
[Role] — From: [archetype] → To: [archetype] — Mechanism: [...]
[Role] — From: [archetype] → To: [archetype] — Mechanism: [...]
```

---

### PART C — Interventions Ranked by Adoption Delta

List at least 3 interventions. Sort highest delta first. Pin each to a simulation month.

```
[Rank 1] [Intervention] — Delta: [+N roles by month M] — Deploy before: [month]
[Rank 2] [Intervention] — Delta: [...] — Deploy before: [month]
[Rank 3] [Intervention] — Delta: [...] — Deploy before: [month]
```

---

## V-03 — Single Axis: Inertia Framing (Incumbent Named and Tracked)

**Variation axis:** Inertia framing — The status-quo workflow that {{topic}} displaces is named
at the top of the document as THE INCUMBENT and referenced at each stage of the simulation.
Chasm analysis must name what THE INCUMBENT offers that {{topic}} does not yet match. Each
intervention must state what habit or workflow it displaces in addition to its adoption delta.

**Hypothesis:** When the incumbent is unnamed, chasm analysis defaults to generic friction
("change resistance," "learning curve") without identifying the specific workflow defending
itself. Naming THE INCUMBENT forces three precise outputs: (1) the chasm cause names the
incumbent's structural advantage, (2) each archetype cohort's delay is explained in terms of
what they lose by switching, (3) interventions target displacement of a specific behavior rather
than promotion of a vague benefit. This raises the specificity of C-03, C-04, and C-09 from
generic to causal.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles (PM, UX, C-01 through
C-12, Support, SRE).

---

### PREAMBLE — Name the Incumbent

Before any simulation, complete this block.

```
THE INCUMBENT:        [The workflow, tool, or habit that {{topic}} replaces or competes with.
                       Be specific: name the exact practice, not just "current process."]

What THE INCUMBENT does well:
  - [Advantage 1 for each archetype that resists early]
  - [Advantage 2]

What {{topic}} must prove to displace it:
  - [Proof point required by early majority]
  - [Proof point required by late majority]
```

This named incumbent must be referenced in SECTION 3 (chasm cause), SECTION 5 (each
intervention's displacement target), and the final churn analysis.

---

### SECTION 1 — Archetype Mapping

Assign each stock role to exactly one Rogers archetype. For each role, add a one-line note on
their relationship to THE INCUMBENT (heavy user / moderate dependency / indifferent / actively
seeking alternative).

| Role | Rogers Archetype | Incumbent dependency |
|------|-----------------|---------------------|
| PM | | |
| UX | | |
| C-01 | | |
| C-02 | | |
| C-03 | | |
| C-04 | | |
| C-05 | | |
| C-06 | | |
| C-07 | | |
| C-08 | | |
| C-09 | | |
| C-10 | | |
| C-11 | | |
| C-12 | | |
| Support | | |
| SRE | | |

---

### SECTION 2 — Month-by-Month Simulation

For each month, name the roles that newly adopt. For each month explain what caused those
roles to detach from THE INCUMBENT and try {{topic}} instead.

Minimum 6 months. Every role from SECTION 1 must appear in at least one month row.

```
Month 1
  Newly adopting:       [roles]
  Archetype cohort:     Innovator
  Detachment from incumbent: [what made these roles willing to try {{topic}} despite THE INCUMBENT?]
  Cumulative:           [N of 16]

Month 2
  Newly adopting:       [roles]
  Archetype cohort:     Early Adopter
  Detachment from incumbent: [...]
  Cumulative:           [N of 16]

Month 3
  Newly adopting:       [roles or "none — chasm"]
  Stall reason:         [what THE INCUMBENT is still offering that {{topic}} hasn't matched]
  Cumulative:           [N of 16]

Month 4
  ...

Month 5
  ...

Month 6
  ...
```

---

### SECTION 3 — Chasm Analysis

```
CHASM-A — Gap:
  Between:       [early-adopter roles that have adopted] and [early-majority roles that haven't]
  Named cause:   [What specific advantage of THE INCUMBENT prevents early-majority crossing?
                  Do not use generic friction — name the workflow, habit, or institutional
                  reason THE INCUMBENT still wins for this cohort.]

CHASM-B — Risk:
  If not bridged: [which roles plateau; what value of {{topic}} goes uncaptured]
  THE INCUMBENT's win condition: [what happens if the chasm persists — incumbent entrenches,
                  {{topic}} gets scoped to power users only, etc.]

CHASM-C — Bridge Condition:
  What early majority needs: [specific evidence that {{topic}} beats THE INCUMBENT
                  on the dimension that matters to this cohort]
  Who can provide it:        [champion roles; mechanism]
```

---

### SECTION 4 — Champion Network

For each champion: who they bridge, how their advocacy addresses THE INCUMBENT's appeal for
late-cohort roles. Minimum 2 champions.

```
Champion: [role]
  Bridges:    [archetype from] → [archetype to]
  Mechanism:  [how this champion's endorsement answers THE INCUMBENT's appeal
               for the target cohort — peer credibility, shared context, tool demo, etc.]
  Influence type: [active sponsorship / passive diffusion — explain]

Champion: [role]
  ...
```

---

### SECTION 5 — Intervention Recommendations

At least 3 interventions, sorted by adoption delta (highest first). Each intervention must
name what habit of THE INCUMBENT it displaces and when it fires.

```
[Rank 1]
  Intervention:         [...]
  Displaces from incumbent: [specific workflow or habit]
  Adoption delta:       [+N roles by month M]
  Deploy before:        Month [M]

[Rank 2]
  ...

[Rank 3]
  ...
```

---

### SECTION 6 — Churn Risk Register

For each churn risk: name the role, the trigger, and what THE INCUMBENT is still offering
that pulls the role back. Minimum 2 entries.

```
[Role] — Trigger: [...] — Incumbent pull: [what THE INCUMBENT still does better for this role]
[Role] — Trigger: [...] — Incumbent pull: [...]
```

---

### SECTION 7 — S-Curve

Numeric adoption counts by phase, consistent with 16-role cast.

```
Phase               | Month range | Adopters at close | % of 16
Innovator ignition  | M1–M2       | [N]               | [%]
Early-adopter spread| M2–M4       | [N]               | [%]
Chasm               | M3–M4       | [N — no change]   | [%]
Early-majority      | M5–M7       | [N]               | [%]
Late-majority close | M7–M9       | [N]               | [%]
```

---

## V-04 — Combined: Lifecycle Emphasis + Output Format

**Variation axes:** Lifecycle emphasis (V-02) + Output format (V-01)

**Hypothesis:** Explicit month blocks (V-02) resolve the temporal coverage gap in C-02 and C-10,
but the fill-contract prose format still allows role omissions to hide in paragraph flow. Adding
mandatory table columns to every month block (V-01) closes the coverage gap: each month table
forces every newly-adopting role to be named in a row, making omission visible as an empty cell
rather than a missing sentence. The two axes are complementary — lifecycle emphasis enforces
temporal completeness, table format enforces role completeness.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles (PM, UX, C-01 through
C-12, Support, SRE). Produce every section below in full. Tables have required columns —
complete all cells. Month blocks have required fields — complete all fields.

---

### SECTION 1 — Archetype Mapping Table

| Role | Rogers Archetype | Primary adoption driver | Earliest likely adoption month |
|------|-----------------|------------------------|-------------------------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

---

### SECTION 2 — Month-by-Month Simulation

For each month, complete the block and the per-adopter table. Minimum 6 months.

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 roles have adopted {{topic}}.

**Month 1**

```
Phase:           PHASE 1 — Innovator Ignition
Cohort:          Innovator
Mechanism:       [what drives first contact]
Cumulative:      [N] of 16
```

| Newly adopting role | Archetype | Specific trigger |
|--------------------|-----------|-----------------|
| | Innovator | |

**Month 2** (complete if innovators continue; skip if phase closes in M1)

| Newly adopting role | Archetype | Specific trigger |
|--------------------|-----------|-----------------|
| | Innovator | |

```
PHASE 1 CLOSE — Innovator exit state: [roles adopted, count, what signal they leave for EA cohort]
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

| Newly adopting role | Archetype | Specific trigger |
|--------------------|-----------|-----------------|
| | Early Adopter | |

```
Cumulative:         [N] of 16
Champion forming?:  [role if emerging; mechanism]
```

**Month 4**

| Newly adopting role | Archetype | Specific trigger |
|--------------------|-----------|-----------------|
| | Early Adopter | |

```
Cumulative:            [N] of 16
```

```
PHASE 2 CLOSE — EA exit state: [roles, count, gap to early majority]
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles] |
| Cause | [Specific friction mechanism for {{topic}}] |
| Risk if not bridged | [Roles that plateau; value uncaptured] |
| Bridge condition | [What EM needs to cross] |
| Champion that can bridge | [Role + mechanism] |

```
PHASE 3 CLOSE — Bridge condition: [what must be true for PHASE 4 entry]
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

| Newly adopting role | Archetype | Specific trigger |
|--------------------|-----------|-----------------|
| | Early Majority | |

```
Cumulative:          [N] of 16
Churn risk active?:  [role + trigger if yes]
```

**Month 6**

| Newly adopting role | Archetype | Specific trigger |
|--------------------|-----------|-----------------|
| | Early Majority | |

```
Cumulative:          [N] of 16
```

```
PHASE 4 CLOSE — EM exit state: [roles, count, % of 16]
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

| Newly adopting role | Archetype | Specific trigger |
|--------------------|-----------|-----------------|
| | Late Majority / Laggard | |

```
Cumulative:            [N] of 16
Non-adopters (if any): [roles + reason]
```

```
PHASE 5 CLOSE — Final state: [N] of 16 adopted ([%])
```

---

### SECTION 3 — Champion Network Table

| Champion role | Bridges from | Bridges to | Bridging mechanism | Influence type |
|--------------|-------------|------------|-------------------|----------------|
| | | | | Active sponsorship / Passive diffusion |
| | | | | |

---

### SECTION 4 — Intervention Table

Sorted by adoption delta, highest first. Minimum 3 rows.

| Rank | Intervention | Target roles | Adoption delta | Deploy before month |
|------|-------------|-------------|---------------|-------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

### SECTION 5 — Churn Risk Table

Minimum 2 rows.

| Role | Archetype | Churn trigger | Reason at risk | Intervention that mitigates |
|------|-----------|--------------|---------------|---------------------------|
| | | | | |
| | | | | |

---

### SECTION 6 — S-Curve Summary Table

| Phase | Month range | Adopters at close | % of 16-role cast |
|-------|------------|-------------------|-------------------|
| Innovator ignition | | | |
| Early-adopter spread | | | |
| Chasm (stall) | | | |
| Early-majority uptake | | | |
| Late-majority close | | | |

Verify: final count = 16 (or document any permanent non-adopters).

---

## V-05 — Full: Lifecycle Emphasis + Output Format + Inertia Framing

**Variation axes:** Lifecycle emphasis (V-02) + Output format (V-01) + Inertia framing (V-03)

**Hypothesis:** V-04 achieves temporal and role completeness through phase headers and mandatory
table columns. Adding inertia framing (V-03) completes the causal layer: each month table gains
an "Incumbent pull" column that names what THE INCUMBENT still offers the hesitating role, each
phase-close explicitly states whether THE INCUMBENT lost ground, and interventions carry a
"Displaces from incumbent" field. The three axes are mutually reinforcing — lifecycle emphasis
provides the temporal spine, table format provides the role-coverage skeleton, and inertia
framing provides the causal tissue that explains delay at each structural slot.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles (PM, UX, C-01 through
C-12, Support, SRE).

---

### PREAMBLE — Incumbent Declaration

Complete before any simulation output.

```
THE INCUMBENT:              [Specific workflow, tool, or habit {{topic}} displaces. Name it.]
What THE INCUMBENT does well for this team:
  - [...]
  - [...]
What {{topic}} must prove to displace it:
  - For early majority: [...]
  - For late majority: [...]
```

THE INCUMBENT must be cited in: PHASE 3 chasm cause, each intervention's displacement target,
and each churn risk's incumbent pull.

---

### SECTION 1 — Archetype Mapping Table

| Role | Rogers Archetype | Incumbent dependency | Earliest adoption month |
|------|-----------------|---------------------|------------------------|
| PM | | heavy / moderate / indifferent / seeking alt | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

---

### SECTION 2 — Month-by-Month Simulation

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

| Newly adopting role | Archetype | Adoption trigger | Incumbent pull (why others don't yet) |
|--------------------|-----------|-----------------|--------------------------------------|
| | Innovator | | |

```
Cumulative: [N] of 16
```

**Month 2** (if applicable)

| Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|--------------------|-----------|-----------------|---------------|
| | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Incumbent position: [has THE INCUMBENT lost ground? describe]
Signal to EA cohort: [what evidence exists that {{topic}} works]
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

| Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|--------------------|-----------|-----------------|---------------|
| | Early Adopter | | |

```
Cumulative: [N] of 16
Champion forming?: [role; mechanism]
```

**Month 4**

| Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|--------------------|-----------|-----------------|---------------|
| | Early Adopter | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Incumbent position: [still dominant with which cohorts? why?]
Champion network: [roles + bridging mechanisms]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values]
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles] |
| Cause | [What specific advantage of THE INCUMBENT prevents EM crossing? Name the habit/workflow.] |
| THE INCUMBENT's win condition | [What THE INCUMBENT delivers that {{topic}} doesn't yet match for EM] |
| Risk if not bridged | [Roles that plateau; incumbent entrenches] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion that provides it | [Role + mechanism + what incumbent argument they counter] |

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 entry]
Incumbent position at chasm: [still dominant / weakening / differentiated]
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

| Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|--------------------|-----------|-----------------|---------------|
| | Early Majority | | |

```
Cumulative: [N] of 16
Churn risk?: [role + trigger; what incumbent behavior reasserts]
```

**Month 6**

| Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|--------------------|-----------|-----------------|---------------|
| | Early Majority | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Incumbent position: [retreating / residual / eliminated in this cohort]
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

| Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|--------------------|-----------|-----------------|---------------|
| | Late Majority / Laggard | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Non-adopters (if any): [roles; reason incumbent still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

---

### SECTION 3 — Champion Network Table

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered |
|--------------|-------------|------------|-------------------|-----------------------------|
| | | | | |
| | | | | |

---

### SECTION 4 — Intervention Table

Sorted by adoption delta, highest first. Minimum 3 rows.

| Rank | Intervention | Target roles | Displaces from incumbent | Adoption delta | Deploy before month |
|------|-------------|-------------|--------------------------|---------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

---

### SECTION 5 — Churn Risk Table

Minimum 2 rows.

| Role | Archetype | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|--------------|---------------|----------------------|
| | | | [what THE INCUMBENT still offers this role] | |
| | | | | |

---

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Explain any non-adopting roles and whether THE INCUMBENT permanently
retains them.
