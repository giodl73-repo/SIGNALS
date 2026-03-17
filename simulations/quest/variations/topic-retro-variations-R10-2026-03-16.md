## quest-variate R10 — topic-retro — 5 Variations

---

## V-01 — Axis: Role Sequence
**Hypothesis:** Making Phase 0 a structurally sealed standalone phase — completed and closed before any signal is opened — eliminates hindsight contamination at the source. Prior belief cannot be reconstructed after signals are read; it must be recorded as a sealed artifact.

---

### Skill: topic-retro

**Purpose:** Post-commitment retrospective on a topic's signals. Determines signal accuracy, identifies gaps, surfaces the unexpected finding, and feeds results back into future signal design.

**Run after a feature ships.** AMEND: focus on specific signal type, adjust time window.

---

### Execution Protocol

You will execute this retro in seven discrete phases. **Phase 0 must be completed and sealed before any signal is opened.** Each phase boundary must be explicitly declared before the next phase begins.

---

### Phase 0 — Prior Belief Capture (SEAL BEFORE PROCEEDING)

Before opening any signal artifacts, record your prior belief for this topic.

Emit the following block verbatim, populated from memory or context only — no signals read:

```
PHASE 0 — PRIOR BELIEF RECORD
Topic: {topic}
Run date: {date}
Prior belief statement: {one sentence: what did the team expect this feature to do or cost?}
Confidence at intake: {Low / Medium / High}
Expected accuracy of signals: {Low / Medium / High}
Signal type most trusted at intake: {namespace}
Signal type least trusted at intake: {namespace}

PHASE 0 SEALED — no revision permitted after this point.
```

**Phase boundary: Phase 0 is now sealed. Proceed to Phase 1.**

---

### Phase 1 — Echo Identification (LOCK BEFORE ACCURACY)

Open signals now. Before scoring accuracy, identify the Echo.

The Echo is the single most surprising finding from this retro — the thing that genuinely was not expected at intake. It must be named before accuracy is scored.

Emit:

```
ECHO (LOCKED)
Finding: {one sentence}
Why surprising: {one sentence referencing Phase 0 prior belief}
Lock time: Phase 1, before accuracy scoring

ECHO IS NOW IMMUTABLE. Any Phase 3–5 analysis that would revise this finding
must be recorded as a conflict artifact, not a revision.
```

**Phase boundary: Echo is now locked and immutable. Proceed to Phase 2.**

---

### Phase 2 — Signal Inventory

List every signal artifact gathered for this topic.

| Namespace | Artifact | Date | Prediction at signal time | C / P / W |
|-----------|----------|------|--------------------------|-----------|

C = Correct, P = Partial, W = Wrong. Leave C/P/W blank for Phase 2; populate in Phase 3.

**Phase boundary: Inventory is complete. Proceed to Phase 3.**

---

### Phase 3 — Accuracy Scoring

Populate the C/P/W column in the Phase 2 table. Then compute per-namespace accuracy.

**Per-namespace accuracy table:**

| Namespace | C | P | W | Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Reliability |
|-----------|---|---|---|--------------------------------------------------------------|-------------|

**Overall accuracy judgment:** {ratio or qualitative rating grounded in per-namespace scores}

**Conflict audit (mandatory — runs unconditionally):**
Review Phase 3 findings against the Phase 1 locked Echo. Does this analysis suggest a different Echo than what was locked?

- [ ] No conflict — the locked Echo is consistent with accuracy findings.
- [ ] Conflict detected — {describe tension}. Echo preserved as locked. Conflict recorded here as artifact.

**Phase boundary: Accuracy is scored. Echo conflict audit is complete. Proceed to Phase 4.**

---

### Phase 4 — Gap Analysis

Identify which signal types were absent.

| Namespace | Signal type missing | Why it matters | Actionable recommendation |
|-----------|---------------------|----------------|--------------------------|

Each row must name a specific namespace and skill, not a generic observation.

**Phase boundary: Gap analysis is complete. Proceed to Phase 5.**

---

### Phase 5 — Echo Feedback Loop

Translate the locked Echo into a concrete change proposal.

| Echo finding | Without this retro (default assumption) | With this retro (actual) |
|---|---|---|
| {locked Echo} | {what the team would have assumed} | {what actually happened} |
| Signal accuracy assumption | {Phase 0 confidence level} | {Phase 3 overall accuracy} |
| Signal design default | {most-trusted namespace at intake} | {namespace with highest Phase 3 score} |

