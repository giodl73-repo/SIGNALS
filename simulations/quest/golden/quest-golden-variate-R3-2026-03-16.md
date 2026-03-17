---
skill: quest-variate
skill_target: quest-golden
round: 3
date: 2026-03-16
rubric: simulations/quest/rubrics/quest-golden-rubric-v3-2026-03-16.md
rubric_version: v3
---

# quest-golden -- Round 3 Variations (V-01 through V-05)

Generated against rubric v3 (14 criteria, C-01..C-14, aspirational denominator = 6).
Single-axis variations for V-01 through V-04. Full synthesis for V-05.

**Axes covered:**
- V-01: spread-design phase (lifecycle emphasis) -- mandatory axis-assignment pre-phase before variation generation
- V-02: named-round convergence gate (phrasing register) -- quest convergence gate names specific round numbers
- V-03: PARTIAL amplifier trajectory table (output format) -- persistent PARTIAL tracking across rounds
- V-04: pre-printed scoring matrix (output format) -- skeleton criterion x variation grid in Phase 2
- V-05: full synthesis (V-01 + V-02 + V-04 combined)

**R2 mechanisms carried forward in all R3 variations (from V-05-R2, composite 100):**
- PHASE 0 inertia naming + rubric load with rationale gate
- Inertia pseudo-variation in Phase 2 leaderboard
- TOP HAD / SECOND LACKED + TOP HAD / INERTIA LACKED delta block in QU2
- QU2 precedes QU3 with explicit "because" rationale clause
- Output contract: verbatim artifact + anti-pattern exclusion language
- Structural termination isolation (PHASE 4 separate from PHASE 3)
- Round Log with inertia-delta column
- What Made It Golden narrative (>= 2 mechanisms with round citations)
- Ablated criteria section (explicit null case)

**Rubric v3 formula:**
Score = (essential_pass/5)*60 + (recommended_pass/3)*30 + (aspirational_pass/6)*10
Golden threshold: all 5 essential PASS AND composite >= 80.

---

## Spread-Design Table

| Plan | Axis | Source signal | Target criteria | Predicted composite |
|------|------|--------------|-----------------|---------------------|
| V-01 | lifecycle emphasis (spread-design phase) | quest-golden.t3 SPREAD-DESIGN PHASE; no current variation enforces divergence before body writing | Potential new pattern: does axis pre-planning prevent duplication in ways rubric does not capture? | 100 |
| V-02 | phrasing register (named-round convergence gate) | Gap: convergence table uses abstract "previous round" -- naming rounds makes false-YES structurally harder | C-01 depth; potential new precision pattern | 100 |
| V-03 | output format (PARTIAL amplifier trajectory table) | quest-golden.t3 PARTIAL AMPLIFIER table; gap: PARTIAL scores are invisible to convergence check | Potential new pattern: PARTIAL tracking reveals systematic under-activation | 100 |
| V-04 | output format (pre-printed scoring matrix) | scout-feasibility R3 template approach; gap: Phase 2 scoring can omit criteria without structural surface | Potential new pattern: criterion-completeness enforcement in scoring | 100 |
| V-05 | combination: V-01 + V-02 + V-04 | All three R3 single-axis mechanisms; independent, non-interfering | Additive composite; expected highest structural reliability | 100 |

---

## V-01 -- Spread-Design Phase First

**axis:** lifecycle emphasis -- mandatory spread-design pre-phase before variation generation
**hypothesis:** Requiring a formal axis-assignment table before writing any variation body prevents
accidental axis duplication and ensures each variation diverges on a distinct dimension. V-05-R2
instructs "single-axis first; combinations later" but provides no structural mechanism to enforce
that design intent before the bodies are written. The spread-design phase makes divergence planning
an auditable, gated step. If a reader produces two V-XX with the same axis, the spread-design gate
catches it before bodies are written.

---

Find the golden prompt for a target skill by systematically outcompeting inertia -- the
unconstrained baseline a capable model produces without variation, rubric, or iteration.
The goal is dual convergence: all essential criteria passing AND no new inertia improvements
discoverable for two consecutive rounds. The converged prompt body is the golden prompt.

---

### PHASE 0 -- SETUP

**Entry condition:** skill name provided.

**Procedure:**
1. **Name the inertia prompt.** Write one paragraph: the prompt body a capable model produces
   for this skill without a quest loop -- no rubric, no variation axis, no convergence logic.
   This is the primary competitor. All variations are compared against it.
2. **Load the rubric.** Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load latest version.
   If no rubric exists: invoke quest-rubric before proceeding. The rubric must exist before
   scoring because variation rankings without a grounded objective function are not comparable
   -- "beating inertia" is only measurable against explicit criteria.
3. Record: inertia summary, rubric path, version, criteria count.

**Exit condition:** inertia documented and rubric loaded.

---

### SPREAD-DESIGN

**Entry condition:** Phase 0 complete. Execute before writing any variation body.

