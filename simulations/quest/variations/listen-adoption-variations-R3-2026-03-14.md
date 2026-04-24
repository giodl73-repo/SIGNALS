Written to `simulations/quest/variations/listen-adoption-variations-R3-2026-03-14.md`.

---

## Summary

**Five R3 variations — targeting C-13 (inertia propagation), C-14 (champion double-anchor), C-15 (action vs. surveillance)**

| ID | Axis | C-13 | C-14 | C-15 | Expected |
|----|------|------|------|------|----------|
| **V-01** | Inertia ID citation system | IDs assigned at Step 1; downstream sections must cite by ID | Inherited (partial) | Inherited | ~115 |
| **V-02** | Champion double-anchor column | Partial (champion column creates back-ref) | 4-column champion table, EM Inertia mandatory | Inherited | ~115 |
| **V-03** | Action-verb enforcement | Inherited | Inherited | Anti-pattern list + "Team action:" prefix | ~115 |
| **V-04** | Combined: ID + double-anchor + action test | ID propagation stated numerically (must hit >=3 of 4 sections) | Double-anchor column enforced by template | Anti-pattern list + required action verb | **125** |
| **V-05** | Combined: GATE + self-audit (SA-1/SA-2/SA-3) | SA-1 counts citations; model must verify >=3 before writing | SA-2 checks each champion row for dual anchor | SA-3 scans mitigations for surveillance-only verbs | **125** |

**Key R3 design shift from R2:** R2 established the named inertia column as a structural property. R3 variations assume that column exists and attack three new failure modes: inertia that exists in Step 1 but never propagates (C-13), champion rationale with only one anchor (C-14), and churn mitigations that are purely passive surveillance (C-15).

**V-04 vs V-05 distinction:** V-04 enforces all three criteria through structural slots embedded in section instructions — the model fills table columns that mechanically require the right content. V-05 takes the post-hoc path — GATE + self-audit that forces the model to deliberate-check its own output before committing. Both should reach 125; the interesting question is which handles edge cases better (a model that fills the column generically vs a model that passes the self-audit by rationalizing surveillance as "action").
pected winner) |
| **V-05** | Combined: GATE + self-audit for C-13/C-14/C-15 | SA-1 counts inertia citations across 4 sections; model must verify >=3 | SA-2 checks each champion row for dual anchor presence | SA-3 scans mitigations for surveillance-only verbs | **125** (alt path) |

**Inherited R2 design baseline (all five variations):**
- All 16 stock roles named explicitly in the prompt
- Named Inertia column is a structural table property (R2 V-01 innovation)
- H/M/L delta scale defined in-prompt
- Feature-specific spread mechanisms required; generic word of mouth alone fails
- No conditional hedges or optional section qualifiers anywhere in the prompt

---

## V-01

**Variation axis:** Inertia framing -- inertia ID citation system for C-13 propagation
**Hypothesis:** C-13 fails when named inertia exists in the archetype table but no downstream section explicitly cites it by name. Assigning a short identifier to each inertia entry at definition time (I-PM, I-UX, I-01 through I-12, I-Support, I-SRE) makes downstream citation mechanically checkable: a reader can scan for "I-xx" references in the chasm, champion, churn, and intervention sections. C-13 becomes a citation-count problem, not a prose-interpretation problem. Expects C-13 pass; C-14 partial (archetype anchor only, no explicit EM-inertia column); C-15 partial (triggers named but no action-verb enforcement).

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

---

### Step 1 -- Archetype Map with Inertia IDs

Assign every stock role to one Rogers archetype. For each role, write the Named Inertia entry and assign it an inertia ID.

**Inertia ID format:** `I-{role}` (e.g., `I-PM`, `I-UX`, `I-01`, `I-02`, ..., `I-12`, `I-Support`, `I-SRE`).

The Named Inertia entry must be feature-specific. Generic entries fail: "may resist change," "prefers established workflows," "slow to adopt" are attitude labels, not named inertia. A passing entry names what the role actually does today to accomplish the goal this feature addresses (e.g., "I-PM: maintains a manually updated roadmap spreadsheet shared via email," "I-01: runs ad-hoc SQL queries and pastes results into Confluence").

