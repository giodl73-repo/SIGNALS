# listen-adoption — R8 Variations (V-01 through V-05)

---

## V-01 — Role Sequence Axis

**Variation axis:** Archetype-first role grouping — roles are sorted into Rogers buckets before any timeline work begins, then referenced by bucket throughout the phase structure.

**Hypothesis:** Pre-grouping eliminates the risk that the model "discovers" archetype membership during timeline generation and produces inconsistent assignments. Sorting first means each phase section can reference its archetype group directly rather than redeciding membership mid-output.

---

```
You are simulating the adoption curve for: {{topic}}

WORK IN ORDER. Complete each section before starting the next.

---

## SECTION 1 — ARCHETYPE ASSIGNMENT

Map all 16 stock roles to exactly one Rogers archetype.

Stock roles (all must appear): PM, UX, C-01, C-02, C-03, C-04, C-05, C-06,
C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Archetype definitions:
- INNOVATOR: seeks novelty before evidence exists; tolerates failure; drives first contact
- EARLY ADOPTER: evaluates fit; becomes internal champion when value confirmed
- EARLY MAJORITY: requires peer proof; adopts when risk feels normalized by colleagues
- LATE MAJORITY: skeptical; moves only after majority normalization or mandate
- LAGGARD: structural resister; adopts last or not at all

Output format — one row per role, no role omitted:

| Role | Archetype | One-sentence rationale |
|------|-----------|------------------------|
| PM   |           |                        |
| UX   |           |                        |
| C-01 |           |                        |
...continue for all 16 roles...

---

## SECTION 2 — ADOPTION PHASES

Use the archetype assignments from Section 1. Phases must appear in this
exact order. Each phase header is a structural gate — you cannot write
PHASE 4 content without first completing PHASE 3.

### PHASE 1 (INNOVATORS)

Time window: Months 1–2
Roles in this phase: [paste roles assigned INNOVATOR from Section 1]

For each INNOVATOR role:
- First contact event: what specific action they take with {{topic}}
- Signal they generate: what observable behavior signals their adoption
- Failure mode: what would cause them to abandon in Month 1–2

### PHASE 2 (EARLY ADOPTERS)

Time window: Months 2–4
Roles in this phase: [paste roles assigned EARLY ADOPTER from Section 1]

For each EARLY ADOPTER role:
- Evidence required from PHASE 1: what innovator signal do they wait for
- Champion activation: what converts them from evaluator to internal advocate
- Spread mechanism: how they share adoption with peers

### PHASE 3 (CHASM)

Time window: Months 4–6
This is a non-adoption interstitial. No new roles adopt in this phase.
Use this phase to diagnose the structural gap.

Chasm drivers (list exactly 5):
1. [structural reason adoption stalls]
2.
3.
4.
5.

Bridge conditions (list exactly 3 — what must be true before PHASE 4 can begin):
1.
2.
3.

Chasm severity rating: LOW / MEDIUM / HIGH
Rationale for rating:

### PHASE 4 (EARLY MAJORITY)

Time window: Months 6–9
Roles in this phase: [paste roles assigned EARLY MAJORITY from Section 1]

For each EARLY MAJORITY role:
- Peer proof waited for: which PHASE 2 role's advocacy moved them
- Proof format: case study / metric / mandate / default-on / other
- Remaining friction: what slows their adoption even after crossing

### PHASE 5 (LATE MAJORITY)

Time window: Months 9–15
Roles in this phase: [paste roles assigned LATE MAJORITY from Section 1]

For each LATE MAJORITY role:
- Normalization event: what single event tipped adoption
- Mandate dependency: YES/NO — does this role require top-down mandate
- Churn risk if mandate absent: HIGH / MEDIUM / LOW

### PHASE 6 (LAGGARDS)

Time window: Month 15+
Roles in this phase: [paste roles assigned LAGGARD from Section 1]

For each LAGGARD role:
- Conversion path (if any): what single intervention could convert them
- Permanent churn risk: YES/NO
- Adoption delta if lost: what % of total adoption is lost if this role never adopts

---

## SECTION 3 — CHAMPION NETWORK

List the 3 roles most critical for crossing from PHASE 2 to PHASE 4.
For each:

**Champion: [role name]**
Archetype: [from Section 1]
Bridge leverage: [why this role's advocacy unlocks EARLY MAJORITY]
Activation condition: [one specific action that activates them]
Risk if absent: [what stalls if this champion does not emerge]

---

## SECTION 4 — INTERVENTIONS

List 5 interventions ranked by adoption delta, largest delta first.

| Rank | Intervention | Target Roles | Delta (% pts) | Effort | Timing |
|------|-------------|--------------|---------------|--------|--------|

---

## SECTION K — AUDIT GATE

Before writing SECTION K, re-read Sections 1–4. Mark each criterion.

| # | Criterion | Gate State (Pass/Fail) | CORRECTION BLOCK Location |
|---|-----------|----------------------|--------------------------|
| 1 | All 16 stock roles present in Section 1 table | | |
| 2 | Each role assigned exactly one archetype | | |
| 3 | Rogers sequence not inverted across Phase 1–6 headers | | |
| 4 | PHASE 3 present as non-adoption interstitial (no roles adopt) | | |
| 5 | Five chasm drivers and three bridge conditions present | | |
| 6 | Champion network covers at least 3 roles | | |
| 7 | Interventions ranked by adoption delta with explicit delta values | | |

For every row where Gate State = Fail, write a CORRECTION BLOCK immediately
after this table:

**CORRECTION BLOCK — Criterion [#]**
BEFORE: [verbatim quote of the failing passage]
AFTER: [corrected version]

**SECTION K INVARIANT:** Every row with Gate State = Fail must have a
CORRECTION BLOCK below this table containing a BEFORE field with a verbatim
quote of the failing content. Failure mode: a Fail row whose CORRECTION BLOCK
Location references a section that contains no CORRECTION BLOCK, or a
CORRECTION BLOCK that contains no BEFORE field, falsifies this invariant.
```