**Procedure:**
1. List the axis bank (do not add axes not on this list):
   - Role sequence (which roles run first, in what order)
   - Output format (table vs prose vs list; scoring granularity)
   - Lifecycle emphasis (phase space allocation; boundary explicitness)
   - Phrasing register (formal/technical vs conversational; imperative vs descriptive)
   - Inertia framing (prominence of status-quo competitor)

2. Assign axes to variations. Round 1: one axis per variation (single-axis isolation).
   Round 2+: consult PARTIAL AMPLIFIER TRAJECTORY TABLE before assigning (see Round Log
   for any PARTIAL entries from prior rounds).

3. Produce the axis-assignment plan:

| Plan | Axis | Source signal | Target criteria | Predicted composite |
|------|------|--------------|-----------------|---------------------|
| V-01 | [axis] | [why this axis] | [which criteria] | [score] |
| V-02 | | | | |
| V-03 | | | | |
| V-04 | | | | |
| V-05 | | | | |

4. Confirm: do any two variations share the same axis? If yes, redesign before proceeding.
   If all axes distinct: SPREAD-DESIGN COMPLETE.

**Exit condition:** axis-assignment table complete with no duplicate single axes; confirmed
before proceeding to PHASE 1.

---

### PHASE 1 -- VARIATION

**Entry condition:** Spread-design complete and confirmed.

**Procedure:**
Generate 5 complete, runnable prompt body variations. Each = full prompt text. No diffs.
No summaries. Axis per variation must match spread-design table.

Label each:
- **Axis:** dimension being varied (must match spread-design table)
- **Hypothesis:** why this axis is expected to outperform inertia
- **Inertia delta:** one phrase -- what this variation adds that the inertia baseline lacks

**Exit condition:** 5 labeled complete variations ready.

---

### PHASE 2 -- SCORING

**Entry condition:** Phase 1 complete; rubric loaded.

**Procedure:**
Score each variation against every criterion (pass/fail + evidence). Compute composite.
Add inertia as a pseudo-variation scored against the same rubric.

| Rank | ID      | Composite | vs Inertia | Notes |
|------|---------|-----------|------------|-------|
| 1    | V-XX    | NN        | +NN        | ...   |
| ...  | ...     | ...       | ...        | ...   |
| --   | INERTIA | NN        | baseline   | unconstrained |

**Exit condition:** ranked leaderboard with inertia row anchoring comparison.

---

### PHASE 3 -- ANALYSIS

**Entry condition:** Phase 2 complete (leaderboard with inertia row available).

**Step QU2 -- Delta Extraction:**

QU2 must precede QU3 because a criterion not grounded in an observed output gap is an
editorial guess, not a discovery -- the loop's value is in what it measures, not what the
author expected. Proposing criteria before naming the gap means the rubric is shaped by
priors, not by what the loop found.

Compare the top variation against two references: second-ranked AND inertia. The inertia
contrast is primary. Fill the delta block:

```
TOP VARIATION:           [V-XX]
SECOND-RANKED:           [V-YY]
TOP HAD / SECOND LACKED: [element present in top, absent from second -- stated as an absence]
TOP HAD / INERTIA LACKED:[element present in top, absent from inertia -- this is the discovery]
SIGNAL NAME:             SIGNAL-R{N}: [name] | none
```

The signal is `none` if the "TOP HAD / INERTIA LACKED" field cannot be filled with a
structural difference. A variation that outscores the runner-up but produces nothing inertia
lacked is not a discovery.

**Step QU3 -- Criterion Proposal (only if signal is not `none`):**

Translate the delta into a criterion. Required fields:
- **Text:** one sentence on what it measures
- **Tier:** essential / recommended / aspirational (assign based on severity of absence --
  essential = output is wrong without it; recommended = better with it; aspirational = excellent)
- **Pass: LOCATION** -- where in the output
- **Pass: OBSERVABLE** -- what specific element must be present
- **Pass: STANDARD** -- what separates pass from fail

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

**Exit condition:** delta block filled with inertia contrast; rubric updated if approved.

---

### PHASE 4 -- CONVERGENCE CHECK

**Entry condition:** Phase 3 complete.

Both conditions must be true before the loop exits -- trial convergence alone means the rubric
stopped evolving before all patterns were found; quest convergence alone means signals ran out
before variations reached the essential bar.

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations pass all essential criteria | YES / NO |
| Quest convergence: this round signal = none AND previous round signal = none | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log and return to SPREAD-DESIGN.

---

### Round Log

| Round | Top  | vs Inertia | QU2 delta (signal) | Criterion    |
|-------|------|------------|--------------------|--------------|
| R-01  | V-XX | +NN        | SIGNAL or none     | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**Both artifacts are required. The loop is not complete until both are verified.**
Do not summarize either. Do not reference a prior variation by name.
Write the complete contents of each file.

**Artifact 1 -- Golden prompt**
Path: `simulations/quest/golden/{skill}-golden-{date}.md`

Required contents:
- Complete prompt body verbatim -- every line that belongs in the deployed skill body,
  not a summary, not "see V-04," not a compressed version. If a reader cannot run this text
  directly as a skill body, it fails this requirement.
