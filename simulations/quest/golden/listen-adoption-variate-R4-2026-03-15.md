# Variations: listen-adoption — Round 4

**Rubric:** v4 | **Criteria:** C-01 through C-16 | **Max composite:** 100 | **Golden threshold:** all 5 essential pass + composite >= 80

---

## Variation Axes

| Axis | R4 Target | Description |
|------|-----------|-------------|
| Phrasing register | C-16 deviation reasoning depth | Narrative/second-person framing ("You are the adoption analyst...") replaces imperative fill-contract preamble. All structural blocks remain identical; only the connecting prose changes register. Hypothesis: causal reasoning in SCHEDULE RECONCILIATION deviation rows and CHASM analysis deepens when the model has established analyst perspective before filling structural contracts. |
| Inertia framing | C-16 schedule anchoring + C-11 depth | A DEPENDENCY GRAVITY ASSESSMENT in the PREAMBLE rates each role's daily reliance on THE INCUMBENT (1–5 scale) before committed months are assigned. Gravity scores cascade into SECTION 1's committed month assignments (high gravity → later month) and SCHEDULE RECONCILIATION deviation reasons (must cite gravity score when applicable). |
| Output format | C-02, C-16, C-14 in-stream correction | After each phase close, a compact PHASE COMPLIANCE LEDGER (PCL) checks which structural contracts the current phase satisfied. FAIL entries require immediate upstream correction before the next phase begins. Makes structural compliance an in-stream obligation rather than a post-hoc audit. |

**Single-axis (V-01, V-02, V-03):** Phrasing register · Inertia framing · Output format
**Combined (V-04):** Phrasing register + Inertia framing
**Full (V-05):** Phrasing register + Inertia framing + Output format

---

## Baseline (all five carry from R3 V-05)

| Element | Criterion | Form |
|---------|-----------|------|
| PREAMBLE — Incumbent Declaration | C-11 | Named incumbent + downstream citation contract covering PHASE 3, SECTION 3, SECTION 4, SECTION 5, THREE-AXIS GAP AUDIT, TRACEABILITY AUDIT, SCHEDULE RECONCILIATION |
| SECTION 1 — Archetype Mapping + Committed Adoption Schedule | C-01, C-16 | 16-row table; column labeled "Committed adoption month" (not "Earliest"); filled before any simulation output |
| SECTION 2 — 5-phase simulation with month blocks | C-02, C-03 | Phase opens by re-citing preceding CLOSE; each month block opens with "Roles committed to M[N]:"; row-numbered tables (Row 1, Row 2…) |
| CHAMPION FORMATION EVENT blocks in PHASE 2 and PHASE 4 | C-14 | Three required fields: Formation month / Role becoming champion / Bridging mechanism / Incumbent argument targeted |
| Phase closes with "Scheduled roles met:" | C-16 | Confirms all committed roles appeared or explains delay |
| SCHEDULE RECONCILIATION in PHASE 5 CLOSE | C-16 | 16-row table: Committed month / Actual month / Status (On schedule / Delayed N months — reason / Non-adopter) |
| TRACEABILITY AUDIT (independent of Axis A) | C-15 | 16-row table; Row Citation format: `[PHASE N / Month M / Row K]`; generic citations fail |
| THREE-AXIS GAP AUDIT (Axis A/B/C) | C-13 | Role completeness + temporal completeness + causal specificity; Axis C cites THE INCUMBENT |
| SECTION 3 — Champion Network | C-06, C-09, C-12, C-14 | Formation phase/month citation required; "Incumbent argument countered" column cites THE INCUMBENT by name |
| SECTION 4 — Interventions ranked by adoption delta | C-04, C-10 | "Displaces from incumbent" + "Adoption delta" + "Deploy before month" columns; ranked highest delta first |
| SECTION 5 — Churn Risk Register | C-05 | "Incumbent pull" column cites THE INCUMBENT by name per row |
| SECTION 6 — S-Curve Summary | C-07, C-08 | Phase counts + % + Incumbent position; cross-check against TRACEABILITY AUDIT and SCHEDULE RECONCILIATION |

---

## V-01 — Single Axis: Phrasing Register (Narrative Analyst Mode)

