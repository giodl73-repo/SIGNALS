# topic-retro Variations — Round 8

---

## V-01 — Axis: Lifecycle Emphasis
**Hypothesis:** Making every phase transition explicit with named boundary markers prevents Echo from being absorbed post-hoc and makes execution sequence auditable by inspection.

---

```markdown
You are running a post-commitment retrospective on a topic's signal history.
A feature has shipped. Your job is to assess the predictive quality of the
signals gathered before commitment, identify what was missing, and surface
the one thing that genuinely surprised you.

If an AMEND instruction is present, honor its scope constraint throughout
every section — inventory, accuracy, gaps, and Echo must all stay within
the specified signal type or time window.

---

## PHASE 0 — PRE-RETRO EPISTEMIC CAPTURE

Before opening any signal artifacts, record your prior belief:

> **Prior belief (before reviewing signals):** [Write one sentence: what do
> you expect the signal accuracy to be, and what do you expect the Echo to
> be about? This must be written before any Phase 1 data is reviewed.]

---

**Phase boundary: Prior belief is now sealed. Proceed to Phase 1.**

---

## PHASE 1 — ECHO (identify before scoring)

Scan all signal artifacts now. Before computing any accuracy scores, name
the single most surprising finding — the thing you did not expect.

**ECHO (LOCKED)**

| Field | Value |
|-------|-------|
| WHEN locked | Phase 1 (before accuracy scoring) |
| LOCK STATUS | LOCKED — do not revise after Phase 2+ |
| Authorized conflict response | Log tension in Phase 3 conflict audit; never revise this record |
| Echo statement | [Single sentence: the one unexpected finding] |

The Echo must be one sentence. It is now immutable.

---

**Phase boundary: Echo is now locked. Proceed to Phase 2.**

---

## PHASE 2 — SIGNAL INVENTORY AND ACCURACY

Build the complete signal inventory. Every artifact known to exist must
appear — no omissions.

Column header definition:
`Score: (C×100 + P×50) / (C+P+W)  [e.g. C=2, P=1, W=1 → 62.5]`

| Namespace | Artifact | Date | Prediction made at signal time | Actual outcome | C/P/W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1→62.5] |
|-----------|----------|------|-------------------------------|----------------|-------|------------------------------------------------------|
| scout     | ...      | ...  | ...                           | ...            | ...   | ...                                                  |

After filling the table, compute per-namespace accuracy using the same
formula. Break out each namespace separately — do not average into a
single number.

**Overall accuracy judgment:** [score or ratio grounded in the table above]

---

**Phase boundary: Accuracy verdict is now recorded. Proceed to Phase 3.**

---

## PHASE 3 — CONFLICT AUDIT (unconditional)

Examine whether any accuracy finding or gap finding in Phase 2 would
tempt revision of the locked Echo from Phase 1.

This audit runs regardless of whether you perceive tension.

| Tension detected? | Description | Resolution |
|-------------------|-------------|------------|
| Yes / No          | [If yes: describe what would have changed the Echo] | Preserve original Echo; log tension here |

If no tension: record "No conflict detected — Echo record stands."

---

**Phase boundary: Conflict audit complete. Proceed to Phase 4.**

---

## PHASE 4 — GAP ANALYSIS

Identify which signal types were absent for this topic.

| Namespace | Signal type absent | Why it mattered | Concrete next action |
|-----------|-------------------|-----------------|----------------------|
| ...       | ...               | ...             | [specific skill to run, question to ask, or threshold to set] |

Generic advice ("gather more signals") does not count as a concrete action.

---

**Phase boundary: Gaps recorded. Proceed to Phase 5.**

---

## PHASE 5 — ECHO FEEDBACK AND FOIL

**Echo feedback loop:**
Translate the locked Echo into one concrete change proposal:
> [Not just "we learned X" but "therefore we should do Y differently" —
> a specific new skill, rubric amendment, or threshold adjustment.]

**Status-quo foil:**

| Dimension | Without This Retro (prior belief) | With This Retro (actual finding) |
|-----------|-----------------------------------|----------------------------------|
| Signal accuracy assumption | [from Phase 0 prior belief] | [from Phase 2 verdict] |
| Echo assumption | [from Phase 0 prior belief] | [from Phase 1 locked Echo] |
| Signal design default | [what the team would have continued doing] | [what the Echo feedback loop changes] |

The "Without This Retro" column must draw from the Phase 0 prior belief
written before signals were reviewed — not reconstructed from hindsight.

---

**Phase boundary: Retro complete.**

---

## CALIBRATION TREND (if prior retro exists)

If a prior retro exists for this team or namespace, compare accuracy scores:

| Retro | Date | Overall score | Trend |
|-------|------|---------------|-------|
| Prior | ... | ... | — |
| This  | ... | ... | ↑ / ↓ / → |

State whether prediction quality is improving, degrading, or stable.
If no prior retro exists, note: "No prior retro available — calibration
baseline established here."
```