- Section "What Made It Golden" immediately after the body: for each structural mechanism
  the loop discovered, state the round it was found and the specific inertia gap it closed.
  Minimum 2 mechanisms with round citations and inertia-gap descriptions.

**Artifact 2 -- Final rubric**
Path: `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`

Required contents:
- All converged criteria (text, tier, pass conditions for each)
- Composite formula with denominator
- Golden threshold stated explicitly
- Version history table
- Standalone file separate from Artifact 1 -- the rubric is the theory of excellence;
  the golden prompt is the evidence; they must be legible independently

**Ablated criteria:** list criteria with zero activations across all rounds and a suggested
probe for each. If none: "No ablated criteria."

---

## V-02 -- Named-Round Convergence Gate

**axis:** phrasing register -- quest convergence gate names the specific round numbers being
compared, not just "previous round"
**hypothesis:** The abstract phrase "previous round signal = none" can be satisfied by a model
that does not explicitly consult the Round Log before declaring convergence. Requiring the model
to write "Round [N] signal = [name or none] AND Round [N-1] signal = [name or none]" forces it
to retrieve concrete round entries before filling the gate. V-05-R2 uses abstract language;
this variation makes the round reference a structural requirement, not a reading exercise.
A model cannot declare Quest convergence YES without citing two named rounds from the log.

---

Find the golden prompt for a target skill by systematically outcompeting inertia -- the
unconstrained baseline a capable model produces without variation, rubric, or iteration.
The goal is dual convergence: all essential criteria passing AND no new inertia improvements
discoverable for two consecutive rounds. The converged prompt body is the golden prompt.

---

### PHASE 0 -- SETUP

**Entry condition:** skill name provided.

**Procedure:**
1. **Name the inertia prompt.** Write one paragraph: the prompt body a capable model produces
   for this skill without a quest loop -- no rubric, no variation axis, no convergence logic.
   This is the primary competitor and the reference for all QU2 contrasts.
2. **Load the rubric.** Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load latest version.
   If no rubric exists: invoke quest-rubric. The rubric must exist before scoring because
   variation rankings without a grounded objective function are not comparable -- "beating
   inertia" is only measurable against explicit criteria.
3. Record: inertia summary, rubric path, version, criteria count.

**Exit condition:** inertia documented and rubric loaded.

---

### PHASE 1 -- VARIATION

**Entry condition:** Phase 0 complete.

**Procedure:**
Generate 5 complete, runnable prompt body variations. Each = full prompt text. No diffs.
No summaries. Single-axis first; combinations in later rounds.

Label each:
- **Axis:** dimension being varied
- **Hypothesis:** why this axis outperforms inertia
- **Inertia delta:** one phrase -- what this variation adds that the inertia baseline lacks

**Exit condition:** 5 labeled complete variations ready.

---

### PHASE 2 -- SCORING

**Entry condition:** Phase 1 complete; rubric loaded.

**Procedure:**
Score each variation against every criterion (pass/fail + evidence). Compute composite.
Add inertia as a pseudo-variation scored against the same rubric.

| Rank | ID      | Composite | vs Inertia | Notes |
|------|---------|-----------|------------|-------|
| 1    | V-XX    | NN        | +NN        | ...   |
| ...  | ...     | ...       | ...        | ...   |
| --   | INERTIA | NN        | baseline   | unconstrained |

**Exit condition:** ranked leaderboard with inertia anchoring.

---

### PHASE 3 -- ANALYSIS

**Entry condition:** Phase 2 complete (leaderboard with inertia row available).

**Step QU2 -- Delta Extraction:**

QU2 must precede QU3 because a criterion not grounded in an observed output gap is an
editorial guess, not a discovery -- the loop's value is in what it measures, not what the
author expected.

Compare the top variation against two references: second-ranked AND inertia. The inertia
contrast is primary. Fill the delta block:

```
TOP VARIATION:           [V-XX]
SECOND-RANKED:           [V-YY]
TOP HAD / SECOND LACKED: [element present in top, absent from second -- stated as an absence]
TOP HAD / INERTIA LACKED:[element present in top, absent from inertia -- this is the discovery]
SIGNAL NAME:             SIGNAL-R{N}: [name] | none
```

The signal is `none` if the "TOP HAD / INERTIA LACKED" field cannot be filled with a
structural difference. A variation that outscores the runner-up but produces nothing inertia
lacked is not a discovery.

**Step QU3 -- Criterion Proposal (only if signal is not `none`):**

Translate the delta into a criterion. Required fields:
- **Text:** one sentence on what it measures
- **Tier:** essential / recommended / aspirational (assign based on severity of absence --
  essential = output is wrong without it; recommended = better with it; aspirational = excellent)
- **Pass: LOCATION** -- where in the output
- **Pass: OBSERVABLE** -- what specific element must be present
- **Pass: STANDARD** -- what separates pass from fail

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

**Exit condition:** delta block filled with inertia contrast; rubric updated if approved.

---

### PHASE 4 -- CONVERGENCE CHECK

**Entry condition:** Phase 3 complete. Consult Round Log before filling this table.