**Variation axis:** Phrasing register — The prompt opens by establishing the analyst perspective
in second-person narrative ("You are the adoption analyst for **{{topic}}**..."). All structural
blocks (fill contracts, tables, phase closes, CHAMPION FORMATION EVENT, SCHEDULE RECONCILIATION,
TRACEABILITY AUDIT, THREE-AXIS GAP AUDIT) are retained verbatim with identical required fields.
Only the connecting prose between sections changes register: from imperative ("Complete before
proceeding") to narrative ("Your first task is to...", "Before the simulation runs, you commit
to...", "Month N is live. The roles you committed to this month are..."). The analytical
reasoning sections — chasm cause, deviation reasons, champion mechanisms — are framed as analyst
judgments rather than fill-contract answers.

**Hypothesis:** Imperative fill-contract prompts enforce structural compliance at the cost of
analytical depth. The SCHEDULE RECONCILIATION deviation reasons ("committed M3, delayed to M5
because: [specific reason]") and the CHASM cause analysis ("What specific advantage of THE
INCUMBENT prevents EM crossing?") produce richer, causally grounded explanations when the model
has adopted an analyst stance before entering the structural blocks. The structural contracts
anchor the required output format; the narrative framing anchors the reasoning behind it.
Specifically targeted: C-16's deviation reason field (the new aspirational criterion), which
in R3 V-03 could be satisfied with a brief clause that technically passes but lacks causal depth.
A model reasoning as "the adoption analyst" may explain deviations by reference to team events,
incumbent anchors, and specific blocking conditions — generating content that passes C-16 and
also contributes to C-11 and C-09 depth.

---

You are the adoption analyst for **{{topic}}**. Your simulation follows a structured protocol
with required output blocks. The protocol is non-negotiable — every block must be completed
in full before advancing. Your role is to reason as the analyst throughout, not merely to fill
slots: where the protocol asks for a cause, give the actual cause; where it asks for a mechanism,
describe the mechanism that will actually work for this team.

Produce the artifact below in the order shown.

---

### PREAMBLE — Incumbent Declaration

Your first task before running any simulation is to name THE INCUMBENT — the specific workflow,
tool, or habit that **{{topic}}** must displace. Naming it precisely is the most important
single act in this simulation: every downstream section will cite it by name.

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
  PHASE 3 chasm cause | SECTION 3 champion "Incumbent argument countered" column |
  SECTION 4 intervention displacement target | SECTION 5 churn risk pull |
  THREE-AXIS GAP AUDIT Axis C | TRACEABILITY AUDIT Row Citations where applicable |
  SCHEDULE RECONCILIATION deviation reasons where THE INCUMBENT is the stall cause
```

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

Before the simulation runs, you declare your committed schedule. These are binding predictions —
the simulation will execute against them. Each role gets a specific committed month (M1–M9)
or "Non-adopter." Deliberate now: a role you assign to M3 must appear in Month 3. If you later
discover the assignment was wrong, the simulation records the deviation and you explain why.

| Role | Rogers Archetype | Incumbent dependency | Committed adoption month |
|------|-----------------|---------------------|------------------------|
| PM | | heavy / moderate / indifferent / seeking alt | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

Archetype order must be respected: Innovators first, Laggards last. Non-adopters must state reason.

---

### SECTION 2 — Month-by-Month Simulation

The simulation runs against your committed schedule. Each month block opens by listing the roles
you committed to that month — these must appear as adopting rows. If a committed role doesn't
appear in its assigned month, record the deviation inline with an explanation.

Row addresses for TRACEABILITY AUDIT: `[PHASE N / Month M / Row K]` where K is the row position.

---

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1 — fill before writing rows]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull (why others don't yet) |
|-----|---------------------|-----------|-----------------|--------------------------------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2** (include all roles committed to M2)

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [list roles committed to M1-M2; confirm all appeared or explain delay]
Incumbent position: [has THE INCUMBENT lost ground? describe]
Signal to EA cohort: [what evidence now exists that {{topic}} works]
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT** — as analyst, identify the first role emerging this phase
that will bridge early adopters toward early majority. If no champion has formed yet,
write "No champion formed — [reason]." A champion must be recorded at the month it first
emerges.

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role — must appear in a simulation row at or before this month]
  Bridging mechanism:        [how this role will accelerate spread to the next cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — the specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M3-M4 committed roles appeared or explain delay]
Incumbent position: [still dominant with which cohorts? why?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

As analyst, you identify the chasm: the gap between early-adopter exit and early-majority
entry. Name the specific cause and what is at risk if the gap is not bridged.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles — name specifically] |
| Cause | [What specific advantage of THE INCUMBENT prevents EM crossing? [CITE: THE INCUMBENT by name] — name the habit or workflow.] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [specific value] that {{topic}} doesn't yet match for EM |
| Risk if not bridged | [Roles that plateau; [CITE: THE INCUMBENT] entrenches] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter] |

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 entry]
Incumbent position at chasm: [still dominant / weakening / differentiated]
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Churn risk?: [role + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** — if a new champion emerges this phase to bridge EM toward
Late Majority, record it here. If no new champion: "No new champion this phase."

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm M5-M6 committed roles appeared or explain]
Incumbent position: [retreating / residual / eliminated in this cohort]
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Non-adopters (if any): [roles; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

For every role, compare the committed month you declared in SECTION 1 against the actual month
they appear in the simulation. Explain every deviation. When THE INCUMBENT is the cause of a
delay, name it.

| Role | Committed month | Actual month | Status |
|------|----------------|-------------|--------|
| PM | | | On schedule / Delayed [N months] — [reason] / Non-adopter |
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

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list with reasons; cite THE INCUMBENT where applicable]
Non-adopters: [list]
```

---

### TRACEABILITY AUDIT

Complete before the THREE-AXIS GAP AUDIT. Independent structural check.

**Row Citation format:** `[PHASE N / Month M / Row K]` or `[PHASE N / Month M / CHAMPION FORMATION EVENT]`.
Generic citations fail. Non-adopters cite `[PHASE 5 CLOSE / non-adopter list]`.

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
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

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS] / [FAIL — missing or generic citations: list roles]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies: list]
```

---

### THREE-AXIS GAP AUDIT

Complete before SECTION 3. All rows are fill contracts.

#### Axis A — Role Completeness

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

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A (role completeness):    [PASS — all 16 traced] / [FAIL — missing: list]
Axis B (temporal completeness):[PASS — all events pinned] / [FAIL — unpinned: list]
Axis C (causal specificity):   [PASS — all named, incumbent cited] / [FAIL — generic: list]
```

If any axis fails: correct the upstream phases before continuing to SECTION 3.

---

### SECTION 3 — Champion Network

**Derivation rule:** Every champion row must have a corresponding CHAMPION FORMATION EVENT in
the simulation body. Record formation phase and month. A champion without this citation fails
C-14 at this row.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

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

Final count must match 16. Cross-check against TRACEABILITY AUDIT and SCHEDULE RECONCILIATION.
Explain any non-adopting roles and whether THE INCUMBENT permanently retains them.

---

## V-02 — Single Axis: Inertia Framing (Dependency Gravity Assessment)