**Change proposal:** {specific skill to add, rubric to amend, or threshold to adjust — one concrete action}

**Phase boundary: Echo feedback loop is complete. Proceed to Phase 6.**

---

### Phase 6 — Calibration

Compare this retro's accuracy to a prior retro for the same team or namespace.

**If a prior retro exists:**

| Dimension | Prior retro | This retro | Trend |
|-----------|-------------|------------|-------|
| Overall accuracy | | | ↑ / → / ↓ |
| Most reliable namespace | | | |
| Most surprising finding | | | |

**If no prior retro exists:**

```
CALIBRATION BASELINE RECORD
Topic: {topic}
Date: {date}
Overall accuracy: {score from Phase 3}
Most reliable namespace: {namespace}
Echo theme: {one phrase}
Note: No prior retro available — calibration baseline established here.
      This record is the forward reference for the next retro on this team or namespace.
```

---

### Output Checklist (self-verify before emitting)

- [ ] Phase 0 prior belief record present and sealed
- [ ] Echo block carries `ECHO (LOCKED)` label and appears before Phase 3
- [ ] Inventory complete — no known artifact omitted
- [ ] Per-namespace scoring uses stated formula with worked example in header
- [ ] Conflict audit emitted a result (conflict or explicit no-conflict)
- [ ] Gap table includes actionable recommendation per row
- [ ] Foil table uses three named comparison dimensions
- [ ] Calibration section emitted — either trend or baseline record
- [ ] AMEND scope honored throughout (if provided)

---

---

## V-02 — Axis: Output Format
**Hypothesis:** Embedding the accuracy formula and a concrete worked example directly in the column header — not in prose — makes the scoring computation self-auditing. A scorer can verify results by inspecting the table alone, without reading surrounding instructions.

---

### Skill: topic-retro

**Purpose:** Post-commitment retrospective on a topic's signals. Determines what was predicted, what happened, what was missed, and what was unexpected.

**Run after a feature ships.** AMEND: focus on specific signal type, adjust time window.

---

### Execution Order (structural constraint)

1. Seal Phase 0 prior belief before opening any artifacts
2. Lock Echo before scoring accuracy
3. Run conflict audit unconditionally
4. Emit calibration section regardless of prior retro availability

Every table that requires computation must embed its formula in the column header.

---

### Phase 0 — Prior Belief Capture

**Complete before opening any signal artifacts. Seal with explicit declaration.**

| Field | Value |
|-------|-------|
| Topic | |
| Run date | |
| Prior belief (one sentence) | |
| Confidence at intake | Low / Medium / High |
| Most trusted namespace | |
| Least trusted namespace | |

**PHASE 0 SEALED — prior belief record is now immutable.**

---

### Phase 1 — Echo

**Complete before scoring accuracy.**

```
ECHO (LOCKED)
{Single sentence: the one finding genuinely not expected at intake}

Locked before accuracy scoring. Immutable from this point forward.
```

**Phase boundary: Echo locked. Accuracy scoring may now begin.**

---

### Phase 2 — Signal Inventory and Accuracy

All known artifacts for this topic. One row per artifact.

| Namespace | Artifact name | Date | Prediction at signal time | C/P/W | Notes |
|-----------|--------------|------|--------------------------|-------|-------|

C = Correct, P = Partial, W = Wrong.

**Per-namespace accuracy:**

| Namespace | C | P | W | Score: (C×100 + P×50) ÷ (C+P+W) [e.g. C=3,P=1,W=0 → 87.5] | Reliability band |
|-----------|---|---|---|--------------------------------------------------------------|-----------------|

Reliability bands: 80–100 = Strong, 50–79 = Moderate, 0–49 = Weak.

**Overall accuracy: {weighted or qualitative judgment grounded in namespace scores}**

---

### Phase 3 — Conflict Audit (mandatory)

Review whether Phase 2 findings would change the locked Echo.

**Conflict audit result (required in all cases):**

| Audit result | Detail |
|---|---|
| ☐ No conflict | Echo consistent with accuracy findings — no revision warranted |
| ☐ Conflict | {nature of tension} — Echo preserved as locked, tension recorded as artifact |

---

### Phase 4 — Gap Analysis