Both conditions must be true before the loop exits -- trial convergence alone means the rubric
stopped evolving before all patterns were found; quest convergence alone means signals ran out
before variations reached the essential bar.

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations in Round [N] pass all essential criteria | YES / NO |
| Quest convergence: Round [N] signal = [name or none] AND Round [N-1] signal = [name or none] | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

**Fill the bracketed values from the Round Log.** Do not declare Quest convergence YES unless
both named rounds are shown in the Round Log with explicit signal values. Declaring convergence
without citing both rounds by number is a structural violation of the dual-gate check.

If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log and return to PHASE 1.

---

### Round Log

| Round | Top  | vs Inertia | QU2 delta (signal) | Criterion    |
|-------|------|------------|--------------------|--------------|
| R-01  | V-XX | +NN        | SIGNAL or none     | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**Both artifacts are required. The loop is not complete until both are verified.**
Do not summarize either. Do not reference a prior variation by name.
Write the complete contents of each file.

**Artifact 1 -- Golden prompt**
Path: `simulations/quest/golden/{skill}-golden-{date}.md`

Required contents:
- Complete prompt body verbatim -- every line that belongs in the deployed skill body,
  not a summary, not "see V-02," not a compressed version. If a reader cannot run this text
  directly as a skill body, it fails this requirement.
- Section "What Made It Golden" immediately after the body: for each structural mechanism
  the loop discovered, state the round it was found and the specific inertia gap it closed.
  Minimum 2 mechanisms with round citations and inertia-gap descriptions.

**Artifact 2 -- Final rubric**
Path: `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`

Required contents:
- All converged criteria (text, tier, pass conditions for each)
- Composite formula with denominator
- Golden threshold stated explicitly
- Version history table
- Standalone file separate from Artifact 1 -- the rubric is the theory of excellence;
  the golden prompt is the evidence; they must be legible independently

**Ablated criteria:** list criteria with zero activations across all rounds and a suggested
probe for each. If none: "No ablated criteria."

---

## V-03 -- PARTIAL Amplifier Trajectory Table

**axis:** output format -- adds a persistent PARTIAL amplifier trajectory table in Phase 3
that accumulates PARTIAL scores across rounds and recommends targeted action
**hypothesis:** V-05-R2 has no mechanism for tracking criteria that score PARTIAL consistently
across rounds. Such criteria are invisible to the convergence check (they do not break trial
convergence) but represent systematically undertested rubric dimensions. A PARTIAL tracking
table surfaces them before they become structural failures and enables targeted axis assignment
in subsequent rounds. The table distinguishes first occurrence (monitor), second (combination
axis), and third+ (rubric clarification).

---

Find the golden prompt for a target skill by systematically outcompeting inertia -- the
unconstrained baseline a capable model produces without variation, rubric, or iteration.
The goal is dual convergence: all essential criteria passing AND no new inertia improvements
discoverable for two consecutive rounds. The converged prompt body is the golden prompt.

---

### PHASE 0 -- SETUP

**Entry condition:** skill name provided.

**Procedure:**
1. **Name the inertia prompt.** Write one paragraph: the prompt body a capable model produces
   for this skill without a quest loop -- no rubric, no variation axis, no convergence logic.
   This is the primary competitor and the reference for all QU2 contrasts.
2. **Load the rubric.** Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load latest version.
   If no rubric exists: invoke quest-rubric. The rubric must exist before scoring because
   variation rankings without a grounded objective function are not comparable -- "beating
   inertia" is only measurable against explicit criteria.
3. Record: inertia summary, rubric path, version, criteria count.

**Exit condition:** inertia documented and rubric loaded.

---

### PHASE 1 -- VARIATION

**Entry condition:** Phase 0 complete.

**Procedure:**
Generate 5 complete, runnable prompt body variations. Each = full prompt text. No diffs.
No summaries. Single-axis first; combinations in later rounds.

Label each:
- **Axis:** dimension being varied
- **Hypothesis:** why this axis outperforms inertia
- **Inertia delta:** one phrase -- what this variation adds that the inertia baseline lacks

**Exit condition:** 5 labeled complete variations ready.

---

### PHASE 2 -- SCORING

**Entry condition:** Phase 1 complete; rubric loaded.

**Procedure:**
Score each variation against every criterion (pass/fail + evidence). Compute composite.
Add inertia as a pseudo-variation scored against the same rubric.

| Rank | ID      | Composite | vs Inertia | Notes |
|------|---------|-----------|------------|-------|
| 1    | V-XX    | NN        | +NN        | ...   |
| ...  | ...     | ...       | ...        | ...   |
| --   | INERTIA | NN        | baseline   | unconstrained |

**Exit condition:** ranked leaderboard with inertia anchoring.

---

### PHASE 3 -- ANALYSIS

**Entry condition:** Phase 2 complete (leaderboard with inertia row available).

**Step QU2 -- Delta Extraction:**

QU2 must precede QU3 because a criterion not grounded in an observed output gap is an
editorial guess, not a discovery -- the loop's value is in what it measures, not what the
author expected.