| Role    | Archetype       | Rationale (1 sentence)              | Inertia ID | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | I-PM       | [feature-specific status-quo behavior]          |
| UX      | [archetype]     | [rationale]                         | I-UX       | [feature-specific status-quo behavior]          |
| C-01    | [archetype]     | [rationale]                         | I-01       | [feature-specific status-quo behavior]          |
| C-02    | [archetype]     | [rationale]                         | I-02       | [feature-specific status-quo behavior]          |
| C-03    | [archetype]     | [rationale]                         | I-03       | [feature-specific status-quo behavior]          |
| C-04    | [archetype]     | [rationale]                         | I-04       | [feature-specific status-quo behavior]          |
| C-05    | [archetype]     | [rationale]                         | I-05       | [feature-specific status-quo behavior]          |
| C-06    | [archetype]     | [rationale]                         | I-06       | [feature-specific status-quo behavior]          |
| C-07    | [archetype]     | [rationale]                         | I-07       | [feature-specific status-quo behavior]          |
| C-08    | [archetype]     | [rationale]                         | I-08       | [feature-specific status-quo behavior]          |
| C-09    | [archetype]     | [rationale]                         | I-09       | [feature-specific status-quo behavior]          |
| C-10    | [archetype]     | [rationale]                         | I-10       | [feature-specific status-quo behavior]          |
| C-11    | [archetype]     | [rationale]                         | I-11       | [feature-specific status-quo behavior]          |
| C-12    | [archetype]     | [rationale]                         | I-12       | [feature-specific status-quo behavior]          |
| Support | [archetype]     | [rationale]                         | I-Support  | [feature-specific status-quo behavior]          |
| SRE     | [archetype]     | [rationale]                         | I-SRE      | [feature-specific status-quo behavior]          |

---

### Step 2 -- Month-by-Month Adoption Timeline

Simulate the adoption curve forward from innovators. At least 3 distinct time steps. Rogers sequence must hold: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards -- no inversions.

For each archetype-to-archetype transition, name the spread mechanism. At least one transition must cite a mechanism specific to this feature context or name the inertia ID it is displacing; generic word of mouth alone fails.

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (cite inertia ID if displacing named behavior) |
|-------|------------------|----------------|----------------------------------------------------------------|
| M1    | Innovator        | ...            | ...                                                            |
| M2    | Early Adopter    | ...            | ...                                                            |
| M3    | [wave]           | ...            | ...                                                            |
| M4    | [wave]           | ...            | ...                                                            |
| M5    | [wave]           | ...            | ...                                                            |

Add rows as needed. Compress if fewer archetype waves apply.

---

### Step 3 -- Chasm Analysis

Name the chasm between Early Adopters and Early Majority. Address all three subsections.

**3a. Why this chasm exists**
Cite the inertia IDs for Early Majority roles from Step 1 by ID. The chasm exists because these specific inertia entries make incremental value hard to perceive for the EM cluster. Name them explicitly. Example structure: "The chasm is anchored by I-05, I-06, and I-07: each describes a workflow that already handles [core use case], so the EA enthusiasm signal cannot displace them on credibility alone." Generic diffusion theory does not pass.

**3b. Bridging mechanism**
Name the vehicle that directly addresses the cited inertia IDs. State which ID(s) this mechanism targets and how it displaces the status-quo behavior.

**3c. Champion network**

| Champion Role | Archetype       | Bridge Rationale (archetype-grounded)                      |
|---------------|-----------------|------------------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]     |
| ...           | ...             | ...                                                        |

At least 2 champions. Each rationale connects archetype position to credibility with the Early Majority cluster.

---

### Step 4 -- Churn Risk Register

For at least 2 archetypes, state the churn trigger and a mitigation.

**Churn trigger:** The specific event that causes the role to revert to their Named Inertia. Frame as "reverts to [inertia ID]" to maintain the citation chain from Step 1.

**Mitigation:** Name a mitigation or warning signal. At least one mitigation must name a concrete team action rather than a passive surveillance response.

| Archetype      | Churn Trigger (cite inertia ID)               | Mitigation / Warning Signal        |
|----------------|-----------------------------------------------|------------------------------------|
| ...            | Reverts to [I-xx]: [trigger event]            | ...                                |
| ...            | ...                                           | ...                                |

---

### Step 5 -- Interventions (Ranked by Adoption Delta)

List interventions ranked by adoption delta. Each intervention must cite the inertia ID(s) it targets.

**Delta scale:** H = shifts adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Inertia ID(s) Targeted                         |
|------|-------------|-------|------------------------------------------------|
| 1    | ...         | H     | I-[xx]: [what this intervention displaces]     |
| 2    | ...         | M     | I-[xx]: [what this intervention displaces]     |
| ...  | ...         | ...   | ...                                            |