---

## V-02 — Output Format Axis

**Variation axis:** Table-heavy with numeric adoption scoring — every role gets a readiness score (0–10) at each phase, making the chasm gap visible as a numeric drop in the aggregate score.

**Hypothesis:** Quantified readiness scores per role per phase force the model to commit to a specific adoption gradient rather than hedging with prose. The chasm becomes measurable as the phase where aggregate readiness drops instead of rising.

---

```
You are simulating the adoption curve for: {{topic}}

Produce a fully quantified adoption simulation. Every role receives a
readiness score (0–10) at each phase. The chasm is the phase where
aggregate readiness fails to increase. All outputs are tabular.

---

## TABLE 1 — ROLE ARCHETYPE MAPPING

Assign each of the 16 stock roles to exactly one Rogers archetype.
Include a readiness baseline score (0–10) representing this role's
pre-adoption state for {{topic}}.

| Role | Rogers Archetype | Baseline Readiness (0–10) | Adoption Driver | Adoption Blocker |
|------|-----------------|--------------------------|-----------------|-----------------|
| PM | | | | |
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

All 16 rows must be populated. No role may be omitted.

---

## TABLE 2 — PHASE READINESS MATRIX

Score each role's readiness (0–10) at the close of each adoption phase.
A score of 7+ indicates active adoption. A score below 4 indicates
resistance or non-adoption. The CHASM phase must show aggregate
readiness stagnating or declining relative to PHASE 2.

Phases must appear in this exact order as column headers:

| Role | Archetype | PHASE 1 INNOVATORS (M1–2) | PHASE 2 EARLY ADOPTERS (M2–4) | PHASE 3 CHASM (M4–6) | PHASE 4 EARLY MAJORITY (M6–9) | PHASE 5 LATE MAJORITY (M9–15) | PHASE 6 LAGGARDS (M15+) |
|------|-----------|--------------------------|-------------------------------|----------------------|-------------------------------|-------------------------------|------------------------|
| PM | | | | | | | |
| UX | | | | | | | |
| C-01 | | | | | | | |
| C-02 | | | | | | | |
| C-03 | | | | | | | |
| C-04 | | | | | | | |
| C-05 | | | | | | | |
| C-06 | | | | | | | |
| C-07 | | | | | | | |
| C-08 | | | | | | | |
| C-09 | | | | | | | |
| C-10 | | | | | | | |
| C-11 | | | | | | | |
| C-12 | | | | | | | |
| Support | | | | | | | |
| SRE | | | | | | | |
| **AGGREGATE** | — | | | | | | |

PHASE 3 (CHASM) rule: the AGGREGATE row for PHASE 3 must be <= PHASE 2
aggregate. If it is higher, a chasm did not occur — re-examine archetype
assignments and lower scores for roles that have not yet received peer proof.

---

## TABLE 3 — CHASM DIAGNOSTIC

Complete this table for PHASE 3:

| Dimension | Value |
|-----------|-------|
| Chasm start month | |
| Chasm end month | |
| Aggregate readiness at PHASE 2 close | |
| Aggregate readiness at PHASE 3 close | |
| Delta (must be <= 0) | |
| Primary chasm driver | |
| Secondary chasm driver | |
| Minimum bridge condition | |
| Champion role most critical for crossing | |
| Estimated months to cross if bridge condition met | |

---

## TABLE 4 — CHAMPION NETWORK

| Champion Role | Archetype | Bridge Leverage | Activation Condition | Adoption Delta if Activated (pts) |
|--------------|-----------|-----------------|---------------------|----------------------------------|

List the 3–5 roles whose activation would produce the highest adoption
delta. Rank by adoption delta, highest first.

---

## TABLE 5 — CHURN RISK REGISTER

| Role | Archetype | Churn Risk (H/M/L) | Churn Driver | Adoption Delta if Lost (pts) | Recovery Intervention |
|------|-----------|-------------------|--------------|-----------------------------|-----------------------|

Include all roles with churn risk MEDIUM or higher.

---

## TABLE 6 — INTERVENTION RANKING

| Rank | Intervention | Target Roles | Delta (pts) | Effort (1–5) | Timing | ROI Score (Delta/Effort) |
|------|-------------|--------------|-------------|--------------|--------|--------------------------|

List exactly 5 interventions. Rank by ROI Score (delta/effort), highest first.

---

## SECTION K — AUDIT GATE

Re-read all tables. Mark each criterion.

| # | Criterion | Gate State (Pass/Fail) | CORRECTION BLOCK Location |
|---|-----------|----------------------|--------------------------|
| 1 | TABLE 1 contains all 16 stock roles, no omissions | | |
| 2 | Each role in TABLE 1 maps to exactly one Rogers archetype | | |
| 3 | TABLE 2 phase columns appear in Rogers order (P1 before P2 before P4 before P5 before P6, with P3 as chasm between P2 and P4) | | |
| 4 | PHASE 3 AGGREGATE score in TABLE 2 is <= PHASE 2 AGGREGATE score | | |
| 5 | TABLE 3 chasm diagnostic delta is <= 0 | | |
| 6 | TABLE 6 interventions ranked by ROI Score with explicit values | | |

For any Fail row, write a CORRECTION BLOCK immediately after this table:

**CORRECTION BLOCK — Criterion [#]**
BEFORE: [verbatim quote of the failing cell or row]
AFTER: [corrected version]

**SECTION K INVARIANT:** Every Fail row must have a CORRECTION BLOCK
following this section. The CORRECTION BLOCK must contain a BEFORE field
quoting the failing content verbatim. Failure mode: a Fail row whose
CORRECTION BLOCK Location points to a section that contains no CORRECTION
BLOCK, or whose CORRECTION BLOCK omits the BEFORE field, falsifies this
invariant. An evaluator can confirm this invariant by finding a BEFORE
field for every Fail row, or refute it by finding any Fail row whose
referenced section is empty or whose CORRECTION BLOCK lacks a BEFORE field.
```

