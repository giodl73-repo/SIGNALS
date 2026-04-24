All 5 variations written to `simulations/quest/variations/listen-adoption-variations-R2-2026-03-14.md` (46KB).

---

## Summary

**Five R2 variations — targeting C-11 (named inertia per archetype) and C-12 (no orphan/conditional sections)**

| ID | Axis | C-11 mechanism | C-12 mechanism | Expected score |
|----|------|----------------|----------------|----------------|
| **V-01** | Inertia framing — column | 4th column in archetype table; blank cell is visibly wrong | All steps present, no qualifiers | ~105 |
| **V-02** | GATE extended to 12 criteria | GATE A explicitly requires feature-specific inertia per row | META-GATE scans for conditional qualifiers before artifact write | ~110 |
| **V-03** | Phrasing register — imperative | "State what this role does today instead" command at each row | All parts present, no qualifiers | ~100 (C-08 risk) |
| **V-04** | Inertia column + GATE (combined) | GATE A enforces Named Inertia column quality | All GATEs mandatory and unconditional | **110** (expected winner) |
| **V-05** | GATE + self-audit (combined) | Self-audit item C-11 counts archetypes and judges quality | Self-audit item C-12 scans own output for conditional phrases | **110** (alt path) |

**Key R2 design shift from R1:** C-11 is no longer a separate Section 0 (R1 V-04's pattern) — it's a structural column in the archetype map that propagates forward. This avoids the "front-loaded inertia essay" failure mode while making per-archetype inertia mechanically checkable. V-04 and V-05 are the expected 110-point candidates; V-03 is the deliberate risk variation that tests whether command phrasing alone can match structural enforcement.
ock roles named explicitly in the prompt -- C-01 omissions are prompt violations, not model failures
- H/M/L delta scale defined in-prompt with a concrete contextual definition -- C-04 pass is deterministic
- Feature-specific spread mechanisms required at each archetype transition -- word of mouth alone does not pass
- No variation uses a conditional qualifier (if confident, if applicable, optional) on any section -- C-12 floor maintained by prompt design
- All five inherit R1 common design baseline; single-axis variations isolate C-11/C-12 targeting strategies; combined variations synthesize the strongest R1 patterns

---

## V-01

**Variation axis:** Inertia framing -- inertia as a required fourth column in the archetype map table
**Hypothesis:** Requiring a Named Inertia column in the archetype map table makes C-11 a structural table property. A blank or generic cell is visibly wrong at a glance. This achieves per-archetype inertia coverage without a separate section, and the inertia column propagates into chasm analysis (C-03) and interventions (C-04) by natural forward reference. Expects C-11 pass; C-12 pass from unconditional section design.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

---

### Step 1 -- Archetype Map with Named Inertia

Assign every stock role to one Rogers archetype. For each role, also populate the Named Inertia column with the specific behavior, workflow, or tool that role uses today instead of this feature.

The Named Inertia column must contain a feature-specific statement. Generic entries fail this column: attitude statements ("may resist change," "slow to adopt") do not name a behavior. A passing entry names what the role is actually doing (e.g., "runs ad-hoc SQL queries in a shared spreadsheet," "manually reviews PRs by checking out branches locally").

| Role    | Archetype       | Rationale (1 sentence)             | Named Inertia (what they do today instead)      |
|---------|-----------------|------------------------------------|--------------------------------------------------|
| PM      | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| UX      | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-01    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-02    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-03    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-04    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-05    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-06    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-07    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-08    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-09    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-10    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-11    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| C-12    | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| Support | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |
| SRE     | [archetype]     | [rationale]                        | [feature-specific status-quo behavior]          |

---

### Step 2 -- Month-by-Month Adoption Timeline

Simulate the adoption curve forward from innovators. At least 3 distinct time steps. Rogers sequence must hold: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards -- no inversions.

For each archetype-to-archetype transition, name the spread mechanism specific to this feature. Ask: given what these roles do today (their Named Inertia from Step 1), what communication channel or event would actually reach them and displace that behavior? Generic word of mouth fails -- at least one transition must cite a mechanism tied to this feature context.

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific)       |
|-------|------------------|----------------|-------------------------------------------|
| M1    | Innovator        | ...            | ...                                       |
| M2    | Early Adopter    | ...            | ...                                       |
| M3    | [wave]           | ...            | ...                                       |
| M4    | [wave]           | ...            | ...                                       |
| M5    | [wave]           | ...            | ...                                       |