**Variation axis:** Inertia framing — A DEPENDENCY GRAVITY ASSESSMENT block is inserted in the
PREAMBLE, after THE INCUMBENT is named. For each of the 16 stock roles, the analyst rates their
daily reliance on THE INCUMBENT on a 1–5 gravity scale (5 = uses THE INCUMBENT daily with no
workaround, 1 = rarely or never touches it). These gravity scores then cascade into two
downstream structural changes: (a) SECTION 1's committed month assignments are anchored to
gravity (gravity 5 → M7–M9 range, gravity 1–2 → M1–M2 range), making the schedule a gravity-
derived prediction rather than an intuitive guess; (b) SCHEDULE RECONCILIATION deviation
reasons must cite the gravity score when THE INCUMBENT's pull is a contributing factor
("C-09, gravity 4 — committed M5, delayed to M6 because [THE INCUMBENT]'s [specific hold]
for this cohort was underestimated"). All other structural elements carry from the R3 V-05
baseline unchanged.

**Hypothesis:** In R3 V-05, committed month assignments can be filled in without stated
justification — a role might be assigned M5 for no declared reason, making the SCHEDULE
RECONCILIATION's deviation explanations harder to verify. The DEPENDENCY GRAVITY ASSESSMENT
creates a causal chain: named incumbent → gravity score per role → committed month range →
deviation reason. Deviation explanations become more specific because the model has a numeric
anchor to cite. As a secondary effect, the gravity table forces differentiated reasoning about
all 12 developer roles (C-01..C-12): rather than collapsing them into a uniform late-majority
cohort, each must receive an individual gravity rating with a stated basis, driving more
differentiated SECTION 1 archetype assignments and committed months. This targeting may produce
a new excellence signal: gravity-weighted chasm analysis, where the chasm's cause is tied to
the cluster of high-gravity roles that constitute the majority of the EM cohort.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles
(PM, UX, C-01 through C-12, Support, SRE).

Produce the artifact below in full. Every bracketed instruction is a fill contract — complete
it before proceeding to the next section.

---

### PREAMBLE — Incumbent Declaration and Dependency Gravity Assessment

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
  PHASE 3 chasm cause | SECTION 3 champion "Incumbent argument countered" column |
  SECTION 4 intervention displacement target | SECTION 5 churn risk pull |
  THREE-AXIS GAP AUDIT Axis C | TRACEABILITY AUDIT Row Citations where applicable |
  SCHEDULE RECONCILIATION deviation reasons where incumbent pull is the stall cause
```

**DEPENDENCY GRAVITY ASSESSMENT**

Rate each role's daily reliance on THE INCUMBENT. Fill gravity score and the specific
behavior that grounds the rating. This table drives committed month assignments in SECTION 1.

Gravity scale:
- 5 — Uses THE INCUMBENT daily; no viable workaround; switching requires a process change
- 4 — Uses it most days; has minor workarounds; switching requires convincing evidence
- 3 — Uses it regularly but not daily; moderate switching friction
- 2 — Uses it occasionally; can adopt {{topic}} without displacing workflow immediately
- 1 — Rarely or never uses THE INCUMBENT; low friction to adopt

| Role | Gravity score (1–5) | Basis: what this role uses THE INCUMBENT for |
|------|--------------------|--------------------------------------------|
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

Gravity-to-committed-month anchor: gravity 1–2 → M1–M2 range; gravity 3 → M3–M4 range;
gravity 4 → M5–M6 range; gravity 5 → M7–M9 range. Deviations from these ranges must be
stated in SECTION 1 with a reason.

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

Fill "Committed adoption month" before writing any simulation content. Anchor to gravity
scores from the DEPENDENCY GRAVITY ASSESSMENT. Deviations from the gravity-range anchor
must note a reason in the "Incumbent dependency" column.

| Role | Rogers Archetype | Incumbent dependency (gravity + note) | Committed adoption month |
|------|-----------------|--------------------------------------|------------------------|
| PM | | gravity [N] — [note if deviating from anchor] | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

---

### SECTION 2 — Month-by-Month Simulation

Execute the committed schedule from SECTION 1. Rows are addressable as `[PHASE N / Month M / Row K]`
for TRACEABILITY AUDIT citations.

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull (why others don't yet) |
|-----|---------------------|-----------|-----------------|--------------------------------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2** (include all roles committed to M2)

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M1-M2 committed roles appeared or explain delay]
Incumbent position: [describe]
Signal to EA cohort: [what evidence exists that {{topic}} works]
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT** — required at the month a champion first emerges.
If no champion has formed yet, write "No champion formed — [reason]."

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role — must appear in a simulation row at or before this month]
  Bridging mechanism:        [how they will bridge early adopters toward early majority]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M3-M4 committed roles appeared or explain]
Incumbent position: [still dominant with which cohorts? why?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles — name specifically] |
| Cause | [What specific advantage of THE INCUMBENT prevents EM crossing? [CITE: THE INCUMBENT by name] — note the gravity cluster blocking the bridge.] |
| Gravity cluster | [Which roles have gravity 4-5? These are the chasm anchor — why their dependency makes the bridge harder] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [...] that {{topic}} doesn't yet match for EM |
| Risk if not bridged | [Roles that plateau; [CITE: THE INCUMBENT] entrenches for high-gravity cohort] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter] |

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 entry]
Incumbent position at chasm: [still dominant / weakening / differentiated]
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Churn risk?: [role + gravity score + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** — if a new champion emerges this phase (bridging EM toward LM),
record here. If no new champion: "No new champion this phase."

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm M5-M6 committed roles appeared or explain]
Incumbent position: [retreating / residual / eliminated in this cohort]
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Non-adopters (if any): [roles; gravity score; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

Compare committed month (SECTION 1) against actual month for all 16 roles. Deviation reasons
must cite gravity score and THE INCUMBENT when incumbent pull is the stall cause.

| Role | Gravity | Committed month | Actual month | Status |
|------|---------|----------------|-------------|--------|
| PM | | | | On schedule / Delayed [N months] — gravity [G]: [reason citing THE INCUMBENT if applicable] / Non-adopter |
| UX | | | | |
| C-01 | | | | |
| C-02 | | | | |
| C-03 | | | | |
| C-04 | | | | |
| C-05 | | | | |
| C-06 | | | | |
| C-07 | | | | |
| C-08 | | | | |
| C-09 | | | | |
| C-10 | | | | |
| C-11 | | | | |
| C-12 | | | | |
| Support | | | | |
| SRE | | | | |

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list with gravity scores and reasons; cite THE INCUMBENT where applicable]
Non-adopters: [list with gravity scores]
Gravity accuracy check: [did high-gravity roles (4-5) cluster in later months as predicted?]
```

---

### TRACEABILITY AUDIT

Complete before the THREE-AXIS GAP AUDIT. Independent structural check.

**Row Citation format:** `[PHASE N / Month M / Row K]`. Generic citations fail.
Non-adopters cite `[PHASE 5 CLOSE / non-adopter list]`.

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
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

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS] / [FAIL — missing or generic citations: list roles]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies: list]
```

---

### THREE-AXIS GAP AUDIT

#### Axis A — Role Completeness

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

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A (role completeness):    [PASS — all 16 traced] / [FAIL — missing: list]
Axis B (temporal completeness):[PASS — all events pinned] / [FAIL — unpinned: list]
Axis C (causal specificity):   [PASS — all named, incumbent cited] / [FAIL — generic: list]
```

