# Variations: listen-adoption — Round 2

**Rubric:** v2 | **Criteria:** C-01 through C-13 | **Max composite:** 100 | **Golden threshold:** all 5 essential pass + composite >= 80

---

## Variation Axes

| Axis | R2 Target | Description |
|------|-----------|-------------|
| Champion displacement annotation | C-12 | Each champion entry carries an explicit "counters / displaces / answers" column naming the specific incumbent argument that champion is positioned to overcome. Converts champion table from passive roster to active displacement plan. |
| Three-axis gap audit block | C-13 | After simulation phases, a required THREE-AXIS GAP AUDIT block certifies closure of all three independent dimensions: (a) role completeness, (b) temporal completeness, (c) causal specificity. Each axis is audited independently so multi-axis gaps cannot hide in each other. |
| Preamble propagation with citation markers | C-11 (stronger) | Named incumbent in preamble block plus explicit [CITE: THE INCUMBENT] markers in each downstream section (chasm, interventions, champions, churn). Each marker must be filled with the incumbent name. Stronger than R1 V-03's soft "must reference" instruction — omission is visible as an unfilled marker. |

**Single-axis (V-01, V-02, V-03):** Champion displacement annotation · Three-axis gap audit block · Preamble propagation with citation markers
**Combined (V-04):** Champion displacement annotation + Preamble propagation with citation markers
**Full (V-05):** Champion displacement annotation + Three-axis gap audit block + Preamble propagation with citation markers

---

## V-01 — Single Axis: Champion Displacement Annotation