At least 2 entries. Ranked in descending delta order.

---

### Step 6 -- Sensitivity Scenarios

Model two scenarios for chasm crossing. Each scenario names a different lever.

**Scenario 1 -- lever: [name it]**
Trajectory: [which archetype waves accelerate and when; cite which inertia IDs weaken under this lever]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves plateau or stall; cite which inertia IDs hold under this lever]

---

### Step 7 -- Signal Readiness

**Proceed signals (at least 2, measurable):**
1. [e.g., >=3 Early Majority roles running sustained workflows after month 3 without reverting to I-05/I-06]
2. [Measurable]

**Abort signal (at least 1, measurable):**
1. [Measurable condition]

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-02

**Variation axis:** Output format -- champion double-anchor column (C-14 structural enforcement)
**Hypothesis:** C-14 fails when champion rationale connects archetype position to EM credibility (C-05 pass) but does not also name the specific EM inertia the champion is positioned to overcome. Extending the champion table from 3 columns to 4 -- adding a mandatory "EM Inertia Bridged" column -- makes C-14 a table-completion problem. A blank or archetype-only entry is visually incomplete. The inertia column also creates a natural back-reference into the archetype map, partially satisfying C-13 through the champion section. Expects C-14 pass; C-13 partial (champion section cites inertia but chasm/interventions may not); C-15 inherited from R2 baseline.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

---

### Step 1 -- Archetype Map with Named Inertia

Assign every stock role to one Rogers archetype. For each role, populate the Named Inertia column with the specific behavior, workflow, or tool that role uses today instead of this feature.

Named Inertia must be feature-specific. Generic entries fail: "may resist change," "prefers established workflows," "slow to adopt" are attitude labels, not named inertia.

| Role    | Archetype       | Rationale (1 sentence)              | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| UX      | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-01    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-02    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-03    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-04    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-05    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-06    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-07    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-08    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-09    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-10    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-11    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-12    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| Support | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| SRE     | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |

---

### Step 2 -- Month-by-Month Adoption Timeline

Simulate the adoption curve forward from innovators. At least 3 distinct time steps. Rogers sequence must hold: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards -- no inversions.

For each archetype-to-archetype transition, name the spread mechanism specific to this feature. Generic word of mouth alone fails -- at least one transition must cite a mechanism tied to this feature context or the Named Inertia of the receiving archetype.

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific)              |
|-------|------------------|----------------|--------------------------------------------------|
| M1    | Innovator        | ...            | ...                                              |
| M2    | Early Adopter    | ...            | ...                                              |
| M3    | [wave]           | ...            | ...                                              |
| M4    | [wave]           | ...            | ...                                              |
| M5    | [wave]           | ...            | ...                                              |

---

### Step 3 -- Chasm Analysis

Name the chasm between Early Adopters and Early Majority.

**3a. Why this chasm exists**
Draw from the Named Inertia entries for Early Majority roles in Step 1. Name the specific inertia entries -- do not reproduce generic diffusion theory.

**3b. Bridging mechanism**
The specific vehicle that directly addresses those Named Inertia entries. State which inertia entries this mechanism displaces.

**3c. Champion network**

The champion table has four required columns. The fourth column -- EM Inertia Bridged -- is mandatory: state the specific Named Inertia entry from Step 1 that this champion is positioned to overcome. "Well-placed to influence the early majority" without naming the inertia fails the fourth column.

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (from Step 1)                           |
|---------------|-----------------|--------------------------------------------------------------|------------------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | [specific Named Inertia entry the champion can displace]   |
| ...           | ...             | ...                                                          | ...                                                        |

At least 2 champions. Both the archetype rationale column and the EM inertia column must be populated per row.

---

### Step 4 -- Churn Risk Register

For at least 2 archetypes, state what triggers churn and name a mitigation or warning signal.

Churn triggers must be named as reversion events: the specific situation that causes the role to return to the Named Inertia behavior from Step 1.

| Archetype      | Churn Trigger (reversion event)               | Mitigation / Warning Signal        |
|----------------|-----------------------------------------------|------------------------------------|
| ...            | ...                                           | ...                                |
| ...            | ...                                           | ...                                |

---

### Step 5 -- Interventions (Ranked by Adoption Delta)