If any axis fails: correct the upstream phases before continuing to SECTION 3.

---

### SECTION 3 — Champion Network

**Derivation rule:** Every champion row must have a corresponding CHAMPION FORMATION EVENT in
the simulation body. Record formation phase and month.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

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

Minimum 2 entries.

| Role | Archetype | Gravity | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|---------|--------------|---------------|----------------------|
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |

---

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Cross-check against TRACEABILITY AUDIT and SCHEDULE RECONCILIATION.
Explain non-adopting roles and whether THE INCUMBENT permanently retains them.

---

## V-03 — Single Axis: Output Format (Phase Compliance Ledger)

**Variation axis:** Output format — After each phase close block, a compact PHASE COMPLIANCE
LEDGER (PCL) lists the structural contracts the current phase was required to satisfy, with a
PASS / FAIL / PARTIAL verdict per item. If any item is FAIL, the model must correct the upstream
phase content before writing the next phase header. The PCL is a structural gate, not an
informational note: the simulation cannot advance past PHASE 2 CLOSE unless the PHASE 2 PCL
clears. The PCL checks only the criteria whose evidence must appear within that phase's body —
it does not re-check earlier phases. All baseline structural elements from R3 V-05 are retained;
the PCL is added after each PHASE CLOSE block.

**Hypothesis:** In R3 V-05, structural failures (missing CHAMPION FORMATION EVENT, absent
"Scheduled roles met:" field, silently omitted committed roles) are caught at the post-simulation
THREE-AXIS GAP AUDIT. By that point, corrections require revising already-written phase bodies —
a large edit. A per-phase compliance gate catches failures at the earliest possible point: if
PHASE 2 CLOSE's PCL shows FAIL for "CHAMPION FORMATION EVENT fired," the model adds the event
before writing Month 5. This prevents structural debt from accumulating. The PCL also makes the
model name which criteria it believes it has satisfied, creating explicit accountability rather
than implicit assumption. The specific new target is C-16: each phase's PCL checks that (a) the
month block opened with a "Roles committed to M[N]:" prompt, and (b) the phase close included a
"Scheduled roles met:" statement. These are the two mid-simulation structural requirements of
C-16 that can fail silently when the model focuses on the adoption narrative.

---

Simulate the adoption curve for **{{topic}}** across the 16 stock roles
(PM, UX, C-01 through C-12, Support, SRE).

Produce the artifact below in full. Every bracketed instruction is a fill contract — complete
it before proceeding to the next section. Phase Compliance Ledgers (PCL) are structural gates:
correct any FAIL before advancing to the next phase.

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
  PHASE 3 chasm cause | SECTION 3 champion "Incumbent argument countered" column |
  SECTION 4 intervention displacement target | SECTION 5 churn risk pull |
  THREE-AXIS GAP AUDIT Axis C | TRACEABILITY AUDIT Row Citations where applicable |
  SCHEDULE RECONCILIATION deviation reasons where applicable
```

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

Fill "Committed adoption month" before writing any simulation content.

| Role | Rogers Archetype | Incumbent dependency | Committed adoption month |
|------|-----------------|---------------------|------------------------|
| PM | | heavy / moderate / indifferent / seeking alt | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

---

### SECTION 2 — Month-by-Month Simulation

Rows addressable as `[PHASE N / Month M / Row K]` for TRACEABILITY AUDIT citations.

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2** (include all roles committed to M2)

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M1-M2 committed roles appeared or explain delay]
Incumbent position: [describe]
Signal to EA cohort: [what evidence exists that {{topic}} works]
```

```
PHASE 1 COMPLIANCE LEDGER
C-01 (archetype mapping present in SECTION 1 — all 16 rows filled): [PASS / FAIL]
C-16a (Month 1 block opened with "Roles committed to M1:" prompt): [PASS / FAIL]
C-16b (Month 2 block opened with "Roles committed to M2:" prompt): [PASS / FAIL]
C-16c (PHASE 1 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-11 (THE INCUMBENT cited by name in at least one Incumbent pull cell): [PASS / FAIL]

If any item is FAIL: correct the upstream phase content before writing PHASE 2.
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT** — required at the month a champion first emerges.
If no champion formed: "No champion formed — [reason]."

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role — must appear in a simulation row at or before this month]
  Bridging mechanism:        [how they will bridge early adopters toward early majority]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M3-M4 committed roles appeared or explain]
Incumbent position: [still dominant with which cohorts? why?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

```
PHASE 2 COMPLIANCE LEDGER
C-14 (CHAMPION FORMATION EVENT fired, or "No champion formed — [reason]" written): [PASS / FAIL]
C-16a (Month 3 block opened with "Roles committed to M3:" prompt): [PASS / FAIL]
C-16b (Month 4 block opened with "Roles committed to M4:" prompt): [PASS / FAIL]
C-16c (PHASE 2 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-09 (CHAMPION FORMATION EVENT includes "Incumbent argument targeted" field, non-generic): [PASS / FAIL / N/A — no champion yet]
C-11 (THE INCUMBENT cited in "Gap to EM" field of PHASE 2 CLOSE): [PASS / FAIL]

If any item is FAIL: correct the upstream phase content before writing PHASE 3.
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles — name specifically] |
| Cause | [What specific advantage of THE INCUMBENT prevents EM crossing? [CITE: THE INCUMBENT by name] — name the habit or workflow.] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [...] that {{topic}} doesn't yet match for EM |
| Risk if not bridged | [Roles that plateau; [CITE: THE INCUMBENT] entrenches] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter] |

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 entry]
Incumbent position at chasm: [still dominant / weakening / differentiated]
```

```
PHASE 3 COMPLIANCE LEDGER
C-03 (Gap element names specific EA and EM roles): [PASS / FAIL]
C-03 (Cause element names specific advantage of THE INCUMBENT — non-generic): [PASS / FAIL]
C-03 (Risk element states what is at risk if chasm is not bridged): [PASS / FAIL]
C-11 (THE INCUMBENT named by name in Cause element): [PASS / FAIL]
C-12 (Champion element cites a specific CHAMPION FORMATION EVENT role): [PASS / FAIL]