---

## V-03 — Lifecycle Emphasis Axis

**Variation axis:** Maximum space per phase — each phase gets a full narrative block with explicit entry criteria, in-phase events, and exit criteria. Transitions between phases are named and gated.

**Hypothesis:** Explicit entry/exit criteria per phase prevent the model from collapsing phases or skipping the chasm. When a phase must state what enables its entry and what enables its exit, the ordering becomes self-enforcing through content rather than header position alone.

---

```
You are simulating the full adoption lifecycle for: {{topic}}

This simulation runs six phases in fixed sequence. Each phase has an
ENTRY GATE (what must be true for this phase to begin), a PHASE BODY
(what happens during this phase), and an EXIT GATE (what must be true
for this phase to close and the next to open). Phases are not
simultaneous — each closes before the next opens.

---

## PRELIMINARY — ROLE ASSIGNMENTS

Before the phase simulation, assign all 16 stock roles to Rogers archetypes.

Stock roles: PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08,
C-09, C-10, C-11, C-12, Support, SRE

Archetype definitions for this simulation:
- INNOVATOR: adopts before proof exists; motivated by novelty and access
- EARLY ADOPTER: adopts after first-contact signal; motivated by competitive advantage
- EARLY MAJORITY: adopts after peer adoption; motivated by risk reduction
- LATE MAJORITY: adopts after majority normalization; motivated by compliance or mandate
- LAGGARD: adopts last or not at all; motivated primarily by external pressure

| Role | Archetype | Primary motivation | Blocking belief (what they currently believe that prevents adoption) |
|------|-----------|-------------------|----------------------------------------------------------------------|
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

### PHASE 1 (INNOVATORS)

**Time window:** Month 1 – Month 2

**ENTRY GATE**
Precondition: {{topic}} is available for first contact. No adoption history
exists yet. Innovator roles are self-motivated; no signal from others required.

**PHASE BODY**

Roles active in this phase: [list all roles assigned INNOVATOR]

For each active role, describe:
1. First contact event — what specific action initiates their engagement
2. Exploration pattern — what they try, what they stress-test
3. Early signal generated — what observable behavior indicates adoption
4. Internal broadcast — how they communicate findings to the rest of the team

Ecosystem state at phase close:
- Number of adopted roles: [count]
- Quality of evidence in circulation: [qualitative description]
- Visibility of adoption to non-innovators: [high/medium/low — with rationale]

**EXIT GATE**
This phase closes when: at least one innovator role has generated a
public signal (shared finding, demo, written note) that early-adopter
roles can observe. If no signal has been generated, PHASE 2 cannot open.

---

### PHASE 2 (EARLY ADOPTERS)

**Time window:** Month 2 – Month 4

**ENTRY GATE**
Precondition: at least one innovator-generated signal is observable by
early-adopter roles. The signal must be specific enough to evaluate
(not just "someone is using it").

**PHASE BODY**

Roles active in this phase: [list all roles assigned EARLY ADOPTER]

For each active role, describe:
1. Signal observed from PHASE 1 — which innovator role's output they watched
2. Evaluation criteria — what they checked before committing
3. Champion emergence — what event converted them from evaluator to advocate
4. Network effect — who they actively pulled toward adoption

Champion network forming in this phase:
- List the 2–3 roles whose PHASE 2 advocacy will determine PHASE 3 bridge viability
- For each: describe their specific bridge behavior

Ecosystem state at phase close:
- Cumulative adopted roles: [count]
- Peer pressure level for non-adopters: [high/medium/low]
- Evidence quality available to early majority: [qualitative description]

**EXIT GATE**
This phase closes when: early-adopter champions have produced peer-facing
artifacts (case studies, metrics, live demos) that early-majority roles
could use to justify adoption. If no peer-facing artifacts exist, the
CHASM phase will deepen.

---

### PHASE 3 (CHASM)

**Time window:** Month 4 – Month 6

**THIS IS A NON-ADOPTION PHASE.** No new roles adopt during PHASE 3.
The chasm is the structural gap between early-adopter enthusiasm and
early-majority caution. It is not a delay — it is a category difference
in what constitutes sufficient proof.

**ENTRY GATE**
Precondition: PHASE 2 has closed. Early-adopter artifacts exist.
Early-majority roles are observing but not yet moving.

**CHASM DIAGNOSIS**

Chasm type: [pragmatist gap / risk aversion / missing reference customer /
workflow incompatibility / org resistance — choose the dominant type]

Structural drivers (list exactly 5 — each must name a specific role
or role class and what belief or condition is holding them back):
1.
2.
3.
4.
5.

Missing bridge elements (what early majority needs but early adopters
did not produce):
- Missing proof type 1:
- Missing proof type 2:
- Missing social proof:

Chasm severity: LOW / MEDIUM / HIGH
Rationale:

**EXIT GATE**
PHASE 3 closes only when all three bridge conditions are met:
1. At least one early-majority-adjacent role has made public contact with {{topic}}
2. At least one case study from a pragmatist-language reference role exists
3. At least one champion from PHASE 2 has directly sponsored an early-majority role

If any bridge condition is unmet, PHASE 3 persists.

---

### PHASE 4 (EARLY MAJORITY)

**Time window:** Month 6 – Month 9

**ENTRY GATE**
Precondition: all three PHASE 3 bridge conditions have been met.
Early-majority roles require pragmatist-language proof, not visionary
enthusiasm.

**PHASE BODY**

Roles active in this phase: [list all roles assigned EARLY MAJORITY]

For each active role, describe:
1. Peer signal that unlocked them — which PHASE 2 champion's evidence they acted on
2. Adoption modality — how they adopt (gradual rollout / single switch / team-wide / piloted)
3. Remaining friction — what still slows them despite crossing
4. Normalization contribution — how their adoption signals the late majority

Ecosystem state at phase close:
- Cumulative adopted roles: [count]
- Adoption visibility across the team: [high/medium/low]
- Late majority awareness: [what they have now seen that they hadn't before]

**EXIT GATE**
This phase closes when: more than half of early-majority roles have
adopted and at least one has produced a visible normalization signal
(routine use, team process integration, public metric).

---

### PHASE 5 (LATE MAJORITY)

**Time window:** Month 9 – Month 15

**ENTRY GATE**
Precondition: PHASE 4 exit gate met. Late majority can see majority
normalization and are now at risk of being visibly behind peers.

**PHASE BODY**

Roles active in this phase: [list all roles assigned LATE MAJORITY]

For each active role, describe:
1. Normalization event that triggered them — what they saw that made non-adoption feel risky
2. Mandate dependency — YES/NO: did this role require a top-down mandate to move
3. Adoption quality — shallow compliance / genuine adoption / partial adoption
4. Churn risk if mandate is later rescinded: HIGH / MEDIUM / LOW

**EXIT GATE**
This phase closes when: all late-majority roles have made at least first
contact and at least one has completed a full adoption cycle.

---

### PHASE 6 (LAGGARDS)

**Time window:** Month 15+

**ENTRY GATE**
Precondition: PHASE 5 exit gate met. Laggards now represent the minority
of non-adopters.

**PHASE BODY**

Roles active in this phase: [list all roles assigned LAGGARD]

For each active role, describe:
1. Resistance mechanism — structural belief, workflow dependency, or identity issue
2. Conversion path (if any) — what single intervention could convert them
3. Conversion probability: HIGH / MEDIUM / LOW / NONE
4. Permanent churn risk: YES / NO
5. Adoption delta impact if permanently lost: [% of total adoption lost]

**EXIT GATE**
This phase closes when: all convertible laggards have adopted or been
classified as permanent churn risk. Permanent churn risks are documented
and accepted, not pursued.

---

## INTERVENTION RANKING

List 5 interventions ranked by adoption delta (highest first).

| Rank | Intervention | Phase Target | Roles Affected | Delta (% pts) | Effort (1–5) | Timing |
|------|-------------|--------------|----------------|---------------|--------------|--------|

---

## SECTION K — AUDIT GATE

Re-read the preliminary role assignments and all six phases. Mark each criterion.

| # | Criterion | Gate State (Pass/Fail) | CORRECTION BLOCK Location |
|---|-----------|----------------------|--------------------------|
| 1 | All 16 stock roles present in PRELIMINARY table | | |
| 2 | Each role maps to exactly one archetype | | |
| 3 | Phases appear in sequence: P1, P2, P3, P4, P5, P6 — no inversion | | |
| 4 | PHASE 3 contains no adopting roles (non-adoption interstitial) | | |
| 5 | Each phase contains ENTRY GATE, PHASE BODY, and EXIT GATE | | |
| 6 | Five structural chasm drivers present in PHASE 3 | | |
| 7 | Interventions ranked by adoption delta with explicit delta values | | |

For any Fail row, write a CORRECTION BLOCK immediately after this table:

**CORRECTION BLOCK — Criterion [#]**
BEFORE: [verbatim quote of the failing content]
AFTER: [corrected version]

**SECTION K INVARIANT:** Every row with Gate State = Fail must have a
CORRECTION BLOCK following this section. The CORRECTION BLOCK must
contain a BEFORE field with a verbatim quote of the failing content.
Failure mode: a Fail row whose CORRECTION BLOCK Location cites a section
that contains no CORRECTION BLOCK, or whose CORRECTION BLOCK is present
but omits the BEFORE field, falsifies this invariant.
```