Add rows if adoption extends beyond M5. Compress if fewer archetype waves apply.

---

### Step 3 -- Chasm Analysis

Name the chasm. Address all three subsections:

**3a. Why this chasm exists for this feature**
Draw from the Named Inertia entries for the Early Majority roles in Step 1. The chasm exists because these specific roles have this specific inertia -- name it. Do not reproduce generic EA-to-EM diffusion theory.

**3b. Bridging mechanism**
The specific vehicle that can overcome the Early Majority named inertia. Must be tied to this feature workflow, trust model, or proof-point requirements of the EM roles -- not generic find-champions or run-demos advice.

**3c. Champion network**

| Champion Role | Archetype       | Bridge Rationale                                          |
|---------------|-----------------|------------------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]    |
| ...           | ...             | ...                                                        |

At least 2 champions. Each rationale must connect archetype position to credibility with the Early Majority cluster.

---

### Step 4 -- Churn Risk Register

For at least 2 archetypes, state what triggers churn and one mitigation or warning signal.

Named trigger required: general dissatisfaction is not a trigger. Frame churn triggers in terms of what would cause a role to revert to the Named Inertia behavior from Step 1.

| Archetype      | Churn Trigger                         | Mitigation / Warning Signal        |
|----------------|---------------------------------------|------------------------------------|
| ...            | ...                                   | ...                                |
| ...            | ...                                   | ...                                |

---

### Step 5 -- Intervention Recommendations (Ranked by Adoption Delta)

List interventions that address the Named Inertia from Step 1 and accelerate adoption. Rank descending by adoption delta. Each intervention must name which inertia or friction it targets.

**Delta scale:** H = expected to shift adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, no full-wave shift; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Inertia / Friction Addressed        |
|------|-------------|-------|-------------------------------------|
| 1    | ...         | H     | ...                                 |
| 2    | ...         | M     | ...                                 |
| ...  | ...         | ...   | ...                                 |

At least 2 entries. Ranked in descending delta order.

---

### Step 6 -- Sensitivity Scenarios

Two scenarios for chasm crossing. Each must name a different lever that changes the adoption trajectory.

**Optimistic scenario -- lever: [name it]**
Month-by-month trajectory: show which waves accelerate and when; reference which Named Inertia entries weaken under this scenario.

**Pessimistic scenario -- lever: [name it]**
Month-by-month trajectory: show plateau or stall; reference which Named Inertia entries hold under this scenario.

Labeling a scenario without naming the lever fails this section.

---

### Step 7 -- Signal Readiness

State the adoption signals that confirm readiness to proceed with broader investment and signals that indicate abort.

**Proceed signals (at least 2):**
1. [Measurable -- e.g., >=3 Early Majority roles running sustained workflows after month 3]
2. [Measurable]

**Abort signal (at least 1):**
1. [Measurable condition that would recommend pausing rollout]

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-02

**Variation axis:** Output format -- GATE structure extended to all 12 rubric criteria (C-01 through C-12)
**Hypothesis:** R1 V-05 GATE pattern scored 100 by mapping C-01 through C-10 to mandatory named sections. V-02 R2 extends this: GATE A now includes a Named Inertia column requirement (C-11), and a META-GATE at the end makes C-12 explicit -- the model must confirm no section carries a conditional qualifier before writing the artifact. The extended GATE structure directly targets 110/110.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Produce your output in the exact section order below. Each GATE must be satisfied before proceeding to the next section. Do not skip, merge, or qualify any section as optional or conditional.

---

### SECTION A -- Archetype Map with Named Inertia

