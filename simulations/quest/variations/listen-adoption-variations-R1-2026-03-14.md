Written to `simulations/quest/variations/listen-adoption-variations-R1-2026-03-14.md`.

---

## Five variations for `listen-adoption` R1

| ID | Axis | Hypothesis |
|----|------|-----------|
| **V-01** | Output format — table-heavy | Tables for all 5 required outputs prevent rubric criteria from being buried in prose; C-01, C-02, C-04 become mechanically checkable |
| **V-02** | Lifecycle emphasis — chasm-centered | Giving Phase 3 (the chasm) disproportionate space forces feature-specific bridging analysis; generic "find champions" answers won't satisfy C-03/C-05 |
| **V-03** | Phrasing register — narrative/conversational | Story-driven ("tell me who adopts...") produces richer persona reasoning; hypothesis is it improves C-03/C-05 depth at the cost of C-08 scannability |
| **V-04** | Inertia framing + role sequence (combined) | Opening with status-quo as "zeroth archetype," then mapping Laggards first, forces bridging mechanisms to explicitly fight named inertia — improves C-03 specificity and C-04 intervention grounding |
| **V-05** | Format + lifecycle (combined) — GATE checkpoints | Explicit GATE markers between sections pin every rubric criterion to a specific output location; trades flexibility for evaluator reliability |

**Key design choices across all five:**
- All 16 stock roles named explicitly in the prompt (not just "16 roles") — makes C-01 omissions a prompt violation, not just a model failure
- All five require feature-specific spread mechanisms, not generic "word of mouth" — raises the floor on C-03/C-07
- All five define the H/M/L delta scale in-prompt — makes C-04 pass condition deterministic
- V-04 is the only one that inverts the mapping order (Laggards first) — worth comparing against V-01's neutral order to see if inertia-first framing produces sharper chasm analysis
ing | Spread Mechanism |
|-------|----------------|----------------|------------------|
| M1    | Innovator      | ...            | ...              |
| M2    | Early Adopter  | ...            | ...              |
| M3    | Early Majority | ...            | [feature-specific mechanism] |
| ...   | ...            | ...            | ...              |

---

### Step 3 — Chasm Analysis

Name the chasm explicitly. State:
- Which archetypes bound it (Early Adopter -> Early Majority)
- What makes this feature's chasm wide or narrow
- The bridging mechanism specific to this feature (not generic advice)

---

### Step 4 — Champion Network

Identify at least 2 specific roles that form the champion network — the social bridge
across the chasm. For each champion, explain why their archetype position enables them
to bridge into Early Majority.

| Champion Role | Archetype | Why They Bridge |
|---------------|-----------|-----------------|
| ...           | ...       | ...             |

---

### Step 5 — Intervention Recommendations

List interventions ranked by adoption delta (descending). Each entry must include
an adoption delta label (High / Medium / Low) or a percentage estimate.
Explain what "High/Medium/Low" means in context once, then apply consistently.

| Rank | Intervention | Adoption Delta | Rationale |
|------|-------------|----------------|-----------|
| 1    | ...         | High           | ...       |
| 2    | ...         | Medium         | ...       |
| ...  | ...         | ...            | ...       |

---

### Step 6 — Churn Risk Register

For at least 2 archetypes, state what triggers churn and how to detect or mitigate it.

| Archetype | Churn Trigger | Mitigation / Warning Signal |
|-----------|--------------|------------------------------|
| ...       | ...          | ...                          |

---

### Step 7 — Sensitivity Analysis (if confident)

Model two named scenarios for chasm crossing:
- Optimistic: name the lever that accelerates crossing
- Pessimistic: name the lever that widens the chasm

Show different adoption trajectories, not just "things go well / badly."

---

### Step 8 — Signal Readiness

State at least 2 measurable adoption signals that would confirm readiness to proceed
(or abort). Each signal must be concrete enough to track in a real team context.
Example format: ">= N roles from Early Majority active after month M."

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-02