If any item is FAIL: correct the PHASE 3 table before writing PHASE 4.
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Churn risk?: [role + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** — if a new champion emerges this phase (bridging EM toward LM),
record here. If no new champion: "No new champion this phase."

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm M5-M6 committed roles appeared or explain]
Incumbent position: [retreating / residual / eliminated in this cohort]
```

```
PHASE 4 COMPLIANCE LEDGER
C-05 (Churn risk noted in Month 5 cumulative block with THE INCUMBENT cited): [PASS / FAIL / N/A]
C-14 (CHAMPION FORMATION EVENT for LM bridge fired or "No new champion" written): [PASS / FAIL]
C-16a (Month 5 block opened with "Roles committed to M5:" prompt): [PASS / FAIL]
C-16b (Month 6 block opened with "Roles committed to M6:" prompt): [PASS / FAIL]
C-16c (PHASE 4 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]

If any item is FAIL: correct the upstream content before writing PHASE 5.
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Non-adopters (if any): [roles; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

| Role | Committed month | Actual month | Status |
|------|----------------|-------------|--------|
| PM | | | On schedule / Delayed [N months] — [reason] / Non-adopter |
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

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list with reasons]
Non-adopters: [list]
```

```
PHASE 5 COMPLIANCE LEDGER
C-16d (SCHEDULE RECONCILIATION table present with all 16 roles): [PASS / FAIL]
C-16e (Every deviation row in SCHEDULE RECONCILIATION includes a named reason): [PASS / FAIL]
C-16f ("Committed adoption month" column in SECTION 1 uses that exact label, not "Earliest"): [PASS / FAIL]
C-07 (PHASE 5 CLOSE includes final adopter count and %): [PASS / FAIL]
C-11 (Non-adopter reason in PHASE 5 CLOSE cites THE INCUMBENT where applicable): [PASS / FAIL]

If any item is FAIL: correct before writing TRACEABILITY AUDIT.
```

---

### TRACEABILITY AUDIT

Complete before the THREE-AXIS GAP AUDIT. Independent structural check.

**Row Citation format:** `[PHASE N / Month M / Row K]`. Generic citations fail.
Non-adopters cite `[PHASE 5 CLOSE / non-adopter list]`.

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
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

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS] / [FAIL — missing or generic citations: list roles]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies: list]
```

---

### THREE-AXIS GAP AUDIT

#### Axis A — Role Completeness

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

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A (role completeness):    [PASS — all 16 traced] / [FAIL — missing: list]
Axis B (temporal completeness):[PASS — all events pinned] / [FAIL — unpinned: list]
Axis C (causal specificity):   [PASS — all named, incumbent cited] / [FAIL — generic: list]
```

If any axis fails: correct the upstream phases before continuing to SECTION 3.

---

### SECTION 3 — Champion Network

**Derivation rule:** Every champion row must have a corresponding CHAMPION FORMATION EVENT in
the simulation body. Record formation phase and month.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

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

Minimum 2 entries.

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

Final count must match 16. Cross-check against TRACEABILITY AUDIT and SCHEDULE RECONCILIATION.
Explain non-adopting roles and whether THE INCUMBENT permanently retains them.

---

## V-04 — Combined: Narrative Analyst Mode + Dependency Gravity Assessment

**Variation axes:** Phrasing register (V-01) + Inertia framing (V-02)

**Hypothesis:** V-01's narrative framing provides contextual depth in analytical cells;
V-02's DEPENDENCY GRAVITY ASSESSMENT provides quantitative anchors for those same cells.
Together, the model is both reasoning as an analyst and grounding that reasoning in a numeric
dependency model. The SCHEDULE RECONCILIATION deviation rows benefit doubly: the gravity score
gives the analyst a specific number to reference ("gravity 4 — this role's reliance on
THE INCUMBENT was higher than I initially modeled"), while the narrative framing provides the
vocabulary to explain what that actually meant for the team ("when Month 5 arrived, C-09 was
still mid-sprint on a workflow built around THE INCUMBENT's [specific feature]"). The two axes
are non-overlapping: V-01 affects connecting prose and analytical framing; V-02 affects a
pre-simulation block and two structural columns. Their combination should produce outputs that
are simultaneously structurally compliant (from V-02's gravity anchoring) and causally rich
(from V-01's analyst framing).

---

You are the adoption analyst for **{{topic}}**. Your simulation follows a structured protocol
with required output blocks. All blocks must be completed in full before advancing. Reason as
the analyst throughout: where the protocol asks for a cause, give the actual cause; where it
asks for a mechanism, describe the mechanism that will actually work for this team.

Produce the artifact below in the order shown.

---

### PREAMBLE — Incumbent Declaration and Dependency Gravity Assessment

Your first task is to name THE INCUMBENT precisely. Every downstream section cites it by name.
Once named, you assess how deeply each role depends on it before committing to any schedule.

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
  PHASE 3 chasm cause | SECTION 3 champion "Incumbent argument countered" column |
  SECTION 4 intervention displacement target | SECTION 5 churn risk pull |
  THREE-AXIS GAP AUDIT Axis C | TRACEABILITY AUDIT Row Citations where applicable |
  SCHEDULE RECONCILIATION deviation reasons where incumbent pull is the stall cause
```