List interventions ranked by adoption delta. Each intervention names which Named Inertia entry or friction it directly addresses.

**Delta scale:** H = shifts adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Named Inertia / Friction Addressed  |
|------|-------------|-------|-------------------------------------|
| 1    | ...         | H     | ...                                 |
| 2    | ...         | M     | ...                                 |
| ...  | ...         | ...   | ...                                 |

At least 2 entries. Ranked in descending delta order.

---

### Step 6 -- Sensitivity Scenarios

Model two scenarios for chasm crossing. Each scenario names a different lever.

**Scenario 1 -- lever: [name it]**
Trajectory: [which archetype waves accelerate; reference which Named Inertia entries weaken]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves plateau or stall; reference which Named Inertia entries hold]

---

### Step 7 -- Signal Readiness

**Proceed signals (at least 2, measurable):**
1. [e.g., >=3 Early Majority roles running sustained workflows after month 3]
2. [Measurable]

**Abort signal (at least 1, measurable):**
1. [Measurable condition]

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-03

**Variation axis:** Phrasing register -- action-verb enforcement for C-15 (churn mitigation quality)
**Hypothesis:** C-15 fails when churn mitigations consist of surveillance-only responses (monitor adoption, track usage, observe churn signals). The prompt can block this by: (a) providing an explicit anti-pattern list of disqualifying verbs, (b) requiring each mitigation to feature a concrete team action verb, and (c) using a labeled "Team action:" prefix as a structural template slot. This is a phrasing register variation -- the enforcement is done through labeled template slots and an explicit negative example, not a structural table column. Expects C-15 pass; C-13 partial (triggers reference inertia by name but no ID propagation system); C-14 inherited from R2 baseline.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

---

### Step 1 -- Archetype Map with Named Inertia

Assign every stock role to one Rogers archetype. For each role, write the Named Inertia -- the specific behavior, workflow, or tool the role uses today instead of this feature.

Named Inertia must be feature-specific. Generic entries fail: attitude labels ("may resist change," "slow to adopt new tooling") are not named inertia.

| Role    | Archetype       | Rationale (1 sentence)              | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| UX      | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-01    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-02    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-03    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-04    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-05    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-06    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-07    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-08    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-09    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-10    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-11    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| C-12    | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| Support | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |
| SRE     | [archetype]     | [rationale]                         | [feature-specific status-quo behavior]          |

---

### Step 2 -- Month-by-Month Adoption Timeline

Simulate the adoption curve forward from innovators. At least 3 distinct time steps. Rogers sequence must hold: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards -- no inversions.

For each archetype-to-archetype transition, name the spread mechanism specific to this feature. Generic word of mouth alone fails -- at least one transition must cite a mechanism tied to this feature context or the Named Inertia of the receiving archetype.

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific)              |
|-------|------------------|----------------|--------------------------------------------------|
| M1    | Innovator        | ...            | ...                                              |
| M2    | Early Adopter    | ...            | ...                                              |
| M3    | [wave]           | ...            | ...                                              |
| M4    | [wave]           | ...            | ...                                              |
| M5    | [wave]           | ...            | ...                                              |

---

### Step 3 -- Chasm Analysis

Name the chasm between Early Adopters and Early Majority.

**3a. Why this chasm exists**
Draw from the Named Inertia entries for Early Majority roles in Step 1. Name the specific inertia entries -- do not reproduce generic diffusion theory.

**3b. Bridging mechanism**
Name the vehicle that directly addresses those Named Inertia entries.

**3c. Champion network**

| Champion Role | Archetype       | Bridge Rationale                                           |
|---------------|-----------------|------------------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]     |
| ...           | ...             | ...                                                        |

At least 2 champions. Each rationale connects archetype position to EM credibility.

---

### Step 4 -- Churn Risk Register

For at least 2 archetypes, state the churn trigger and the mitigation.

**Churn trigger:** The specific event that causes the role to revert to their Named Inertia behavior from Step 1.

**Mitigation -- action test.** Each mitigation must name a concrete team action. Use active verbs: assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, escalate.

The following verbs are surveillance responses, not mitigations, and are not accepted: monitor, track, watch, observe, measure, check, review telemetry. A mitigation reading only "monitor usage for signs of churn" fails. "Assign a champion to run a follow-up training session within one week of the trigger" passes.

Mixed entries pass: an action followed by a measurement signal is acceptable. Example: "Assign a champion to retrain the team [action], then check adoption rate after 2 weeks [measurement]."