**Variation axis:** Lifecycle emphasis — chasm-centered
**Hypothesis:** Spending the majority of the prompt space on chasm mechanics (C-03, C-05,
C-07) forces deeper bridging analysis and makes generic "find champions" answers fail
the specificity bar.

---

You are simulating how a feature crosses the adoption chasm inside a product team.

**Inputs:**
- Topic: the feature
- Signal: prior artifacts (read if present)

**Stock roles:** PM, UX, C-01 through C-12, Support, SRE (16 total)

---

### Phase 1 — Archetype Assignment

Assign each of the 16 stock roles to one Rogers archetype:
Innovator / Early Adopter / Early Majority / Late Majority / Laggard

Cover all 16. No duplicates. Brief rationale per role.

---

### Phase 2 — Pre-Chasm Momentum

Describe months 1-2 (or equivalent early phase):
- Which roles try first (Innovators and Early Adopters)
- What attracts them specifically to this feature
- How the word spreads within this early cluster
- What early signals confirm momentum is real

---

### Phase 3 — The Chasm (this is the heart of the output)

Name the chasm. This is the gap between Early Adopters (enthusiasts who adopt for
the feature's own sake) and Early Majority (pragmatists who adopt only when it
demonstrably reduces friction or risk in their workflow).

Address all of the following for this specific feature:

**3a. Why the chasm exists here**
What is the specific friction or trust gap that separates this feature's early adopters
from the pragmatist majority? Do not give generic diffusion theory — tie it to what
this feature does and who the Early Majority roles are.

**3b. The bridging mechanism**
Name the mechanism that can carry adoption across: embedded workflow integration,
a reference customer (which role, which use case), a mandate signal, a demo format
that speaks to pragmatist risk aversion, or another feature-specific vehicle.

**3c. Champion network**
Name at least 2 specific stock roles who occupy the structural position to bridge
Early Adopters to Early Majority. Explain each champion's archetype position and why
it gives them credibility with the Early Majority cluster.

**3d. Chasm width estimate**
Rate the chasm: Narrow / Moderate / Wide. Justify with feature-specific reasoning.

---

### Phase 4 — Post-Chasm Spread

Describe the Early Majority adoption period:
- Which roles adopt and in what sequence
- The spread mechanism in this phase (must differ from Phase 2)
- The transition into Late Majority and what triggers it
- Any Laggard profile for this feature

---

### Phase 5 — Churn Risk

For at least 2 archetypes, name the churn trigger and one mitigation or warning signal.
Churn in Early Adopters is often different from churn in Early Majority — call out
the distinction if it applies to this feature.

---

### Phase 6 — Interventions Ranked by Adoption Delta

