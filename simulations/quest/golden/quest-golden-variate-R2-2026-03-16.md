---
skill: quest-variate
skill_target: quest-golden
round: 2
date: 2026-03-16
rubric: simulations/quest/rubrics/quest-golden-rubric-v2-2026-03-16.md
rubric_version: v2
---

# quest-golden -- Round 2 Variations (V-01 through V-05)

Generated against rubric v2 (13 criteria, C-01..C-13, aspirational denominator = 5).
Single-axis variations for V-01 through V-03. Combinations for V-04 and V-05.

**Axes covered:**
- V-01: output-contract (single) -- explicit terminal artifact checklist at GOLDEN OUTPUT
- V-02: contrast-delta notation (single) -- structured delta-pair block in QU2 step
- V-03: rationale-reinforced (single) -- "because" clauses at every ordering constraint
- V-04: inertia-framing + lifecycle + output-contract (combination -- extends V-05-R1)
- V-05: inertia + lifecycle + output-contract + contrast-delta + rationale (full synthesis)

**R1 gaps driving these axes:**

C-02 and C-03 were universally PARTIAL across all 5 R1 variations. R1 scorecard gap analysis:
"None of the five axes directly address artifact writing as a terminal act. R2 should test an
output-contract axis." V-01 is that single-axis probe. V-04 and V-05 carry it into combinations.

C-10 universally FAIL. No R1 variation included ablated criteria tracking. Addressed in all R2
variations via explicit "Ablated criteria" check in GOLDEN OUTPUT.

C-11, C-12, C-13 are new aspirationals in v2. C-11 (structural termination isolation) was
present in V-01-R1 and V-03-R1 via CONVERGENCE JUDGE / PHASE 4. C-12 (contrast-enforced signal
isolation) was present in V-02-R1 via contrast column. C-13 (rationale-grounded sequencing) was
present in V-04-R1 via "because..." phrasing. V-03-R2 tests C-13 on a structural backbone.

**Rubric v2 formula (all variations must score against):**
Score = (essential_pass/5)*60 + (recommended_pass/3)*30 + (aspirational_pass/5)*10
Golden threshold: all 5 essential PASS AND composite >= 80.

---

## V-01 -- Output Contract

**axis:** output-contract
**hypothesis:** Adding a dedicated GOLDEN OUTPUT section whose sole purpose is a verbatim
artifact checklist will convert C-02 and C-03 from universally PARTIAL to PASS. Every R1
variation produced "write the full prompt verbatim" and "standalone rubric file" in some form,
but none stated "not a summary, not a label, not a reference to a prior variation" or "not
embedded inside the golden prompt file." The checklist is the only new structure. The rest of
the loop is V-03-R1 lifecycle phases unchanged. Risk: structural phase gates are inherited from
R1; C-11 should remain PASS. The single axis test isolates whether explicit verbatim-contract
language in the terminal section alone is sufficient to earn C-02/C-03.

---

Find the golden prompt for a target skill through systematic variation and rubric-grounded
scoring. The loop runs until dual convergence: all essential criteria pass across all variations
AND no new excellence patterns emerge for two consecutive rounds.

---

### PHASE 0 -- INITIALIZATION

**Entry condition:** skill name provided.

**Procedure:**
1. Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load latest version.
2. If no rubric exists: invoke quest-rubric. Do not proceed until confirmed.
3. Record: rubric path, version, criteria count.

**Exit condition:** rubric confirmed with criteria count > 0.

---

### PHASE 1 -- VARIATION

**Entry condition:** Phase 0 complete.

**Procedure:**
1. Generate 5 complete, runnable prompt body variations. Each = full prompt text. No diffs.
2. Label each: axis + hypothesis.
3. Single-axis first; combinations in later rounds.

**Exit condition:** 5 labeled complete variations ready.

---

### PHASE 2 -- SCORING

**Entry condition:** Phase 1 complete; rubric loaded.

**Procedure:**
1. Score each variation against every criterion (pass/fail + evidence).
2. Compute composite using rubric formula. Rank all variations.