**GATE A -- all of the following must be true before proceeding:**
- All 16 roles appear in the table; each appears exactly once
- All 5 archetype labels (Innovator, Early Adopter, Early Majority, Late Majority, Laggard) are used at least once
- The Named Inertia column is populated for every row with a feature-specific statement naming the behavior, workflow, or tool the role uses today instead of this feature
- Generic entries fail GATE A: "may resist change," "prefers established workflows," "slow to adopt new tooling" are not named inertia

| Role    | Archetype       | Rationale (1 sentence)             | Named Inertia (feature-specific)                 |
|---------|-----------------|------------------------------------|--------------------------------------------------|
| PM      | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| UX      | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-01    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-02    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-03    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-04    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-05    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-06    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-07    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-08    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-09    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-10    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-11    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| C-12    | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| Support | [archetype]     | [rationale]                        | [named status-quo behavior]                      |
| SRE     | [archetype]     | [rationale]                        | [named status-quo behavior]                      |

---

### SECTION B -- Adoption Timeline

**GATE B -- all of the following must be true before proceeding:**
- At least 3 distinct time steps
- Rogers sequence intact: Innovators before Early Adopters; Early Adopters before Early Majority; Early Majority before Late Majority; Late Majority before Laggards
- Each archetype-level transition has a named spread mechanism; word of mouth alone fails -- at least one mechanism must cite something specific to this feature context or the EM roles Named Inertia

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific)       |
|-------|------------------|----------------|-------------------------------------------|
| M1    | Innovator        | ...            | ...                                       |
| M2    | Early Adopter    | ...            | ...                                       |
| M3    | [wave]           | ...            | ...                                       |
| M4    | [wave]           | ...            | ...                                       |
| M5    | [wave]           | ...            | ...                                       |

---

### SECTION C -- Chasm Analysis

**GATE C -- all of the following must be true before proceeding:**
- The word "chasm" appears in this section
- The Early Majority roles Named Inertia entries from SECTION A are cited in the explanation of why the chasm exists
- A bridging mechanism is named that directly addresses those inertia entries (not generic)
- Champion network table has at least 2 rows; each row connects the champion archetype position to credibility with the Early Majority

**C1. Why this chasm exists**
[Feature-specific -- draw from the EM roles Named Inertia in SECTION A. What is the specific friction or trust gap that the EA cluster cannot bridge on enthusiasm alone?]

**C2. Bridging mechanism**
[The vehicle that directly addresses the EM Named Inertia. Not "find champions." The mechanism must name what it does to displace the specific inertia entries you surfaced.]

**C3. Champion network**

| Champion Role | Archetype       | Bridge Rationale (archetype-grounded)                       |
|---------------|-----------------|--------------------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]      |
| ...           | ...             | ...                                                          |

---

### SECTION D -- Churn Risk Register

**GATE D -- all of the following must be true before proceeding:**
- At least 2 archetype rows
- Each churn trigger is named (not "general dissatisfaction" or "may churn"); frame trigger as the event that causes the role to revert to their Named Inertia behavior
- Each row has a mitigation or warning signal

| Archetype      | Churn Trigger                         | Mitigation / Warning Signal        |
|----------------|---------------------------------------|------------------------------------|
| ...            | ...                                   | ...                                |
| ...            | ...                                   | ...                                |

---

### SECTION E -- Interventions (Ranked by Adoption Delta)

**GATE E -- all of the following must be true before proceeding:**
- At least 2 entries
- Each entry has a delta label (H, M, or L)
- List is in descending delta order
- Delta scale defined once before the table
- Each intervention names a specific inertia or friction from SECTION A or SECTION C that it addresses

**Delta scale:** H = expected to shift adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Inertia / Friction Addressed        |
|------|-------------|-------|-------------------------------------|
| 1    | ...         | H     | ...                                 |
| 2    | ...         | M     | ...                                 |
| ...  | ...         | ...   | ...                                 |

---

### SECTION F -- Sensitivity Scenarios