---

## V-02 — Axis: Output Format (Tables-First)
**Hypothesis:** Leading with formula-in-header tables and requiring the header to carry a worked example forces mechanical verifiability before any narrative interpretation begins.

---

```markdown
You are running a post-commitment retrospective on a topic's signal history.
A feature has shipped. Produce structured output in the order below.
Every score must be computed from the stated formula — no qualitative
judgments substituted for numbers.

If an AMEND instruction is present, restrict inventory, accuracy, gaps,
and Echo to the specified signal type or time window throughout.

---

## Step 1 — Echo (before any scoring)

State the single most surprising finding now, before computing accuracy.

**ECHO (LOCKED)**

| Field | Value |
|-------|-------|
| WHEN locked | Step 1, before accuracy scoring |
| LOCK STATUS | LOCKED |
| Authorized conflict response | Log only in Step 4 conflict column; never revise |
| Echo | [One sentence — the one thing genuinely not expected] |

---

## Step 2 — Signal Inventory

Every signal artifact for this topic. No omissions.

Use this exact column header for the Score column:
`Score: (C×100 + P×50) / (C+P+W) [e.g. C=3,P=1,W=0 → 91.7]`

| Namespace | Artifact name | Date | Prediction at signal time | Actual outcome | C / P / W | Score: (C×100+P×50)/(C+P+W) [e.g. C=3,P=1,W=0→91.7] | Conflict with Echo? |
|-----------|--------------|------|--------------------------|----------------|-----------|------------------------------------------------------|---------------------|
|           |              |      |                          |                |           |                                                      | Yes/No — note if Yes |

The last column runs unconditionally. Enter "No conflict" if none exists.

---

## Step 3 — Per-Namespace Accuracy Rollup

Aggregate the Step 2 table by namespace.

Use this exact column header:
`NS Score: (ΣC×100 + ΣP×50) / Σ(C+P+W) [e.g. C=2,P=2,W=1 → 60.0]`

| Namespace | Artifacts | ΣC | ΣP | ΣW | NS Score: (ΣC×100+ΣP×50)/Σ(C+P+W) [e.g. C=2,P=2,W=1→60.0] | Signal quality verdict |
|-----------|-----------|----|----|----|------------------------------------------------------------|----------------------|
| scout     |           |    |    |    |                                                            |                      |
| draft     |           |    |    |    |                                                            |                      |
| flow      |           |    |    |    |                                                            |                      |
| [etc.]    |           |    |    |    |                                                            |                      |
| **TOTAL** |           |    |    |    |                                                            | **Overall judgment** |

---

## Step 4 — Conflict Audit

Scan every "Conflict with Echo?" entry from Step 2. This step runs
whether or not you detected conflict.

| Echo field | Conflict row (if any) | Would Echo have changed to? | Resolution |
|------------|----------------------|----------------------------|------------|
| [Echo text] | [Row ref or "none"] | [Revised Echo or "N/A"] | Preserve original; log tension here |

If no conflicts: enter "Conflict audit complete — no tension detected."

---

## Step 5 — Gap Analysis

| Namespace | Signal type absent | Impact on decision | Next action (specific skill or question) |
|-----------|-------------------|-------------------|------------------------------------------|
|           |                   |                   |                                          |

Each "Next action" must name a concrete skill (e.g., `/scout:feasibility`)
or a specific question to investigate. "Gather more signals" fails.

---

## Step 6 — Echo Feedback and Foil

**Echo → change proposal:**
> [The locked Echo translates to: run skill X / amend rubric Y / set
> threshold Z. One specific change, not a general observation.]

**Status-quo foil:**

| | Without This Retro | With This Retro |
|--|-------------------|-----------------|
| Accuracy assumption | [what the team believed going in] | [Step 3 overall score] |
| Most surprising gap | [assumed sufficient coverage] | [Step 5 top gap] |
| Signal design default | [what would have continued unchanged] | [Step 6 change proposal] |

---

## Step 7 — Calibration Trend (if prior data exists)

| Retro | Date | Overall NS Score | Δ vs prior |
|-------|------|-----------------|------------|
| Prior | | | — |
| This  | | | +N / −N / 0 |

Verdict: improving / degrading / stable. If no prior retro: "Baseline established."
```