Signal types absent for this topic.

| Namespace | Missing skill | Decision impact | Next-topic action |
|-----------|--------------|-----------------|-------------------|

Each row must name a specific skill, not a category.

---

### Phase 5 — Echo Feedback and Status-Quo Foil

**Foil table — three named comparison dimensions:**

| Dimension | Without this retro (default) | With this retro (actual) |
|-----------|------------------------------|--------------------------|
| Signal accuracy assumption | {Phase 0 expected accuracy} | {Phase 2 overall score} |
| Echo assumption | {what team assumed would be surprising, if anything} | {locked Echo} |
| Signal design default | {least-trusted namespace at intake} | {lowest-scoring namespace in Phase 2} |

**Change proposal:** {one concrete action: skill to add, rubric criterion to amend, or threshold to set}

---

### Phase 6 — Calibration

| Scenario | Action |
|---|---|
| Prior retro exists | Compare overall accuracy, most reliable namespace, Echo theme; emit trend row (↑/→/↓) |
| No prior retro | Emit baseline record: topic, date, accuracy score, most reliable namespace, Echo theme, note "calibration baseline established here" |

```
CALIBRATION SECTION
[populate from scenario above]
```

---

### Format Rules

- Every computed column carries its formula and a worked example in the column header
- Phase 0 prior belief is populated from memory only — no signal lookup permitted
- Foil table has exactly three named rows
- Conflict audit emits a row with a checked result regardless of whether tension is perceived
- Calibration section is never skipped

---

---

## V-03 — Axis: Lifecycle Emphasis
**Hypothesis:** Declaring an explicit phase-seal statement at every phase boundary — not just phase numbers — makes the execution sequence provably auditable by inspection. A reviewer can verify that Echo was locked before accuracy was scored by reading boundary markers alone, without trusting author prose.

---

### Skill: topic-retro

**Purpose:** Retrospective on a topic's signal set after the feature ships. Surfaces accuracy, gaps, unexpected findings, and design improvements.

**AMEND:** scope to a specific signal type or time window; all phases apply within that scope.

---

### Phase 0 — PRIOR BELIEF CAPTURE

**Constraint: this phase runs before any signal artifact is opened.**

Record the team's prior belief state from memory or intake context only.

```
╔══════════════════════════════════════════════════════════╗
║  PHASE 0 — PRIOR BELIEF RECORD                          ║
║  Topic:                                                  ║
║  Date:                                                   ║
║  Prior belief:                                           ║
║  Confidence at intake: Low / Medium / High               ║
║  Most trusted namespace:                                 ║
║  Expected accuracy: Low / Medium / High                  ║
╚══════════════════════════════════════════════════════════╝
```

---

```
════════════════════════════════════════════════════════════
PHASE BOUNDARY — Phase 0 → Phase 1
Phase 0 prior belief record is now sealed.
No revision permitted after this boundary.
Signals may now be opened.
════════════════════════════════════════════════════════════
```

---

### Phase 1 — ECHO IDENTIFICATION

**Constraint: Echo must be locked before accuracy scoring begins.**

Open signal artifacts. Identify the one finding that was genuinely not expected at intake.

```
╔══════════════════════════════════════════════════════════╗
║  ECHO (LOCKED)                                          ║
║  Finding:                                                ║
║  Why surprising (vs Phase 0 prior belief):               ║
║  Locked: Phase 1, before accuracy scoring                ║
╚══════════════════════════════════════════════════════════╝
```

---

```
════════════════════════════════════════════════════════════
PHASE BOUNDARY — Phase 1 → Phase 2
Echo is now immutable.
Any later analysis that would change the Echo must be recorded
as a conflict artifact. The Echo itself is not revised.
Accuracy scoring may now begin.
════════════════════════════════════════════════════════════
```

---

### Phase 2 — SIGNAL INVENTORY

List every artifact gathered for this topic.

| Namespace | Artifact | Date | Prediction at signal time | C / P / W |
|-----------|----------|------|--------------------------|-----------|

---

```
════════════════════════════════════════════════════════════
PHASE BOUNDARY — Phase 2 → Phase 3
Signal inventory is complete.
No artifact may be added after this boundary.
Proceed to accuracy scoring.
════════════════════════════════════════════════════════════
```

---

### Phase 3 — ACCURACY SCORING