**GATE F -- all of the following must be true before proceeding:**
- Two scenarios present
- Each scenario names a different lever (label alone without naming the lever fails)
- Each scenario shows a distinct adoption trajectory month-by-month
- A reader can compare the two scenarios to identify which factor most affects chasm width

**Scenario 1 -- lever: [name it]**
Trajectory: [month-by-month -- which waves accelerate, which stall; reference which Named Inertia entries are affected]

**Scenario 2 -- lever: [name it]**
Trajectory: [month-by-month -- must differ from Scenario 1; reference which Named Inertia entries hold or break]

---

### SECTION G -- Signal Readiness

**GATE G -- all of the following must be true before proceeding:**
- At least 2 measurable proceed signals
- At least 1 measurable abort signal
- Every signal is concrete and trackable; vague signals ("adoption increases," "team feels ready") fail

**Proceed signals:**
1. [Measurable -- e.g., >=3 Early Majority roles running sustained workflows after month 3]
2. [Measurable]

**Abort signal:**
1. [Measurable condition that would recommend pausing rollout]

---

### META-GATE -- Completeness and Conditionality Check

Before writing the artifact, verify each item:

- [ ] C-01: SECTION A table has all 16 rows; each role assigned to exactly one archetype
- [ ] C-02: SECTION B has >=3 time steps; Rogers sequence intact (no inversions)
- [ ] C-03: SECTION C contains "chasm"; bridging mechanism is feature-specific
- [ ] C-04: SECTION E has >=2 interventions with delta labels; list is ranked descending
- [ ] C-05: SECTION C champion table has >=2 rows with archetype-grounded bridge rationale
- [ ] C-06: SECTION D has >=2 rows; each has a named trigger and a mitigation
- [ ] C-07: SECTION B spread mechanisms are feature-specific (not generic word of mouth alone)
- [ ] C-08: SECTION B is presented as a table or clearly labeled month headers (scannable)
- [ ] C-09: SECTION F has two scenarios; each names a different lever
- [ ] C-10: SECTION G has >=2 measurable proceed signals and >=1 abort signal
- [ ] C-11: SECTION A Named Inertia column has feature-specific statements (at least 3 archetypes have distinct, non-generic entries)
- [ ] C-12: No section in the output is marked optional, skipped, or qualified with "if confident," "if applicable," "if time permits," or equivalent

If any item is unchecked, revise before proceeding. Only write the artifact after all 12 items are checked.

---

Write artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-03

**Variation axis:** Phrasing register -- imperative per-archetype commands that name inertia at the assignment step
**Hypothesis:** An explicit "state the specific behavior this role does today instead of this feature" command issued at the archetype assignment block produces per-archetype inertia statements without a table column or a separate section. Tests whether command-register phrasing alone achieves C-11 coverage. The richer persona reasoning from command-register prompts may improve champion rationale depth (C-05); the deliberate trade-off is that prose format risks C-08 scannability if the model drifts.

---

You are running the `listen-adoption` skill for Signal.

**Feature topic:** (from Topic input)
**Prior signals:** (read Signal artifacts if present before proceeding)

**Cast:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE -- all 16 must be assigned an archetype before the timeline begins.

---

**PART 1 -- Cast Assignment**

Assign each of the 16 stock roles to one Rogers archetype: Innovator, Early Adopter, Early Majority, Late Majority, or Laggard.

For each role, do two things:
1. State the archetype and a one-sentence rationale.
2. State specifically what this role does today instead of this feature. This is a named behavior -- not an attitude. It answers: what workflow, tool, or habit will persist unless this feature actively displaces it?

Present as a table: Role | Archetype | Rationale | Today Behavior (named inertia).

All 16 rows required. A row with generic inertia ("prefers familiar tools") is incomplete -- name the specific tool or behavior.

---

**PART 2 -- Adoption Timeline**

Simulate the adoption curve month by month. At least 3 distinct months. Rogers sequence must hold: Innovators before Early Adopters; Early Adopters before Early Majority; no inversions.

Present with clearly labeled month headers or a timeline table -- something scannable to any month without reading surrounding prose.