---

## V-03 — Axis: Role Sequence (Echo-First, Conversational Register)
**Hypothesis:** Framing the retro as a two-character dialogue — an Archivist who seals findings and an Analyst who scores — makes the sequencing constraint feel natural rather than procedural, improving Echo immutability compliance.

---

```markdown
You are running a post-commitment signal retro. Two roles collaborate here:

- **Archivist** — surfaces the unexpected finding and seals it before any
  scoring begins. Owns the Echo. Cannot be overruled by later analysis.
- **Analyst** — scores signal accuracy, audits conflicts, identifies gaps.
  May not revise the Archivist's sealed finding.

If an AMEND instruction scopes the retro to a specific signal type or
time window, both roles honor that scope throughout.

---

### Archivist speaks first

Before the Analyst reviews any signal scores, the Archivist reads all
signal artifacts and names the one thing that was genuinely unexpected.

**ECHO (LOCKED)**

| Field | Value |
|-------|-------|
| Locked by | Archivist, before Analyst scoring |
| Lock status | LOCKED |
| If Analyst finds conflict | Log it below; Archivist record stands |
| Echo | [One sentence. The single most surprising thing.] |

The Archivist is done. The Echo is sealed.

---

### Analyst takes over

The Analyst now works through the signal inventory, accuracy scoring,
conflict check, and gaps. The sealed Echo above does not change.

**Signal inventory**

Every artifact for this topic. One row per artifact.

Score formula header: `Score: (C×100+P×50)/(C+P+W) [e.g. C=1,P=2,W=1→50.0]`

| Namespace | Artifact | Date | Prediction at signal time | Actual | C/P/W | Score: (C×100+P×50)/(C+P+W) [e.g. C=1,P=2,W=1→50.0] |
|-----------|----------|------|--------------------------|--------|-------|------------------------------------------------------|

**Per-namespace accuracy**

Aggregate the above by namespace using the same formula.

`NS Score: (ΣC×100+ΣP×50)/Σ(C+P+W) [e.g. C=2,P=0,W=2→50.0]`

| Namespace | NS Score: (ΣC×100+ΣP×50)/Σ(C+P+W) [e.g. C=2,P=0,W=2→50.0] | Reliable? |
|-----------|-------------------------------------------------------------|-----------|

**Overall accuracy judgment:** [score or ratio, grounded in the table]

**Conflict audit** (Analyst runs this unconditionally)

Did any accuracy finding tempt the Analyst to revise the Archivist's Echo?

| Tension? | What would have changed | Analyst resolution |
|----------|------------------------|--------------------|
| Yes/No   | [describe or "none"]   | Echo preserved; tension logged |

If no tension: "No conflict — Archivist record stands."

**Gap analysis**

What signal types were missing, and what would the Analyst recommend?

| Namespace | Signal type missing | Why it would have mattered | Recommended action |
|-----------|--------------------|-----------------------------|-------------------|
|           |                    |                             | [specific skill or question] |

---

### Echo feedback loop (joint)

Both roles contribute one line each:

- **Archivist:** The Echo teaches us ______. The prior assumption was ______.
- **Analyst:** Therefore, the concrete change is: [specific skill / rubric amendment / threshold].

**Status-quo foil**

| | Without this retro | With this retro |
|--|-------------------|-----------------|
| Accuracy assumption | [prior default] | [Analyst overall score] |
| Echo known? | No — Archivist finding would not exist | Yes — sealed in Phase 0 |
| Signal design | [what continues unchanged] | [Analyst's change proposal] |

---

### Calibration trend (Analyst, if prior retro exists)

| Retro | Overall score | Δ | Trend |
|-------|--------------|---|-------|
| Prior | | | — |
| This  | | | ↑/↓/→ |

If no prior retro: "Calibration baseline established here."
```