Populate C/P/W in the Phase 2 table, then compute per-namespace scores.

| Namespace | C | P | W | Score: (C×100 + P×50) ÷ (C+P+W) [e.g. C=2,P=2,W=1 → 60.0] | Band |
|-----------|---|---|---|--------------------------------------------------------------|------|

**Overall accuracy judgment:** {ratio or qualitative — grounded in namespace scores}

**Conflict audit — runs unconditionally:**

| | |
|---|---|
| **Audit result** | ☐ No conflict — Echo consistent with accuracy findings |
| | ☐ Conflict — {describe} — Echo preserved as locked, tension recorded |

---

```
════════════════════════════════════════════════════════════
PHASE BOUNDARY — Phase 3 → Phase 4
Accuracy scoring is complete.
Conflict audit result is recorded.
Proceed to gap analysis.
════════════════════════════════════════════════════════════
```

---

### Phase 4 — GAP ANALYSIS

| Namespace | Missing signal type | Consequence if absent | Recommended action |
|-----------|---------------------|----------------------|--------------------|

---

```
════════════════════════════════════════════════════════════
PHASE BOUNDARY — Phase 4 → Phase 5
Gap analysis is complete.
Proceed to Echo feedback loop and status-quo foil.
════════════════════════════════════════════════════════════
```

---

### Phase 5 — ECHO FEEDBACK AND STATUS-QUO FOIL

**Foil table — three named comparison dimensions:**

| Dimension | Without this retro | With this retro |
|---|---|---|
| Signal accuracy assumption | {Phase 0 expected accuracy} | {Phase 3 overall score} |
| Echo assumption | {what would have remained assumed} | {locked Echo from Phase 1} |
| Signal design default | {namespace assumed reliable at intake} | {highest-scoring namespace in Phase 3} |

**Change proposal:** {one specific action derived from the Echo — skill, rubric amendment, or threshold}

---

```
════════════════════════════════════════════════════════════
PHASE BOUNDARY — Phase 5 → Phase 6
Echo feedback loop is complete.
Foil table is finalized.
Proceed to calibration.
════════════════════════════════════════════════════════════
```

---

### Phase 6 — CALIBRATION

If prior retro available: compare accuracy, reliable namespace, Echo theme — emit trend.

If no prior retro:

```
╔══════════════════════════════════════════════════════════╗
║  CALIBRATION BASELINE RECORD                            ║
║  Topic:                                                  ║
║  Date:                                                   ║
║  Overall accuracy:                                       ║
║  Most reliable namespace:                                ║
║  Echo theme:                                             ║
║  Note: No prior retro available —                        ║
║        calibration baseline established here.           ║
╚══════════════════════════════════════════════════════════╝
```

---

```
════════════════════════════════════════════════════════════
PHASE BOUNDARY — Phase 6 complete
Retro is finalized. All phases sealed.
════════════════════════════════════════════════════════════
```

---

---

## V-04 — Axes: Role Sequence + Phrasing Register
**Hypothesis:** Framing the retro as a structured discovery sequence in a direct, active voice — "do this, then this" — reduces procedural friction while preserving the structural constraints that matter. Teams engage more honestly when the retro feels like uncovering something rather than filling in a compliance template.

---

### Skill: topic-retro

Run this after the feature ships. Your job is to reconstruct the signal story: what you predicted, what actually happened, what surprised you, and what you'd do differently next time.

This is structured but not bureaucratic. Work through the phases in order. The sequence is the integrity mechanism — phase ordering is not optional.

**AMEND:** If given a scope constraint (specific signal type or time window), apply it throughout.

---

### Step 1 — Capture your prior belief before you look at anything

Before you open a single signal artifact, write down what you thought going in.

This step is sealed before Step 2. You cannot read signals first and then fill this in.

```
PHASE 0 — PRIOR BELIEF (sealed before signals opened)

Topic: ___
Date: ___
What did the team expect this feature to accomplish or cost? (one sentence): ___
How confident were you in your signals? Low / Medium / High
Which signal namespace did you trust most going in? ___
Which did you trust least? ___

SEALED.
```

**Boundary: Phase 0 is closed. Now open your signals.**

---

### Step 2 — Name the surprise before you score anything

Read your signals. Before you start scoring accuracy, identify the one thing that genuinely surprised you — the finding you could not have written in Phase 0.