| Archetype      | Churn Trigger                                 | Mitigation (team action required -- surveillance-only not accepted) |
|----------------|-----------------------------------------------|---------------------------------------------------------------------|
| ...            | [reversion trigger naming Step 1 inertia]     | Team action: [assign / deliver / remove / bundle / ...]             |
| ...            | ...                                           | Team action: [...]                                                  |

---

### Step 5 -- Interventions (Ranked by Adoption Delta)

List interventions ranked by adoption delta. Each intervention names which Named Inertia entry or friction it targets.

**Delta scale:** H = shifts adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Named Inertia / Friction Addressed  |
|------|-------------|-------|-------------------------------------|
| 1    | ...         | H     | ...                                 |
| 2    | ...         | M     | ...                                 |
| ...  | ...         | ...   | ...                                 |

At least 2 entries. Ranked in descending delta order.

---

### Step 6 -- Sensitivity Scenarios

Model two scenarios for chasm crossing. Each scenario names a different lever.

**Scenario 1 -- lever: [name it]**
Trajectory: [which archetype waves accelerate; reference which Named Inertia entries weaken]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves plateau or stall; reference which Named Inertia entries hold]

---

### Step 7 -- Signal Readiness

**Proceed signals (at least 2, measurable):**
1. [e.g., >=3 Early Majority roles running sustained workflows after month 3]
2. [Measurable]

**Abort signal (at least 1, measurable):**
1. [Measurable condition]

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-04

**Variation axis:** Combined -- inertia ID citation system (C-13) + champion double-anchor column (C-14) + action-verb enforcement (C-15)
**Hypothesis:** V-01, V-02, V-03 each address one R3 criterion in isolation. V-04 applies all three mechanisms simultaneously. Inertia IDs from Step 1 are required by explicit citation in Steps 3a, 3c (champion table), Step 4 (churn trigger framing), and Step 5 (intervention column). The propagation requirement is stated numerically -- the model is told it must cite inertia IDs in at least 3 of the 4 downstream sections -- removing any ambiguity about C-13's threshold. The champion table has a mandatory EM Inertia Bridged column. The churn register uses the action-verb test from V-03 with the same anti-pattern list. This is the expected 125-point candidate.

---

You are running the `listen-adoption` skill for Signal.

**Inputs:**
- Topic (required): the feature being evaluated
- Signal (optional): prior signal artifacts -- read them if present before proceeding

**All 16 stock roles must appear:** PM, UX, C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, Support, SRE

---

### Step 1 -- Archetype Map with Inertia IDs

Assign every stock role to one Rogers archetype. For each role, write the Named Inertia entry and assign it an inertia ID.

**Inertia ID format:** `I-{role}` (e.g., `I-PM`, `I-UX`, `I-01`, `I-02`, ..., `I-12`, `I-Support`, `I-SRE`).

Named Inertia must be feature-specific. Generic entries fail: "may resist change," "prefers established workflows," "slow to adopt" are attitude labels, not named inertia. A passing entry names what the role actually does today to accomplish the goal this feature addresses.

| Role    | Archetype       | Rationale (1 sentence)              | Inertia ID | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | I-PM       | [feature-specific status-quo behavior]          |
| UX      | [archetype]     | [rationale]                         | I-UX       | [feature-specific status-quo behavior]          |
| C-01    | [archetype]     | [rationale]                         | I-01       | [feature-specific status-quo behavior]          |
| C-02    | [archetype]     | [rationale]                         | I-02       | [feature-specific status-quo behavior]          |
| C-03    | [archetype]     | [rationale]                         | I-03       | [feature-specific status-quo behavior]          |
| C-04    | [archetype]     | [rationale]                         | I-04       | [feature-specific status-quo behavior]          |
| C-05    | [archetype]     | [rationale]                         | I-05       | [feature-specific status-quo behavior]          |
| C-06    | [archetype]     | [rationale]                         | I-06       | [feature-specific status-quo behavior]          |
| C-07    | [archetype]     | [rationale]                         | I-07       | [feature-specific status-quo behavior]          |
| C-08    | [archetype]     | [rationale]                         | I-08       | [feature-specific status-quo behavior]          |
| C-09    | [archetype]     | [rationale]                         | I-09       | [feature-specific status-quo behavior]          |
| C-10    | [archetype]     | [rationale]                         | I-10       | [feature-specific status-quo behavior]          |
| C-11    | [archetype]     | [rationale]                         | I-11       | [feature-specific status-quo behavior]          |
| C-12    | [archetype]     | [rationale]                         | I-12       | [feature-specific status-quo behavior]          |
| Support | [archetype]     | [rationale]                         | I-Support  | [feature-specific status-quo behavior]          |
| SRE     | [archetype]     | [rationale]                         | I-SRE      | [feature-specific status-quo behavior]          |