Compare the top variation against two references: second-ranked AND inertia. The inertia
contrast is primary. Fill the delta block:

```
TOP VARIATION:           [V-XX]
SECOND-RANKED:           [V-YY]
TOP HAD / SECOND LACKED: [element present in top, absent from second -- stated as an absence]
TOP HAD / INERTIA LACKED:[element present in top, absent from inertia -- this is the discovery]
SIGNAL NAME:             SIGNAL-R{N}: [name] | none
```

The signal is `none` if the "TOP HAD / INERTIA LACKED" field cannot be filled with a
structural difference. A variation that outscores the runner-up but produces nothing inertia
lacked is not a discovery.

**Step QU2b -- PARTIAL Amplifier Trajectory Table (update after every round):**

After filling the delta block, update the PARTIAL tracker. Add any criterion that scored
PARTIAL in this round for any variation:

| Round | Criterion | Occurrence | Count | Recommended action |
|-------|-----------|------------|-------|--------------------|
| [R-N] | [C-NN]    | First / Repeated | [N] | Monitor / Combination axis / Rubric clarification |

Rules:
- First occurrence: flag for monitoring; no action yet.
- Second occurrence (Repeated): designate as a combination axis target in the next round
  spread-design step. Add "PARTIAL-[C-NN]" to the axis bank for that round.
- Third occurrence or more: escalate to rubric clarification -- the pass condition may be
  underspecified; review criterion text before continuing.

Carry this table forward every round. Do not discard rows.
If no PARTIAL scores this round: "No PARTIAL activations this round."

**Step QU3 -- Criterion Proposal (only if signal is not `none`):**

Translate the delta into a criterion. Required fields:
- **Text:** one sentence on what it measures
- **Tier:** essential / recommended / aspirational (assign based on severity of absence --
  essential = output is wrong without it; recommended = better with it; aspirational = excellent)
- **Pass: LOCATION** -- where in the output
- **Pass: OBSERVABLE** -- what specific element must be present
- **Pass: STANDARD** -- what separates pass from fail

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

**Exit condition:** delta block filled; PARTIAL table updated; rubric updated if approved.

---

### PHASE 4 -- CONVERGENCE CHECK

**Entry condition:** Phase 3 complete.

Both conditions must be true before the loop exits -- trial convergence alone means the rubric
stopped evolving before all patterns were found; quest convergence alone means signals ran out
before variations reached the essential bar.

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations pass all essential criteria | YES / NO |
| Quest convergence: this round signal = none AND previous round signal = none | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log and return to PHASE 1.

---

### Round Log

| Round | Top  | vs Inertia | QU2 delta (signal) | Criterion    |
|-------|------|------------|--------------------|--------------|
| R-01  | V-XX | +NN        | SIGNAL or none     | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**Both artifacts are required. The loop is not complete until both are verified.**
Do not summarize either. Do not reference a prior variation by name.
Write the complete contents of each file.

**Artifact 1 -- Golden prompt**
Path: `simulations/quest/golden/{skill}-golden-{date}.md`

Required contents:
- Complete prompt body verbatim -- every line that belongs in the deployed skill body,
  not a summary, not "see V-03," not a compressed version. If a reader cannot run this text
  directly as a skill body, it fails this requirement.
- Section "What Made It Golden" immediately after the body: for each structural mechanism
  the loop discovered, state the round it was found and the specific inertia gap it closed.
  Minimum 2 mechanisms with round citations and inertia-gap descriptions.

**Artifact 2 -- Final rubric**
Path: `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`

Required contents:
- All converged criteria (text, tier, pass conditions for each)
- Composite formula with denominator
- Golden threshold stated explicitly
- Version history table
- Standalone file separate from Artifact 1 -- the rubric is the theory of excellence;
  the golden prompt is the evidence; they must be legible independently

**Ablated criteria:** list criteria with zero activations across all rounds and a suggested
probe for each. If none: "No ablated criteria."

---

## V-04 -- Pre-Printed Scoring Matrix

**axis:** output format -- Phase 2 uses a pre-printed criterion-by-variation scoring grid
(template-completion surface)
**hypothesis:** V-05-R2 instructs "score each variation against every criterion" but provides
no structural surface to ensure every criterion is scored for every variation. A pre-printed
matrix with one row per criterion and one column per variation (plus INERTIA) forces the scorer
to fill every cell, preventing criterion omission. This mirrors the scout-feasibility R3 template
approach that prevented section omission. Expected: criterion-completeness enforcement in the
scoring phase without affecting any other mechanism.

---

Find the golden prompt for a target skill by systematically outcompeting inertia -- the
unconstrained baseline a capable model produces without variation, rubric, or iteration.
The goal is dual convergence: all essential criteria passing AND no new inertia improvements
discoverable for two consecutive rounds. The converged prompt body is the golden prompt.

---

### PHASE 0 -- SETUP

**Entry condition:** skill name provided.

**Procedure:**
1. **Name the inertia prompt.** Write one paragraph: the prompt body a capable model produces
   for this skill without a quest loop -- no rubric, no variation axis, no convergence logic.
   This is the primary competitor and the reference for all QU2 contrasts.