**Variation axis:** Champion displacement annotation — The champion network table carries a required
"Incumbent argument countered" column. Each champion entry must name the specific objection, habit,
or workflow advantage that champion is positioned to overcome — not generic resistance language, but
a named incumbent behavior (e.g., "manual review habit in standups", "distrust of AI-generated
summaries without explicit author sign-off", "existing Jira triage flow that predates {{topic}}").

**Hypothesis:** Without a required column, champion tables describe bridging mechanisms (who bridges
whom, by what channel) but skip the displacement question: what specific argument does this champion
answer? C-12 fails not because champions are absent but because the "what argument does this champion
counter?" field is discretionary. Making it a required column converts every champion entry from
structural description ("PM bridges Innovator to Early Adopter via demo culture") to active
displacement claim ("PM bridges Innovator to Early Adopter via demo culture / counters: fear that
{{topic}} adds review overhead without reducing defect rate"). This forces C-09 to PASS as a
byproduct — every influence pathway carries a specific argument it displaces.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles
(PM, UX, C-01 through C-12, Support, SRE).

Produce all sections below in full. Complete every column in every table row before continuing.

---

### SECTION 1 — Archetype Mapping

Assign each role to exactly one Rogers archetype. No role may be omitted.

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

Minimum 6 months. Every role from SECTION 1 must appear in at least one row.
Cumulative count in the final row must equal 16 (or note permanent non-adopters with reason).

| Month | Newly adopting roles | Archetype cohort | Adoption mechanism | Cumulative (of 16) |
|-------|---------------------|-----------------|-------------------|--------------------|
| M1 | | Innovator | | |
| M2 | | | | |
| M3 | | | | |
| M4 | | | | |
| M5 | | | | |
| M6 | | | | |

For any month with zero newly adopting roles: write one sentence naming the stall cause.

---

### SECTION 3 — Chasm Analysis

**Gap location:** Between [early-adopter roles] and [early-majority roles] — name specific roles.

**Cause:** Why does the gap exist for {{topic}} specifically? Name the mechanism — not
"change resistance" but the concrete friction: trust deficit, workflow disruption, unclear ROI,
missing social proof, tool complexity, institutional process lock-in.

**Risk if not bridged:** Which roles plateau? What feature value goes uncaptured? What is the
competitive consequence if the chasm persists for 3+ months?

---

### SECTION 4 — Champion Network

The "Incumbent argument countered" column is required and must be filled for every champion.
Name the specific argument, objection, or habit that this champion is positioned to overcome.
Generic entries ("reduces resistance", "builds trust") fail this column — name the thing.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered |
|--------------|-------------|------------|-------------------|------------------------------|
| | | | | |
| | | | | |

Minimum 2 champions. For each champion, add one sentence below the table describing
whether their advocacy is active sponsorship or passive diffusion, and why.

---

### SECTION 5 — Intervention Recommendations

Sorted by adoption delta, highest first. Minimum 3 interventions.

| Rank | Intervention | Target roles | Adoption delta | Earliest effective month |
|------|-------------|-------------|---------------|------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

Adoption delta: "+N roles by month M" or "+X% coverage by [date]". No vague qualifiers.

---

### SECTION 6 — Churn Risk Register

Minimum 2 entries.

| Role | Archetype | Churn trigger | Why at risk |
|------|-----------|--------------|------------|
| | | | |
| | | | |

---

### SECTION 7 — S-Curve Summary

| Phase | Month range | Adopters at close | % of 16 |
|-------|------------|-------------------|---------|
| Innovator ignition | | | |
| Early-adopter spread | | | |
| Chasm (stall) | | | |
| Early-majority uptake | | | |
| Late-majority close | | | |

Final count must reconcile with 16. Explain any non-adopting roles.

---

## V-02 — Single Axis: Three-Axis Gap Audit Block

**Variation axis:** Three-axis gap audit block — After the simulation phases and before the
champion/intervention/churn sections, the prompt requires a THREE-AXIS GAP AUDIT block. The
audit checks three independent dimensions: (a) role completeness — all 16 roles individually
named and traceable to a specific adoption month; (b) temporal completeness — every adoption
event, gap, and intervention pinned to a specific month or month range; (c) causal specificity
— every gap, risk, and stall explained with a named cause rather than generic change-resistance
language. The audit is a fill contract: incomplete rows are visible gaps, not missing sentences.

**Hypothesis:** Outputs routinely close two of three axes but not all three simultaneously.
Role completeness often fails silently when narrative flow absorbs roles into cohorts without
naming each individually. Temporal completeness fails when interventions are stated without
a deploy-by month. Causal specificity fails when chasm cause reads "teams are slow to change"
rather than naming the specific workflow being defended. The THREE-AXIS GAP AUDIT block makes
all three independent — satisfying two cannot substitute for the third. This directly forces
C-13 PASS while pulling C-07 (quantified curve), C-08 (full role traceability), and C-10
(interventions pinned to simulation) toward PASS as structural preconditions of the audit.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles
(PM, UX, C-01 through C-12, Support, SRE).

Produce all sections below in order. Complete every field before proceeding to the next section.

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

**Entry state:** 0 of 16 roles have adopted {{topic}}.

#### Month 1

```
Roles newly adopting:    [list]
Archetype cohort:        Innovator
Mechanism:               [what triggers first contact]
Cumulative adopters:     [N] of 16
```

#### Month 2 (skip if innovators complete in M1)

```
Roles newly adopting:    [list or "none — innovator phase complete"]
Cumulative adopters:     [N] of 16
```

```
PHASE 1 CLOSE
Adopters: [roles, count]
Signal to early adopters: [what evidence exists that {{topic}} works]
```

---

### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

#### Month 3

```
Roles newly adopting:    [list]
Archetype cohort:        Early Adopter
Mechanism:               [demo culture, pairing, visible wins, peer referral]
Cumulative adopters:     [N] of 16
Champion emerging?:      [role if yes; mechanism]
```

#### Month 4

```
Roles newly adopting:    [list]
Mechanism:               [...]
Cumulative adopters:     [N] of 16
```

```
PHASE 2 CLOSE
Adopters: [roles, count]
Gap to early majority: [what is missing for EM entry]
Champion network: [roles, bridging mechanisms]
```

---

### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

```
CHASM-A — Gap:
  Between:    [early-adopter roles] and [early-majority roles]
  Cause:      [Specific friction for {{topic}} — name the mechanism, not generic resistance]

CHASM-B — Risk:
  At risk:    [roles that plateau; feature value uncaptured]
  Stall:      [estimated duration or "indefinite" — with reason]

CHASM-C — Bridge:
  EM needs:   [specific evidence type to cross]
  Provider:   [champion role + mechanism]
```

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 to begin]
```

---

### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

#### Month 5

```
Roles newly adopting:    [list]
Archetype cohort:        Early Majority
Mechanism:               [what bridged them]
Cumulative adopters:     [N] of 16
Churn risk activating?:  [role + trigger if yes]
```

#### Month 6

```
Roles newly adopting:    [list]
Mechanism:               [...]
Cumulative adopters:     [N] of 16
```

```
PHASE 4 CLOSE
Adopters: [roles, count, % of 16]
```

---

### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

#### Month 7–9

```
Roles newly adopting:    [list]
Archetype cohort:        Late Majority / Laggard
Mechanism:               [social pressure, mandate, removal of alternative]
Cumulative adopters:     [N] of 16
Remaining holdouts:      [roles; permanent non-adoption?]
```

```
PHASE 5 CLOSE
Final adoption count: [N] of 16 ([%])
Non-adopters (if any): [roles; reason]
```

---

### THREE-AXIS GAP AUDIT

Complete this block before proceeding to PART A. Every row is a fill contract — an empty
or generic cell is an audit failure, not a missing sentence.

#### Axis A — Role Completeness

All 16 roles must appear in the table below, each traced to its adoption month. Roles not yet
adopted by PHASE 5 CLOSE are listed as non-adopters with reason.

| Role | Adoption month | Archetype cohort |
|------|---------------|-----------------|
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

#### Axis B — Temporal Completeness

List every distinct event (adoption wave, stall, chasm, bridge, intervention) pinned to its
month. No event may appear without a month reference.

| Event | Month | Type |
|-------|-------|------|
| | | Adoption wave / Stall / Chasm / Bridge / Intervention |

#### Axis C — Causal Specificity

List each gap, risk, or stall from the simulation. Each must carry a named cause — not
"change resistance" or "adoption friction" but the specific mechanism (workflow being replaced,
trust deficit source, institutional lock-in, missing proof type).

| Gap / Risk / Stall | Named cause | Section where stated |
|--------------------|------------|---------------------|
| | | |
| | | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A (role completeness):    [PASS — all 16 traced] / [FAIL — missing: list]
Axis B (temporal completeness):[PASS — all events pinned] / [FAIL — unpinned: list]
Axis C (causal specificity):   [PASS — all named causes] / [FAIL — generic: list]
```

If any axis fails, correct the upstream simulation sections before continuing.

---

### PART A — Churn Risk Register

Minimum 2 entries.

```
[Role] — Trigger: [...] — Why at risk: [...]
[Role] — Trigger: [...] — Why at risk: [...]
```

---

### PART B — Champion Network

Minimum 2 champions. For each: who they bridge, the mechanism, and whether advocacy is
active sponsorship or passive diffusion.

```
[Role] — From: [archetype] → To: [archetype] — Mechanism: [...]
         Influence type: [Active sponsorship / Passive diffusion — explain]
```

---

### PART C — Interventions Ranked by Adoption Delta

Minimum 3 interventions, highest delta first. Pin each to a simulation month.

```
[Rank 1] [Intervention] — Delta: [+N roles by month M] — Deploy before: Month [M]
[Rank 2] [Intervention] — Delta: [...] — Deploy before: Month [M]
[Rank 3] [Intervention] — Delta: [...] — Deploy before: Month [M]
```

---

## V-03 — Single Axis: Preamble Propagation with Citation Markers

**Variation axis:** Preamble propagation with citation markers — A named incumbent is declared
in a preamble block before the simulation begins. Each downstream section that touches chasm
cause, interventions, champions, or churn carries an explicit [CITE: THE INCUMBENT] marker
that must be replaced with the incumbent's name and the specific connection to it. The marker
makes omission visible: an unfilled [CITE: THE INCUMBENT] is a structural gap, not a missing
sentence buried in prose.

**Hypothesis:** R1 V-03 introduced the named incumbent and asked sections to "reference" it —
but soft instructions allow sections to name the incumbent once in passing without integrating
it as a causal thread. C-11 requires 3+ downstream sections to reference the incumbent by name
with substantive connection. The difference between R1 V-03 and V-03 here is mechanical
enforcement: instead of instructing sections to reference THE INCUMBENT, each section contains
a labeled slot that cannot be left blank. A section with an unfilled [CITE] slot fails C-11 at
that location regardless of whether its prose mentions the incumbent elsewhere. This raises
C-11 from a soft-reference request to a structural fill contract, matching the intent of the
criterion: the incumbent is the through-thread, not a one-time mention.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles
(PM, UX, C-01 through C-12, Support, SRE).

---

### PREAMBLE — Incumbent Declaration

Complete this block before any simulation output. Every field is required.

```
THE INCUMBENT:
  [The specific workflow, tool, or habit that {{topic}} replaces or competes with.
   Name it precisely — not "current process" but the actual named thing.]

What THE INCUMBENT does well for this team:
  - [Advantage 1: which cohorts rely on this and why]
  - [Advantage 2: what {{topic}} does not yet match]

What {{topic}} must prove to displace it:
  - For early majority: [specific proof point required]
  - For late majority:  [specific proof point required]

Downstream citation contract:
  THE INCUMBENT must appear by name in: SECTION 3 (chasm cause),
  SECTION 5 (each intervention's displacement target), SECTION 4 (champion mechanism),
  and SECTION 6 (each churn risk's incumbent pull).
```

---

### SECTION 1 — Archetype Mapping

| Role | Rogers Archetype | Incumbent dependency |
|------|-----------------|---------------------|
| PM | | heavy / moderate / indifferent / seeking alt |
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

Incumbent dependency: heavy = daily workflow dependency / moderate = occasional use /
indifferent = doesn't use it / seeking alt = actively looking for replacement

---

### SECTION 2 — Month-by-Month Simulation

Minimum 6 months. Every role from SECTION 1 must appear in at least one month row.

```
Month 1
  Newly adopting:         [roles]
  Archetype cohort:       Innovator
  Detachment trigger:     [what made these roles willing to try {{topic}} despite THE INCUMBENT?]
  Cumulative:             [N of 16]

Month 2
  Newly adopting:         [roles]
  Archetype cohort:       [...]
  Detachment trigger:     [...]
  Cumulative:             [N of 16]

Month 3
  Newly adopting:         [roles or "none — chasm"]
  Stall reason:           [what THE INCUMBENT still offers that {{topic}} hasn't matched — [CITE: THE INCUMBENT]]
  Cumulative:             [N of 16]

Month 4
  Newly adopting:         [roles]
  Detachment trigger:     [...]
  Cumulative:             [N of 16]

Month 5
  Newly adopting:         [roles]
  Detachment trigger:     [...]
  Cumulative:             [N of 16]

Month 6
  Newly adopting:         [roles]
  Detachment trigger:     [...]
  Cumulative:             [N of 16]
```

---

### SECTION 3 — Chasm Analysis

```
CHASM-A — Gap:
  Between:        [early-adopter roles] and [early-majority roles — name both]
  Named cause:    [Why does EM not follow automatically? Name the specific advantage of
                   [CITE: THE INCUMBENT] that prevents EM crossing. Do not use generic
                   friction — name the workflow, habit, or institutional reason THE INCUMBENT
                   still wins for this cohort.]

CHASM-B — Risk:
  At risk:        [roles that plateau; feature value uncaptured]
  Incumbent win:  [CITE: THE INCUMBENT] wins condition — what happens if chasm persists:
                  [incumbent entrenches / {{topic}} scoped to power users / etc.]

CHASM-C — Bridge:
  EM needs:       [specific evidence that {{topic}} beats [CITE: THE INCUMBENT]
                   on the dimension that matters to this cohort]
  Provider:       [champion role + mechanism + what THE INCUMBENT argument they address]
```

---

### SECTION 4 — Champion Network

For each champion: who they bridge, how their advocacy addresses THE INCUMBENT's appeal
for late-cohort roles. Minimum 2 champions.

The [CITE: THE INCUMBENT] marker in each champion entry must be replaced with the incumbent
name and a specific connection — what argument of THE INCUMBENT does this champion answer?

```
Champion: [role]
  Bridges:    [archetype from] → [archetype to]
  Mechanism:  [how this champion's endorsement answers the appeal of [CITE: THE INCUMBENT]
               for the target cohort]
  Answers:    [THE INCUMBENT's specific argument that this champion counters]
  Influence:  [Active sponsorship / Passive diffusion — explain]

Champion: [role]
  Bridges:    [archetype from] → [archetype to]
  Mechanism:  [how this champion's endorsement answers the appeal of [CITE: THE INCUMBENT]]
  Answers:    [THE INCUMBENT's specific argument countered]
  Influence:  [Active sponsorship / Passive diffusion — explain]
```

---

### SECTION 5 — Intervention Recommendations

Minimum 3 interventions, sorted by adoption delta (highest first). Each intervention must
name what habit of [CITE: THE INCUMBENT] it displaces and when it fires.

```
[Rank 1]
  Intervention:             [...]
  Displaces from incumbent: [CITE: THE INCUMBENT] — specific workflow or habit displaced
  Adoption delta:           [+N roles by month M]
  Deploy before:            Month [M]

[Rank 2]
  Intervention:             [...]
  Displaces from incumbent: [CITE: THE INCUMBENT] — [...]
  Adoption delta:           [...]
  Deploy before:            Month [M]

[Rank 3]
  Intervention:             [...]
  Displaces from incumbent: [CITE: THE INCUMBENT] — [...]
  Adoption delta:           [...]
  Deploy before:            Month [M]
```

---

### SECTION 6 — Churn Risk Register

Minimum 2 entries. Each entry must name the incumbent pull — what [CITE: THE INCUMBENT]
still offers that draws this role back.

```
[Role] — Trigger: [...] — Incumbent pull: [CITE: THE INCUMBENT] still offers [...]
[Role] — Trigger: [...] — Incumbent pull: [CITE: THE INCUMBENT] still offers [...]
```

---

### SECTION 7 — S-Curve and Incumbent Position

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Explain any non-adopting roles and whether
[CITE: THE INCUMBENT] permanently retains them.

---

## V-04 — Combined: Champion Displacement Annotation + Preamble Propagation

**Variation axes:** Champion displacement annotation (V-01) + Preamble propagation with
citation markers (V-03)

**Hypothesis:** V-01 forces the champion displacement question via a required table column.
V-03 forces incumbent threading via fill-contract citation markers in downstream sections.
Combined, they address C-12 and C-11 simultaneously and are mutually reinforcing: the
preamble's named incumbent gives champions a concrete argument to counter (making the
"Incumbent argument countered" column easier and more specific to fill), and the champion
table's explicit counter-annotation populates the [CITE: THE INCUMBENT] answer field in
SECTION 4 with a named displacement claim rather than a generic acknowledgment. The
combination produces causal tissue throughout: incumbent names the argument, champions
are positioned to counter specific named arguments, and citation markers track propagation.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles
(PM, UX, C-01 through C-12, Support, SRE).