For each archetype transition, state the spread mechanism. Ask: given what these roles do today (their named behavior from Part 1), what channel or event would actually reach them and make them try this feature? Feature-specific grounding required. Word of mouth as the only mechanism fails.

---

**PART 3 -- The Chasm**

Name the chasm explicitly.

**3a. Why it exists for this feature**
Draw from the Part 1 named behaviors of the Early Majority roles. The chasm exists because these specific roles have a specific inertia -- state it. Do not reproduce generic diffusion theory.

**3b. Bridging mechanism**
The specific vehicle that can overcome the EM roles named inertia. What does it do that generic champion-finding cannot? Tie it to what these roles respond to given their current named behavior.

**3c. Champion network**
Name at least 2 stock roles who can bridge the chasm. For each:
- State their archetype
- State why their position on the Rogers curve gives them credibility with the Early Majority cluster
- Connect their credibility to the EM roles named inertia from Part 1

Present as a table: Champion Role | Archetype | Bridge Rationale.

---

**PART 4 -- Churn Risks**

For at least 2 archetypes, name:
- What specific event or condition triggers churn (not general dissatisfaction -- a named event or condition)
- How this trigger connects to reversion to the named behavior from Part 1
- One mitigation or warning signal you can track

Present as a table: Archetype | Churn Trigger | Reversion Behavior | Mitigation / Warning Signal.

---

**PART 5 -- Interventions Ranked by Adoption Delta**

List interventions that directly fight the named inertia from Part 1 and accelerate adoption across the chasm. Rank descending by adoption delta.

**Delta scale:** H = expected to move at least one full archetype wave within one quarter; M = meaningful but sub-wave; L = directional, marginal near-term effect.

At least 2 interventions. Each entry: intervention, delta label (H/M/L), which named inertia it addresses.

Ranked list. Most impactful first.

---

**PART 6 -- Two Futures**

Two scenarios for chasm crossing. Each must name a different lever.

**Scenario A -- lever: [name it]**
What does the adoption curve look like month-by-month when this lever fires? Which archetypes accelerate? Which named inertia entries weaken?

**Scenario B -- lever: [name it]**
What does the adoption curve look like when this lever fails? Where does adoption plateau? Which named inertia entries hold?

Labeling a scenario without naming the lever fails this section.

---

**PART 7 -- Signal Readiness**

State at least 2 measurable adoption signals that confirm readiness to proceed with broader investment. Each signal must be trackable in a real team context.

State at least 1 abort signal.

Concrete format: ">= N roles from [archetype] running [specific behavior] after month M."

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-04

**Variation axes:** Inertia framing (inertia as required archetype table column) + Output format (GATE checkpoints for all sections)
**Hypothesis:** R1 analysis identified V-04 inertia-first approach as the source of C-11 and V-05 GATE structure as the source of C-12. V-04 R2 combines them directly: GATE A enforces the Named Inertia column (C-11 via structural requirement), all GATEs are present and unconditional (C-12 via format enforcement), and the inertia column is cross-referenced by SECTION C and SECTION E. Expected to score 110/110.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Produce your output in the exact section order below. Each GATE must be satisfied before proceeding. Do not skip, merge, or mark any section optional or conditional.

---

### SECTION A -- Archetype Map with Named Inertia

**GATE A -- complete when all conditions met:**
- All 16 roles present; each assigned to exactly one of the 5 canonical archetypes
- All 5 archetype labels used at least once
- Named Inertia column populated for every row with a feature-specific statement that names what the role actively does today instead of this feature
- Generic attitude statements ("may resist change," "slow to adopt") fail GATE A; the entry must describe a behavior, workflow, or tool

| Role    | Archetype       | Rationale (1 sentence)             | Named Inertia (what they do today instead)      |
|---------|-----------------|------------------------------------|--------------------------------------------------|
| PM      | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| UX      | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-01    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-02    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-03    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-04    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-05    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-06    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-07    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-08    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-09    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-10    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-11    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-12    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| Support | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| SRE     | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |

---

### SECTION B -- Adoption Timeline