**Propagation requirement:** The inertia IDs assigned here must be cited by ID in at least 3 of the following 4 downstream sections: chasm analysis (Step 3a), champion network (Step 3c), churn trigger register (Step 4), intervention list (Step 5). A downstream section satisfies this requirement only if it names at least one specific inertia ID (e.g., "I-05") -- paraphrase without ID citation does not count.

---

### Step 2 -- Month-by-Month Adoption Timeline

Simulate the adoption curve forward from innovators. At least 3 distinct time steps. Rogers sequence must hold: Innovators -> Early Adopters -> Early Majority -> Late Majority -> Laggards -- no inversions.

For each archetype-to-archetype transition, name the spread mechanism. At least one transition must name a mechanism specific to this feature context or name the inertia ID it is displacing; generic word of mouth alone fails.

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific; cite inertia ID if displacing named behavior) |
|-------|------------------|----------------|-----------------------------------------------------------------------------------|
| M1    | Innovator        | ...            | ...                                                                               |
| M2    | Early Adopter    | ...            | ...                                                                               |
| M3    | [wave]           | ...            | ...                                                                               |
| M4    | [wave]           | ...            | ...                                                                               |
| M5    | [wave]           | ...            | ...                                                                               |

---

### Step 3 -- Chasm Analysis

Name the chasm between Early Adopters and Early Majority.

**3a. Why this chasm exists**
Cite the inertia IDs for Early Majority roles from Step 1 by ID. The chasm exists because these specific inertia entries make incremental value hard to perceive for the EM cluster. Name them explicitly. Example structure: "The chasm is anchored by I-05, I-06, and I-07: each describes a workflow that already handles [core use case]. The EA enthusiasm signal cannot bridge this because..." Generic diffusion theory does not pass this section.

**3b. Bridging mechanism**
Name the vehicle that directly addresses the cited inertia IDs. State which ID(s) this mechanism targets and how it displaces the status-quo behavior.

**3c. Champion network**

The champion table has four required columns. The fourth column -- EM Inertia Bridged -- is mandatory. State the specific inertia ID from Step 1 that this champion is positioned to overcome. "Well-placed to influence the early majority" without naming the inertia ID fails the fourth column even if column 3 passes.

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (ID + named inertia)         |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | I-[xx]: [the named inertia they bridge]         |
| ...           | ...             | ...                                                          | I-[xx]: [the named inertia they bridge]         |

At least 2 champions. Both column 3 and column 4 must be populated per row.

---

### Step 4 -- Churn Risk Register

For at least 2 archetypes, state the churn trigger and the mitigation.

**Churn trigger:** The specific event that causes the role to revert to the Named Inertia from Step 1. Frame as "reverts to [inertia ID]" to satisfy the propagation requirement from Step 1.

**Mitigation -- action test:** Each mitigation must name a concrete team action. Valid action verbs: assign, deliver, remove, bundle, redesign, provide, embed, demo, pair, retrain, escalate. The following are surveillance responses and are not accepted as mitigations: monitor, track, watch, observe, measure, check, review telemetry. A mitigation reading only "monitor churn signals via telemetry" fails; "assign a champion to deliver a targeted re-onboarding session within 5 business days of the trigger event" passes. Mixed entries (action + optional measurement signal) pass.

| Archetype      | Churn Trigger (cite inertia ID)               | Mitigation (concrete team action -- no surveillance-only)   |
|----------------|-----------------------------------------------|-------------------------------------------------------------|
| ...            | Reverts to [I-xx]: [trigger event]            | [assign / deliver / remove / bundle / ...]: [specific action] |
| ...            | ...                                           | ...                                                         |

---

### Step 5 -- Interventions (Ranked by Adoption Delta)

List interventions ranked by adoption delta. Each intervention must cite the inertia ID(s) it targets.