---

## V-04 — Combined: Echo-First + Multi-Field Lock Record + Foil Prior Belief
**Hypothesis:** Combining pre-retro epistemic capture (C-22), a multi-field Echo Lock Record (C-21), and a foil table anchored to the pre-retro prior belief creates the tightest closed-loop epistemic artifact — every output field is traceable to either intake or close, not hindsight.

---

```markdown
You are running a post-commitment signal retro for a topic that has shipped.
This retro is a closed-loop epistemic artifact: every finding is anchored
to either pre-retro intake (before signal data is opened) or post-retro
close (after all phases complete). Nothing is reconstructed from hindsight.

If an AMEND instruction is present, it governs scope throughout: inventory,
accuracy, gaps, Echo, and foil must all respect the specified constraint.

---

## INTAKE — Record prior belief before opening signal data

Write one sentence for each field below. Do this before reading any
signal artifacts.

| Field | Your prior belief (write now, before Phase 1) |
|-------|----------------------------------------------|
| Expected overall accuracy | [e.g., "I expect roughly 70% of predictions were correct"] |
| Expected Echo topic | [e.g., "I expect the surprise will be about adoption timing"] |
| Expected primary gap | [e.g., "I expect we were thin on listen namespace signals"] |

**Intake is sealed. Proceed to Phase 1.**

---

## PHASE 1 — ECHO

Read all signal artifacts now. Name the one thing you did not expect.

**ECHO LOCK RECORD**

| Field | Value |
|-------|-------|
| WHEN locked | Phase 1 — before any accuracy scoring |
| LOCK STATUS | LOCKED |
| Authorized conflict response | Log in Phase 3 conflict audit; never revise this record |
| Echo statement | [One sentence: the single most surprising finding] |
| Intake prediction match? | Yes / No — compare to intake "Expected Echo topic" |

The Echo Lock Record is now immutable.

---

**Phase boundary: Echo Lock Record sealed. Proceed to Phase 2.**

---

## PHASE 2 — SIGNAL INVENTORY AND ACCURACY

Every signal artifact for this topic. One row per artifact.

Score column header:
`Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1→62.5]`

| Namespace | Artifact | Date | Prediction at signal time | Actual outcome | C/P/W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1→62.5] |
|-----------|----------|------|--------------------------|----------------|-------|------------------------------------------------------|

**Per-namespace rollup**

`NS Score: (ΣC×100+ΣP×50)/Σ(C+P+W) [e.g. C=3,P=1,W=2→66.7]`

| Namespace | Artifacts | ΣC | ΣP | ΣW | NS Score: (ΣC×100+ΣP×50)/Σ(C+P+W) [e.g. C=3,P=1,W=2→66.7] | Reliable? |
|-----------|-----------|----|----|----|------------------------------------------------------------|-----------|
| scout     |           |    |    |    |                                                            |           |
| draft     |           |    |    |    |                                                            |           |
| [etc.]    |           |    |    |    |                                                            |           |
| **TOTAL** |           |    |    |    |                                                            |           |

**Overall accuracy judgment:** [grounded in the rollup table]

---

**Phase boundary: Accuracy verdict recorded. Proceed to Phase 3.**

---

## PHASE 3 — CONFLICT AUDIT (unconditional)

This audit runs regardless of whether you detect tension.

| Would any accuracy finding revise the Echo? | What would change | Resolution |
|--------------------------------------------|-------------------|------------|
| Yes / No                                   | [describe or "N/A"] | Preserve Lock Record; log tension here |

If no conflict: "Conflict audit complete — Echo Lock Record stands."

---

**Phase boundary: Conflict audit complete. Proceed to Phase 4.**

---

## PHASE 4 — GAP ANALYSIS

| Namespace | Signal type absent | Decision impact | Next action |
|-----------|-------------------|-----------------|-------------|
|           |                   |                 | [/skill:name or specific question] |

---

**Phase boundary: Gaps recorded. Proceed to Phase 5.**

---

## PHASE 5 — ECHO FEEDBACK AND FOIL

**Echo → change proposal:**
> [Specific: run skill X, amend rubric criterion Y, or set threshold Z.
> Not "we should gather more signals."]

**Status-quo foil (closed-loop)**

| Dimension | Without This Retro (from INTAKE) | With This Retro (from Phase 2 + 4) |
|-----------|----------------------------------|-------------------------------------|
| Accuracy assumption | [intake "Expected overall accuracy"] | [Phase 2 overall score] |
| Echo known? | [intake "Expected Echo topic"] | [Phase 1 Echo statement] |
| Primary gap identified? | [intake "Expected primary gap"] | [Phase 4 top gap] |
| Signal design | [what would have continued unchanged] | [Phase 5 change proposal] |

The "Without This Retro" column draws exclusively from INTAKE fields —
not from hindsight reconstruction.

---

**Phase boundary: Retro complete. POST-RETRO recorded above.**

---

## CALIBRATION TREND (if prior retro exists)

| Retro | Date | Overall score | Δ |
|-------|------|--------------|---|
| Prior | | | — |
| This  | | | +N/−N/0 |

Trend: improving / degrading / stable.
If no prior: "Calibration baseline established."
```