---

## V-04 — Phrasing Register + Inertia Framing Axes

**Variation axis:** Conversational register + status-quo competitor framing — the prompt names the current workflow {{topic}} is displacing and foregrounds resistance as the primary analytical object throughout.

**Hypothesis:** Naming the status-quo competitor (the thing people are *currently* doing that {{topic}} must displace) surfaces role-specific resistance drivers that neutral framing misses. Conversational register reduces hedge-language in rationale fields.

---

```
You are mapping how a team actually moves — or doesn't — when {{topic}}
lands in their workflow.

Before we get to who adopts, we need to name what {{topic}} is replacing.
Every role on this team is already doing something. That something has
inertia. The adoption story is really the displacement story.

---

## PART 1 — WHO THEY ARE AND WHAT THEY'RE PROTECTING

Name the current workflow or tool that {{topic}} displaces for this team.
Call it THE INCUMBENT.

THE INCUMBENT: [name it — one phrase]

Now map all 16 stock roles. For each role, name:
- their Rogers archetype (one of: Innovator, Early Adopter, Early Majority,
  Late Majority, Laggard)
- what they currently do with THE INCUMBENT that they'd have to give up
- the specific belief that makes giving it up feel risky

Work through every role. No role may be skipped.

| Role | Archetype | What they do with THE INCUMBENT | Belief that creates inertia |
|------|-----------|--------------------------------|----------------------------|
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

## PART 2 — THE PHASES (WITH DISPLACEMENT AS LENS)

Walk through six phases in this order. Each phase must appear as a named
header. PHASE 3 is the chasm — no one new adopts during it.

### PHASE 1 (INNOVATORS)

Months 1–2. These are the people who will try {{topic}} before anyone
asks them to.

For each INNOVATOR role from Part 1:
- What specifically pulls them away from THE INCUMBENT this early?
- What do they do with {{topic}} in Month 1 that they couldn't do before?
- What do they tell their colleagues, and how do colleagues react?

Be specific about the colleague reaction. The reaction determines whether
PHASE 2 opens on schedule or stalls.

### PHASE 2 (EARLY ADOPTERS)

Months 2–4. These are the people who were watching. They've seen the
INNOVATORS do something interesting and they're deciding whether it's
worth disrupting their current setup.

For each EARLY ADOPTER role from Part 1:
- What specific thing from PHASE 1 caught their attention?
- What does "evaluating" look like for this role — what are they actually
  checking, and against what standard?
- What is the moment they switch? Name it concretely.
- How does their adoption change what THE INCUMBENT looks like to people
  who haven't switched yet?

After covering all early adopters, describe the champion network forming:
which 3 roles are now most actively pulling others toward {{topic}}?

### PHASE 3 (CHASM)

Months 4–6. The early adopters are in. The early majority is watching.
Nobody new is moving. This is not a delay — it's a different kind of
resistance.

Early adopters are enthusiastic. The early majority is pragmatic. They're
not impressed by enthusiasm. They need to know that switching from THE
INCUMBENT is safe, proven, and reversible if it doesn't work.

What the early majority roles from Part 1 currently believe:
- About {{topic}}: [their specific belief]
- About THE INCUMBENT: [why it still feels safer]
- About the early adopters: [why they're not convinced by their advocacy]

What needs to change for PHASE 4 to open (list exactly 3 bridge conditions):
1.
2.
3.

What happens if the chasm isn't crossed by Month 8:
- Reversion risk: could THE INCUMBENT win back even the early adopters?
- Stall pattern: does adoption plateau here permanently or just delay?

### PHASE 4 (EARLY MAJORITY)

Months 6–9. The bridge conditions from PHASE 3 were met. Now the pragmatists
are moving.

For each EARLY MAJORITY role from Part 1:
- Which bridge condition landed for them specifically?
- What does their adoption look like — do they switch fully, partially, or
  in a specific use-case slice?
- What's the first sign they're genuinely adopted vs. compliance-adopting?
- What does their adoption do to THE INCUMBENT's perceived legitimacy on
  the team?

### PHASE 5 (LATE MAJORITY)

Months 9–15. The team is now majority-on {{topic}}. The late majority
can see that THE INCUMBENT is becoming the exception.

For each LATE MAJORITY role from Part 1:
- What made THE INCUMBENT feel unsafe to stick with?
- Is their adoption driven by peer pressure, mandate, or genuine conviction?
- How sticky is their adoption? Would they revert to THE INCUMBENT if given
  a clean exit?

### PHASE 6 (LAGGARDS)

Month 15+. A small number of roles are still on THE INCUMBENT. They know
they're outliers. They're staying anyway.

For each LAGGARD role from Part 1:
- What's actually keeping them on THE INCUMBENT at this point?
- Is it structural (workflow dependency), political (team dynamics), or
  identity (this is how we do things)?
- What's the single thing that could move them — and how realistic is it?
- If they never adopt, what does the team lose?

---

## PART 3 — CHURN RISK REGISTER

Some roles may revert to THE INCUMBENT even after initial adoption.
These are not laggards — they tried {{topic}} and are at risk of pulling back.

Identify all roles with reversion risk (from any phase). For each:

**Role: [name]**
Archetype: [from Part 1]
Reversion trigger: [what specific event would send them back to THE INCUMBENT]
Reversion probability: HIGH / MEDIUM / LOW
Impact if they revert: [how does their reversion affect others on the team]
Retention intervention: [one concrete action that reduces reversion probability]

---

## PART 4 — INTERVENTION RANKING

Rank 5 interventions that would increase total adoption.
For each, say what it does to THE INCUMBENT's position — does it
weaken the incumbent, strengthen {{topic}}, or both?

| Rank | Intervention | Primary effect on THE INCUMBENT | Target roles | Delta (% pts) | Effort | Timing |
|------|-------------|--------------------------------|--------------|---------------|--------|--------|

---

## SECTION K — AUDIT GATE

Check the output you just produced.

| # | Criterion | Gate State (Pass/Fail) | CORRECTION BLOCK Location |
|---|-----------|----------------------|--------------------------|
| 1 | All 16 stock roles in Part 1 table | | |
| 2 | Each role has exactly one archetype | | |
| 3 | Phases 1–6 appear in Rogers sequence with Phase 3 as non-adoption chasm | | |
| 4 | Phase 3 explicitly states no new roles adopt | | |
| 5 | Three bridge conditions listed in Phase 3 | | |
| 6 | THE INCUMBENT named and referenced consistently | | |
| 7 | Interventions ranked by adoption delta | | |

For any Fail row, write a CORRECTION BLOCK immediately after this table:

**CORRECTION BLOCK — Criterion [#]**
BEFORE: [verbatim quote of the failing content]
AFTER: [corrected version]

**SECTION K INVARIANT:** Every Fail row must be followed by a CORRECTION
BLOCK with a BEFORE field containing a verbatim quote of the failing
content. Failure mode: a Fail row whose CORRECTION BLOCK Location cites
a section with no CORRECTION BLOCK present, or a CORRECTION BLOCK
present but missing its BEFORE field, falsifies this invariant. Confirm
by finding a non-empty BEFORE field for every Fail row; refute by finding
any Fail row whose referenced section is empty or whose CORRECTION BLOCK
omits BEFORE.
```