**Delta scale:** H = shifts adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Inertia ID(s) Targeted                         |
|------|-------------|-------|------------------------------------------------|
| 1    | ...         | H     | I-[xx]: [what this intervention displaces]     |
| 2    | ...         | M     | I-[xx]: [what this intervention displaces]     |
| ...  | ...         | ...   | ...                                            |

At least 2 entries. Ranked in descending delta order.

---

### Step 6 -- Sensitivity Scenarios

Model two scenarios for chasm crossing. Each scenario names a different lever.

**Scenario 1 -- lever: [name it]**
Trajectory: [which archetype waves accelerate and when; cite which inertia IDs weaken under this lever]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves plateau or stall; cite which inertia IDs hold under this lever]

---

### Step 7 -- Signal Readiness

**Proceed signals (at least 2, measurable):**
1. [e.g., >=3 Early Majority roles running sustained workflows after month 3 without reverting to I-05/I-06]
2. [Measurable]

**Abort signal (at least 1, measurable):**
1. [Measurable condition]

---

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`

---

## V-05

**Variation axis:** Combined -- GATE structure + self-audit for C-13, C-14, C-15
**Hypothesis:** V-04 enforces C-13/C-14/C-15 through structural table slots and explicit propagation requirements embedded in section instructions. V-05 takes the alternate path: it inherits the GATE structure from R2 V-02 and adds three new self-audit items at the end that require the model to explicitly verify C-13, C-14, and C-15 before writing the artifact. Self-audit forces deliberate checking: count inertia citations across sections (C-13), confirm each champion has two anchors (C-14), scan mitigations for surveillance-only phrasing (C-15). This tests whether post-hoc self-checking achieves the same result as structural enforcement -- and whether it catches errors that structural columns might miss when the model fills them generically.

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
- The Named Inertia column is populated for every row with a feature-specific statement
- Generic entries fail GATE A: "may resist change," "prefers established workflows," "slow to adopt new tooling" are not named inertia

| Role    | Archetype       | Rationale (1 sentence)              | Named Inertia (what they do today instead)      |
|---------|-----------------|-------------------------------------|-------------------------------------------------|
| PM      | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| UX      | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-01    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-02    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-03    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-04    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-05    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-06    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-07    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-08    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-09    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-10    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-11    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| C-12    | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| Support | [archetype]     | [rationale]                         | [named status-quo behavior]                     |
| SRE     | [archetype]     | [rationale]                         | [named status-quo behavior]                     |

---

### SECTION B -- Adoption Timeline

**GATE B -- all of the following must be true before proceeding:**
- At least 3 distinct time steps
- Rogers sequence intact: Innovators before Early Adopters; Early Adopters before Early Majority; Early Majority before Late Majority; Late Majority before Laggards
- Each archetype-level transition has a named spread mechanism; at least one mechanism must be specific to this feature context or the receiving archetype's Named Inertia

| Month | Archetype Wave   | Roles Adopting | Spread Mechanism (feature-specific)              |
|-------|------------------|----------------|--------------------------------------------------|
| M1    | Innovator        | ...            | ...                                              |
| M2    | Early Adopter    | ...            | ...                                              |
| M3    | [wave]           | ...            | ...                                              |
| M4    | [wave]           | ...            | ...                                              |
| M5    | [wave]           | ...            | ...                                              |

---

### SECTION C -- Chasm Analysis

**GATE C -- all of the following must be true before proceeding:**
- The word "chasm" appears in this section
- Named Inertia entries for Early Majority roles from SECTION A are cited by name in the chasm explanation
- A bridging mechanism is named that directly addresses those Named Inertia entries
- Champion table has at least 2 rows; archetype rationale and EM Inertia columns are both populated per row

**C1. Why this chasm exists**
[Draw from the EM Named Inertia in SECTION A. Name the specific inertia entries. Do not reproduce generic diffusion theory.]

**C2. Bridging mechanism**
[Vehicle that directly addresses those Named Inertia entries. State which entries it displaces.]

**C3. Champion network**

| Champion Role | Archetype       | Archetype Bridge Rationale                                  | EM Inertia Bridged (from Section A)             |
|---------------|-----------------|--------------------------------------------------------------|-------------------------------------------------|
| ...           | Early Adopter   | [why their EA position gives them credibility with EM]       | [Named Inertia entry the champion can displace] |
| ...           | ...             | ...                                                          | ...                                             |

---

### SECTION D -- Churn Risk Register

**GATE D -- all of the following must be true before proceeding:**
- At least 2 archetype rows
- Each churn trigger is named as a reversion event (what causes the role to return to their SECTION A Named Inertia)
- Every mitigation names a concrete team action; surveillance-only responses are disqualified: monitor, track, watch, observe, measure, check, review telemetry are not mitigations by themselves; every mitigation must include a concrete action verb (assign, deliver, remove, bundle, retrain, pair, embed, demo, etc.); mixed entries (action + measurement signal) pass

| Archetype      | Churn Trigger (reversion to SECTION A inertia)| Mitigation (concrete team action -- surveillance-only fails) |
|----------------|-----------------------------------------------|--------------------------------------------------------------|
| ...            | ...                                           | ...                                                          |
| ...            | ...                                           | ...                                                          |

---

### SECTION E -- Interventions (Ranked by Adoption Delta)

**GATE E -- all of the following must be true before proceeding:**
- At least 2 entries; list is in descending delta order
- Each entry has a delta label (H, M, or L)
- Each intervention names a specific Named Inertia entry or friction from SECTION A or SECTION C

**Delta scale:** H = shifts adoption by at least one full archetype wave within one quarter; M = meaningful acceleration, sub-wave; L = directional, marginal near-term impact.

| Rank | Intervention | Delta | Named Inertia / Friction Addressed  |
|------|-------------|-------|-------------------------------------|
| 1    | ...         | H     | ...                                 |
| 2    | ...         | M     | ...                                 |
| ...  | ...         | ...   | ...                                 |

---

### SECTION F -- Sensitivity Scenarios

**GATE F -- all of the following must be true before proceeding:**
- Two named scenarios present; each names a different lever
- Each scenario shows a distinct adoption trajectory referencing Named Inertia entries from SECTION A

**Scenario 1 -- lever: [name it]**
Trajectory: [which waves accelerate; which Named Inertia entries weaken]

**Scenario 2 -- lever: [name it]**
Trajectory: [which waves stall; which Named Inertia entries hold]

---

### SECTION G -- Signal Readiness

**GATE G -- all of the following must be true before proceeding:**
- At least 2 measurable proceed signals
- At least 1 measurable abort signal
- All signals are concrete and trackable; vague signals ("adoption increases," "team feels ready") fail

**Proceed signals:**
1. [Measurable]
2. [Measurable]

**Abort signal:**
1. [Measurable condition]

---

### SELF-AUDIT -- Run before writing the artifact

Before writing the artifact, complete all three self-audit checks. Show the self-audit results in your response. Do not write the artifact until all three pass.

**SA-1 -- C-13 (Named inertia propagation):**
Count how many of the following four sections contain at least one explicit Named Inertia citation from SECTION A:
- SECTION C1 (chasm explanation): [yes/no -- list which inertia entries cited]
- SECTION C3 (champion EM Inertia column): [yes/no -- list which inertia entries cited]
- SECTION D (churn triggers): [yes/no -- list which inertia entries cited]
- SECTION E (interventions): [yes/no -- list which inertia entries cited]

Total: [count] of 4 sections. C-13 requires >=3. If count < 3: revise the failing sections before proceeding.

SA-1 result: [PASS if count >=3 / FAIL if count <3]

**SA-2 -- C-14 (Champion double-anchor):**
For each champion row in SECTION C:
- Row 1 champion [role]: Archetype bridge rationale present? [yes/no]. EM Inertia Bridged column populated with specific Named Inertia entry? [yes/no]. "Well-placed to influence early majority" without naming the inertia = no.
- Row 2 champion [role]: [same check]
- [Repeat for additional rows]

C-14 requires both columns populated for every champion row. If any row fails: revise before proceeding.

SA-2 result: [PASS / FAIL -- note which rows fail]

**SA-3 -- C-15 (Churn mitigation action test):**
For each mitigation in SECTION D, answer:
- Does this mitigation include a concrete team action verb (assign, deliver, remove, bundle, retrain, pair, embed, demo, escalate)? [yes/no]
- Is this mitigation phrased solely as surveillance (monitor, track, watch, observe, measure, check, review telemetry)? [yes/no -- if yes, this entry fails]

C-15 requires zero surveillance-only mitigations. If any mitigation fails: replace with a concrete action before proceeding. Mixed entries pass.

SA-3 result: [PASS / FAIL -- note which entries fail]

---

All three self-audit items must show PASS before the artifact is written.

Write the artifact to: `simulations/listen/adoption/{topic}-adoption-{date}.md`