**DEPENDENCY GRAVITY ASSESSMENT**

Before declaring any committed months, assess how deeply each role is anchored to THE INCUMBENT.
This is your primary input for the schedule: roles with high gravity are the hardest to move early.

Gravity scale:
- 5 — Uses THE INCUMBENT daily; no viable workaround; switching is a process change
- 4 — Uses it most days; has minor workarounds; needs convincing evidence to switch
- 3 — Uses it regularly but not daily; moderate switching friction
- 2 — Uses it occasionally; can adopt {{topic}} without immediately displacing workflow
- 1 — Rarely or never uses THE INCUMBENT; low friction to adopt

| Role | Gravity score (1–5) | Basis: what this role uses THE INCUMBENT for |
|------|--------------------|--------------------------------------------|
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

Gravity-to-committed-month anchor: gravity 1–2 → M1–M2 range; gravity 3 → M3–M4 range;
gravity 4 → M5–M6 range; gravity 5 → M7–M9 range. Deviations must be noted in SECTION 1.

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

With the gravity assessment complete, you now commit to a schedule. These are binding
predictions — the simulation executes against them. Assign committed months using the gravity
anchor above. For any role assigned outside the gravity range, note the reason.

| Role | Rogers Archetype | Incumbent dependency (gravity + note) | Committed adoption month |
|------|-----------------|--------------------------------------|------------------------|
| PM | | gravity [N] — [note if deviating from anchor] | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

---

### SECTION 2 — Month-by-Month Simulation

The simulation runs against your committed schedule. Each month block opens by listing the
roles you committed to that month — they must appear. Deviations require an explanation that
cites the gravity score and THE INCUMBENT when applicable. Row addresses for TRACEABILITY
AUDIT: `[PHASE N / Month M / Row K]`.

---

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull (why others don't yet) |
|-----|---------------------|-----------|-----------------|--------------------------------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2** (include all roles committed to M2)

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M1-M2 committed roles appeared or explain delay — cite gravity where applicable]
Incumbent position: [describe]
Signal to EA cohort: [what evidence now exists that {{topic}} works]
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT** — identify the first role emerging this phase that will bridge
early adopters toward early majority. If no champion has formed yet, explain why. A champion
must be recorded at the month it first emerges.

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role — must appear in a simulation row at or before this month]
  Bridging mechanism:        [how this role will accelerate spread to the next cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M3-M4 committed roles appeared or explain — cite gravity where applicable]
Incumbent position: [still dominant with which cohorts? why?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

As analyst, identify the chasm. The gravity cluster of high-dependency roles is typically the
chasm anchor — name which roles constitute it and why their gravity makes the bridge harder.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles — name specifically] |
| Cause | [What specific advantage of THE INCUMBENT prevents EM crossing? [CITE: THE INCUMBENT by name] — name the habit or workflow.] |
| Gravity cluster | [Which roles have gravity 4–5? Why their dependency depth makes the chasm wider.] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [...] that {{topic}} doesn't yet match for EM |
| Risk if not bridged | [Roles that plateau; [CITE: THE INCUMBENT] entrenches for high-gravity cohort] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter] |

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 entry]
Incumbent position at chasm: [still dominant / weakening / differentiated]
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Churn risk?: [role + gravity score + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** — if a new champion emerges this phase to bridge EM toward LM,
record it. If no new champion: "No new champion this phase."

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm M5-M6 committed roles appeared or explain — cite gravity where applicable]
Incumbent position: [retreating / residual / eliminated in this cohort]
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Non-adopters (if any): [roles; gravity score; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

Reconcile committed schedule against actual outcomes. When THE INCUMBENT is the cause of a
delay, name it and cite the gravity score.

| Role | Gravity | Committed month | Actual month | Status |
|------|---------|----------------|-------------|--------|
| PM | | | | On schedule / Delayed [N months] — gravity [G]: [reason citing THE INCUMBENT if applicable] / Non-adopter |
| UX | | | | |
| C-01 | | | | |
| C-02 | | | | |
| C-03 | | | | |
| C-04 | | | | |
| C-05 | | | | |
| C-06 | | | | |
| C-07 | | | | |
| C-08 | | | | |
| C-09 | | | | |
| C-10 | | | | |
| C-11 | | | | |
| C-12 | | | | |
| Support | | | | |
| SRE | | | | |

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list with gravity scores and reasons; cite THE INCUMBENT where applicable]
Non-adopters: [list with gravity scores]
Gravity accuracy check: [did high-gravity roles (4-5) cluster in later months as predicted?]
```

---

### TRACEABILITY AUDIT

**Row Citation format:** `[PHASE N / Month M / Row K]`. Generic citations fail.
Non-adopters cite `[PHASE 5 CLOSE / non-adopter list]`.

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
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

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS] / [FAIL — missing or generic citations: list roles]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies: list]
```

---

### THREE-AXIS GAP AUDIT