**GATE B -- complete when all conditions met:**
- At least 3 distinct time steps
- Rogers sequence intact: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards; no inversion
- Each archetype-level transition has a named spread mechanism; generic word of mouth alone fails; at least one mechanism must name something tied to the Named Inertia entries in SECTION A

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific)       |
|-------|------------------|----------------|-------------------------------------------|
| M1    | Innovator        | ...            | ...                                       |
| M2    | Early Adopter    | ...            | ...                                       |
| M3    | [wave]           | ...            | ...                                       |
| M4    | [wave]           | ...            | ...                                       |
| M5    | [wave]           | ...            | ...                                       |

Add rows if adoption extends beyond M5. Compress if fewer archetype waves apply.

---

### SECTION C -- Chasm Analysis

**GATE C -- complete when all conditions met:**
- The word "chasm" appears in this section
- The Early Majority roles Named Inertia entries from SECTION A are cited as the explanation for why the chasm exists (not generic diffusion theory)
- A bridging mechanism is named that directly addresses those EM inertia entries
- Champion network table has at least 2 rows; each row states a champion role, their archetype, and an archetype-grounded bridge rationale

**C1. Why this chasm exists**
[Reference the EM roles Named Inertia from SECTION A -- what specific friction or trust gap separates the EA cluster from the EM cluster for this feature?]

**C2. Bridging mechanism**
[The vehicle that directly addresses the EM Named Inertia. Must be tied to this feature workflow or proof-point requirements -- not "find champions" without specifics.]

**C3. Champion network**

| Champion Role | Archetype       | Bridge Rationale (archetype-grounded)                       |
|---------------|-----------------|--------------------------------------------------------------|
| ...           | Early Adopter   | [why their archetype position gives credibility with EM]    |
| ...           | ...             | ...                                                          |

---

### SECTION D -- Churn Risk Register

**GATE D -- complete when all conditions met:**
- At least 2 archetype rows
- Each churn trigger is named; frame triggers as the event that causes reversion to the Named Inertia behavior from SECTION A
- Each row has a mitigation or warning signal; no row says only "monitor adoption"

| Archetype      | Churn Trigger (event / condition)     | Mitigation / Warning Signal        |
|----------------|---------------------------------------|------------------------------------|
| ...            | ...                                   | ...                                |
| ...            | ...                                   | ...                                |

---

### SECTION E -- Interventions (Ranked by Adoption Delta)

**GATE E -- complete when all conditions met:**
- At least 2 entries
- Each has a delta label (H, M, or L)
- List is in descending delta order (highest first)
- Delta scale defined before the table
- Each intervention names a specific Named Inertia entry or friction from SECTION A or SECTION C that it addresses

**Delta scale:** H = expected to shift adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Named Inertia / Friction Addressed  |
|------|-------------|-------|-------------------------------------|
| 1    | ...         | H     | ...                                 |
| 2    | ...         | M     | ...                                 |
| ...  | ...         | ...   | ...                                 |

---

### SECTION F -- Sensitivity Scenarios

**GATE F -- complete when all conditions met:**
- Two scenarios present
- Each names a different lever; a scenario labeled only "optimistic" or "pessimistic" without naming the lever fails GATE F
- Each shows a distinct adoption trajectory month-by-month; scenarios differ on which Named Inertia entries hold or break
- A reader can compare the two to identify which factor most determines chasm width

**Scenario 1 -- lever: [name it]**
Trajectory: [month-by-month -- which archetype waves accelerate; which Named Inertia entries weaken under this lever]

**Scenario 2 -- lever: [name it]**
Trajectory: [month-by-month -- which archetype waves stall; which Named Inertia entries hold under this lever]

---

### SECTION G -- Signal Readiness

**GATE G -- complete when all conditions met:**
- At least 2 measurable proceed signals; concrete and trackable in a real team context
- At least 1 measurable abort signal
- No vague signals ("adoption improves," "team gains confidence")

**Proceed signals:**
1. [Measurable -- e.g., >=3 Early Majority roles running sustained active workflows after month 3]
2. [Measurable]