---

### PREAMBLE — Incumbent Declaration

Complete before any simulation output.

```
THE INCUMBENT:
  [Specific workflow, tool, or habit {{topic}} displaces. Name it precisely.]

What THE INCUMBENT does well:
  - [Advantage 1 — which cohorts rely on this and why]
  - [Advantage 2 — what {{topic}} does not yet match]

What {{topic}} must prove to displace it:
  - For early majority: [...]
  - For late majority:  [...]

Downstream citation contract:
  THE INCUMBENT must be cited by name in:
    SECTION 3 (chasm cause) | SECTION 4 (each champion's "Answers" field) |
    SECTION 5 (each intervention's displacement target) | SECTION 6 (each churn risk's pull)
```

---

### SECTION 1 — Archetype Mapping

| Role | Rogers Archetype | Incumbent dependency | Primary adoption driver |
|------|-----------------|---------------------|------------------------|
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

Incumbent dependency: heavy / moderate / indifferent / seeking alt

---

### SECTION 2 — Month-by-Month Simulation

Minimum 6 months. Every role from SECTION 1 must appear in at least one row.
Cumulative count must reconcile with 16.

| Month | Newly adopting roles | Archetype cohort | Adoption mechanism | Detachment from incumbent | Cumulative (of 16) |
|-------|---------------------|-----------------|-------------------|--------------------------|--------------------|
| M1 | | Innovator | | | |
| M2 | | | | | |
| M3 | | | | | |
| M4 | | | | | |
| M5 | | | | | |
| M6 | | | | | |