---

## V-05 — Combined: Role Sequence + Phase Architecture + Falsification Enforcement

**Variation axes:** Archetype-first role sequence (V-01) + named phase headers as structural lock (V-03) + explicit falsification invariant in audit gate (new combined emphasis).

**Hypothesis:** Combining pre-sorted archetype groups with named phase headers that architecturally reference those groups makes it impossible to write a later phase without completing the prior phase header. The falsification invariant is made maximally explicit, naming both confirmation path (finding a BEFORE field for every Fail row) and refutation path (finding any Fail row with a missing CORRECTION BLOCK or missing BEFORE field).

---

```
You are running an adoption simulation for: {{topic}}

This prompt has two locked sequences. First: archetype grouping (BLOCK A).
Second: six named phases that reference BLOCK A groups by name (BLOCK B).
You cannot write BLOCK B without completing BLOCK A. You cannot write
PHASE 4 without writing PHASE 3. The structure enforces Rogers ordering.

---

## BLOCK A — ARCHETYPE GROUPS

Map all 16 stock roles into Rogers archetype groups.
Each role belongs to exactly one group. No role may be omitted.

Stock roles: PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07,
C-08, C-09, C-10, C-11, C-12, Support, SRE

### GROUP 1 — INNOVATORS
[List every role assigned to this group]
For each role: [role name] — [one-sentence adoption driver]

### GROUP 2 — EARLY ADOPTERS
[List every role assigned to this group]
For each role: [role name] — [one-sentence adoption driver]

### GROUP 3 — EARLY MAJORITY
[List every role assigned to this group]
For each role: [role name] — [one-sentence adoption driver]

### GROUP 4 — LATE MAJORITY
[List every role assigned to this group]
For each role: [role name] — [one-sentence adoption driver]

### GROUP 5 — LAGGARDS
[List every role assigned to this group]
For each role: [role name] — [one-sentence adoption driver]

BLOCK A COMPLETENESS CHECK (before proceeding to BLOCK B):
Count roles assigned: GROUP 1 [n] + GROUP 2 [n] + GROUP 3 [n] +
GROUP 4 [n] + GROUP 5 [n] = [total]. Total must equal 16.
If total != 16, find the missing roles and assign them before continuing.

---

## BLOCK B — PHASE SIMULATION

Reference BLOCK A groups by name. Each phase header is a structural
gate — writing PHASE 2 requires PHASE 1 to be complete. PHASE 3 is
a non-adoption interstitial. Writing PHASE 4 requires PHASE 3 to be
complete and its bridge conditions to be stated.

### PHASE 1 (INNOVATORS)

Roles: GROUP 1 from BLOCK A (paste role names here)
Time window: Month 1–2

For each GROUP 1 role:
- **First contact event:** [what they do with {{topic}} in Month 1]
- **Signal generated:** [what observable output indicates adoption]
- **Propagation:** [what they share with GROUP 2 and how]

Phase close state:
- Roles adopted: [count]
- Signal quality available to GROUP 2: [strong / moderate / weak]
- Reason PHASE 2 can now open: [one sentence]

### PHASE 2 (EARLY ADOPTERS)

Roles: GROUP 2 from BLOCK A (paste role names here)
Time window: Month 2–4

Entry condition: at least one GROUP 1 role has generated an observable
signal that GROUP 2 roles can evaluate. If no signal exists from PHASE 1,
state this explicitly and do not proceed to PHASE 2 narrative.

For each GROUP 2 role:
- **Signal observed from PHASE 1:** [which role's signal; what it showed]
- **Evaluation standard:** [what this role checks before committing]
- **Champion activation:** [what event converted them to advocate]
- **Bridge artifact produced:** [what they created that GROUP 3 could use]

Champion network:
Name the 2–3 GROUP 2 roles whose bridge artifacts are most critical for
crossing the chasm. For each: why their specific artifact format works
for GROUP 3 where GROUP 1 signals did not.

Phase close state:
- Cumulative roles adopted: [count]
- Bridge artifact quality: [strong / moderate / weak]
- Reason PHASE 3 applies: [why GROUP 3 has not moved despite artifacts]

### PHASE 3 (CHASM)

**NON-ADOPTION PHASE.** No roles from any group adopt during PHASE 3.
The chasm is not a scheduling gap — it is a structural category
difference between what counts as proof for GROUP 2 versus GROUP 3.

Time window: Month 4–6

Chasm type: [pragmatist gap / risk aversion / missing reference persona /
workflow incompatibility / political resistance — choose one dominant type]

Why GROUP 2 artifacts did not cross:
[Explain specifically why the bridge artifacts from PHASE 2 were
insufficient for GROUP 3. Reference the GROUP 3 role list from BLOCK A.]

Structural chasm drivers (exactly 5):
1.
2.
3.
4.
5.

Bridge conditions — all three must be satisfied before PHASE 4 opens:
**BC-1:** [specific condition]
**BC-2:** [specific condition]
**BC-3:** [specific condition]

Responsible roles for bridge building:
| Bridge Condition | Responsible Role | Action Required | Deadline |
|-----------------|-----------------|-----------------|----------|
| BC-1 | | | |
| BC-2 | | | |
| BC-3 | | | |

Phase close condition: BC-1 AND BC-2 AND BC-3 must be marked MET before
PHASE 4 begins.

BC-1: MET / UNMET
BC-2: MET / UNMET
BC-3: MET / UNMET

### PHASE 4 (EARLY MAJORITY)

Roles: GROUP 3 from BLOCK A (paste role names here)
Time window: Month 6–9

Entry condition: all three bridge conditions from PHASE 3 are MET.
If any is UNMET, state this and hold PHASE 4 until conditions are met.

For each GROUP 3 role:
- **BC that unlocked them:** [which bridge condition landed for this role]
- **Adoption modality:** [full / partial / use-case slice / compliance]
- **Normalization signal:** [how their adoption signals GROUP 4]

Phase close state:
- Cumulative roles adopted: [count]
- Majority threshold reached: YES / NO (majority = >50% of all 16 roles)
- Signal strength for GROUP 4: [strong / moderate / weak]

### PHASE 5 (LATE MAJORITY)

Roles: GROUP 4 from BLOCK A (paste role names here)
Time window: Month 9–15

Entry condition: majority threshold reached in PHASE 4 (>50% of 16
roles adopted). If threshold not reached, GROUP 4 may not move.

For each GROUP 4 role:
- **Normalization event:** [what they saw that made non-adoption feel risky]
- **Mandate required:** YES / NO
- **Adoption quality:** [genuine / compliance / partial]
- **Reversion risk:** HIGH / MEDIUM / LOW

### PHASE 6 (LAGGARDS)

Roles: GROUP 5 from BLOCK A (paste role names here)
Time window: Month 15+

Entry condition: PHASE 5 complete. GROUP 5 roles are now the visible
minority of non-adopters.

For each GROUP 5 role:
- **Resistance mechanism:** [structural / political / identity]
- **Conversion path:** [one specific intervention — or NONE]
- **Permanent churn risk:** YES / NO
- **Adoption delta if lost:** [% of total adoption]

---

## CHAMPION NETWORK SUMMARY

After completing all six phases, synthesize:

| Champion Role | Group | Phase Active | Bridge Contribution | Adoption Delta Enabled (% pts) |
|--------------|-------|-------------|---------------------|-------------------------------|

List roles ranked by adoption delta enabled, highest first.

---

## INTERVENTION RANKING

| Rank | Intervention | Phase Target | Groups Affected | Delta (% pts) | Effort (1–5) | Timing |
|------|-------------|--------------|-----------------|---------------|--------------|--------|

5 interventions, ranked by adoption delta, largest first.

---

## SECTION K — AUDIT GATE

Re-read BLOCK A and BLOCK B before marking any criterion.

| # | Criterion | Gate State (Pass/Fail) | CORRECTION BLOCK Location |
|---|-----------|----------------------|--------------------------|
| 1 | BLOCK A contains all 16 stock roles across all five groups | | |
| 2 | Each role in BLOCK A assigned to exactly one group | | |
| 3 | BLOCK A COMPLETENESS CHECK total = 16 | | |
| 4 | Phase headers appear in Rogers order: P1 INNOVATORS, P2 EARLY ADOPTERS, P3 CHASM, P4 EARLY MAJORITY, P5 LATE MAJORITY, P6 LAGGARDS | | |
| 5 | PHASE 3 explicitly contains no adopting roles | | |
| 6 | All three bridge conditions stated in PHASE 3 with responsible roles | | |
| 7 | PHASE 4 entry condition references PHASE 3 bridge conditions | | |
| 8 | Champion network table present with adoption delta values | | |
| 9 | Interventions ranked by adoption delta with explicit delta values | | |

For every row where Gate State = Fail, write a CORRECTION BLOCK
immediately after this table:

**CORRECTION BLOCK — Criterion [#]**
BEFORE: [verbatim quote of the failing content — do not paraphrase]
AFTER: [corrected version]

**SECTION K INVARIANT:** Every row in SECTION K with Gate State = Fail
must have a corresponding CORRECTION BLOCK following this table. The
CORRECTION BLOCK must contain a BEFORE field with a verbatim quote of
the failing content. This invariant can be confirmed by finding a
non-empty BEFORE field for every Fail row in the table above. It can
be refuted by finding any Fail row whose CORRECTION BLOCK Location
cites a section that contains no CORRECTION BLOCK, or by finding any
CORRECTION BLOCK that is present but omits the BEFORE field entirely.
Failure mode: a Fail row pointing to an empty section, or a CORRECTION
BLOCK with no BEFORE field, falsifies this invariant.
```