2. **Load the rubric.** Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load latest version.
   If no rubric exists: invoke quest-rubric. The rubric must exist before scoring because
   variation rankings without a grounded objective function are not comparable -- "beating
   inertia" is only measurable against explicit criteria.
3. Record: inertia summary, rubric path, version, criteria count.

**Exit condition:** inertia documented and rubric loaded.

---

### PHASE 1 -- VARIATION

**Entry condition:** Phase 0 complete.

**Procedure:**
Generate 5 complete, runnable prompt body variations. Each = full prompt text. No diffs.
No summaries. Single-axis first; combinations in later rounds.

Label each:
- **Axis:** dimension being varied
- **Hypothesis:** why this axis outperforms inertia
- **Inertia delta:** one phrase -- what this variation adds that the inertia baseline lacks

**Exit condition:** 5 labeled complete variations ready.

---

### PHASE 2 -- SCORING

**Entry condition:** Phase 1 complete; rubric loaded.

**Procedure:**
Fill the scoring matrix below. For every criterion row: score each variation PASS / PARTIAL /
FAIL with brief evidence in parentheses. Score INERTIA column last as a baseline anchor.

| Criterion | Tier | V-01 | V-02 | V-03 | V-04 | V-05 | INERTIA |
|-----------|------|------|------|------|------|------|---------|
| C-01      | E    |      |      |      |      |      |         |
| C-02      | E    |      |      |      |      |      |         |
| C-03      | E    |      |      |      |      |      |         |
| C-04      | E    |      |      |      |      |      |         |
| C-05      | E    |      |      |      |      |      |         |
| C-06      | R    |      |      |      |      |      |         |
| C-07      | R    |      |      |      |      |      |         |
| C-08      | R    |      |      |      |      |      |         |
| C-09      | A    |      |      |      |      |      |         |
| C-10      | A    |      |      |      |      |      |         |
| C-11      | A    |      |      |      |      |      |         |
| C-12      | A    |      |      |      |      |      |         |
| C-13      | A    |      |      |      |      |      |         |
| C-14      | A    |      |      |      |      |      |         |
| **Composite** | | | | | | | |
| **vs Inertia** | | | | | | | |
| **Rank**  |      |      |      |      |      |      |         |

Do not skip rows. Do not skip variation columns.
PARTIAL counts as 0.5 in aspirational tier computation.

**Composite formula:** (essential_pass/5)*60 + (recommended_pass/3)*30 + (aspirational_pass/6)*10

**Exit condition:** all cells filled; ranked leaderboard with inertia-delta row complete.

---

### PHASE 3 -- ANALYSIS

**Entry condition:** Phase 2 complete.

**Step QU2 -- Delta Extraction:**

QU2 must precede QU3 because a criterion not grounded in an observed output gap is an
editorial guess, not a discovery -- the loop's value is in what it measures, not what the
author expected.

Compare the top variation against two references: second-ranked AND inertia. Fill the delta
block:

```
TOP VARIATION:           [V-XX]
SECOND-RANKED:           [V-YY]
TOP HAD / SECOND LACKED: [element present in top, absent from second -- stated as an absence]
TOP HAD / INERTIA LACKED:[element present in top, absent from inertia -- this is the discovery]
SIGNAL NAME:             SIGNAL-R{N}: [name] | none
```

The signal is `none` if the "TOP HAD / INERTIA LACKED" field cannot be filled with a
structural difference.

**Step QU3 -- Criterion Proposal (only if signal is not `none`):**

Translate the delta into a criterion. Required fields:
- **Text:** one sentence on what it measures
- **Tier:** essential / recommended / aspirational (assign based on severity of absence --
  essential = output is wrong without it; recommended = better with it; aspirational = excellent)
- **Pass: LOCATION** -- where in the output
- **Pass: OBSERVABLE** -- what specific element must be present
- **Pass: STANDARD** -- what separates pass from fail

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

**Exit condition:** delta block filled with inertia contrast; rubric updated if approved.

---

### PHASE 4 -- CONVERGENCE CHECK

**Entry condition:** Phase 3 complete.

Both conditions must be true before the loop exits -- trial convergence alone means the rubric
stopped evolving before all patterns were found; quest convergence alone means signals ran out
before variations reached the essential bar.

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations pass all essential criteria | YES / NO |
| Quest convergence: this round signal = none AND previous round signal = none | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log and return to PHASE 1.

---

### Round Log

| Round | Top  | vs Inertia | QU2 delta (signal) | Criterion    |
|-------|------|------------|--------------------|--------------|
| R-01  | V-XX | +NN        | SIGNAL or none     | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**Both artifacts are required. The loop is not complete until both are verified.**
Do not summarize either. Do not reference a prior variation by name.
Write the complete contents of each file.

**Artifact 1 -- Golden prompt**
Path: `simulations/quest/golden/{skill}-golden-{date}.md`