For stall months (zero new adopters): state what THE INCUMBENT is still offering that {{topic}} hasn't matched.

---

### SECTION 3 — Chasm Analysis

```
CHASM-A — Gap:
  Between:    [early-adopter roles] and [early-majority roles]
  Named cause:[What specific advantage of THE INCUMBENT prevents EM crossing?
               [CITE: THE INCUMBENT by name] — name the workflow or habit, not generic friction.]

CHASM-B — Risk:
  At risk:    [roles that plateau; value uncaptured]
  Incumbent win condition: if chasm persists, [CITE: THE INCUMBENT] [entrenches / etc.]

CHASM-C — Bridge:
  EM needs:   [specific evidence type]
  Provider:   [champion role + mechanism + THE INCUMBENT argument answered]
```

---

### SECTION 4 — Champion Network

Two required columns: "Bridging mechanism" and "Incumbent argument countered."
Both must be specific — generic entries fail both columns.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | Active / Passive |

Minimum 2 champions. "Incumbent argument countered" must name the exact claim, habit, or
advantage of THE INCUMBENT that this champion is positioned to displace.

---

### SECTION 5 — Intervention Recommendations

Sorted by adoption delta, highest first. Minimum 3 interventions.
Each intervention names what it displaces from THE INCUMBENT.