#### Axis A — Role Completeness

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

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A (role completeness):    [PASS — all 16 traced] / [FAIL — missing: list]
Axis B (temporal completeness):[PASS — all events pinned] / [FAIL — unpinned: list]
Axis C (causal specificity):   [PASS — all named, incumbent cited] / [FAIL — generic: list]
```

If any axis fails: correct the upstream phases before continuing to SECTION 3.

---

### SECTION 3 — Champion Network

**Derivation rule:** Every champion row must have a corresponding CHAMPION FORMATION EVENT in
the simulation body. Record formation phase and month.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

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

Minimum 2 entries.

| Role | Archetype | Gravity | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|---------|--------------|---------------|----------------------|
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |

---

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Cross-check against TRACEABILITY AUDIT and SCHEDULE RECONCILIATION.
Explain non-adopting roles and whether THE INCUMBENT permanently retains them.

---

## V-05 — Full: Narrative Analyst Mode + Dependency Gravity Assessment + Phase Compliance Ledger

**Variation axes:** Phrasing register (V-01) + Inertia framing (V-02) + Output format (V-03)

**Hypothesis:** Each R4 axis closes a distinct structural gap that the other two cannot cover.
V-01's narrative framing deepens analytical reasoning in deviation rows and the chasm section.
V-02's gravity assessment grounds committed month assignments in a declared dependency model,
making deviations numerically traceable. V-03's phase compliance ledgers catch structural
failures in-stream rather than at the final audit. The three axes are mutually non-overlapping:
V-01 affects connecting prose and analytical framing throughout; V-02 adds a pre-simulation
block and a gravity column to SECTION 1 and SCHEDULE RECONCILIATION; V-03 adds a gating block
after each PHASE CLOSE. Their combination produces a self-verifying artifact: the gravity model
declares dependency before the schedule; the schedule is executed with analyst commentary; per-
phase compliance gates catch failures immediately; and the SCHEDULE RECONCILIATION closes by
reconciling declared gravity, committed months, and actual outcomes in a single auditable table.
A simulation passing all three R4 axes simultaneously should demonstrate C-16 at full depth —
not just the structural requirement (committed column, scheduled roles met, reconciliation table)
but the causal specificity (deviation reasons cite gravity and THE INCUMBENT) that transforms
the reconciliation from a ledger into an explanation.

---

You are the adoption analyst for **{{topic}}**. Your simulation follows a structured protocol
with required output blocks. All blocks must be completed in full before advancing. Phase
Compliance Ledgers (PCL) are structural gates — correct any FAIL before writing the next phase.
Reason as the analyst throughout: where the protocol asks for a cause, give the actual cause;
where it asks for a mechanism, describe the mechanism that will actually work for this team.

Produce the artifact below in the order shown.

---

### PREAMBLE — Incumbent Declaration and Dependency Gravity Assessment

Your first task is to name THE INCUMBENT precisely. Then assess how deeply each role depends
on it — this gravity model drives your committed schedule and explains any deviations.

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
  PHASE 3 chasm cause | SECTION 3 champion "Incumbent argument countered" column |
  SECTION 4 intervention displacement target | SECTION 5 churn risk pull |
  THREE-AXIS GAP AUDIT Axis C | TRACEABILITY AUDIT Row Citations where applicable |
  SCHEDULE RECONCILIATION deviation reasons where incumbent pull is the stall cause
```

**DEPENDENCY GRAVITY ASSESSMENT**

Rate each role's daily reliance on THE INCUMBENT before declaring any committed months.

Gravity scale:
- 5 — Uses THE INCUMBENT daily; no viable workaround; switching is a process change
- 4 — Uses it most days; minor workarounds; needs convincing evidence to switch
- 3 — Uses it regularly but not daily; moderate switching friction
- 2 — Uses it occasionally; can adopt {{topic}} without immediately displacing workflow
- 1 — Rarely or never uses THE INCUMBENT; low friction to adopt

| Role | Gravity score (1–5) | Basis: what this role uses THE INCUMBENT for |
|------|--------------------|--------------------------------------------|
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

Gravity-to-committed-month anchor: gravity 1–2 → M1–M2; gravity 3 → M3–M4;
gravity 4 → M5–M6; gravity 5 → M7–M9. Deviations must be noted in SECTION 1.

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

With gravity assessed, commit to a schedule. These are binding predictions.
For any role assigned outside the gravity anchor range, note the reason.

| Role | Rogers Archetype | Incumbent dependency (gravity + note) | Committed adoption month |
|------|-----------------|--------------------------------------|------------------------|
| PM | | gravity [N] — [note if deviating from anchor] | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

---

### SECTION 2 — Month-by-Month Simulation

The simulation runs against your committed schedule. Each month block opens by listing your
committed adopters for that month — they must appear. Deviations require explanation citing
gravity and THE INCUMBENT where applicable. Row addresses: `[PHASE N / Month M / Row K]`.

---

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull (why others don't yet) |
|-----|---------------------|-----------|-----------------|--------------------------------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2** (include all roles committed to M2)

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M1-M2 committed roles appeared or explain — cite gravity where applicable]
Incumbent position: [describe]
Signal to EA cohort: [what evidence now exists that {{topic}} works]
```

```
PHASE 1 COMPLIANCE LEDGER
C-01 (archetype mapping present in SECTION 1 — all 16 rows filled): [PASS / FAIL]
C-16a (Month 1 block opened with "Roles committed to M1:" prompt): [PASS / FAIL]
C-16b (Month 2 block opened with "Roles committed to M2:" prompt): [PASS / FAIL]
C-16c (PHASE 1 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-11 (THE INCUMBENT cited in at least one Incumbent pull cell): [PASS / FAIL]
V-02 (DEPENDENCY GRAVITY ASSESSMENT complete — all 16 roles have gravity score and basis): [PASS / FAIL]

If any item is FAIL: correct the upstream content before writing PHASE 2.
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT** — identify the first role that will bridge early adopters toward
early majority. If no champion has formed yet, explain why. A champion must be recorded at the
month it first emerges.

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role — must appear in a simulation row at or before this month]
  Bridging mechanism:        [how this role will accelerate spread to the next cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M3-M4 committed roles appeared or explain — cite gravity where applicable]