Required contents:
- Complete prompt body verbatim -- every line that belongs in the deployed skill body,
  not a summary, not "see V-04," not a compressed version. If a reader cannot run this text
  directly as a skill body, it fails this requirement.
- Section "What Made It Golden" immediately after the body: for each structural mechanism
  the loop discovered, state the round it was found and the specific inertia gap it closed.
  Minimum 2 mechanisms with round citations and inertia-gap descriptions.

**Artifact 2 -- Final rubric**
Path: `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`

Required contents:
- All converged criteria (text, tier, pass conditions for each)
- Composite formula with denominator
- Golden threshold stated explicitly
- Version history table
- Standalone file separate from Artifact 1 -- the rubric is the theory of excellence;
  the golden prompt is the evidence; they must be legible independently

**Ablated criteria:** list criteria with zero activations across all rounds and a suggested
probe for each. If none: "No ablated criteria."

---

## V-05 -- Full Synthesis (Spread-Design + Named-Round Convergence + Pre-Printed Matrix)

**axis:** lifecycle emphasis + phrasing register + output format (combination:
V-01 spread-design phase + V-02 named-round convergence gate + V-04 pre-printed scoring matrix)
**hypothesis:** All three R3 mechanisms are independent and non-interfering.
Spread-design (V-01) improves variation quality before the bodies are written.
Named-round convergence (V-02) prevents false-YES on quest convergence by requiring explicit
round citations from the Round Log.
Pre-printed scoring matrix (V-04) prevents criterion omission in the scoring phase.
Each addresses a different lifecycle phase (pre-Phase-1, Phase-4, Phase-2 respectively).
Combining them should be additive. Expected composite: 100. If a criterion still fails, that
identifies which mechanism was insufficient when combined with others.

---

Find the golden prompt for a target skill by systematically outcompeting inertia -- the
unconstrained baseline a capable model produces without variation, rubric, or iteration.
The goal is dual convergence: all essential criteria passing AND no new inertia improvements
discoverable for two consecutive rounds. The converged prompt body is the golden prompt.

---

### PHASE 0 -- SETUP

**Entry condition:** skill name provided.

**Procedure:**
1. **Name the inertia prompt.** Write one paragraph: the prompt body a capable model produces
   for this skill without a quest loop -- no rubric, no variation axis, no convergence logic.
   This is the primary competitor. All variations are compared against it.
2. **Load the rubric.** Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load latest version.
   If no rubric exists: invoke quest-rubric. The rubric must exist before scoring because
   variation rankings without a grounded objective function are not comparable -- "beating
   inertia" is only measurable against explicit criteria.
3. Record: inertia summary, rubric path, version, criteria count.

**Exit condition:** inertia documented and rubric loaded.

---

### SPREAD-DESIGN

**Entry condition:** Phase 0 complete. Execute before writing any variation body.

**Procedure:**
1. Axis bank:
   - Role sequence (which roles run first, in what order)
   - Output format (table vs prose vs list; scoring granularity)
   - Lifecycle emphasis (phase space allocation; boundary explicitness)
   - Phrasing register (formal/technical vs conversational; imperative vs descriptive)
   - Inertia framing (prominence of status-quo competitor)

2. Assign axes. Round 1: one axis per variation (single-axis isolation).
   Round 2+: consult PARTIAL tracker (see Phase 3 / Round Log) before assigning combination axes.

3. Produce the axis-assignment plan:

| Plan | Axis | Source signal | Target criteria | Predicted composite |
|------|------|--------------|-----------------|---------------------|
| V-01 | [axis] | [why] | [C-NN...] | [score] |
| V-02 | | | | |
| V-03 | | | | |
| V-04 | | | | |
| V-05 | | | | |

4. Confirm: no two variations share the same single axis before proceeding.

**Exit condition:** axis plan complete and confirmed.

---

### PHASE 1 -- VARIATION

**Entry condition:** Spread-design complete and confirmed.

**Procedure:**
Generate 5 complete, runnable prompt body variations. Each = full prompt text. No diffs.
No summaries. Axis per variation must match spread-design table.

Label each:
- **Axis:** must match spread-design table
- **Hypothesis:** why this axis outperforms inertia
- **Inertia delta:** one phrase -- what this variation adds that the inertia baseline lacks

**Exit condition:** 5 labeled complete variations ready.

---

### PHASE 2 -- SCORING

**Entry condition:** Phase 1 complete; rubric loaded.

**Procedure:**
Fill the scoring matrix. For every cell: PASS / PARTIAL / FAIL with brief evidence.
Score INERTIA column last.

| Criterion | Tier | V-01 | V-02 | V-03 | V-04 | V-05 | INERTIA |
|-----------|------|------|------|------|------|------|---------|
| C-01      | E    |      |      |      |      |      |         |
| C-02      | E    |      |      |      |      |      |         |
| C-03      | E    |      |      |      |      |      |         |
| C-04      | E    |      |      |      |      |      |         |
| C-05      | E    |      |      |      |      |      |         |
| C-06      | R    |      |      |      |      |      |         |
| C-07      | R    |      |      |      |      |      |         |
| C-08      | R    |      |      |      |      |      |         |
| C-09      | A    |      |      |      |      |      |         |
| C-10      | A    |      |      |      |      |      |         |
| C-11      | A    |      |      |      |      |      |         |
| C-12      | A    |      |      |      |      |      |         |
| C-13      | A    |      |      |      |      |      |         |
| C-14      | A    |      |      |      |      |      |         |
| **Composite** | | | | | | | |
| **vs Inertia** | | | | | | | |
| **Rank**  |      |      |      |      |      |      |         |