**Exit condition:** ranked leaderboard with per-criterion pass/fail.

---

### PHASE 3 -- ANALYSIS

**Entry condition:** Phase 2 complete.

**Step QU2 -- Excellence Signal Isolation:**
Compare top variation to second only. Name the observable output difference: what the winner
had that the runner-up lacked. The signal is a contrast, not a property list. Name it:
`SIGNAL-R{N}: {name}`. If no distinguishing difference: `none`.

**Step QU3 -- Criterion Proposal (only if QU2 signal is not `none`):**
Propose a rubric criterion:
- **Text:** one sentence on what it measures
- **Tier:** essential / recommended / aspirational
- **Pass condition:** LOCATION + OBSERVABLE + STANDARD

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

**Exit condition:** signal named; rubric updated if criterion approved.

---

### PHASE 4 -- CONVERGENCE CHECK

**Entry condition:** Phase 3 complete.

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations pass all essential criteria | YES / NO |
| Quest convergence: this round signal = none AND previous round signal = none | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log row and return to PHASE 1.

---

### Round Log

| Round | Variations | Top composite | QU2 signal | Criterion added |
|-------|------------|--------------|------------|-----------------|
| R-01  | V-01..V-05 | NN           | SIGNAL or none | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**Both artifacts are required before convergence is complete.**
Do not summarize either. Do not reference a prior variation by name.
Write the complete contents of each file.

**Artifact 1 -- Golden prompt**
Path: `simulations/quest/golden/{skill}-golden-{date}.md`

Required contents -- each item must be present:
- Complete prompt body verbatim: every line of the deployed skill body, not a summary,
  not a label, not "see V-03," not a compressed version. If a reader cannot run this text
  directly as a skill body, it fails this requirement.
- Section "What Made It Golden" immediately after the body: each structural mechanism the
  loop discovered, the round it was found, and the output gap it closed. Minimum 2
  mechanisms with explicit round citations.

**Artifact 2 -- Final rubric**
Path: `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`

Required contents -- each item must be present:
- All converged criteria with text, tier, and pass conditions
- Composite formula with denominator
- Golden threshold stated explicitly
- Version history table
- File is standalone: not embedded inside Artifact 1; navigable without opening the
  golden prompt file

**Ablated criteria:** list any criteria with zero activations across all rounds with a
suggested probe. If none: "No ablated criteria."

---

## V-02 -- Contrast-Delta Notation

**axis:** contrast-delta notation (output-format variant: structured field pair replacing
prose QU2 extraction)
**hypothesis:** A named delta block -- with "TOP HAD" and "SECOND LACKED" as paired required
fields -- structurally prevents the extractor from filling the signal with a property both
variations shared. V-02-R1 was the only R1 variation to PASS C-07 (excellence signal
isolation), exclusively because its contrast column forced gap-stating. That mechanism was
in the scoring matrix, not the extraction step itself. This variation moves the constraint
into the skill body: the delta block fields must describe the same element from opposite
sides, and cannot be filled with shared properties. This directly targets C-12 (new in v2).
Risk: the delta block requires careful reading to fill correctly; C-09 and C-13 may not
improve unless rationale is also added.

---

Find the golden prompt for a target skill through systematic variation and rubric-grounded
scoring. The loop runs until dual convergence: all essential criteria pass AND no new
excellence patterns emerge for two consecutive rounds.

---

### PHASE 0 -- INITIALIZATION

**Entry condition:** skill name provided.

**Procedure:**
1. Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load latest.
2. If no rubric exists: invoke quest-rubric before proceeding.
3. Record: rubric path, version, criteria count.

**Exit condition:** rubric confirmed with criteria count > 0.

---

### PHASE 1 -- VARIATION

**Entry condition:** Phase 0 complete.

**Procedure:**
1. Generate 5 complete, runnable prompt body variations. Each = full prompt text. No diffs.
2. Label each: axis + hypothesis. Single-axis first; combinations later.

**Exit condition:** 5 labeled complete variations ready.

---

### PHASE 2 -- SCORING