**Abort signal:**
1. [Measurable condition that would recommend pausing or halting rollout]

---

Write artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-05

**Variation axes:** Output format (GATE checkpoints) + Phrasing register (self-audit against 12-criterion checklist)
**Hypothesis:** After producing all output sections, the model runs a mandatory 12-item self-audit that maps directly to C-01 through C-12 pass conditions. For C-11, the self-audit requires counting archetypes with feature-specific inertia (must reach >=3) and judging quality against the pass criterion -- not just checking structural presence. For C-12, the self-audit requires scanning for conditional qualifiers in the output and removing them if found. This meta-cognitive layer tests whether explicit pass-condition verification produces higher inertia specificity than structural enforcement alone.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

Produce your output in the section order below. After drafting all sections (A through G), run the 12-item self-audit. Revise any section that fails before writing the artifact.

---

### SECTION A -- Archetype Map with Named Inertia

Assign every stock role to one Rogers archetype. For each role, also state the Named Inertia: the specific behavior, workflow, or tool the role uses today instead of this feature. Generic resistance language fails -- name what they do, not how they feel about change.

| Role    | Archetype       | Rationale (1 sentence)             | Named Inertia (what they do today instead)      |
|---------|-----------------|------------------------------------|--------------------------------------------------|
| PM      | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| UX      | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-01    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-02    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-03    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-04    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-05    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-06    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-07    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-08    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-09    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-10    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-11    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| C-12    | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| Support | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |
| SRE     | [archetype]     | [rationale]                        | [named status-quo behavior or tool]             |

---

### SECTION B -- Adoption Timeline

Simulate the adoption curve forward. At least 3 distinct time steps. Rogers sequence must hold; no inversions. For each archetype-to-archetype transition, name a spread mechanism specific to this feature. At least one mechanism must directly address a Named Inertia entry from SECTION A.

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific)       |
|-------|------------------|----------------|-------------------------------------------|
| M1    | Innovator        | ...            | ...                                       |
| M2    | Early Adopter    | ...            | ...                                       |
| M3    | [wave]           | ...            | ...                                       |
| M4    | [wave]           | ...            | ...                                       |
| M5    | [wave]           | ...            | ...                                       |

---

### SECTION C -- Chasm Analysis

Name the chasm. State why it exists for this feature by drawing from the EM roles Named Inertia entries in SECTION A. State the bridging mechanism that addresses those inertia entries. Name the champion network.

**C1. Why this chasm exists**
[Cite EM Named Inertia from SECTION A -- feature-specific friction, not generic EA-to-EM diffusion theory]

**C2. Bridging mechanism**
[Specific vehicle that addresses the EM Named Inertia -- tied to this feature workflow or trust model]

**C3. Champion network**

| Champion Role | Archetype       | Bridge Rationale (archetype-grounded)                       |
|---------------|-----------------|--------------------------------------------------------------|
| ...           | Early Adopter   | [why their archetype position gives credibility with EM]    |
| ...           | ...             | ...                                                          |

At least 2 champions with archetype-grounded rationale.

---

### SECTION D -- Churn Risk Register

For at least 2 archetypes, state the named trigger that causes churn and one mitigation or warning signal. Frame triggers as the event that causes reversion to the Named Inertia behavior from SECTION A.

| Archetype      | Churn Trigger (named event / condition) | Mitigation / Warning Signal      |
|----------------|------------------------------------------|----------------------------------|
| ...            | ...                                      | ...                              |
| ...            | ...                                      | ...                              |

---

### SECTION E -- Interventions (Ranked by Adoption Delta)

List interventions that address Named Inertia from SECTION A and accelerate adoption. Rank descending. Each intervention names the inertia or friction it fights.

**Delta scale:** H = expected to shift adoption by at least one full archetype wave within one quarter; M = meaningful sub-wave acceleration; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Named Inertia / Friction Addressed  |
|------|-------------|-------|-------------------------------------|
| 1    | ...         | H     | ...                                 |
| 2    | ...         | M     | ...                                 |
| ...  | ...         | ...   | ...                                 |