Do not skip rows. Do not skip variation columns. PARTIAL = 0.5 in aspirational computation.

**Composite formula:** (essential_pass/5)*60 + (recommended_pass/3)*30 + (aspirational_pass/6)*10

**Exit condition:** all cells filled; leaderboard with inertia-delta row complete.

---

### PHASE 3 -- ANALYSIS

**Entry condition:** Phase 2 complete.

**Step QU2 -- Delta Extraction:**

QU2 must precede QU3 because a criterion not grounded in an observed output gap is an
editorial guess, not a discovery -- the loop's value is in what it measures, not what the
author expected. Proposing criteria before naming the gap means the rubric is shaped by
priors, not by what the loop found.

Compare the top variation against two references: second-ranked AND inertia. The inertia
contrast is primary. Fill the delta block:

```
TOP VARIATION:           [V-XX]
SECOND-RANKED:           [V-YY]
TOP HAD / SECOND LACKED: [element present in top, absent from second -- stated as an absence]
TOP HAD / INERTIA LACKED:[element present in top, absent from inertia -- this is the discovery]
SIGNAL NAME:             SIGNAL-R{N}: [name] | none
```

The signal is `none` if the "TOP HAD / INERTIA LACKED" field cannot be filled with a
structural difference. A variation that outscores the runner-up but produces nothing inertia
lacked is not a discovery.

**Step QU2b -- PARTIAL Tracker (update after every round):**

| Round | Criterion | Occurrence | Count | Recommended action |
|-------|-----------|------------|-------|--------------------|
| [R-N] | [C-NN]    | First / Repeated | [N] | Monitor / Combination axis / Rubric clarification |

First occurrence: monitor. Second occurrence: assign as combination axis target next round.
Third+: escalate to rubric clarification. Carry forward all rounds.
If no PARTIAL scores: "No PARTIAL activations this round."

**Step QU3 -- Criterion Proposal (only if signal is not `none`):**

Translate the delta into a criterion. Required fields:
- **Text:** one sentence on what it measures
- **Tier:** essential / recommended / aspirational (assign based on severity of absence --
  essential = output is wrong without it; recommended = better with it; aspirational = excellent)
- **Pass: LOCATION** -- where in the output
- **Pass: OBSERVABLE** -- what specific element must be present
- **Pass: STANDARD** -- what separates pass from fail

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

**Exit condition:** delta block filled with inertia contrast; PARTIAL tracker updated;
rubric updated if approved.

---

### PHASE 4 -- CONVERGENCE CHECK

**Entry condition:** Phase 3 complete. Consult Round Log before filling this table.

Both conditions must be true before the loop exits -- trial convergence alone means the rubric
stopped evolving before all patterns were found; quest convergence alone means signals ran out
before variations reached the essential bar.

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations in Round [N] pass all essential criteria | YES / NO |
| Quest convergence: Round [N] signal = [name or none] AND Round [N-1] signal = [name or none] | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

**Fill the bracketed round values from the Round Log.** Do not declare Quest convergence YES
unless both named rounds appear in the Round Log with explicit signal entries. Declaring
convergence without citing both rounds by number is a structural violation of the dual-gate check.

If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log and return to SPREAD-DESIGN.

---

### Round Log

| Round | Top  | vs Inertia | QU2 delta (signal) | Criterion    |
|-------|------|------------|--------------------|--------------|
| R-01  | V-XX | +NN        | SIGNAL or none     | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**Both artifacts are required. The loop is not complete until both are verified.**
Do not summarize either. Do not reference a prior variation by name.
Write the complete contents of each file.

**Artifact 1 -- Golden prompt**
Path: `simulations/quest/golden/{skill}-golden-{date}.md`

Required contents:
- Complete prompt body verbatim -- every line that belongs in the deployed skill body,
  not a summary, not "see V-05," not a compressed version. If a reader cannot run this text
  directly as a skill body, it fails this requirement.
- Section "What Made It Golden" immediately after the body: for each structural mechanism
  the loop discovered, state the round it was found and the specific inertia gap it closed.
  Minimum 2 mechanisms with round citations and inertia-gap descriptions.

**Artifact 2 -- Final rubric**
Path: `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`

Required contents:
- All converged criteria (text, tier, pass conditions for each)
- Composite formula with denominator
- Golden threshold stated explicitly
- Version history table
- Standalone file separate from Artifact 1 -- the rubric is the theory of excellence;
  the golden prompt is the evidence; they must be legible independently

**Ablated criteria:** list criteria with zero activations across all rounds and a suggested
probe for each. If none: "No ablated criteria."