**Entry condition:** Phase 1 complete; rubric loaded.

**Procedure:**
Score each variation against every criterion (pass/fail + evidence).
Compute composite. Rank all variations.

**Exit condition:** ranked leaderboard with per-criterion pass/fail.

---

### PHASE 3 -- ANALYSIS

**Entry condition:** Phase 2 complete.

**Step QU2 -- Delta Extraction:**

Fill the delta block for the top and second-ranked variation:

```
TOP VARIATION:  [ID]
SECOND-RANKED:  [ID]
TOP HAD:        [structural element, mechanism, or output property present in TOP]
SECOND LACKED:  [the same element stated as an absence -- "no X" or "missing X"]
SIGNAL NAME:    SIGNAL-R{N}: [name] | none
```

Rules for filling the delta block:
- TOP HAD and SECOND LACKED must describe the same element from opposite sides.
  If both variations had the element, it is not the signal.
- The signal is `none` if no asymmetric element exists.
- Do not fill TOP HAD with a property both variations shared. The delta block must
  encode an absence in SECOND LACKED, not a shared quality.

**Step QU3 -- Criterion Proposal (only if SIGNAL NAME is not `none`):**

Translate the delta into a rubric criterion:
- **Text:** one sentence on what it measures
- **Tier:** essential / recommended / aspirational
- **Pass: LOCATION** -- where in the output to look
- **Pass: OBSERVABLE** -- what specific element must be present
- **Pass: STANDARD** -- threshold between pass and fail

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

**Exit condition:** delta block filled; signal named; rubric updated if approved.

---

### PHASE 4 -- CONVERGENCE CHECK

**Entry condition:** Phase 3 complete.

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations pass all essential criteria | YES / NO |
| Quest convergence: this round signal = none AND previous round signal = none | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log and return to PHASE 1.

---

### Round Log

| Round | Variations | Top composite | QU2 signal | Criterion added |
|-------|------------|--------------|------------|-----------------|
| R-01  | V-01..V-05 | NN           | SIGNAL or none | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**Golden prompt** -- `simulations/quest/golden/{skill}-golden-{date}.md`
Write the full converged prompt body verbatim. Followed by "What Made It Golden":
>= 2 mechanism descriptions, each naming the round it was found and the output gap it closed.

**Final rubric** -- `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`
All criteria, formula, denominator, golden threshold, version history. Standalone file.

**Ablated criteria:** criteria with zero activations and a suggested probe for each.
If none: "No ablated criteria."

---

## V-03 -- Rationale-Reinforced Sequencing

**axis:** rationale-grounded sequencing (phrasing-register variant: "because" clauses at
all ordering constraints, on a structural role-sequence backbone)
**hypothesis:** V-04-R1 earned PASS on C-04 (essential) by grounding QU2-before-QU3 in
purpose, but V-04-R1 scored lowest overall (56) because the conversational register weakened
all structural gates. This variation takes V-01-R1 role-sequence (which earned C-01, C-04,
C-05 PASS) and adds explicit rationale clauses at RUBRIC KEEPER (why rubric before scoring),
CRITERION AUTHOR (why QU2 before QU3), and CONVERGENCE JUDGE (why both conditions required),
without softening the register elsewhere. Hypothesis: rationale clauses embedded in a
structural role backbone earn C-04 and C-13 without degrading C-01 or C-05. Also expected
to earn C-02 and C-03 PASS via explicit Golden Output verbatim-contract language.

---

Find the golden prompt for a target skill through systematic variation and scoring.

The loop has six roles. Each executes in strict sequence per round. Do not merge or skip roles.

---

### RUBRIC KEEPER

Runs once at loop start and again after any approved criterion.

At start: load the rubric from `simulations/quest/rubrics/`. If none exists: invoke quest-rubric.
The rubric must exist before scoring because variation rankings without a grounded objective
function are not comparable -- qualitative judgment in place of rubric scoring means each
variation is measured against something different, and excellence signals cannot be derived
from criterion gaps. Record: rubric path and criteria count before proceeding.