At least 2 entries, ranked descending.

---

### SECTION F -- Sensitivity Scenarios

Two scenarios for chasm crossing. Each names a different lever. Each shows a distinct adoption trajectory month-by-month.

**Scenario 1 -- lever: [name it]**
Trajectory: [which waves accelerate; which Named Inertia entries weaken]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves stall; which Named Inertia entries hold]

---

### SECTION G -- Signal Readiness

State the measurable signals that confirm readiness and the signals that recommend abort.

**Proceed signals (at least 2):**
1. [Measurable and trackable]
2. [Measurable and trackable]

**Abort signal (at least 1):**
1. [Measurable condition recommending pause or halt]

---

### SELF-AUDIT -- Verify against 12 pass conditions before writing artifact

Work through each item. For any item that fails, revise the relevant section before proceeding.

**C-01 -- All 16 roles mapped:**
Check: Does SECTION A have exactly 16 rows? Is each role assigned to exactly one archetype? Are all 5 archetype labels present?
[ ] PASS  [ ] FAIL -- revise SECTION A

**C-02 -- Month-by-month sequence:**
Check: Does SECTION B have >=3 distinct time steps? Does Rogers sequence hold (no inversions)?
[ ] PASS  [ ] FAIL -- revise SECTION B

**C-03 -- Chasm named with feature-specific bridging:**
Check: Does "chasm" appear in SECTION C? Is the bridging mechanism tied to this feature specifics (not generic "find champions")?
[ ] PASS  [ ] FAIL -- revise SECTION C

**C-04 -- Interventions ranked by adoption delta:**
Check: Does SECTION E have >=2 entries? Does each have a delta label? Is the list in descending delta order?
[ ] PASS  [ ] FAIL -- revise SECTION E

**C-05 -- Champion network named:**
Check: Does SECTION C champion table have >=2 rows? Does each row connect archetype position to EM credibility?
[ ] PASS  [ ] FAIL -- revise SECTION C3

**C-06 -- Churn risk per archetype:**
Check: Does SECTION D have >=2 rows? Does each row have a named trigger (not "may churn") and a mitigation?
[ ] PASS  [ ] FAIL -- revise SECTION D

**C-07 -- Spread mechanism per transition:**
Check: Does SECTION B annotate each archetype transition with a spread mechanism? Is at least one mechanism feature-specific (not generic word of mouth alone)?
[ ] PASS  [ ] FAIL -- revise SECTION B

**C-08 -- Structured/scannable month view:**
Check: Is SECTION B presented as a table or clearly labeled month headers? Can I scan to any month without reading surrounding prose?
[ ] PASS  [ ] FAIL -- reformat SECTION B

**C-09 -- Sensitivity scenarios with named levers:**
Check: Does SECTION F have two scenarios? Does each name a different lever (not just a tone label)?
[ ] PASS  [ ] FAIL -- revise SECTION F

**C-10 -- Signal readiness:**
Check: Does SECTION G have >=2 measurable proceed signals and >=1 abort signal? Are they concrete enough to track in a real team context?
[ ] PASS  [ ] FAIL -- revise SECTION G

**C-11 -- Named inertia per archetype:**
Check: Count the archetypes that have a feature-specific Named Inertia entry in SECTION A -- entries that name a specific behavior, workflow, or tool (not generic resistance language). Is the count >=3?
Archetype count with feature-specific inertia: ___
[ ] PASS (>=3 archetypes with feature-specific, non-generic entries)
[ ] FAIL -- revise Named Inertia column in SECTION A for failing rows, then recount

**C-12 -- No orphan or conditional sections:**
Scan all sections A through G. Search for any of the following phrases or equivalents: "if applicable," "if confident," "optional," "if time permits," "you may skip," "if data is available," "if relevant."
[ ] None found -- PASS
[ ] Found: [list location] -- remove or make unconditional, then re-scan

All 12 items must show PASS before proceeding to artifact write.

---

Write artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`