List interventions that would accelerate adoption across the chasm or deepen
post-chasm spread. Rank descending by adoption delta. Label each H/M/L.
Explain once what H means in this context (e.g., "H = expected to shift >=2 archetype
waves in one quarter").

At least 2 interventions. Ranked list required.

---

### Phase 7 — Sensitivity Scenarios

Two scenarios for chasm crossing:

**Optimistic:** Which single lever, if it fires, collapses the chasm? What does
adoption look like month-by-month in this scenario?

**Pessimistic:** Which single lever, if it fails, widens the chasm indefinitely?
What does adoption plateau look like?

Each scenario must name a different lever — not just "things go well."

---

### Phase 8 — Signal Readiness

State at least 2 measurable adoption signals that confirm this feature has crossed
the chasm and signal readiness to invest in broader rollout. Make them trackable.

---

Write artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-03

**Variation axis:** Phrasing register — narrative/conversational
**Hypothesis:** A story-driven prompt ("tell me who adopts, then who follows, then who
resists") produces richer role-persona reasoning at the cost of scannability; testing
whether narrative framing degrades C-08 (structured month view) while improving
depth on C-03 and C-05.

---

You are a product adoption strategist. I'm going to give you a feature to analyze.
Your job is to tell me the adoption story — who picks it up first, why, what happens
at the chasm, and what we need to do to get the pragmatists on board.

**Feature topic:** (from Topic input)
**Prior signals:** (read Signal artifacts if present)

**The cast:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10,
C-11, C-12, Support, SRE. All 16 roles must appear somewhere in your story.

---

**Tell me who they are first.**

Start with an archetype table — assign every one of the 16 roles to their Rogers
archetype: Innovator, Early Adopter, Early Majority, Late Majority, or Laggard.
Add a one-sentence rationale for each assignment. This is your cast list.

---

**Tell me the adoption story, month by month.**

Walk me through at least 3 months. Who hears about the feature first? What do they
do with it? How does word travel — and I mean specifically how, not just "they talk
about it." What does month 2 look like differently from month 1? When does the wave
slow down?

Use clearly labeled month headers (Month 1, Month 2, etc.) or a timeline table —
something I can scan without reading every word.

---

**Tell me about the chasm.**

At some point the early enthusiasts stop spreading the word and the pragmatists
haven't started yet. That's the chasm. Name it. Tell me why it exists specifically
for this feature — what's the friction, the trust gap, the missing proof point?

Then tell me how to bridge it. What's the specific vehicle for this feature — a demo
format that speaks to pragmatist risk aversion, a workflow integration that removes the
try-it cost, a reference team whose use case the pragmatists recognize? Don't just say
"find champions." Tell me which roles in our cast are the champions and why their
position in the Rogers curve gives them the credibility to carry this across.

---

**Tell me who might drop off.**

For at least 2 archetypes, tell me what triggers churn. Early Adopters often churn
when the feature gets "too mainstream" — does that apply here? What about Early
Majority — what makes them give up and revert to old habits? Give me a warning signal
for each.

---

**Tell me what to do about it.**

Give me a ranked list of interventions. Rank by adoption delta — the expected
acceleration in adoption if we do this. Use High / Medium / Low and tell me once
what "High" means here. At least 2 interventions. Most impactful first.

---

**Tell me the two futures.**

Optimistic: one lever fires, the chasm narrows fast. What's the lever? What does
month-by-month adoption look like?

Pessimistic: one lever fails, the chasm widens. What's the lever? What does
the adoption plateau look like?

Name the levers. "Things go well" is not a scenario.

---

**Tell me when we're ready.**

Give me 2 measurable signals I can track in a real dashboard that tell me we've
crossed the chasm. Something like "at least 3 Early Majority teams running active
workflows after month 3." Make them concrete.

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-04

**Variation axis:** Inertia framing + role sequence (combined)
**Hypothesis:** Opening with status-quo inertia as the "zeroth archetype" and sequencing
Laggards-first (characterizing resistance before mapping adopters) surfaces stickier
chasm analysis — the bridging mechanism has to fight inertia explicitly, improving C-03
specificity and C-04 intervention quality.

---

You are simulating adoption of a proposed feature. Before mapping who will adopt,
you must characterize the gravitational pull of the status quo — the force that keeps
teams from adopting anything at all.

**Inputs:**
- Topic: the feature
- Signal: prior artifacts for this topic (read if present)

**Stock roles:** PM, UX, C-01 through C-12, Support, SRE (all 16 must appear)

---

### Section 0 — The Inertia Baseline

Before assigning Rogers archetypes, characterize "no adoption" as a competitor.
Answer: What are teams doing today instead of this feature? Why is that good enough?
What would have to change for a pragmatist to consider switching?

This inertia profile will anchor your chasm analysis and your interventions.

---

### Section 1 — Laggard and Late-Majority Profile (Resistance Mapping)

Start from the hardest end of the curve and work inward.

For the Late Majority and Laggard roles in your cast:
- Which stock roles belong here? (Assign all 16 by the end of all sections.)
- What specifically makes them resistant to this feature — is it the inertia you
  characterized above, or something feature-specific?
- What would have to be true before they adopt at all?

---

### Section 2 — Early Majority Profile (The Pragmatist Gate)

Early Majority roles are the real market. They won't adopt until adoption feels safe,
proven, and friction-free.

- Which stock roles are Early Majority?
- What proof point do they require? (Reference team? Integration into their workflow?
  A mandate? A metric that shows peer teams are ahead of them?)
- What is the specific trust mechanism for this feature?

---

### Section 3 — Early Adopters and Innovators

- Which stock roles are Innovators and Early Adopters?
- What draws them to this feature specifically?
- Why will their enthusiasm not automatically transfer to the Early Majority?

Complete your archetype table here — all 16 roles assigned, no omissions.

---

### Section 4 — Month-by-Month Timeline

Now simulate the adoption curve forward from the innovators.

Use a structured format (table or labeled month headers). At least 3 time steps.
Rogers order must hold: Innovators -> Early Adopters -> Early Majority -> Late Majority
-> Laggards.

For each archetype-to-archetype transition, name the spread mechanism. It must be
specific to this feature — explain why this particular mechanism works here given
the inertia you characterized in Section 0.

---

### Section 5 — Chasm Analysis

Name the chasm. Explain why the gap between Early Adopters and Early Majority is
hard to cross for this specific feature, grounded in your inertia profile.

State the bridging mechanism. It must directly address the pragmatist trust gap and
the inertia barrier you named in Section 0 — not generic diffusion advice.

Name the champion network: at least 2 stock roles who can bridge the gap. Explain
why each champion's archetype position gives them credibility with the pragmatist block.

---

### Section 6 — Interventions (Ranked by Adoption Delta)

List interventions that fight inertia and accelerate adoption. Rank descending by
adoption delta. Label each H/M/L. Explain once what "High" means.

At least 2 interventions. Frame each intervention as a direct response to a named
friction — the inertia barrier, a pragmatist trust gap, or a churn trigger.

---

### Section 7 — Churn Risks

For at least 2 archetypes, name the trigger that causes them to revert to the
status-quo behavior you described in Section 0. Give one mitigation or warning signal.

---

### Section 8 — Sensitivity Scenarios

Two scenarios:
- Optimistic: the inertia barrier weakens — name the lever and show the faster
  adoption trajectory month-by-month
- Pessimistic: the inertia barrier holds — name the lever and show the plateau

Scenarios must differ on a named lever, not just tone.

---

### Section 9 — Signal Readiness

State at least 2 measurable signals that confirm adoption has overcome inertia and
crossed the chasm. Make them trackable in a real team context.

---

Write artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-05

**Variation axis:** Format + lifecycle (combined) — structured tables throughout, explicit
phase gates between lifecycle stages
**Hypothesis:** Combining rigid tabular output requirements with explicit "GATE" checkpoints
between phases reduces prose drift and makes every rubric criterion addressable at a
specific location in the output — trading flexibility for evaluator reliability.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts — read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06,
C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Produce your output in the exact section order below. Do not merge sections.
Each section gate must be satisfied before proceeding to the next.

---

### SECTION A — Archetype Map

**GATE A:** All 16 roles assigned. Each role appears exactly once. All 5 archetype
labels used at least once.

Produce this table in full:

| Role    | Archetype       | Rationale                          |
|---------|-----------------|------------------------------------|
| PM      | [archetype]     | [1-sentence rationale]             |
| UX      | [archetype]     | [1-sentence rationale]             |
| C-01    | [archetype]     | [1-sentence rationale]             |
| C-02    | [archetype]     | [1-sentence rationale]             |
| C-03    | [archetype]     | [1-sentence rationale]             |
| C-04    | [archetype]     | [1-sentence rationale]             |
| C-05    | [archetype]     | [1-sentence rationale]             |
| C-06    | [archetype]     | [1-sentence rationale]             |
| C-07    | [archetype]     | [1-sentence rationale]             |
| C-08    | [archetype]     | [1-sentence rationale]             |
| C-09    | [archetype]     | [1-sentence rationale]             |
| C-10    | [archetype]     | [1-sentence rationale]             |
| C-11    | [archetype]     | [1-sentence rationale]             |
| C-12    | [archetype]     | [1-sentence rationale]             |
| Support | [archetype]     | [1-sentence rationale]             |
| SRE     | [archetype]     | [1-sentence rationale]             |

---

### SECTION B — Adoption Timeline

**GATE B:** At least 3 distinct months. Rogers order preserved. Each archetype-level
transition has a named spread mechanism (feature-specific, not just "word of mouth").

Produce this table:

| Month | Archetype Wave  | Roles Adopting | Spread Mechanism (feature-specific) |
|-------|-----------------|----------------|--------------------------------------|
| M1    | Innovator       | ...            | ...                                  |
| M2    | Early Adopter   | ...            | ...                                  |
| M3    | [wave]          | ...            | ...                                  |
| M4    | [wave]          | ...            | ...                                  |
| M5    | [wave]          | ...            | ...                                  |

Add rows if adoption extends beyond M5. Compress if fewer waves apply.

---

### SECTION C — Chasm Analysis

**GATE C:** The word "chasm" appears. A feature-specific bridging mechanism is named.
A champion network of at least 2 roles is identified with archetype-based rationale.

Produce three labeled subsections:

**C1. Why the chasm exists here**
[Feature-specific explanation of the Early Adopter / Early Majority gap]

**C2. Bridging mechanism**
[The specific vehicle for crossing — tied to this feature's workflow, trust model,
or proof-point requirements of the Early Majority roles in your archetype map]

**C3. Champion network**

| Champion Role | Archetype       | Bridge Rationale                   |
|---------------|-----------------|------------------------------------|
| ...           | Early Adopter   | [why their EA position gives credibility with EM] |
| ...           | Early Majority  | [why they can vouch to Late Majority once adopted] |

---

### SECTION D — Churn Risk Register

**GATE D:** At least 2 archetypes covered. Each entry has a named trigger and a
mitigation or warning signal.

| Archetype       | Churn Trigger                        | Mitigation / Warning Signal       |
|-----------------|--------------------------------------|-----------------------------------|
| ...             | ...                                  | ...                               |
| ...             | ...                                  | ...                               |

---

### SECTION E — Interventions (Ranked)

**GATE E:** At least 2 entries. Each has an adoption delta label. List is in
descending delta order. Delta scale defined once before the table.

**Delta scale:** H = expected to accelerate adoption by at least one archetype wave
within the current quarter; M = meaningful but slower impact; L = directional, no
near-term wave shift.

| Rank | Intervention | Delta | Rationale |
|------|-------------|-------|-----------|
| 1    | ...         | H     | ...       |
| 2    | ...         | M     | ...       |
| ...  | ...         | ...   | ...       |

---

### SECTION F — Sensitivity Scenarios

**GATE F:** Two named scenarios. Each names a different lever. Each shows a different
adoption trajectory. Scenarios are comparable on the same dimension.

**Optimistic scenario — lever: [name it]**
Month-by-month trajectory: [show which waves accelerate and when]

**Pessimistic scenario — lever: [name it]**
Month-by-month trajectory: [show plateau or stall point]

---

### SECTION G — Signal Readiness

**GATE G:** At least 2 measurable signals. Each is concrete and trackable.

State the adoption signals that confirm readiness to proceed with broader investment:
1. [Measurable signal — e.g., ">= N roles from Early Majority active in sustained
   workflow after month M"]
2. [Measurable signal]

State any abort signals (adoption signals that would recommend pausing rollout):
1. [Abort signal]

---

Write artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`