```
ECHO (LOCKED)

{One sentence: the single most unexpected finding from this retro.}

Locked here. If later analysis would change this, record the tension — don't revise the Echo.
```

**Boundary: Echo is locked. Now score accuracy.**

---

### Step 3 — Build the signal inventory and score it

List every artifact. One row per artifact.

| Namespace | Artifact | Date | What you predicted | C / P / W |
|-----------|----------|------|-------------------|-----------|

Then compute per-namespace:

| Namespace | C | P | W | Score: (C×100 + P×50) ÷ (C+P+W) [e.g. C=1,P=2,W=2 → 40.0] | Verdict |
|-----------|---|---|---|--------------------------------------------------------------|---------|

**Overall: {one judgment grounded in the namespace scores}**

---

### Step 4 — Run the conflict check (always)

Does your accuracy scoring suggest a different Echo than what you locked in Step 2?

Answer this directly — don't skip it even if no conflict seems obvious:

> Conflict check: ☐ No conflict — locked Echo holds. ☐ Conflict detected — {describe tension} — Echo preserved, tension recorded here.

---

### Step 5 — Name the gaps

What signal types were missing?

| Namespace | Missing skill | What decision it would have improved | What to run next time |
|-----------|--------------|-------------------------------------|----------------------|

Name specific skills, not categories.

---

### Step 6 — Close the loop on the Echo

Translate the locked Echo into something actionable. Use the foil table to make the cost concrete.

| Dimension | Without this retro | With this retro |
|---|---|---|
| Signal accuracy assumption | {what Phase 0 expected} | {what Phase 3 found} |
| Echo assumption | {what would have stayed assumed} | {locked Echo} |
| Signal design default | {namespace you trusted most at intake} | {namespace that scored highest} |

**What to do differently:** {one specific change — a skill to add, a rubric criterion to amend, or a threshold to set}

---

### Step 7 — Calibrate against your history

If you have a prior retro for this team or namespace: compare accuracy trend, most reliable namespace, and Echo theme. Call the trend (improving / stable / degrading).

If this is your first retro:

```
CALIBRATION BASELINE
Topic: ___ | Date: ___ | Accuracy: ___ | Most reliable: ___ | Echo theme: ___
No prior retro — baseline established here for forward comparison.
```

---

---

## V-05 — Axes: Inertia Framing + Output Format
**Hypothesis:** Opening the retro with the status-quo foil table — before any signal analysis — forces the team to confront cost-of-inaction first. Every subsequent finding is interpreted against a named baseline, not a blank slate. This makes the Echo's change proposal feel like relief from a demonstrated cost rather than speculative improvement.

---

### Skill: topic-retro

**Purpose:** Post-commitment retrospective. Surfaces accuracy, gaps, and the unexpected finding — grounded in demonstrated cost against the status-quo default.

**Opening invariant:** the status-quo foil table runs first, before signal inventory. It is populated from Phase 0 prior belief and updated in Phase 5. **AMEND** scope applies throughout all phases.

---

### Phase 0 — Prior Belief and Status-Quo Foil (SEAL BEFORE SIGNALS)

Before opening any signal artifacts, capture the default assumption — what the team would have done without this retro — and lock it as Phase 0.

**Part A — Prior belief record:**

```
PHASE 0 — PRIOR BELIEF RECORD
Topic: ___
Date: ___
Prior belief (one sentence): ___
Confidence at intake: Low / Medium / High
Most trusted namespace: ___
Least trusted namespace: ___
```

**Part B — Status-quo foil (draft column only; "With This Retro" populated in Phase 5):**

| Dimension | Without this retro (default assumption) | With this retro (actual — fill in Phase 5) |
|-----------|----------------------------------------|-------------------------------------------|
| Signal accuracy assumption | {Phase 0 expected accuracy level} | — |
| Echo assumption | {what surprising finding, if any, was anticipated} | — |
| Signal design default | {namespace most relied upon without reflection} | — |

```
PHASE 0 SEALED — prior belief and default assumptions are now immutable.
Signals may now be opened.
```

**Phase boundary: Phase 0 sealed. Proceed to Phase 1.**

---

### Phase 1 — Echo Identification (LOCK BEFORE ACCURACY)

Read signals. Before scoring, name the one finding not anticipated in Phase 0.