---

## Summary

| Variation | Axis | Key Hypothesis | C-24 Mechanism | C-25 Mechanism |
|-----------|------|---------------|----------------|----------------|
| V-01 | Role sequence (archetype-first) | Pre-grouping prevents mid-timeline archetype drift | Explicit BEFORE-field rule + failure mode | PHASE 1–6 headers; PHASE 3 named non-adoption |
| V-02 | Output format (numeric scoring) | Aggregate readiness scores make chasm gap measurable and undeniable | Fail rows trigger CORRECTION BLOCK; BEFORE field required | PHASE 1–6 as column headers in matrix; PHASE 3 aggregate must be <= PHASE 2 |
| V-03 | Lifecycle emphasis (entry/exit gates) | Explicit entry/exit criteria per phase prevent phase collapse and chasm skipping | BEFORE field required in all correction blocks + falsification stated | PHASE 1–6 with full gate structure; PHASE 3 entry/exit cannot be bypassed |
| V-04 | Register + inertia framing (incumbent-first) | Naming THE INCUMBENT foregrounds displacement and surfaces role-specific resistance | Confirm by BEFORE field; refute by absent BEFORE field — both paths stated | PHASE 1–6 headers with PHASE 3 as explicit non-adoption chasm |
| V-05 | Combined: sequence + architecture + falsification | Archetype groups in BLOCK A + phase headers referencing BLOCK A + dual-path invariant = structural impossibility of Rogers inversion | Dual-path invariant: confirm path (BEFORE field present for every Fail) + refute path (missing CORRECTION BLOCK or missing BEFORE) | PHASE 1–6 headers as structural gates; each phase references BLOCK A groups by name |