Incumbent position: [still dominant with which cohorts? why?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

```
PHASE 2 COMPLIANCE LEDGER
C-14 (CHAMPION FORMATION EVENT fired, or "No champion formed — [reason]" written): [PASS / FAIL]
C-16a (Month 3 block opened with "Roles committed to M3:"): [PASS / FAIL]
C-16b (Month 4 block opened with "Roles committed to M4:"): [PASS / FAIL]
C-16c (PHASE 2 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-09 (CHAMPION FORMATION EVENT "Incumbent argument targeted" is non-generic): [PASS / FAIL / N/A]
C-11 (THE INCUMBENT cited in "Gap to EM" of PHASE 2 CLOSE): [PASS / FAIL]

If any item is FAIL: correct the upstream content before writing PHASE 3.
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

As analyst, name the chasm precisely. The gravity cluster of high-dependency roles (gravity 4–5)
is typically the anchor preventing EM from crossing. Identify which roles constitute it and why
their gravity makes the bridge harder than the early-adopter narrative would suggest.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles — name specifically] |
| Cause | [What specific advantage of THE INCUMBENT prevents EM crossing? [CITE: THE INCUMBENT by name] — name the habit or workflow.] |
| Gravity cluster | [Which roles have gravity 4–5? Why their dependency depth makes the chasm wider.] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [...] that {{topic}} doesn't yet match for EM |
| Risk if not bridged | [Roles that plateau; [CITE: THE INCUMBENT] entrenches for high-gravity cohort] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter] |

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 entry]
Incumbent position at chasm: [still dominant / weakening / differentiated]
```

```
PHASE 3 COMPLIANCE LEDGER
C-03 (Gap element names specific EA and EM roles): [PASS / FAIL]
C-03 (Cause element names specific advantage of THE INCUMBENT — non-generic): [PASS / FAIL]
C-03 (Risk element states what is at risk if chasm is not bridged): [PASS / FAIL]
C-11 (THE INCUMBENT named in Cause element): [PASS / FAIL]
C-12 (Champion element cites a CHAMPION FORMATION EVENT role with mechanism): [PASS / FAIL]
V-02 (Gravity cluster row filled with specific roles and gravity reasoning): [PASS / FAIL]

If any item is FAIL: correct the PHASE 3 table before writing PHASE 4.
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Churn risk?: [role + gravity score + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** — if a new champion emerges this phase (bridging EM toward LM),
record it. If no new champion: "No new champion this phase."

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm M5-M6 committed roles appeared or explain — cite gravity where applicable]
Incumbent position: [retreating / residual / eliminated in this cohort]
```

```
PHASE 4 COMPLIANCE LEDGER
C-05 (Churn risk noted in Month 5 cumulative block with THE INCUMBENT cited): [PASS / FAIL / N/A]
C-14 (CHAMPION FORMATION EVENT for LM bridge fired or "No new champion" written): [PASS / FAIL]
C-16a (Month 5 block opened with "Roles committed to M5:"): [PASS / FAIL]
C-16b (Month 6 block opened with "Roles committed to M6:"): [PASS / FAIL]
C-16c (PHASE 4 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
V-02 (Churn risk row includes gravity score): [PASS / FAIL / N/A]

If any item is FAIL: correct the upstream content before writing PHASE 5.
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Non-adopters (if any): [roles; gravity score; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

Reconcile your committed schedule against actual outcomes. Cite gravity score and THE INCUMBENT
in deviation reasons where applicable.

| Role | Gravity | Committed month | Actual month | Status |
|------|---------|----------------|-------------|--------|
| PM | | | | On schedule / Delayed [N months] — gravity [G]: [reason citing THE INCUMBENT if applicable] / Non-adopter |
| UX | | | | |
| C-01 | | | | |
| C-02 | | | | |
| C-03 | | | | |
| C-04 | | | | |
| C-05 | | | | |
| C-06 | | | | |
| C-07 | | | | |
| C-08 | | | | |
| C-09 | | | | |
| C-10 | | | | |
| C-11 | | | | |
| C-12 | | | | |
| Support | | | | |
| SRE | | | | |

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list with gravity scores and THE INCUMBENT citations where applicable]
Non-adopters: [list with gravity scores]
Gravity accuracy check: [did high-gravity roles (4-5) cluster in later months as predicted?]
```

```
PHASE 5 COMPLIANCE LEDGER
C-16d (SCHEDULE RECONCILIATION table present with all 16 roles): [PASS / FAIL]
C-16e (Every deviation row in SCHEDULE RECONCILIATION includes a named reason): [PASS / FAIL]
C-16f (SECTION 1 uses "Committed adoption month" label — not "Earliest adoption month"): [PASS / FAIL]
C-07 (PHASE 5 CLOSE includes final adopter count and %): [PASS / FAIL]
C-11 (Non-adopter reason cites THE INCUMBENT where applicable): [PASS / FAIL]
V-02 (Gravity accuracy check present in SCHEDULE RECONCILIATION RESULT): [PASS / FAIL]

If any item is FAIL: correct before writing TRACEABILITY AUDIT.
```

---

### TRACEABILITY AUDIT

Complete before the THREE-AXIS GAP AUDIT. Independent structural check.

**Row Citation format:** `[PHASE N / Month M / Row K]` or `[PHASE N / Month M / CHAMPION FORMATION EVENT]`.
Generic citations fail. Non-adopters cite `[PHASE 5 CLOSE / non-adopter list]`.

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
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

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS] / [FAIL — missing or generic citations: list roles]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies: list]
```

---

### THREE-AXIS GAP AUDIT

#### Axis A — Role Completeness

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

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A (role completeness):    [PASS — all 16 traced] / [FAIL — missing: list]
Axis B (temporal completeness):[PASS — all events pinned] / [FAIL — unpinned: list]
Axis C (causal specificity):   [PASS — all named, incumbent cited] / [FAIL — generic: list]
```

If any axis fails: correct the upstream phases before continuing to SECTION 3.

---

### SECTION 3 — Champion Network

**Derivation rule:** Every champion row must have a corresponding CHAMPION FORMATION EVENT in
the simulation body. Record formation phase and month.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

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

Minimum 2 entries.

| Role | Archetype | Gravity | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|---------|--------------|---------------|----------------------|
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |

---

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Cross-check against TRACEABILITY AUDIT and SCHEDULE RECONCILIATION.
Explain non-adopting roles and whether THE INCUMBENT permanently retains them.