| Rank | Intervention | Target roles | Displaces from incumbent | Adoption delta | Deploy before month |
|------|-------------|-------------|--------------------------|---------------|-------------------|
| 1 | | | [CITE: THE INCUMBENT] — [habit/workflow] | | |
| 2 | | | [CITE: THE INCUMBENT] — [habit/workflow] | | |
| 3 | | | [CITE: THE INCUMBENT] — [habit/workflow] | | |

---

### SECTION 6 — Churn Risk Register

Minimum 2 entries. Each names the incumbent pull explicitly.

| Role | Archetype | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|--------------|---------------|----------------------|
| | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | [CITE: THE INCUMBENT] still offers: [...] | |

---

### SECTION 7 — S-Curve Summary

| Phase | Month range | Adopters at close | % of 16 | Incumbent position |
|-------|------------|-------------------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

---

## V-05 — Full: Champion Displacement Annotation + Three-Axis Gap Audit + Preamble Propagation

**Variation axes:** Champion displacement annotation (V-01) + Three-axis gap audit block (V-02)
+ Preamble propagation with citation markers (V-03)

**Hypothesis:** Each R2 axis closes a distinct gap. V-01 forces causal specificity in the
champion table (C-12). V-02 forces simultaneous closure of role, temporal, and causal
completeness through an independent audit (C-13). V-03 forces incumbent threading throughout
downstream sections via explicit fill-contract markers (C-11 to full propagation depth). The
three axes are mutually reinforcing without overlap: the preamble provides the named thread
(V-03), the audit certifies the thread was maintained across all three dimensions (V-02), and
the champion table carries the displacement annotations that make the causal specificity axis
of the audit passable (V-01). A simulation that passes all three R2 axes simultaneously
satisfies C-11, C-12, and C-13 structurally — not by discretionary completeness, but by
unfilled markers and failed audit rows becoming visible failures.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles
(PM, UX, C-01 through C-12, Support, SRE).