---

## V-05 — Combined: Structured Phases + Calibration-First Framing + Full Foil
**Hypothesis:** Opening with calibration context (what we knew about our signal quality before this retro) and closing with the foil anchored to that baseline maximizes the feedback loop — the retro produces not just findings but a measurable update to the team's signal model.

---

```markdown
You are running a post-commitment signal retro. A feature has shipped.
This retro answers three questions:

1. How accurate were our signals? (Were predictions correct?)
2. What was missing? (Gaps that would have changed the decision)
3. What surprised us? (The Echo — the one thing we didn't expect)

Run phases in order. Each phase is sealed before the next begins.

If an AMEND instruction is present, all phases respect its scope.

---

## PRE-RETRO — Epistemic baseline

Before reviewing any signals, capture two things:

**Calibration context (if prior retro data exists):**
What was the team's last known signal accuracy score?

| Prior retro | Date | Score | Source |
|-------------|------|-------|--------|
| [topic or "N/A"] | | | |

If no prior: "No prior retro — this establishes the baseline."

**Prior belief (before opening signal data):**

| What I expect | My pre-retro belief |
|---------------|---------------------|
| Overall accuracy | |
| Where signals were weakest | |
| What the Echo will be about | |

**Pre-retro sealed. Proceed to Phase 1.**

---

## PHASE 1 — ECHO LOCK

Read all signal artifacts. Before scoring anything, name the one finding
that genuinely surprised you.

**ECHO LOCK RECORD**

| Field | Value |
|-------|-------|
| WHEN locked | Phase 1 — before accuracy scoring |
| LOCK STATUS | LOCKED |
| Authorized conflict response | Log only in Phase 3; never revise this record |
| Echo | [One sentence — the single most unexpected finding] |

Compare to pre-retro belief: Did the Echo match your expectation?
> [Yes / No — one sentence noting the match or divergence]

---

**Phase boundary: Echo is immutable. Phase 2 begins.**

---

## PHASE 2 — SIGNAL INVENTORY

Every known artifact for this topic. One row per signal.

Score header: `Score: (C×100+P×50)/(C+P+W) [e.g. C=1,P=1,W=2→37.5]`

| Namespace | Artifact | Date | Prediction at signal time | Actual | C/P/W | Score: (C×100+P×50)/(C+P+W) [e.g. C=1,P=1,W=2→37.5] |
|-----------|----------|------|--------------------------|--------|-------|------------------------------------------------------|

**Per-namespace rollup**

NS Score header: `NS Score: (ΣC×100+ΣP×50)/Σ(C+P+W) [e.g. C=4,P=2,W=2→75.0]`

| Namespace | ΣC | ΣP | ΣW | NS Score: (ΣC×100+ΣP×50)/Σ(C+P+W) [e.g. C=4,P=2,W=2→75.0] | Reliable? |
|-----------|----|----|----|------------------------------------------------------------|-----------|
| scout     |    |    |    |                                                            |           |
| draft     |    |    |    |                                                            |           |
| flow      |    |    |    |                                                            |           |
| [etc.]    |    |    |    |                                                            |           |
| **TOTAL** |    |    |    |                                                            |           |

**Overall accuracy judgment:** [score + one-sentence verdict]

---

**Phase boundary: Accuracy recorded. Phase 3 begins.**

---

## PHASE 3 — CONFLICT AUDIT (runs unconditionally)

| Tension with Phase 1 Echo? | What Phase 2 would change | Resolution |
|---------------------------|--------------------------|------------|
| Yes / No                  | [or "N/A"]               | Preserve Echo Lock Record; log here |

No-conflict entry required: "Conflict audit complete — no revision."

---

**Phase boundary: Audit complete. Phase 4 begins.**

---

## PHASE 4 — GAP ANALYSIS

| Namespace | Signal type absent | Would it have changed decision? | Recommended action |
|-----------|-------------------|---------------------------------|-------------------|
|           |                   | Yes / Possibly / No             | [/skill:name or specific question, not generic advice] |

---

**Phase boundary: Gaps recorded. Phase 5 begins.**

---

## PHASE 5 — FEEDBACK AND CALIBRATION CLOSE

**Echo change proposal:**
> [Specific: run /skill:X, add criterion C-N to rubric Y, set threshold Z
> for namespace N. One actionable change derived from the locked Echo.]

**Calibration update**

| Retro | Date | Overall score | Δ vs prior | Trend |
|-------|------|--------------|------------|-------|
| Prior (pre-retro) | | | — | — |
| This retro | | | +N/−N/0 | ↑/↓/→ |

State: prediction quality is [improving / degrading / stable] for this
team / namespace.

**Status-quo foil**

The "Pre-retro belief" column draws from PRE-RETRO fields above —
not reconstructed from hindsight.

| Dimension | Without This Retro (pre-retro belief) | With This Retro (actual finding) |
|-----------|---------------------------------------|----------------------------------|
| Accuracy | [pre-retro "Overall accuracy" belief] | [Phase 2 overall score] |
| Weakest namespace | [pre-retro "Where signals weakest"] | [Phase 2 lowest NS Score] |
| Echo | [pre-retro "What Echo will be about"] | [Phase 1 locked Echo] |
| Signal design | [what continues unchanged] | [Phase 5 change proposal] |

**Calibration verdict:**
> [Did this retro confirm, refine, or overturn the prior calibration
> baseline? One sentence.]
```

---

## Variation Summary

| ID | Axis | Primary novelty | Key hypotheses tested |
|----|------|-----------------|----------------------|
| V-01 | Lifecycle emphasis | `Phase boundary:` markers between every phase | Structural sealing prevents post-hoc Echo revision |
| V-02 | Output format | Formula + worked example baked into every column header | Header-as-instruction makes scoring mechanically verifiable |
| V-03 | Role sequence | Archivist/Analyst split; conversational framing | Named roles make sequencing feel natural, not procedural |
| V-04 | Echo-first + Lock Record + Foil prior belief | Multi-field Echo Lock Record + INTAKE sealed before Phase 1 | Tightest closed-loop — every field traceable to intake or close |
| V-05 | Structured phases + calibration-first | Pre-retro calibration baseline; foil anchored to it | Retro produces measurable update to team signal model |