```
ECHO (LOCKED)
Finding: {one sentence}
Contrast with Phase 0: {why Phase 0 prior belief did not predict this}
Lock status: immutable from Phase 1 forward

Any Phase 3+ finding that would revise this Echo must be recorded as a conflict
artifact. The Echo itself does not change.
```

**Phase boundary: Echo locked. Proceed to Phase 2.**

---

### Phase 2 — Signal Inventory

| Namespace | Artifact | Date | Prediction at signal time | C / P / W |
|-----------|----------|------|--------------------------|-----------|

**Phase boundary: Inventory complete. Proceed to Phase 3.**

---

### Phase 3 — Accuracy Scoring

| Namespace | C | P | W | Score: (C×100 + P×50) ÷ (C+P+W) [e.g. C=2,P=0,W=3 → 40.0] | Reliability |
|-----------|---|---|---|--------------------------------------------------------------|-------------|

**Overall accuracy: {ratio or qualitative judgment}**

**Conflict audit (mandatory — emits result in all cases):**

| Conflict audit | Result |
|---|---|
| Echo vs accuracy findings | ☐ No conflict — locked Echo holds ∙ ☐ Conflict — {describe} — Echo preserved, tension recorded |

**Phase boundary: Accuracy scored. Conflict audit complete. Proceed to Phase 4.**

---

### Phase 4 — Gap Analysis

| Namespace | Missing skill | Without this signal (default) | With this signal (what we'd have known) | Recommended action |
|-----------|--------------|------------------------------|----------------------------------------|-------------------|

Each row must name a specific skill and contrast the without/with states.

**Phase boundary: Gap analysis complete. Proceed to Phase 5.**

---

### Phase 5 — Status-Quo Foil Completion and Echo Change Proposal

Return to the Phase 0 foil table. Populate the "With This Retro" column.

| Dimension | Without this retro (Phase 0 — immutable) | With this retro (actual) |
|-----------|------------------------------------------|--------------------------|
| Signal accuracy assumption | {locked from Phase 0} | {Phase 3 overall score} |
| Echo assumption | {locked from Phase 0} | {locked Echo from Phase 1} |
| Signal design default | {locked from Phase 0} | {highest-scoring namespace in Phase 3} |

**Demonstrated cost of inaction:** {one sentence: what the team would have gotten wrong without this retro}

**Change proposal:** {specific skill to add, rubric criterion to amend, or threshold to set — derived from the Echo and the foil delta}

**Phase boundary: Foil complete. Change proposal recorded. Proceed to Phase 6.**

---

### Phase 6 — Calibration

**If prior retro available:**

| Dimension | Prior retro | This retro | Trend |
|-----------|-------------|------------|-------|
| Overall accuracy | | | ↑ / → / ↓ |
| Most reliable namespace | | | |
| Echo theme | | | |

**If no prior retro:**

```
CALIBRATION BASELINE RECORD
Topic: ___ | Date: ___ | Overall accuracy: ___
Most reliable namespace: ___ | Echo theme: ___
No prior retro available — calibration baseline established here.
This record is the forward reference for the next retro on this team or namespace.
```

---

### Pre-Emit Checklist

| Check | Requirement |
|---|---|
| Phase 0 sealed | Prior belief and foil draft present before any signal opened |
| Echo locked | `ECHO (LOCKED)` block appears before Phase 3 |
| Inventory complete | No known artifact omitted from Phase 2 |
| Formula in header | Per-namespace table column carries formula + worked example |
| Conflict audit | Explicit result emitted (no-conflict or conflict artifact) |
| Foil table | Three named rows, "Without" column populated from Phase 0 |
| Change proposal | One specific action — not generic advice |
| Calibration | Either trend or baseline record — never skipped |
| AMEND scope | All phases honor scope constraint if provided |

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | Key Structural Bet |
|-----------|-------------|----------------|-------------------|
| V-01 | Role sequence | — | Phase 0 seal prevents hindsight contamination structurally, not by author trust |
| V-02 | Output format | — | Formula + worked example in column header makes scoring self-auditing |
| V-03 | Lifecycle emphasis | — | Explicit boundary declarations make phase-sealing provably auditable by inspection |
| V-04 | Role sequence | Phrasing register | Direct imperative voice reduces friction while preserving structural constraints |
| V-05 | Inertia framing | Output format | Foil table leads — every finding is interpreted against a named cost baseline |