---

### PREAMBLE — Incumbent Declaration

Complete before any simulation output. All fields required.

```
THE INCUMBENT:
  [Specific workflow, tool, or habit {{topic}} displaces. Name it precisely — not
   "current process" but the actual named thing.]

What THE INCUMBENT does well for this team:
  - [Advantage 1: which cohorts rely on this and why]
  - [Advantage 2: what {{topic}} does not yet match]

What {{topic}} must prove to displace it:
  - For early majority: [specific proof point]
  - For late majority:  [specific proof point]

Downstream citation contract — THE INCUMBENT must appear by name in:
  SECTION 3 (chasm cause) | SECTION 4 (champion "Answers" column) |
  SECTION 5 (intervention displacement target) | SECTION 6 (churn risk pull)
  THREE-AXIS GAP AUDIT Axis C (causal specificity entries)
```

---

### SECTION 1 — Archetype Mapping

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
| | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2** (skip if phase closes in M1)

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
| | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |

```
Cumulative: [N] of 16
Champion forming?: [role; mechanism; what THE INCUMBENT argument they're positioned to answer]
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
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles] |
| Cause | [What specific advantage of THE INCUMBENT prevents EM crossing? [CITE: THE INCUMBENT by name] — name the habit or workflow.] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [specific value] that {{topic}} doesn't yet match for EM |
| Risk if not bridged | [Roles that plateau; [CITE: THE INCUMBENT] entrenches] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion | [Role + mechanism + what THE INCUMBENT argument they counter — CITE: THE INCUMBENT] |

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
Churn risk?: [role + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
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
Non-adopters (if any): [roles; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

---

### THREE-AXIS GAP AUDIT

Complete this block before SECTION 3. All rows are fill contracts — empty or generic
cells are audit failures, not missing content.

#### Axis A — Role Completeness

All 16 roles listed and traced to their adoption month. Non-adopters listed with reason.

| Role | Adoption month | Archetype cohort | Source (phase + month where named) |
|------|---------------|-----------------|-------------------------------------|
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

#### Axis B — Temporal Completeness

Every distinct event pinned to its month. Unpinned events fail this axis.

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

Each gap, risk, and stall from the simulation must carry a named cause — not generic
resistance language. Must cite THE INCUMBENT by name where applicable.

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |
| | | | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A (role completeness):    [PASS — all 16 traced] / [FAIL — missing: list]
Axis B (temporal completeness):[PASS — all events pinned] / [FAIL — unpinned: list]
Axis C (causal specificity):   [PASS — all named, incumbent cited] / [FAIL — generic: list]
```

If any axis fails: correct the upstream phases before continuing to SECTION 3.

---

### SECTION 3 — Champion Network

Two required columns: "Bridging mechanism" and "Incumbent argument countered."
"Incumbent argument countered" = the specific claim, habit, or advantage of THE INCUMBENT
that this champion is positioned to displace. Generic entries fail.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | Active / Passive |

Minimum 2 champions.

---

### SECTION 4 — Intervention Recommendations

Sorted by adoption delta, highest first. Minimum 3 interventions.

| Rank | Intervention | Target roles | Displaces from incumbent | Adoption delta | Deploy before month |
|------|-------------|-------------|--------------------------|---------------|-------------------|
| 1 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 2 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 3 | | | [CITE: THE INCUMBENT] — [habit] | | |

---

### SECTION 5 — Churn Risk Register

Minimum 2 entries. Incumbent pull must cite THE INCUMBENT by name.

| Role | Archetype | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|--------------|---------------|----------------------|
| | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | [CITE: THE INCUMBENT] still offers: [...] | |

---

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Explain any non-adopting roles and whether
THE INCUMBENT permanently retains them.