After QU4 approval: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md` with incremented version.

---

### VARIATOR

Generate 5 complete, runnable prompt body variations for the target skill. Each = full prompt
body text, not a diff, not a summary. Label each: axis (single-axis first) + hypothesis.

---

### SCORER

Apply the current rubric to each variation. Pass or fail per criterion with evidence. Compute
composite using the rubric formula. Rank all variations. State top and gap to second.

---

### ANALYST (QU2)

Compare the top variation to second only. Name what the winner had that the runner-up lacked --
the contrast, not a description of the winner. Properties shared by both variations are not
signals of excellence; only differences qualify. Name it: `SIGNAL-R{N}: {name}`. If none: `none`.

---

### CRITERION AUTHOR (QU3)

QU2 must precede QU3 because a criterion not grounded in an observed output gap is an editorial
guess: it reflects the author's priors rather than what the loop actually measured. A criterion
proposed without first naming the observable difference that motivated it cannot be verified
against the evidence. Execute only if ANALYST named a signal.

Propose a rubric criterion:
- **Text:** one sentence stating what it measures
- **Tier:** essential / recommended / aspirational -- assign based on severity of absence,
  because tier determines the criterion's weight in the composite formula
- **Pass condition:** LOCATION + OBSERVABLE + STANDARD

Present for approval (QU4). If approved: RUBRIC KEEPER writes the updated rubric.
If rejected: record reason, continue.

---

### CONVERGENCE JUDGE

Both conditions must be true before the loop exits -- trial convergence alone means the rubric
stopped evolving before all patterns were found; quest convergence alone means signals ran out
before variations reached the essential bar. Checking only one exits the loop too early.

1. **Trial convergence:** all variations pass all essential criteria in the current rubric.
2. **Quest convergence:** this round's signal was `none` AND the previous round's was `none`.

If both true: proceed to Golden Output. If either false: append round log row, return to VARIATOR.

---

### Per-Round Record

| Round | Variations | Top composite | Excellence signal | Criterion added |
|-------|------------|--------------|-------------------|-----------------|
| R-01  | V-01..V-05 | NN           | SIGNAL or none    | C-NN or none    |

---

### Golden Output (at dual convergence only)

Write two artifacts:

**Golden prompt** -- `simulations/quest/golden/{skill}-golden-{date}.md`
Full converged prompt body verbatim. Not a label. Not a summary. Every line of the deployable
skill body -- if a reader cannot use this text directly to run the skill, it fails. Include
"What Made It Golden" immediately after: each structural mechanism, the round it was found,
the output gap it closed. Minimum 2 mechanisms with round citations.

**Final rubric** -- `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`
All criteria, composite formula, denominator, golden threshold, version history. Standalone
file -- separate from the golden prompt, because the rubric is the theory of excellence and
the golden prompt is the evidence; conflating them makes neither independently legible.

**Ablated criteria:** criteria with zero activations and a suggested probe for each.
If none: "No ablated criteria."

---

## V-04 -- Combination: V-05-R1 + Output Contract

**axis:** inertia-framing + lifecycle-emphasis + output-contract (combination)
**hypothesis:** V-05-R1 scored highest in R1 (composite 78) with PASS on C-01, C-04, C-05,
C-06, C-07, C-09. Its only essential failures were C-02 (PARTIAL) and C-03 (PARTIAL) -- the
GOLDEN OUTPUT section described artifacts but lacked explicit "not a summary, not a label"
and "standalone file" contract language. Adding that contract to V-05-R1's GOLDEN OUTPUT
section should convert both essentials to PASS without disturbing any of V-05-R1's other
results. Expected composite: >= 90 if all essentials pass. C-08 was PARTIAL in R1 (criterion
proposal lacks tier + pass-condition completeness enforcement); watch for whether contract
language in GOLDEN OUTPUT transfers to proposal completeness.

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
2. **Load the rubric.** Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load latest.
   If none: invoke quest-rubric before proceeding. The rubric defines what "beating inertia"
   means in measurable terms.
3. Record: inertia summary, rubric path, version, criteria count.

**Exit condition:** inertia baseline documented and rubric loaded.

---

### PHASE 1 -- VARIATION

**Entry condition:** Phase 0 complete.

**Procedure:**
Generate 5 complete, runnable prompt body variations. Each = full prompt text. No diffs.
Single-axis first; combinations in later rounds.

Label each:
- **Axis:** dimension being varied
- **Hypothesis:** how this axis is expected to outperform inertia
- **Inertia delta:** one phrase -- what this variation adds vs the inertia baseline

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

### PHASE 3 -- ANALYSIS (QU2 then QU3)

**Entry condition:** Phase 2 complete (leaderboard with inertia row available).

**Step QU2 -- Excellence Signal Isolation:**

Compare top variation against two references:
1. Second-ranked variation (within-field contrast)
2. Inertia baseline (inertia contrast -- the more important of the two)

Name what the top variation had that neither the runner-up NOR the inertia baseline had.
This is the pure excellence signal -- something the loop discovered that unconstrained
generation misses. Name it: `SIGNAL-R{N}: {name}`. If no such difference: `none`. A variation
that outscores the runner-up but matches inertia on the new dimension is not a discovery.

**Step QU3 -- Criterion Proposal (only if QU2 is not `none`):**

Propose a rubric criterion:
- **Text:** what it measures
- **Tier:** essential / recommended / aspirational
- **Pass condition:** LOCATION + OBSERVABLE + STANDARD

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

**Exit condition:** signal named with inertia contrast; rubric updated if approved.

---

### PHASE 4 -- CONVERGENCE CHECK

**Entry condition:** Phase 3 complete.

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations pass all essential criteria | YES / NO |
| Quest convergence: this round signal = none AND previous round signal = none | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log and return to PHASE 1.

---

### Round Log

| Round | Top  | vs Inertia | QU2 signal     | Criterion    |
|-------|------|------------|----------------|--------------|
| R-01  | V-XX | +NN        | SIGNAL or none | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**Both artifacts are required before convergence is complete.**
Write each fully. Do not summarize. Do not reference a prior variation by name.

**Artifact 1 -- Golden prompt**
Path: `simulations/quest/golden/{skill}-golden-{date}.md`

Required contents:
- Full converged prompt body verbatim -- the complete runnable text, not a summary,
  not a label, not "see V-05." Every line that belongs in the deployed skill body.
- Section "What Made It Golden" immediately after the body: each structural mechanism
  the loop discovered, the round it was found, and the specific inertia gap it closed.
  Minimum 2 mechanisms with round and inertia-gap citations.

**Artifact 2 -- Final rubric**
Path: `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`

Required contents:
- All converged criteria with text, tier, and pass conditions
- Composite formula with denominator
- Golden threshold stated explicitly
- Version history table
- Standalone file -- separate from Artifact 1; not embedded inside the golden prompt file

**Ablated criteria:** list criteria with zero activations across all rounds with a suggested
probe for each. If none: "No ablated criteria."

---

## V-05 -- Full Synthesis

**axis:** inertia-framing + lifecycle-emphasis + output-contract + contrast-delta +
rationale-grounded sequencing (full combination)
**hypothesis:** Each of the four R2 single-axis variations targets a distinct criterion gap.
Combined, they should reach all 5 essential criteria and most aspirationals:
- Inertia + lifecycle (V-05-R1 core): earns C-01, C-04, C-05, C-06, C-07, C-09, C-11
- Output contract: earns C-02, C-03, C-10
- Contrast-delta notation: earns C-12
- Rationale clauses: earns C-13
No two mechanisms target the same step. Hypothesis: the combination is additive and
non-interfering. Expected composite: > 90. If a criterion still fails, that identifies
which mechanism was insufficient when combined with others.

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
2. **Load the rubric.** Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load latest.
   If none: invoke quest-rubric. The rubric must exist before scoring because variation rankings
   without a grounded objective function are not comparable -- "beating inertia" is only
   measurable against explicit criteria.
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
